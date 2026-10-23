from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).resolve().parent;W=R.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
qa=R/'proof/AUDIT_REPORT_QA.json';x=json.loads(qa.read_text());x['actual_visual_review']={'status':'PASS','reviewer':'root','contact_folios':list(range(1,x['report_pages']+1)),'fullsize_scope':'Opening summary and table transition; final identification; representative fullsize source/delta pages during27→28pagepaginationrepair.','notes':'Removed one-line spillpage. All47beforeaftergroups retained. Contact inspection is layout scope, not a fresh separate language review.'};dump(qa,x)
engine=W/'engine';assert (engine/'scripts/rse-language.py').is_file()
files=[]
for p in R.rglob('*'):
 if not p.is_file():continue
 rel=p.relative_to(R)
 if p.suffix.lower() in ['.png','.jpg','.jpeg','.pyc']:continue
 if any(z in rel.parts for z in ['__pycache__','renders','contacts','audit-renders','visuals','visuals-final','visuals-poppler','visual-work']):continue
 if p.name in ['SHA256_MANIFEST.json','ARCHIVE_RECEIPT.json','LIBRARY_RECEIPT.json','GITHUB_SAVE.json','git-payload.json','delivery-uploads.json']:continue
 if rel.parts[0]=='git-stage':continue
 files.append((p,'detective-v8/'+str(rel)))
for p in engine.rglob('*'):
 if p.is_file() and '__pycache__' not in p.parts:files.append((p,'engine/'+str(p.relative_to(engine))))
manifest={'candidate_sha256':sha(R/'candidate/candidate.json'),'reading_pdf_sha256':sha(R/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf'),
 'audit_pdf_sha256':sha(R/'proof/DETECTIVE_EN_V8_AUDYT_I_ZMIANY.pdf'),'files':[{'path':name,'sha256':sha(p),'bytes':p.stat().st_size} for p,name in sorted(files,key=lambda x:x[1])],
 'manifest_self_hash':'Excluded to avoid a circular hash; delivery receipts created after this immutable archive are saved separately.'}
dump(R/'SHA256_MANIFEST.json',manifest);files.append((R/'SHA256_MANIFEST.json','detective-v8/SHA256_MANIFEST.json'))
out=W/'deliverables/RSE_DETECTIVE_EN_V8_AUDIT_20261022.zip';out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p,name in sorted(files,key=lambda x:x[1]):z.write(p,name)
with zipfile.ZipFile(out) as z:assert z.testzip() is None
receipt={'archive':str(out),'archive_sha256':sha(out),'bytes':out.stat().st_size,'members':len(files),'candidate_sha256':manifest['candidate_sha256'],'pdf_sha256':manifest['reading_pdf_sha256'],'report_sha256':manifest['audit_pdf_sha256']}
dump(R/'qa/ARCHIVE_RECEIPT.json',receipt);print(json.dumps(receipt,indent=2))
