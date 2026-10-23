#!/usr/bin/env python3
"""Read-only independent saved-PDF preservation binding. No puzzle solving.

Compare the V8 full-book baseline with a final full book; only whitespace is
normalized on reflowed pages. Dialogue is removed only after exact ordered
speech and immediate speaker-label matching. No footer/content exceptions.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import fitz

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def norm(text):
    return re.sub(r'\s+', ' ', text).strip()

def digest_text(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def speech_remainder(page_text, turns, field, colon=True):
    text = norm(page_text)
    cursor = 0
    chunks, checks = [], []
    for item in turns:
        speech = norm(item['turn'][field])
        start = text.find(speech, cursor)
        end = start + len(speech) if start >= 0 else -1
        prefix = text[cursor:start] if start >= 0 else ''
        speaker = item['turn']['speaker']
        suffix = re.escape(speaker) + (r'\s*:\s*$' if colon else r'\s*$')
        label_ok = start >= 0 and bool(re.search(r'\b' + suffix, prefix))
        check = {'scene': item['scene'], 'turn': item['number'],
                 'speaker': speaker, 'speech_present_in_order': start >= 0,
                 'immediate_speaker_label': label_ok}
        checks.append(check)
        if start < 0:
            return None, checks
        chunks.append(text[cursor:start])
        chunks.append(f"<HM_SPEECH_{item['scene']}_{item['number']}>")
        cursor = end
    chunks.append(text[cursor:])
    return ''.join(chunks), checks

def pix_hash(page, scale):
    fitz.TOOLS.store_shrink(100)
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    return hashlib.sha256(pix.samples).hexdigest(), [pix.width, pix.height, pix.n]

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', type=Path, default=ROOT/'candidate/candidate.json')
    ap.add_argument('--scenes', type=Path, default=ROOT/'candidate/final-scenes.json')
    ap.add_argument('--baseline-book', type=Path, default=WORKSPACE/'detective-v8/proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf')
    ap.add_argument('--book', type=Path, default=ROOT/'proof/DETECTIVE_EN_V10_FULL_ENGLISH.pdf')
    ap.add_argument('--standalone', type=Path, default=ROOT/'proof/HAPPY_MAKERS_COMMS_V10_EN.pdf')
    ap.add_argument('--expected-hash', required=True)
    ap.add_argument('--out', type=Path, default=ROOT/'reviews/story-final/PDF_PRESERVATION_BINDING.json')
    ap.add_argument('--scale', type=float, default=.3)
    args = ap.parse_args()
    candidate_hash = sha(args.candidate)
    if candidate_hash != args.expected_hash:
        raise SystemExit(f'Expected canonical hash mismatch: {candidate_hash}')
    final = json.loads(args.scenes.read_text())
    if final.get('candidate_sha256') != candidate_hash:
        raise SystemExit('Final-scene packet does not bind requested canonical hash')
    scenes = final['scenes']
    folios = {}
    for scene in scenes:
        for number, turn in enumerate(scene['turns'], 1):
            turn_folios = {int(re.match(r'page(\d+)\.', unit).group(1)) for unit in turn['ids']}
            if len(turn_folios) != 1:
                raise SystemExit(f'Cross-folio turn cannot be silently normalized: {scene["id"]}/{number}')
            folio = next(iter(turn_folios))
            folios.setdefault(folio, []).append({'scene':scene['id'], 'number':number, 'turn':turn})
    assert len(scenes) == 34 and sum(len(s['turns']) for s in scenes) == 183
    assert len(folios) == 35
    old, new, standalone = fitz.open(args.baseline_book), fitz.open(args.book), fitz.open(args.standalone)
    findings = []
    if len(old) != 225 or len(new) != 225 or len(standalone) != 34:
        raise SystemExit(f'Unexpected PDF counts baseline={len(old)}, book={len(new)}, standalone={len(standalone)}')
    unchanged, changed = [], []
    for folio in range(1, 226):
        old_text, new_text = old[folio-1].get_text(), new[folio-1].get_text()
        if folio not in folios:
            old_pix, old_dim = pix_hash(old[folio-1], args.scale)
            new_pix, new_dim = pix_hash(new[folio-1], args.scale)
            row = {'folio':folio,'text_identical':old_text==new_text,
                   'pixels_identical':old_pix==new_pix and old_dim==new_dim,
                   'baseline_pixel_sha256':old_pix,'new_pixel_sha256':new_pix,
                   'raster_dimensions':new_dim}
            unchanged.append(row)
            if not row['text_identical'] or not row['pixels_identical']:
                findings.append({'folio':folio,'finding':'Untouched leaf text/pixel difference'})
        else:
            before, old_checks = speech_remainder(old_text, folios[folio], 'v8_text')
            after, new_checks = speech_remainder(new_text, folios[folio], 'final_text')
            all_checks = all(c['speech_present_in_order'] and c['immediate_speaker_label'] for c in old_checks + new_checks)
            same = before is not None and after is not None and before == after
            row = {'folio':folio,'spoken_turns':len(folios[folio]),
                   'all_old_and_final_speech_and_speakers_present_and_ordered':all_checks,
                   'old_speech_checks':old_checks,'new_speech_checks':new_checks,
                   'non_comms_remainder_exact':same,
                   'baseline_remainder_sha256':digest_text(before) if before is not None else None,
                   'new_remainder_sha256':digest_text(after) if after is not None else None}
            changed.append(row)
            if not same or not all_checks:
                findings.append({'folio':folio,'finding':'Changed leaf speech/speaker or strict nonComms remainder mismatch'})
                # Bounded evidence, never edit or remove unmatched content.
                if before is not None and after is not None:
                    import difflib
                    row['remainder_difference'] = list(difflib.unified_diff(before.split(), after.split(), lineterm=''))[:80]
    solo_checks = []
    for page, scene in enumerate(scenes, 1):
        turns = [{'scene':scene['id'],'number':i,'turn':t} for i,t in enumerate(scene['turns'],1)]
        _, checks = speech_remainder(standalone[page-1].get_text(), turns, 'final_text', colon=False)
        ok = len(checks)==len(turns) and all(c['speech_present_in_order'] and c['immediate_speaker_label'] for c in checks)
        solo_checks.append({'page':page,'scene':scene['id'],'turns':len(turns),'speech_and_speaker_sequence':'PASS' if ok else 'FIX','checks':checks})
        if not ok:
            findings.append({'standalone_page':page,'scene':scene['id'],'finding':'Standalone speech/speaker order mismatch'})
    receipt = {'reviewer':'/root/hm10_story_guard','stage':'actual_pdf_preservation_binding',
               'status':'PASS' if not findings else 'FIX','candidate_sha256':candidate_hash,
               'final_scenes_sha256':sha(args.scenes),'baseline_v8_pdf_sha256':sha(args.baseline_book),
               'new_pdf_sha256':sha(args.book),'standalone_pdf_sha256':sha(args.standalone),
               'book_pages':len(new),'standalone_pages':len(standalone),
               'method':'Independent saved-PDF extraction;190untouchedleaves exact text and raster-byte identity;35changedfolios strict normalized-whitespace nonComms remainders after exact ordered speech replacement with identical scene/turn placeholders and immediate speaker matching. All183speech/speaker pairs separately located in34page standalone. No footer or content exceptions.',
               'raster_scale':args.scale,'unchanged_page_count':len(unchanged),'unchanged_page_results':unchanged,
               'reflowed_page_count':len(changed),'reflowed_page_results':changed,
               'final_spoken_turns_present_and_ordered':all(x['all_old_and_final_speech_and_speakers_present_and_ordered'] for x in changed),
               'standalone_all183_turn_speaker_roundtrips':all(x['speech_and_speaker_sequence']=='PASS' for x in solo_checks),
               'standalone_checks':solo_checks,'puzzles_re_solved':False,
               'visual_review_limit':'Low-resolution pixel identity only on untouched leaves; changed-leaf layout/full-size visual QA is separate.',
               'unresolved_findings':findings}
    assert len(unchanged)==190
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':receipt['status'],'candidate_sha256':candidate_hash,'book_pdf_sha256':receipt['new_pdf_sha256'],'standalone_pdf_sha256':receipt['standalone_pdf_sha256'],'untouched':len(unchanged),'reflowed':len(changed),'turns':183,'findings':findings,'receipt':str(args.out)},indent=2))
    return 0 if not findings else 1

if __name__ == '__main__':
    sys.exit(main())
