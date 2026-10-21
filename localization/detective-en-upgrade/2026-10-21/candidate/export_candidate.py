import json,hashlib,re
from pathlib import Path
R=Path('detective-upgrade');C=R/'candidate';x=json.loads((C/'candidate-segments.json').read_text());proto=json.loads((R/'run-v5/candidate.json').read_text());proto['segments']=[{'id':s['id'],'text':s['target_text']} for s in x['segments']]
(C/'candidate.json').write_text(json.dumps(proto,ensure_ascii=False,indent=2)+'\n')
allowed=set(json.loads((R/'run-v5/change-scope.json').read_text())['allowed_changed_segments']);changed=[s['id'] for s in x['segments'] if s['text']!=s['target_text']];protected=[s for s in x['segments'] if not s['editable'] and s['text']!=s['target_text']]
assert not set(changed)-allowed
assert not protected
report={'candidate_sha256':hashlib.sha256((C/'candidate.json').read_bytes()).hexdigest(),'source_pdf_sha256':x['source_sha256'],'run_sha256':proto['run_sha256'],'segment_count':len(x['segments']),'actual_changed_ids':changed,'outside_allowlist':sorted(set(changed)-allowed),'protected_drift':[s['id'] for s in protected],'page_coverage':list(range(1,226)),'status':'DRAFT_AWAITING_INDEPENDENT_REVIEW','visual_fit':'NOT RUN','production_renderer':'NOT MODIFIED'}
(C/'writer-validation.json').write_text(json.dumps(report,indent=2)+'\n')
coverage=[]
for p in range(1,226):
 ss=[s for s in x['segments'] if s['page']==p];coverage.append({'pdf_page':p,'segment_ids':[s['id'] for s in ss],'changed_ids':[s['id'] for s in ss if s['decision']=='FIX'],'decision':'FIX' if any(s['decision']=='FIX' for s in ss) else 'KEEP','review_scope':'Narrative/voice/logic and reader handoffs; all printed clues/hints/answers retained except explicitly allowed non-clue production-aside deletion at p158. Artwork remains source-bound.'})
(C/'page-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
ledger=json.loads((C/'change-ledger.json').read_text())
for e in ledger:
 e['actual_changed_ids']=[s['id'] for s in x['segments'] if s['page']==e['page'] and s['decision']=='FIX']
 e['reasoning_status']='writer proposal for independent review'
(C/'change-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(report['candidate_sha256'],len(changed),'changed',len(coverage),'pages')
