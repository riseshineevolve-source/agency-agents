"""Verify exact independent receipts, prepare handoff, package reproducible V6."""
from pathlib import Path
import json, hashlib, subprocess, zipfile, shutil
import yaml

R=Path(__file__).resolve().parent; W=R.parent; O=W/'detective-upgrade'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
dump=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
ch=h(R/'candidate/candidate.json')
assert ch=='d9dcc50eaccea03f693b1ade4ea001d522379d9def9f0467dd2e21ddd7e9fedc'
base=load(R/'baseline/candidate-v5.json');new=load(R/'candidate/candidate.json')
assert [s['id'] for s in base['segments']]==[s['id'] for s in new['segments']]
delta=[b['id'] for a,b in zip(base['segments'],new['segments']) if a['text']!=b['text']]
assert delta==[s['id'] for s in load(R/'candidate/change-ledger.json')]
assert len(delta)==27 and len(new['segments'])==3067
model=load(R/'reviews/puzzle-initial/independent-results.json')
assert len(model['cases'])==9 and all(x['complete_assignment_count']==1 and x['matches_intended_roster_postcheck_only'] for x in model['cases'])

receipts=[]
for path,stages in [('reviews/native/review.json',['native_language','audience']),('reviews/puzzle-final/review.json',['meaning','logic'])]:
    p=R/path;o=load(p)
    assert o['candidate_sha256']==ch and o['status'].startswith('PASS')
    for stage in stages:
        receipts.append({'stage':stage,'status':'PASS','candidate_sha256':ch,'reviewer':o['reviewer'],
                         'evidence':'Actual independent V6 bounded delta/closure review;3040unchanged units inherit accepted V5. Artwork/production scope is separate.',
                         'evidence_file':path,'evidence_sha256':h(p)})
dump(R/'qa/reviews.cli.json',{'candidate_sha256':ch,'reviews':receipts})
ledger=load(R/'run-r2/issue-ledger.json');ledger['candidate_sha256']=ch
for issue in ledger['issues']:
    issue['classification']='FIX';issue['final_classification']='KEEP'
    issue['resolution']='Owner-authorized source correction implemented; exact language/mechanics/logic and actual corrected figure reviews pass.'
dump(R/'run-r2/issue-ledger.json',ledger)
report=R/'qa/FINAL_LANGUAGE_CHECK_V6.json'
if report.exists():
    assert load(report)['candidate_sha256']==ch
    report.unlink()  # generated QA only, never a source/master/review
subprocess.run(['python',str(W/'rse/scripts/rse-language.py'),'check','--run',str(R/'run-r2'),
                '--candidate',str(R/'candidate/candidate.json'),'--reviews',str(R/'qa/reviews.cli.json'),
                '--output',str(report)],check=True,capture_output=True,text=True)
assert load(report)['deterministic_qa']=='PASS' and not load(report)['unresolved_issues']

fig=load(R/'reviews/figures/review.json')
assert ch in json.dumps(fig) and 'PASS' in fig['status']
for p in [R/'proof/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf',R/'proof/DETECTIVE_EN_V6_READING_PROOF.pdf']:
    assert h(p) in json.dumps(fig),('Unbound figure/proof',p)
qa=load(R/'proof/PROOF_QA.json');qa['changed_page_visual_review']='PASS_ROOT_VISUAL_14_FOLIOS_AND_INDEPENDENT_FOUR_LEAF_PIXEL_REVIEW'
qa['root_visually_reviewed_folios']=[20,24,25,27,42,54,74,96,97,154,164,165,190,211]
qa['independent_figure_review']='../reviews/figures/review.json';dump(R/'proof/PROOF_QA.json',qa)

orig=load(O/'source/intake-v5.json')['segments'];original={s['id']:s['text'] for s in orig}
v5={s['id']:s['text'] for s in base['segments']}
targets={s['id']:s['text'] for s in new['segments']}
ops=[{'id':s['id'],'source_folio':int(s['id'][4:7]),'expected_source_text_sha256':hashlib.sha256(original[s['id']].encode()).hexdigest(),
      'target_text':s['text'],'target_text_sha256':hashlib.sha256(s['text'].encode()).hexdigest()} for s in new['segments'] if s['text']!=original[s['id']]]
