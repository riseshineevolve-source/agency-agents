from pathlib import Path
import hashlib,json,zipfile,shutil
R=Path(__file__).resolve().parent;W=R.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
engine=R/'engine-snapshot'
for rel in ['scripts/rse-language.py','tools/rse-language/profiles/gentle-steps.json','tools/rse-language/profiles/generic.json','tools/rse-language/profiles/detective-academy.json']:
 p=engine/rel;p.parent.mkdir(exist_ok=True,parents=True);shutil.copy2(W/'engine-v10'/rel,p)
files=[]
for p in R.rglob('*'):
 if not p.is_file() or any(x in p.parts for x in ['private-helpers','render','git-stage','__pycache__']):continue
 rel=p.relative_to(R)
 if p.suffix not in ['.md','.json','.py','.docx','.yml']:continue
 if p.name in ['source-bundle.json','git-payload.json','LIBRARY_RECEIPT.json','GITHUB_SAVE.json','ARCHIVE_RECEIPT.json','UPLOAD_REQUEST.json','SHA256_MANIFEST.json']:continue
 files.append(p)
manifest={'candidates':json.loads((R/'qa/FINAL_SUMMARY.json').read_text())['candidates'],'files':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(files)]}
mp=R/'qa/SHA256_MANIFEST.json';mp.write_text(json.dumps(manifest,indent=2)+'\n');files.append(mp)
out=R/'deliverables/RSE_SWIETA_ARTYKULY_PL_EN_V4_20261023.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(files):z.write(p,str(p.relative_to(R)))
with zipfile.ZipFile(out) as z:assert z.testzip() is None
receipt={'path':str(out),'sha256':sha(out),'bytes':out.stat().st_size,'files':len(files),'complete_sources_reviews_cli_and_word':True}
(R/'qa/ARCHIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
