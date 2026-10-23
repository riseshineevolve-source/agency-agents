from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).resolve().parent;W=R.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=[]
for p in R.rglob('*'):
 if not p.is_file() or any(x in p.parts for x in ['__pycache__','renders','visual-work','visuals','git-stage']):continue
 rel=p.relative_to(R)
 if p.suffix not in ['.json','.md','.py','.pdf']:continue
 if str(rel) in ['qa/ARCHIVE_RECEIPT.json','qa/LIBRARY_RECEIPT.json','qa/GITHUB_SAVE.json'] or p.name.startswith('git-payload'):continue
 if p.suffix=='.pdf' and rel.parts[0]!='proof':continue
 files.append(p)
for rel in ['build_book.py','candidate/candidate.json','candidate/candidate-segments.json','candidate/candidate-pages.json','candidate/reader-manuscript.md','candidate/reader-order.json','proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf','qa/BOUNDARY_CHECK.json','qa/FINAL_CONTENT_VERIFICATION.json','reviews/FINAL_REVIEW_BUNDLE.json']:
 files.append(W/'detective-v8'/rel)
for rel in ['candidate/candidate.json','candidate/candidate-segments.json','candidate/reader-manuscript.md','candidate/reader-order.json','qa/FINAL_CONTENT_VERIFICATION.json','reviews/FINAL_REVIEW_BUNDLE.json']:
 files.append(W/'detective-v9'/rel)
files.append(W/'recovery/unpacked/detective-v7/candidate/candidate.json')
files.extend(p for p in (W/'engine-v10').rglob('*') if p.is_file() and p.suffix in ['.py','.json','.md'] and '__pycache__' not in p.parts)
files=sorted(set(files))
manifest={'candidate_sha256':sha(R/'candidate/candidate.json'),'files':[{'path':str(p.relative_to(W)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files if p.name!='SHA256_MANIFEST.json']}
(R/'SHA256_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
if R/'SHA256_MANIFEST.json' not in files:files.append(R/'SHA256_MANIFEST.json')
out=W/'deliverables/RSE_DETECTIVE_HM_COMMS_V10_20261023.zip';out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:z.write(p,str(p.relative_to(W)))
with zipfile.ZipFile(out) as z:assert z.testzip() is None
receipt={'archive_path':str(out),'archive_sha256':sha(out),'bytes':out.stat().st_size,'files':len(files),'candidate_sha256':sha(R/'candidate/candidate.json'),'complete_final_sources_reviews_qa':True,'baseline_v8_pdf_included':True}
(R/'qa/ARCHIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