packet={'format':'rse-detective-editorial-import-v6','candidate_sha256':ch,
 'source_pdf_sha256':h(W/'upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf'),
 'v5_baseline_sha256':h(R/'baseline/candidate-v5.json'),'canonical_candidate':'../candidate/candidate.json',
 'operations_from_original225':ops,
 'operations_from_v5':[{'id':s['id'],'expected_v5_text_sha256':s['baseline_sha256'],'target_text':s['after'],'target_text_sha256':s['target_sha256']} for s in load(R/'candidate/change-ledger.json')],
 'all_target_hashes':{s['id']:hashlib.sha256(s['text'].encode()).hexdigest() for s in new['segments']},
 'figure_contract':'../art/FIGURE_PATCH_MANIFEST.json','corrected_source_folios':[24,25,97,211],
 'source_to_destination_remap':{'source16':'destination15','source27':'destination26','other_folios':'Use existing BookFactory mapping; never treat source folio as destination unconditionally.'},
 'existing_eight_raster_slots':'Retain prior source slot coverage/import requirements; PHOTO24/25 caption amendments now explicitly owner-authorized.',
 'production_writer':'Existing exclusive BookFactory writer only; no renderer/source branch changed by this packet.',
 'receiving_chat_acknowledgment':'NOT_RECEIVED','production_layout_receipt':'NOT_RECEIVED','print_ready':False}
dump(R/'integration/EDITORIAL_IMPORT_PACKET_V6.json',packet)

summary={'status':'V6_OWNER_READ_CANDIDATE__SIX_SOURCE_EXCEPTIONS_REPAIRED', 'candidate_sha256':ch,
 'baseline_v5_sha256':h(R/'baseline/candidate-v5.json'),'units':3067,'changed_units_from_v5':27,'unchanged_units_from_v5':3040,
 'changed_source_folios':sorted({int(i[4:7]) for i in delta}),'operations_from_original225':len(ops),
 'repaired_map_cases':[2,7,10,15,20],'independent_variants_checked':9,'each_complete_assignment_count':1,
 'intended_rosters_and_case26_case30_payoffs':'PRESERVED',
 'case03':'PHOTO A/B only external captions. Inside-photo017/071evidence and later archive trail preserved.',
 'figure_edits':'Four marker replacements on two Case20 leaves, plus two external photo captions. All raster artwork unchanged.',
 'reading_proof':'225pages,177text leaves plus48original evidence leaves including corrected figures.',
 'language_qa':load(report)['status'],'figure_qa':fig['status'],
 'production_import_and_final_typesetting':'PENDING_SOLE_BOOK_FACTORY_WRITER','physical_print':'NOT_RUN','freeze_granted':False,'publication':False,
 'github_ci':'NOT_CONFIRMED_AT_FINAL_HEAD__LOCAL_CHECKS_COMPLETED_NO_ACTIONS_DISPATCH',
 'model_policy_ack':{'policy':'rse-weekly-usage-2026-10-21-v1','recommended_profile':'production','runtime_model_observed':'NOT_EXPOSED','runtime_reasoning_observed':'NOT_EXPOSED','runtime_speed_observed':'NOT_EXPOSED','application_status':'RECOMMENDATION_ONLY'},
 'revenue_policy_ack':'Bounded owner-requested six-case release-blocker correction only; no factory features or new translation.',
 'next_safe_task':'Existing BookFactory writer consumes exact V6 text/figure packet, binds mapped destination receipts and final illustrated typesetting. No new localization rewrite without concrete defect.'}
