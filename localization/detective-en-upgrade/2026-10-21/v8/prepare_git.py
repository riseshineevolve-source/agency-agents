from pathlib import Path
import copy,hashlib,json,yaml
R=Path(__file__).resolve().parent;W=R.parent
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ch=sha(R/'candidate/candidate.json');ph=sha(R/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf')
archive=load(R/'qa/ARCHIVE_RECEIPT.json');receipt=load(R/'qa/LIBRARY_RECEIPT.json')
assert len(receipt['results'])==3 and all(x['status']=='succeeded' and x['local_metadata_applied'] for x in receipt['results'])
basepath='localization/detective-en-upgrade/2026-10-21';target=basepath+'/v8'
mail=yaml.safe_load((R/'mailbox-before.yml').read_text());old=copy.deepcopy(mail)
mail['updated']='2026-10-22'
mail['status']='V8_OWNER_READ_CANDIDATE__ACTUAL_JOINT_WHOLE_BOOK_AUDIT_COMPLETE'
milestone={'owner_authority':'Explicit22October request: actual agents for joint whole-book English audit, all errors and weak passages fixed, final full version.',
 'path':target,'candidate_sha256':ch,'baseline_v7_sha256':'df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1',
 'source_folios':225,'stable_units':3067,'changed_units':146,'changed_folios':41,'semantic_groups':47,'actual_specialist_agents':4,'single_writer':'root',
 'agent_lenses':['native/story/comedy','child-teen/support/mentor/developmental sensitivity','all30puzzle meaning/logic','reader/promise/marketing/sales'],
 'actual_review':'Four real independent final stages PASS exacthash; fullbaseline/all-case reading plus exact bounded final closure, not fabricated repeated whole-book rereads.',
 'puzzles':'All16freshCSP fullrosters=1;all14nonspatialactuallyresolved;90hints/30solutionsread;05all720→1;21all24uprightorders→1;26derived14maps.',
 'preservation':'All27V6repairs,16witnessboards,30answerheaders,107printedplacements and31puzzle/evidencefigures unchanged.',
 'corrections':'Explicitgeometry/marker/occupancykey;8zoneexclusions+14rowtrace;15workedmaps+05code/27overlayproof;hatprop;accessiblecredential/help;Rulecopy132;promise/payoff04/23/25;Diloending;148/184nativePDFtextpatches.',
 'comms_delta':'All30mainComms reviewed; onlyNiniCase04taskredirectchangedfromV7. Strong existing jokes preserved.',
 'reading_pdf_sha256':ph,'reading_pdf_pages':225,'report_pdf_sha256':sha(R/'proof/DETECTIVE_EN_V8_AUDYT_I_ZMIANY.pdf'),'report_pdf_pages':28,
 'proof':'225serialization/offpage checksPASS;minimum173regeneratedbody10.5pt;50retainedleavespixelidentical;148/184boundedtextpatches;actualaudience42fullsize+reader19+independentevidencebindings;root225thumbnail-layoutscope.',
 'archive_sha256':archive['archive_sha256'],'library':receipt['results'],
 'cli':'run-r2 OWNER_READ_CANDIDATE deterministicPASS, no unresolvedissues/sourceambiguities.',
 'production_source_or_renderer_changed':False,'pl_versions_changed':False,'main_merged':False,'published':False,'frozen':False,'ci':'NOT_CONFIRMED_GREEN; no Actionsdispatch',
 'handoff':'ExistingexclusiveBookFactorywriter consumesV8packet over inheritedV7contract and fourV6correctedleaves. Finalproductionfit/print/ownerrelease separate.'}
mail['milestone']['detective_en_v8_joint_audit']=milestone
for d in mail['dependencies_needed']:
 if d.get('lane')=='detective_book_factory' and 'df4b39f8793de32' in d.get('need',''):
  d['need']='Consume EXACT V8 candidate '+ch+' and v8/integration/EDITORIAL_IMPORT_PACKET_V8.json over inherited V7 original-source packet.146V8operations/3067targethashes; all27V6repairs/fourcorrectedleaves preserved. Existing16→15/27→26remaps retained. Finalproductimport/fit/print receipts remain pending; no PLmigration.'
for p in ['README.md','candidate/candidate.json','proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf','proof/DETECTIVE_EN_V8_AUDYT_I_ZMIANY.pdf']:
 path=target+'/'+p
 if path not in mail['reusable_outputs']:mail['reusable_outputs'].append(path)
mail['next_safe_task']='Existing soleBookFactorywriter consumes exact V8 editorial import packet, inherited V7sourcecontract and preserved V6figures; bind final typeset import/fit/print receipts. No further prose pass without concrete defect or new ownerrequest.'
mail['checkpoint_reference']=target+'/CHECKPOINT.md'
mail['revenue_policy_ack']='Owner-requested actualjointwholeEnglishauditandbounded146unitrepairs complete. Fourusefulspecialists,onewriter. Noenginefeatures, competingtranslation, Actionsdispatch orpublication.'
for k in old:
 if k not in ['updated','status','milestone','dependencies_needed','reusable_outputs','next_safe_task','checkpoint_reference','revenue_policy_ack']:
  assert mail[k]==old[k],('unrelated mailbox drift',k)
for k,v in old['milestone'].items():assert mail['milestone'][k]==v
stage=R/'git-stage';stage.mkdir(exist_ok=True)
(stage/'polish_localization.yml').write_text(yaml.safe_dump(mail,allow_unicode=True,sort_keys=False,width=120))
active={'state':'V8_OWNER_READ_CANDIDATE__ACTUAL_REVIEWS_PASS__PRODUCTION_HANDOFF_PENDING','owner':None,
 'candidate_sha256':ch,'checkpoint':'v8/CHECKPOINT.md','rule':'V7historical;V8owner-authorizedjointEnglishaudit. ExistingBookFactoryexclusiveproductionwriter. AllV6repairs retained.','next_safe_task':mail['next_safe_task']}
(stage/'ACTIVE_WRITER.json').write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
(stage/'README.md').write_text('''# Detective Academy English — current V8\n\nThe current complete English editorial master is under `v8/`; exact candidate, reading PDF, actual joint review and scope are in `v8/CHECKPOINT.md`.\n\nV8 completes the owner-requested multidisciplinary whole-book audit: four actual specialist agents, one writer,47semantic repairs/146stableunits/41folios. All30cases/90hints/30solutions reviewed. All16maps have one full roster under actual fresh independent enumeration; all14other tasks checked. All27V6repairs,107placements and final inputs remain.\n\nThe225pageEnglishPDF and28pagePolishaudit/change report are saved, together with the complete source/QA/review archive. Exact Library identities and versions are in `v8/qa/LIBRARY_RECEIPT.json`. Historical V7/V6 remain versioned.\n\nExisting soleBookFactorywriter consumes `v8/integration/EDITORIAL_IMPORT_PACKET_V8.json` over inheritedV7sourcecontract. Productionlayout/physicalprint/release are separate. No PLmigration, productrendererchange, mainmerge, publication or freeze.\n''')
files=[];omitted=[]
top={'README.md','CHECKPOINT.md','RECOVERY.md','OWNER_AUTHORITY.json','SHA256_MANIFEST.json','build_candidate.py','build_book.py','build_audit_report.py','finalize.py','package.py','prepare_git.py','edits-base.json','edits-clarity.json','edits-solutions.json'}
for p in R.rglob('*'):
 if not p.is_file() or p.suffix not in ['.json','.md','.py']:continue
 rel=p.relative_to(R);parts=rel.parts
 keep=(len(parts)==1 and p.name in top) or parts[0] in ['qa','integration','source-models','reviews']
 if parts[0]=='candidate':keep=p.name not in ['candidate-segments.json','candidate-pages.json']
 if parts[0]=='baseline':keep=p.name in ['SOURCE_INVENTORY.json','v8-intake-r2.json']
 if parts[0]=='run-r2':keep=p.name in ['change-scope.json','issue-ledger.json','SOURCE_AND_WORKFLOW.md']
 if parts[0]=='proof':keep=len(parts)==2 and p.suffix=='.json'
 if any(z in parts for z in ['__pycache__','visuals','visuals-final','visuals-poppler','visual-work','renders','contacts','audit-renders','git-stage']):keep=False
 if str(rel)=='qa/GITHUB_ARCHIVE_INDEX.json':keep=False
 if not keep:continue
 archive_only=(str(rel) in ['baseline/v8-intake-r2.json','integration/INHERITED_V7_IMPORT_PACKET.json','reviews/puzzles-r1/spatial-enumerations.json','reviews/reader-market-r1/reader-market-review.json','reviews/audience-r1/audience-review-v7-diagnostic.json','reviews/story-humor-r1/findings.json','reviews/audience-final/audience-coverage.json','reviews/story-humor-final/coverage.json','reviews/story-humor-r1/coverage.json','reviews/reader-market-final/full_findings.json','source-models/HISTORICAL_TRUTH_REVIEW.json'] or (parts[0]=='reviews' and p.name in ['build_report.py','build_review.py']))
 if archive_only:
  omitted.append({'path':str(rel),'sha256':sha(p),'bytes':p.stat().st_size});continue
 if p.stat().st_size>950000:continue
 files.append((p,target+'/'+str(rel)))
elements=[{'path':path,'mode':'100644','type':'blob','content':p.read_text()} for p,path in sorted(files,key=lambda x:x[1])]
index={'full_archive_library_file_id':'libfile_da1bed141d108191a32b9d5d4a7a893b','current_version_number':3,'archive_sha256':archive['archive_sha256'],'omitted_duplicate_or_detailed_files':omitted,'reason':'Complete140filearchive retains full run/richmetadata and verbose coverage; Git keeps canonical master, actual receipts, diagnostic prose, finalfreshsolver outputs and exact import/QA. Inherited V7packet already versioned under v7/.'}
indexpath=R/'qa/GITHUB_ARCHIVE_INDEX.json';indexpath.write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
elements.append({'path':target+'/qa/GITHUB_ARCHIVE_INDEX.json','mode':'100644','type':'blob','content':indexpath.read_text()})
for fn,dest in [('polish_localization.yml','orchestration/control-plane/mailboxes/polish_localization.yml'),('ACTIVE_WRITER.json',basepath+'/ACTIVE_WRITER.json'),('README.md',basepath+'/README.md'),('CHECKPOINT.md',basepath+'/CHECKPOINT.md')]:
 p=R/'CHECKPOINT.md' if fn=='CHECKPOINT.md' else stage/fn
 elements.append({'path':dest,'mode':'100644','type':'blob','content':p.read_text()})
out=R/'git-payload.json';out.write_text(json.dumps(elements,ensure_ascii=False,separators=(',',':')))
print(json.dumps({'elements':len(elements),'payload_bytes':out.stat().st_size,'candidate_sha256':ch,'archive_sha256':archive['archive_sha256']},indent=2))
