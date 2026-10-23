from pathlib import Path
import copy,hashlib,json,yaml
R=Path(__file__).resolve().parent;W=R.parent
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ch=sha(R/'candidate/candidate.json');receipt=load(R/'qa/LIBRARY_RECEIPT.json');archive=load(R/'qa/ARCHIVE_RECEIPT.json');qa=load(R/'proof/PROOF_QA.json')
assert len(receipt['results'])==3 and all(x['status']=='succeeded' and x['local_metadata_applied'] for x in receipt['results'])
basepath='localization/detective-en-upgrade/2026-10-21';target=basepath+'/v9';stage=R/'git-stage';stage.mkdir(exist_ok=True)
mail=yaml.safe_load((R/'mailbox-before.yml').read_text());before=copy.deepcopy(mail)
mail['updated']='2026-10-22';mail['status']='HM_COMMS_FINAL_OWNER_READ_CANDIDATE__V8_NON_COMMS_LOCKED_AND_PRESERVED'
mail['milestone']['detective_hm_comms_final']={
 'owner_authority':'Explicit22Octoberrequest: restorefulleroriginalHMComms, mergegoodV7, sharpwarmfamilywit; onlyCommsunlocked, allV8puzzlesandothertextpreserved.',
 'path':target,'baseline_v8_sha256':'d0faccca46f0023d564154a1fe3f6a559ce37ac31dc53f6d2b4fe7d4f1b9fc1e','candidate_sha256':ch,
 'scenes':34,'spoken_turns':183,'changed_spoken_turns':173,'changed_stable_units':210,'changed_folios':35,'single_writer':'root','actual_specialist_agents':4,
 'actual_reviews':'native/comedy,audience,meaning,family-continuitylogicPASSexacthash; actualR1FIXhistoryand17turn15sceneclosure retained; all34initialdialoguesread.',
 'protected':'2847nonCommsunits,mixed137prefix,143nonCommsV8repairs,27V6repairs,allpuzzles/hints/solutions and183speakerorder exact.',
 'book_pdf_sha256':qa['book_pdf_sha256'],'book_pages':225,'comms_pdf_sha256':qa['standalone_pdf_sha256'],'comms_pages':34,
 'pdf_checks':'Independent190leaftext/pixelidentity+35strictnonCommsremainders+183speech/speakerroundtripsPASS. Actualindependent16fullsizePopplerviews; root69folios/8contactsoverview+2fullsize. Bookmin10.5pt,Comms11.5pt.',
 'cli':'OWNER_READ_CANDIDATE deterministicPASS; noopenissues/sourceambiguities. Unchangedpuzzlesnotre-solved.',
 'archive_sha256':archive['archive_sha256'],'archive_files':archive['files'],'library':receipt['results'],
 'production_source_renderer_PL_main_merge_publication_freeze':False,'ci':'Nohostedgreenclaim; noActionsdispatch',
 'handoff':'ExistingsoleBookFactorywriter consumes210HMCommsdeltaoverV8/V7contracts. Fullspokenwording andportraitorder retained; noabridgingtofit. Finaltypesetting/physicalproofseparate.'}
for d in mail.get('dependencies_needed',[]):
 if d.get('lane')=='detective_book_factory' and 'd0faccca46f0023d564154a1fe3f6a559ce37ac31dc53f6d2b4fe7d4f1b9fc1e' in d.get('need',''):
  d['need']='Consume EXACT HMCommsfinal candidate '+ch+' and v9/integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_FINAL.json over existingV8/V7contracts.210Commsoperations/3067targethashes,183unchangedspeakerportraitorder; allV8nonComms/27V6repairs/figuresretained. Fullwordingmustsurviveimport; finaltypesetfit/art/physicalproof remainswithsoleBookFactorywriter. NoPLmigration.'
mail['next_safe_task']='ExistingsoleBookFactorywriterconsumesexactHMCommsfinaldelta overlockedV8. Preservefullspokenwordingand183speakerorder; verifyrealproductionfitandphysicalproof. No furtherdialoguerewritewithoutactualdefectorownerrequest.'
mail['checkpoint_reference']=target+'/CHECKPOINT.md'
for p in ['README.md','CHECKPOINT.md','candidate/candidate.json','candidate/HAPPY_MAKERS_COMMS_FINAL_EN.md','integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_FINAL.json']:
 if target+'/'+p not in mail['reusable_outputs']:mail['reusable_outputs'].append(target+'/'+p)
mail['revenue_policy_ack']='OwnerHMComms-onlyrequestcomplete: fouractualusefulreviewers,onewriter,bounded34scenes. Noenginefeatures,puzzlere-audits,publicationorpaidfallback.'
for k,v in before['milestone'].items():assert mail['milestone'][k]==v
(stage/'polish_localization.yml').write_text(yaml.safe_dump(mail,allow_unicode=True,sort_keys=False,width=120))
active={'state':'HM_COMMS_FINAL_OWNER_READ_CANDIDATE__V8_PROTECTED__PRODUCTION_HANDOFF_PENDING','owner':None,'candidate_sha256':ch,
 'baseline_v8_sha256':'d0faccca46f0023d564154a1fe3f6a559ce37ac31dc53f6d2b4fe7d4f1b9fc1e','checkpoint':'v9/CHECKPOINT.md',
 'rule':'OnlyHMCommsupdatedbyexplicitownerrequest. AllotherV8text/puzzlesprotectedandverifiedunchanged. ExistingexclusiveBookFactoryproductionwriterunchanged.',
 'next_safe_task':mail['next_safe_task']}