dump(R/'qa/FINAL_V6_SUMMARY.json',summary)
readme=f'''# Detective Academy EN V6 — owner-directed corrections, 21 October 2026

Current full English candidate: `candidate/candidate.json`, SHA256 `{ch}`.
V5 remains the unchanged historical baseline. V6 changes exactly27of3067units;3040remain identical.

## Closed exceptions

- Case03: only PHOTO A/PHOTO B external labels. The real017/071difference remains inside photographs. The page27callback now relies on internal photograph evidence, not removed captions.
- Case02: whole-grid corner and explicit local shared-edge/same-room beside.
- Case07: explicit metal frame C2 grid-distance anchor, all visible wheeled equipment cases, matched solution wording. C2is an owner-authorized repair, not a claim that old source identified its range marker.
- Case10: visible wheeled robot arm replaces ambiguous chargingpod; hint updated.
- Case15: independent row/column direction offsets, same-room shared-edge beside, symbol-led key matching actual usable furniture.
- Case20: explicit lower-row/right-column/one-row-one-column instructions; E5/E7/F7allusablecadetbunks; E7/F7markers corrected in both unsolved97and solved211.

All five repaired maps have exactly ONE complete intended witness assignment. Nine independently enumerated variants pass. Four actual corrected figure leaves preserve all raster payloads, walls and witness placements. Two independent exact-text reviewers and the independent figure reviewer passed their stated scopes. Existing Case26message and Case30inputs remain unchanged.

## Files

- `proof/DETECTIVE_EN_V6_READING_PROOF.pdf`: complete225-page reading proof with177textproofleaves and48original illustration/evidence leaves. Includes the six bounded visual amendments.
- `proof/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf`: original leaves24,25,97,211with actual caption/symbol corrections.
- `candidate/reader-manuscript.md`: clean full reader text companion.
- `candidate/change-ledger.json`: exact27before/afterchanges.
- `integration/EDITORIAL_IMPORT_PACKET_V6.json`: {len(ops)}operations from original225or27fromV5, plus3067targethashes and figure contract. Consume all prior V5story improvements too.
- `qa/FINAL_LANGUAGE_CHECK_V6.json`, `qa/FINAL_V6_SUMMARY.json`, `reviews/`: actual hash-bound QA and scope limits.

## Production handoff

The exclusive BookFactory writer remains responsible for real product import and final layout. Source16maps to destination15; source27maps to destination26in the recovered Studio adapter. Do not paste by folio number alone. Preserve the prior eight raster-slot receipts requirement. The attached reading proof is suitable for content review; it is not final BookFactory typesetting or KDP print approval. Product source/renderer, PLR8, main and publication are unchanged.

Source PDF: owner225pageattachment `DETECTIVE_ACADEMY_EN_20261021_225P.pdf`, Library id `libfile_cfd6cede96588191806f3fac3602a3b9`, SHA256 `{packet['source_pdf_sha256']}`. Original source bytes are not duplicated in this package. Current RSE language CLI is required for rechecks. `run-r2` is the canonical bounded run; the earlier preparation run is historical and excluded.

Model/revenue policies acknowledged: bounded exception work, deterministic checks first, no Actions dispatch or paid fallback. Runtime model controls were not exposed; no client model change is claimed. No content freeze, release or publication granted.
'''
(R/'README.md').write_text(readme)
(R/'CHECKPOINT.md').write_text(readme)

mail=yaml.safe_load((R/'integration/mailbox-before.yml').read_text())
mail['updated']='2026-10-21';mail['status']=summary['status']
mail.setdefault('milestone',{})
if not isinstance(mail['milestone'],dict):mail['previous_milestone']=mail['milestone'];mail['milestone']={}
mail['milestone']['detective_en_v6_owner_fixes']={'candidate_sha256':ch,'path':'localization/detective-en-upgrade/2026-10-21/v6',
 'changed_units':27,'unchanged_units':3040,'repaired_cases':[2,3,7,10,15,20], 'full_assignments_each_repaired_map':1,
 'independent_models':9,'actual_corrected_figures':'PASS','reading_proof_pages':225,'production_import':'PENDING_EXISTING_BOOK_FACTORY_WRITER'}
