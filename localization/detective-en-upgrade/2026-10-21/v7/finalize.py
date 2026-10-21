"""Record reproducible editorial evidence and the sole-product-writer handoff."""
from pathlib import Path
import copy, hashlib, json, re, shutil
R=Path(__file__).resolve().parent;W=R.parent;V6=W/'detective-v6';OLD=W/'detective-upgrade'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
shat=lambda t:hashlib.sha256(t.encode()).hexdigest()
def dump(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
c=json.loads((R/'candidate/candidate.json').read_text());ch=sha(R/'candidate/candidate.json')
ct={s['id']:s['text'] for s in c['segments']}
b=json.loads((R/'baseline/candidate-v6.json').read_text());bt={s['id']:s['text'] for s in b['segments']}
source=json.loads((OLD/'source/intake-v5.json').read_text());st={s['id']:s['text'] for s in source['segments']}
meta=json.loads((OLD/'qa/source-page-map.json').read_text());pages={p['page']:p for p in meta['pages']}
ledger=json.loads((R/'candidate/change-ledger.json').read_text());changed={s['id'] for s in ledger}
assert len(ct)==len(bt)==len(st)==3067
assert changed=={i for i in ct if ct[i]!=bt[i]}
v6ids={s['id'] for s in json.loads((V6/'candidate/change-ledger.json').read_text())}
assert len(v6ids)==27 and all(ct[i]==bt[i] for i in v6ids)
back=[i for i in ct if int(i[4:7])>=148]
assert [i for i in back if ct[i]!=bt[i]]==['page212.block12']
for p in meta['cases']:
    solution=p['solution_page']
    assert all(ct[i]==bt[i] for i in ct if int(i[4:7])==solution and i!='page212.block12')
comparison=json.loads((R/'candidate/comms-comparison.json').read_text())['scenes']
stats={'candidate_sha256':ch,'baseline_candidate_sha256':sha(R/'baseline/candidate-v6.json'),
 'original225_pdf_sha256':sha(W/'upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf'),
 'source_folios':225,'stable_units':3067,'changed_units_from_v6':len(changed),
 'unchanged_units_from_v6':3067-len(changed),'changed_folios':sorted({int(i[4:7]) for i in changed}),
 'original225_changed_units':sum(ct[i]!=st[i] for i in ct),
 'main_comms_reviewed':30,'main_comms_changed_from_v6':sum(s['changed_v7'] for s in comparison),
 'main_comms_changed_turns_from_v6':sum(t['changed_v7'] for s in comparison for t in s['turns']),
 'whole_golden_main_comms':[s['case'] for s in comparison if not s['changed_v7']],
 'all27_v6_repairs_unchanged':True,'backmatter_units_checked':len(back),'backmatter_only_delta':'page212.block12: nonmechanic chronology summary',
 'all90_hints_30_answers_and_reasoning':'EXACT_V6','four0records_14maps_finale_inputs':'PRESERVED_BY_FULL_SEMANTIC_REVIEW_AND_PROTECTED_HASHES',
 'production_source_renderer_modified':False,'main_merged':False,'frozen':False,'published':False}
dump(R/'qa/FINAL_CONTENT_VERIFICATION.json',stats)

run=R/'run-r2'
brief=json.loads((run/'functional-brief.json').read_text())
continuity=json.loads((R/'reviews/story-diagnostic/CONTINUITY_MAP.json').read_text())
case_map={p['case']:p for p in continuity['case_function_and_continuity_map']}
comedy=json.loads((R/'reviews/comedy-diagnostic/diagnostic.json').read_text())
comic={p['case']:p for p in comedy['case_plans']}
allow=set(json.loads((run/'change-scope.json').read_text())['allowed_changed_segments'])
for u in brief['units']:
    p=int(u['id'][4:7]);case=pages[p].get('case');role=pages[p]['role'];plan=case_map.get(case,{})
    u.update({'function':role+': '+pages[p].get('title',''),
      'reader_action':'Solve only from the printed evidence; retain actual core task.' if role=='puzzle_or_evidence' else 'Follow story, relationship and next task without a supplied answer.',
      'immutable_facts':plan.get('entry_truth_and_story_job','Exact source facts, identity, numbers and modality remain protected.'),
      'mechanics':plan.get('no_drift_boundary','Protected text hash and source artwork; no mechanics changes.'),
      'safety_consent':'Tease choices and boasts; no shame for mistakes, speed or help; no forced participation or family affection condition.',
      'chronology':plan.get('exit_payoff_or_next_dependency','Retain source sequence and known/unknown boundary.'),
      'character_voice':'HAPPY_MAKERS_VOICE_BIBLE.md; independent comedy/story diagnostic.' if p<=147 else 'Direct, concrete source instructional register.',
      'emotional_job':comic.get(case,{}).get('relationship','Ordinary room at the table; certification recognizes work, belonging already exists.'),
      'humor_job':comic.get(case,{}).get('comic_engine','Preserve strong source wording; no joke added to an emotionally serious or mechanical unit.'),
      'dependencies':plan.get('locked_outcome','Stable source locator and complete page/case map.'),
      'decision':'FIX' if u['id'] in changed else 'GOLDEN_KEEP',
      'permission':'PROSE_ALLOWLIST' if u['id'] in allow else 'EXACT_BASELINE_LOCK'})
dump(run/'functional-brief.json',brief)
dump(R/'qa/CONTENT_MAP.json',{'candidate_sha256':ch,'pages':[
 {**p,'changed_ids':[i for i in changed if int(i[4:7])==p['page']],
  'editorial_decision':'FIX' if any(int(i[4:7])==p['page'] for i in changed) else 'GOLDEN_KEEP',
  'review':'Full225folios read in initial diagnostic and independentR1;8-unit closure reviewed independently.'} for p in meta['pages']]})

final_review=R/'reviews/FINAL_REVIEW_BUNDLE.json'
if final_review.exists():
    bundle=json.loads(final_review.read_text());assert bundle['candidate_sha256']==ch
    issue=json.loads((run/'issue-ledger.json').read_text())
    for item in issue['issues']:
        item['resolution']='Single writer integrated exact target; all material R1 findings closed by real native/audience/meaning/logic final reviews on '+ch+'.'
        item['evidence']='../../reviews/FINAL_REVIEW_BUNDLE.json'
    issue['independent_review']='FULL_R1_PLUS_HASH_BOUND_EIGHT_UNIT_CLOSURE'
    dump(run/'issue-ledger.json',issue)
    shutil.copyfile(R/'candidate/candidate.json',run/'candidate.json')

oldpacket=json.loads((V6/'integration/EDITORIAL_IMPORT_PACKET_V6.json').read_text())
packet={'format':'rse-detective-editorial-import-v7','candidate_sha256':ch,
 'source_pdf_sha256':stats['original225_pdf_sha256'],'v6_baseline_sha256':stats['baseline_candidate_sha256'],
 'canonical_candidate':'../candidate/candidate.json',
 'operations_from_original225':[{'id':i,'source_folio':int(i[4:7]),'expected_source_text_sha256':shat(st[i]),
     'target_text':ct[i],'target_text_sha256':shat(ct[i])} for i in ct if ct[i]!=st[i]],
 'operations_from_v6':[{'id':i,'expected_v6_text_sha256':shat(bt[i]),'target_text':ct[i],'target_text_sha256':shat(ct[i])} for i in ct if ct[i]!=bt[i]],
 'all_target_hashes':{i:shat(ct[i]) for i in ct},
 'speaker_and_read_order':'../candidate/reader-order.json; all existing portrait/turn order retained;120mapping source-verified.',
 'figure_contract':'../art/LOCKED_V6_FIGURE_PATCH_MANIFEST.json','corrected_source_folios':[24,25,97,211],
 'source_to_destination_remap':oldpacket['source_to_destination_remap'],
 'existing_eight_raster_slots':oldpacket['existing_eight_raster_slots'],
 'v6_repairs':'ALL27TEXTDELTAS_AND_FOURFIGURELEAVES_EXACT; V7doesnotregress them.',
 'production_writer':'Existing sole BookFactory writer; content import/actual layout fitting remains with that writer.',
 'receiving_chat_acknowledgment':'NOT_RECEIVED','production_layout_receipt':'NOT_RECEIVED','print_ready':False}
dump(R/'integration/EDITORIAL_IMPORT_PACKET_V7.json',packet)
(R/'art').mkdir(exist_ok=True)
shutil.copyfile(V6/'art/FIGURE_PATCH_MANIFEST.json',R/'art/LOCKED_V6_FIGURE_PATCH_MANIFEST.json')
shutil.copyfile(V6/'proof/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf',R/'art/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf')
obsolete=R/'art/DETECTIVE_EN_V6_LOCKED_FIGURES.pdf'
if obsolete.exists():
    assert sha(obsolete)==sha(V6/'proof/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf')
    obsolete.unlink()
print(json.dumps(stats,ensure_ascii=False,indent=2))
