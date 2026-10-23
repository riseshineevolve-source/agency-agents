from pathlib import Path
import hashlib,json,zipfile,shutil
R=Path(__file__).resolve().parent;W=R.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
ch=sha(R/'candidate/candidate.json')
proof=R/'proof/DETECTIVE_EN_V7_FULL_READING_PROOF.pdf';comparison=R/'proof/HM_COMMS_ORIGINAL_V6_V7_COMPARISON.pdf'
visual=json.loads((R/'reviews/proof-native/VISUAL_REVIEW.json').read_text())
assert visual['status']=='PASS'
assert sha(proof) in json.dumps(visual)
compvisual=json.loads((R/'proof/VISUAL_COMPARISON_REVIEW.json').read_text())
assert compvisual['status']=='PASS' and compvisual['comparison_pdf_sha256']==sha(comparison)
qa=json.loads((R/'proof/PROOF_QA.json').read_text())
assert qa['reading_proof_sha256']==sha(proof) and qa['comparison_sha256']==sha(comparison)
qa['actual_visual_review']='PASS: independent69folio/25fullsize reading-proof sample; all34comparisonpages seen byroot. Unsampled readingfolios excluded fromvisualclaim; all225copy/offpage and52pixel-identitychecks PASS.'
qa['visual_receipts']=['../reviews/proof-native/VISUAL_REVIEW.json','VISUAL_COMPARISON_REVIEW.json']
dump(R/'proof/PROOF_QA.json',qa)
stats=json.loads((R/'qa/FINAL_CONTENT_VERIFICATION.json').read_text())
prior=json.loads((R/'diagnostic/PRIOR_COMMS_AUDIT.json').read_text())
dump(R/'baseline/SOURCE_INVENTORY.json',{
 'owner225':{'library_file_id':'libfile_cfd6cede96588191806f3fac3602a3b9','sha256':stats['original225_pdf_sha256'],'pages':225},
 'v6':{'candidate_sha256':stats['baseline_candidate_sha256'],'source_repairs':27,'corrected_source_folios':[24,25,97,211],
       'reading_proof_library_file_id':'libfile_94471e8e05548191adec7eee0ccdf2e0','current_version_before_v7':0},
 'v7':{'candidate_sha256':ch,'scope':'Complete225folio diagnosis;701unit bounded allowlist;229actualchanges.',
       'run':'run-r2','parent_r1_candidate':'candidate-v7-r1.json'},
 'tool':{'cli_sha256':sha(W/'rse/scripts/rse-language.py'),'project_profile_sha256':sha(W/'rse/tools/rse-language/profiles/detective-academy.json'),
         'installed_skill_pr':'https://github.com/riseshineevolve-source/agency-agents/pull/40'},
 'product_or_pl_source_migration':False})
run=json.loads((R/'run-r2/run.json').read_text())
dump(R/'run-r2/RUN_RECEIPT.json',{'run_sha256':run['manifest_sha256'],'source_sha256':run['source_sha256'],
 'mode':'upgrade','source_language':'en','target_language':'en','scope':'bounded','project':'detective-academy',
 'full_run_metadata':'Included in recovery archive; recreate with build_candidate.py and pinned source/tool.',
 'run_json_sha256':sha(R/'run-r2/run.json'),'functional_brief_sha256':sha(R/'run-r2/functional-brief.json'),
 'candidate_sha256':ch,'deterministic_and_four_independent_stages':'PASS; exact QA/CLI_CHECK.json and reviews/FINAL_REVIEW_BUNDLE.json.'})
