from pathlib import Path
import json,yaml,hashlib
R=Path(__file__).resolve().parent;prefix='localization/detective-en-upgrade/2026-10-21/'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ch=sha(R/'candidate/candidate.json');stage=R/'git-stage';stage.mkdir(exist_ok=True)
mail=yaml.safe_load((R/'mailbox-before.yml').read_text());mail['updated']='2026-10-23';mail['status']='HM_COMMS_V10_RHYTHM_OWNER_READ_CANDIDATE__NON_COMMS_PRESERVED'
mail['branch_or_repo_state']['language_tool_current_head']='65191b3518399691dcdcbeaec905539dcfbaab9f'
mail['branch_or_repo_state']['detective_v10_parent_head']='22a43c14a6069bb3f37443c128c3e2d4b890436e'
mail['milestone']='Owner-requested English HMComms rhythm revision complete. One actual agent author, three independent reviewers cover four stages. All34scenes/183turns, all30case-intro/task contexts considered. Real R1FIX and eight-turn final closure, CLI PASS, PDF preservation PASS. Exact candidate '+ch
for d in mail['dependencies_needed']:
 if d['lane']=='detective_book_factory' and 'fa020029' in d['need']:
  d['need']='Consume EXACT V10 HMComms candidate '+ch+' and v10/integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_V10.json over V9/V8/V7 contracts.215Comms operations/3067target hashes;183speaker/portrait turns unchanged. All nonComms text and prior puzzle repairs retained. Preserve full wording through production fit; final art/physical proof stays with existing sole BookFactory writer. No PL migration.'
mail['next_safe_task']='Existing sole BookFactory writer consumes exact V10 HMComms delta. Preserve full dialogue and183speaker order; verify production fit/art and physical proof. No further dialogue rewrite without actual defect or owner request.'
mail['checkpoint_reference']=prefix+'v10/CHECKPOINT.md';mail['revenue_policy_ack']='Four actual useful agents: one dialogue writer, three independent reviewers; bounded34scenes. No puzzle re-audit, engine feature, paid fallback or publication.'
for f in ['README.md','CHECKPOINT.md','candidate/candidate.json','candidate/HAPPY_MAKERS_COMMS_RHYTHM_EN.md','integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_V10.json']:
 p=prefix+'v10/'+f
 if p not in mail['reusable_outputs']:mail['reusable_outputs'].append(p)
(stage/'mailbox.yml').write_text(yaml.safe_dump(mail,allow_unicode=True,sort_keys=False,width=110))
active={'state':'HM_COMMS_V10_RHYTHM_OWNER_READ_CANDIDATE','owner':None,'candidate_sha256':ch,'baseline_candidate_sha256':'fa020029727aebaedbefe36c8a8ea7704ee350a5d9def5ff195b3377fa72d3a3','checkpoint':'v10/CHECKPOINT.md','rule':'Only220HMComms units editable.2847protected nonComms units exact; all143V8nonComms repairs exact.34scenes/183speaker turns. No further rewrite without defect/owner request.','next_safe_task':mail['next_safe_task']}
(stage/'ACTIVE_WRITER.json').write_text(json.dumps(active,indent=2)+'\n')
(stage/'README.md').write_text('''# Detective Academy English — V10 Happy Makers dialogue

Current complete editorial master: `v10/candidate/candidate.json`; exact hash and actual receipts: `v10/CHECKPOINT.md`. The owner requested another HMComms-only revision after rejecting V9 rhythm and humour. One actual dialogue author and three independent reviewers covered all30case contexts,34scenes and183turns. Four real stages and deterministic CLI PASS; eight bounded final fixes retained in history.

Read `v10/proof/HAPPY_MAKERS_COMMS_V10_EN.pdf` or full225page `v10/proof/DETECTIVE_EN_V10_FULL_ENGLISH.pdf` from the saved archive/Library versions. Exact file identities and versions: `v10/qa/LIBRARY_RECEIPT.json`.2847protected nonComms units and143V8nonComms repairs remain exact. Independent190leaf and35reflowedleaf preservation,183speech/speaker pairs PASS. Actual visual scope is recorded; no physical-print claim.

Existing sole BookFactory writer consumes `v10/integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_V10.json` over V9/V8/V7 contracts. Preserve full wording and portrait order. Historical sources stay versioned. No product renderer, PL migration, main merge, publication or freeze.
''')
files=[]
for p in R.rglob('*'):
 if not p.is_file() or any(s in p.parts for s in ['git-stage','renders','__pycache__']):continue
 rel=p.relative_to(R)
 if p.suffix not in ['.json','.md','.py','.yml']:continue
 if p.name.startswith('git-payload') or p.name=='mailbox-before.yml' or str(rel) in ['qa/GITHUB_SAVE.json','qa/upload-request.json']:continue
 # Large reproducible adapter intermediates are fully archived; canonical and source truth remain in Git.
 if str(rel) in ['candidate/candidate-segments.json','candidate/candidate-pages.json'] or rel.parts[0]=='run':continue
 files.append({'path':prefix+'v10/'+str(rel),'mode':'100644','type':'blob','content':p.read_text()})
files += [{'path':'orchestration/control-plane/mailboxes/polish_localization.yml','mode':'100644','type':'blob','content':(stage/'mailbox.yml').read_text()},*({'path':prefix+f,'mode':'100644','type':'blob','content':(stage/f).read_text()} for f in ['README.md','ACTIVE_WRITER.json']),{'path':prefix+'CHECKPOINT.md','mode':'100644','type':'blob','content':(R/'CHECKPOINT.md').read_text()}]
(R/'git-payload.json').write_text(json.dumps(files,ensure_ascii=False))
print(json.dumps({'files':len(files),'payload_chars':len((R/'git-payload.json').read_text()),'candidate_sha256':ch}))