(stage/'ACTIVE_WRITER.json').write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
(stage/'README.md').write_text('''# Detective Academy English - V8 with final HM Comms\n\nCurrent complete editorial master: `v9/candidate/candidate.json`, exacthash andactualreviews in `v9/CHECKPOINT.md`. TheownerrequestedonlyHMComms changesafterV8. AllV8nonCommscontent,puzzles,hints,solutionsandfiguresremainexact. HistoricalV8/V7/V6stayversioned.\n\nFouractualreviewers/onewriterrestoredoriginalcomicvoicesandmergedsuccessfulV7familybeatsinto34fullerexchanges/183turns. Finalnative/comedy,audience,meaningandcontinuityPASS.210stableunitschangeon35folios;2847nonCommsunits andallpriorpuzzlerepairsremainexact.\n\nStandalone34pageCommsPDF andcomplete225pagebookweresaved, withthecomplete103fileprovenance/review/QAarchive. Exactidentitiesandversions: `v9/qa/LIBRARY_RECEIPT.json`. IndependentPDFbinding:190leavestext/pixelsidentical,35reflowedleavesnonCommsremainderequal,all183speakerturnspresent. Finalvisualscopeisexplicit,notafalse225fullsizeprintclaim.\n\nTheexistingsoleBookFactorywriterconsumes`v9/integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_FINAL.json`overV8/V7contracts. Preservefullspokenwordingandportraitorder; donotabridgetofit. Productiontypesetting/physicalprint/releaseareseparate. NoPLmigration,productrendererchange,merge,publicationorfreeze.\n''')
elements=[];omitted=[]
for p in sorted(R.rglob('*')):
 if not p.is_file() or p.suffix not in ['.json','.md','.py']:continue
 rel=p.relative_to(R);parts=rel.parts
 if any(z in parts for z in ['library-helpers','__pycache__','renders','visual-work','visuals','visuals-poppler','git-stage']):continue
 keep=(len(parts)==1 and p.name not in ['git-payload.json']) or parts[0] in ['qa','reviews']
 if parts[0]=='candidate':keep=p.name not in ['candidate-pages.json','candidate-segments.json']
 if parts[0]=='diagnostic':keep=p.name=='SOURCE_PACKET.md'
 if parts[0]=='integration':keep=p.name=='EDITORIAL_IMPORT_PACKET_HM_COMMS_FINAL.json'
 if parts[0]=='baseline':keep=p.name=='SOURCE_INVENTORY.json'
 if parts[0]=='run':keep=p.name in ['issue-ledger.json','change-scope.json','SOURCE_AND_WORKFLOW.md']
 if parts[0]=='proof':keep=p.suffix=='.json' and len(parts)==2
 if p.name in ['UPLOAD_REQUEST.json','CLI_CHECK.stdout.json']:keep=False
 if not keep:continue
 if p.stat().st_size>600000:omitted.append({'path':str(rel),'sha256':sha(p),'bytes':p.stat().st_size});continue
 elements.append({'path':target+'/'+str(rel),'mode':'100644','type':'blob','content':p.read_text()})
index={'complete_archive_library_file_id':'libfile_da1bed141d108191a32b9d5d4a7a893b','current_version_number':4,'archive_sha256':archive['archive_sha256'],
 'archive_files':archive['files'],'includes':'FullV9textmetadata/engine/R1andfinalreviews/currentPDFs plusexactV8baselinePDFandreadingadapter; verboseCLIandrichmetadata arearchived.',
 'omitted_large_text_files':omitted,'prior_V8_and_V7_contracts':'Alreadyversionedin../v8and../v7; includedinfullarchive.'}
(R/'qa/GITHUB_ARCHIVE_INDEX.json').write_text(json.dumps(index,indent=2)+'\n')
elements=[x for x in elements if not x['path'].endswith('/qa/GITHUB_ARCHIVE_INDEX.json')]
elements.append({'path':target+'/qa/GITHUB_ARCHIVE_INDEX.json','mode':'100644','type':'blob','content':(R/'qa/GITHUB_ARCHIVE_INDEX.json').read_text()})
for f,d in [('polish_localization.yml','orchestration/control-plane/mailboxes/polish_localization.yml'),('ACTIVE_WRITER.json',basepath+'/ACTIVE_WRITER.json'),('README.md',basepath+'/README.md')]:
 elements.append({'path':d,'mode':'100644','type':'blob','content':(stage/f).read_text()})
elements.append({'path':basepath+'/CHECKPOINT.md','mode':'100644','type':'blob','content':(R/'CHECKPOINT.md').read_text()})
(R/'git-payload.json').write_text(json.dumps(elements,ensure_ascii=False,separators=(',',':')))
print(json.dumps({'elements':len(elements),'payload_chars':len((R/'git-payload.json').read_text()),'payload_bytes':(R/'git-payload.json').stat().st_size,'candidate_sha256':ch}))