checkpoint=f'''# Detective EN V7 checkpoint

Status: OWNER_READ_CANDIDATE. Complete English editorial pass; no owner content freeze or publication.

Exact candidate: `{ch}`. Source authority: owner's explicit request to use rse-language for another complete English upgrade, especially witty, affectionate Happy Makers Comms. Baseline V6: `{stats['baseline_candidate_sha256']}`.

All225folios and30mainComms were actually read. V7 changes229stableunits/48folios and105spoken turns in25mainComms;05/11/16/17/27remain whole strong scenes. Earlier V6vsowner225 changed15mainComms/27turns, with no extra V5→V6Comms editing. Three-way artifact makes the difference reviewable.

Actual independent native/audience/meaning/logic reviews PASS on the exact final hash. R1concrete findings are retained and closed. CLI `run-r2` reports OWNER_READ_CANDIDATE with deterministicPASS and no unresolved issues/source ambiguities.

All27V6fixes, maps,90hints,30answers and reasoning remain exact. Only nonmechanic summary212block12 fixes the first-instruction chronology. Four0records/14maps/finaleinputs unchanged. No new map solve or invented geometry claim.

Reading artifact:225folios, `{sha(proof)}`, {proof.stat().st_size}bytes.173text leaves and52locked/source-designed leaves.225copy/offpagechecks and52pixel-identitychecksPASS. Independent visual69folio sample/25fullsizePASS; unsampled156notvisuallyapproved.

Comparison artifact:34pages, `{sha(comparison)}`. All34visually inspected;495main-scene spoken-version roundtripsPASS.

Import `integration/EDITORIAL_IMPORT_PACKET_V7.json` through the existing sole BookFactory writer. It includes original225/V6 operations,3067target hashes, speaker mapping and retained destination remaps. Four corrected V6figure leaves reused unchanged. Actual product import, final fitting, receiving-chat acknowledgment and print proof remain unclaimed.

Source branch: `codex/detective-en-story-upgrade-20261021`, PR43. No main merge or Actions dispatch. CI at final checkpoint not confirmed as green. Historical V5/V6artifacts stay versioned. PLV04R8/FINAL70authority unchanged.
'''
(R/'CHECKPOINT.md').write_text(checkpoint)
# Manifest excludes itself and mutable external persistence receipts: no self-hash loop.
def eligible(p):
 rel=p.relative_to(R)
 if any(z.startswith('.') or z=='__pycache__' for z in rel.parts):return False
 if rel.parts[0] in ['tmp']:return False
 if p.name in ['SHA256_MANIFEST.json','PERSISTENCE_RECEIPT_V7.json','LOCAL_DELIVERY.json','mailbox-before.yml']:return False
 if p.suffix.lower() in ['.png','.jpg','.jpeg','.pyc']:return rel.as_posix() in ['reviews/story-diagnostic/source-p120.png','reviews/proof-native/original137.png']
 return p.is_file()
files=sorted(p for p in R.rglob('*') if p.is_file() and eligible(p))
manifest={'candidate_sha256':ch,'scope':'All packaged files excluding this manifest and later external persistence receipts.','files':[{ 'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
dump(R/'SHA256_MANIFEST.json',manifest)
files.append(R/'SHA256_MANIFEST.json')
archive=W/'deliverables/RSE_DETECTIVE_EN_V7_EDITORIAL_20261021.zip';archive.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:z.write(p,'detective-v7/'+p.relative_to(R).as_posix())
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
delivery={'candidate_sha256':ch,'archive_path':str(archive),'archive_sha256':sha(archive),'archive_bytes':archive.stat().st_size,
 'reading_pdf':{'path':str(proof),'sha256':sha(proof),'bytes':proof.stat().st_size,'pages':225},
 'comparison_pdf':{'path':str(comparison),'sha256':sha(comparison),'bytes':comparison.stat().st_size,'pages':34},
 'archive_files':len(files),'receipt_added_after_archive':'External persistence receipt is deliberately outside the immutable archive.'}
dump(R/'integration/LOCAL_DELIVERY.json',delivery)
request={'uploads':[
 {'local_path':str(proof),'purpose':'replace_library_file','library_file_id':'libfile_94471e8e05548191adec7eee0ccdf2e0','expected_current_version':0,'version_reason':'V7: full English editorial upgrade,25Comms/105turns; allV6puzzlefixes preserved.'},
 {'local_path':str(comparison),'purpose':'create_library_file','library_artifact_type':'report'},
 {'local_path':str(archive),'purpose':'replace_library_file','library_file_id':'libfile_da1bed141d108191a32b9d5d4a7a893b','expected_current_version':1,'version_reason':'V7: updated complete source/review/recovery packet, full225folioPDF and original/V6/V7Comms comparison.'}]}
dump(R/'tmp/library-upload-request.json',request)
print(json.dumps(delivery,indent=2))