mail['model_policy_ack']=summary['model_policy_ack']
mail['revenue_policy_ack']=summary['revenue_policy_ack']
mail['next_safe_task']=summary['next_safe_task']
mail['checkpoint_reference']='localization/detective-en-upgrade/2026-10-21/v6/CHECKPOINT.md'
mail['blocker']=[b for b in mail.get('blocker',[]) if not (isinstance(b,str) and b.startswith('Current EN owner225source:'))]
mail['blocker'].append('V6 EN content and four corrected source leaves are complete; actual sole-BookFactory import, final typesetting and print proof receipts remain pending.')
mail['resolved_en_source_exceptions']={'version':'V6','cases':[2,3,7,10,15,20], 'status':'OWNER_AUTHORIZED_REPAIRS_COMPLETE','candidate_sha256':ch}
mail.setdefault('dependencies_needed',[])
if not isinstance(mail['dependencies_needed'],list):mail['dependencies_needed']=[mail['dependencies_needed']]
mail['dependencies_needed']=[d for d in mail['dependencies_needed'] if not (isinstance(d,dict) and d.get('lane')=='detective_book_factory' and 'Consume currentV5' in d.get('need',''))]
mail['dependencies_needed'].append({'lane':'detective_book_factory','need':'Consume exact owner-authorized V6 candidate d9dcc50e... and EDITORIAL_IMPORT_PACKET_V6.json.27V5deltas/'+str(len(ops))+'original225deltas,3067targethashes, corrected source24/25/97/211. Source16→destination15/source27→destination26. Supply actual final typeset import/fit receipts; no chat delivery inferred.'})
(R/'integration/polish_localization.yml').write_text(yaml.safe_dump(mail,sort_keys=False,allow_unicode=True,width=110))
lease={'state':'V6_OWNER_READ_CANDIDATE__SOURCE_EXCEPTIONS_CLOSED__PRODUCTION_HANDOFF_PENDING','owner':None,
 'candidate_sha256':ch,'checkpoint':'v6/CHECKPOINT.md','rule':'V5retained; V6is exact owner-authorized bounded correction. Existing BookFactory remains sole production writer.',
 'next_safe_task':summary['next_safe_task']}
dump(R/'integration/ACTIVE_WRITER.json',lease)

# Write package only after all reviews and checks. Exclude temporary renders,
# superseded preparation, local helper scripts and the old mailbox snapshot.
manifest={}
include=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(R)
    if any(part.startswith('.') for part in rel.parts):continue
    if p.suffix.lower() in ['.png','.jpg','.jpeg']:continue
    if rel.parts[0] in ['tmp','run'] or 'renders' in rel.parts or rel.name in ['mailbox-before.yml','SHA256_MANIFEST.json','LOCAL_DELIVERY.json','v6-intake.json']:continue
    include.append(p);manifest[str(rel)]=h(p)
dump(R/'SHA256_MANIFEST.json',manifest)
include.append(R/'SHA256_MANIFEST.json')
archive=W/'deliverables/RSE_DETECTIVE_EN_V6_FIXED_20261021.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in include:z.write(p,arcname='RSE_DETECTIVE_EN_V6/'+str(p.relative_to(R)))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert hashlib.sha256(z.read('RSE_DETECTIVE_EN_V6/candidate/candidate.json')).hexdigest()==ch
dump(R/'integration/LOCAL_DELIVERY.json',{'archive':str(archive.resolve()),'archive_sha256':h(archive),'archive_bytes':archive.stat().st_size,
 'reading_proof_sha256':h(R/'proof/DETECTIVE_EN_V6_READING_PROOF.pdf'),'figure_proof_sha256':h(R/'proof/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf')})
print(json.dumps({'candidate_sha256':ch,'original225_operations':len(ops),'v5_operations':27,'archive':str(archive),'archive_bytes':archive.stat().st_size,'local_qa':'PASS'},indent=2))
