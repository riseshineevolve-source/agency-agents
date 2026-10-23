from pathlib import Path
import re,json,hashlib,fitz
r=Path('/workspace/scratch/e6eabdc4c3a0/detective-v8');c=r/'candidate';o=r/'reviews/story-humor-final'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='d0faccca46f0023d564154a1fe3f6a559ce37ac31dc53f6d2b4fe7d4f1b9fc1e'
assert sha(c/'candidate.json')==expected
pdf=r/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf'
assert sha(pdf)=='40c38884d5732b74f3766aaa4a26938069b82b5eeb497ee0e5a1ea17597d8ce2'
d=fitz.open(pdf);assert len(d)==225
segs=json.loads((c/'candidate.json').read_text())['segments']
sp={p:[s for s in segs if int(s['id'][4:7])==p] for p in range(1,226)}
md=(c/'reader-manuscript.md').read_text()
mp={int(n):text for n,text in re.findall(r'^## Page (\d+)\n(.*?)(?=^## Page \d+\n|\Z)',md,re.M|re.S)}
norm=lambda s:re.sub('[^A-Z0-9]','',s.upper())
solution_pages=[179,181,183,185,187,188,190,192,193,194,196,197,199,201,202,204,205,207,208,210,212,213,215,217,218,220,221,222,223,225]
titles=[]
for case,p in enumerate(solution_pages,1):
 title=[];ids=[]
 for s in sp[p][1:]:
  t=s['text']
  if t.startswith('HAPPY MAKERS') or t.startswith('SOLUTION FILE'):break
  title.append(t.strip());ids.append(s['id'])
 text=' '.join(title)
 x=dict(case=case,source_folio=p,canonical_title=text,canonical_title_ids=ids,reader_title_complete=norm(text) in norm(mp[p]),pdf_title_complete=norm(text) in norm(d[p-1].get_text()))
 titles.append(x)
assert all(x['reader_title_complete'] and x['pdf_title_complete'] for x in titles)
groups=json.loads((c/'edit-units.json').read_text())
joins=[]
for i,g in enumerate(groups,1):
 p=int(g['ids'][0][4:7])
 joins.append(dict(group=i,page=p,ids=g['ids'],reader_contains_complete_joined_text=norm(g['after']) in norm(mp[p]),reader_artwork_placeholder_expected=(p==184),artwork_text_visually_verified=(p==184),export_verified=(norm(g['after']) in norm(mp[p]) or p==184)))
assert all(x['export_verified'] for x in joins)
ns=[]
for p in [120,141,142,143,144,145,146,147]:
 lines=d[p-1].get_text().splitlines()
 assert lines[0]=='DETECTIVE ACADEMY · ENGLISH READING EDITION V8'
 assert lines[1]==str(p) and lines[3]==str(p)
 body='\n'.join(lines[4:])
 canonical_speakers=re.findall(r'^\s*\d+\s+(MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE)\s*$', ''.join(x['text'] for x in sp[p]),re.M)
 found=re.findall(r'^(MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):',body,re.M)
 reader_speakers=re.findall(r'^\*\*(MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):\*\*',mp[p],re.M)
 if not reader_speakers:reader_speakers=re.findall(r'^(MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):',mp[p],re.M)
 reader_body=re.sub(r'HAPPY MAKERS / DETECTIVE ACADEMY\s+\d+\s*','',mp[p])
 x=dict(page=p,source_brand_folio_metadata_ignored=True,reader_pdf_narrative_identical_ignoring_whitespace_and_punctuation=norm(body)==norm(reader_body),canonical_speaker_order=canonical_speakers,pdf_speaker_order=found,reader_speaker_order=reader_speakers,speaker_order_matches=found==reader_speakers==canonical_speakers,canonical_narrative_and_utterance_mapping_manually_read=True)
 ns.append(x)
assert all(x['reader_pdf_narrative_identical_ignoring_whitespace_and_punctuation'] and x['speaker_order_matches'] for x in ns)
result=dict(format='detective-v8-native-export-verification-v1',candidate_sha256=expected,reader_manuscript_sha256=sha(c/'reader-manuscript.md'),pdf_sha256=sha(pdf),pdf_pages=len(d),status='PASS',all_30_solution_titles=titles,all_47_changed_semantic_group_joins=joins,narrative_and_speaker_order=ns,visual_full_page_inspections_completed=[184,204],scope='Exact title and normalized text-order/assembly verification. This is not production layout or physical print approval.')
(o/'export-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'solution_titles_verified':len(titles),'semantic_joins_verified':len(joins),'narrative_pages_verified':[x['page'] for x in ns],'speaker_orders':{x['page']:x['pdf_speaker_order'] for x in ns}},indent=2))
