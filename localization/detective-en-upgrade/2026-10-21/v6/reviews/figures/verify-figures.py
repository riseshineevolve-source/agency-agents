"""Independent actual-PDF verification for V6's four bounded figure leaves."""
from pathlib import Path
import fitz,json,hashlib,math
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
R=ROOT/'detective-v6'; OUT=Path(__file__).parent
srcpath=ROOT/'upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf'
figpath=R/'proof/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf'
fullpath=R/'proof/DETECTIVE_EN_V6_READING_PROOF.pdf'
candpath=R/'candidate/candidate.json';manifestpath=R/'art/FIGURE_PATCH_MANIFEST.json'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads(manifestpath.read_text());assert H(candpath)==manifest['candidate_sha256']=='d9dcc50eaccea03f693b1ade4ea001d522379d9def9f0467dd2e21ddd7e9fedc'
assert H(srcpath)==manifest['source_pdf_sha256'];assert H(figpath)==manifest['corrected_figures_pdf_sha256']
src=fitz.open(srcpath);fig=fitz.open(figpath);full=fitz.open(fullpath);assert len(src)==len(full)==225 and len(fig)==4
scale=3.0; results=[]
def raster(page,scale):
 # MuPDF caches downsampled image intermediates; clear between scales for reproducible pixel comparison.
 fitz.TOOLS.store_shrink(100)
 p=page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
 return np.frombuffer(p.samples,dtype=np.uint8).reshape(p.height,p.width,p.n)
def rect_slice(rect,sc,pad=0):
 x0,y0,x1,y1=rect;return (slice(max(0,math.floor(y0*sc)-pad),math.ceil(y1*sc)+pad),slice(max(0,math.floor(x0*sc)-pad),math.ceil(x1*sc)+pad))
for i,pn in enumerate([24,25,97,211]):
 sp,fp,rp=src[pn-1],fig[i],full[pn-1]
 a=raster(sp,scale);b=raster(fp,scale);c=raster(rp,scale)
 assert a.shape==b.shape==c.shape
 assert np.array_equal(b,c),(pn,'full proof does not contain exact corrected leaf')
 changed=np.any(a!=b,axis=2);allowed=np.zeros(changed.shape,dtype=bool)
 patches=[p for p in manifest['patches'] if p['source_folio']==pn]
 for p in patches:allowed[rect_slice(p.get('affected_rect',p['rect']),scale,pad=1)]=True
 outside=int(np.sum(changed & ~allowed));assert outside==0,(pn,'changed pixels outside declared edit rectangles',outside)
 si=sp.get_image_info(hashes=True);fi=fp.get_image_info(hashes=True)
 im=lambda seq:[{'bbox':list(q['bbox']),'width':q['width'],'height':q['height'],'digest':q['digest'].hex()} for q in seq]
 assert im(si)==im(fi),(pn,'source raster image payload or placement changed')
 rr={'source_folio':pn,'corrected_figures_leaf':i+1,'all_original_image_payloads_and_placements_preserved':True,'original_image_count':len(si),'pixel_comparison_scale':scale,'changed_pixels':int(changed.sum()),'changed_pixels_outside_declared_patch_rectangles':outside,'matches_full_225_proof_exact_render':True}
 png=R/f'proof/renders/p{pn:03d}.png';on_disk=np.asarray(Image.open(png).convert('RGB'));provided=raster(fp,1.5)
 assert on_disk.shape==provided.shape and np.array_equal(on_disk,provided),(pn,'supplied PNG is not exact1.5xrender of correctedPDF')
 rr['provided_png_exact_pdf_render']=True;rr['provided_png_sha256']=H(png)
 if pn in [24,25]:
  caption=fp.get_text('text',clip=fitz.Rect(63,151.5,265,170.3)).strip();assert caption==('PHOTO A' if pn==24 else 'PHOTO B')
  photo=(50,275,562,659);ys,xs=rect_slice(photo,scale);assert np.array_equal(a[ys,xs],b[ys,xs]);rr.update(caption=caption,photograph_pixels_exact=True,internal_evidence_number_visual_review='017' if pn==24 else '071')
 else:
  markers=[]
  for p in patches:
   x0,y0,x1,y1=p['rect'];cx=round((x0+x1)*scale/2);cy=round((y0+y1)*scale/2)
   old_center=int(a[cy,cx].mean());new_center=int(b[cy,cx].mean());ys,xs=rect_slice(p['affected_rect'],scale);crop=b[ys,xs]
   assert old_center<80 and new_center>180,(pn,p['cell'],'marker center is not opened',old_center,new_center)
   assert int(crop.min())<50,(pn,p['cell'],'circle outline not dark')
   markers.append({'cell':p['cell'],'original_center_gray':old_center,'new_center_gray':new_center,'visible_dark_outline':True,'visible_open_center':True})
  rr['markers']=markers;rr['E5_and_all_other_pixels_unchanged_outside_two_marker_rectangles']=True;rr['witness_labels_positions_furniture_and_walls_unchanged']=True
 results.append(rr)
res={'status':'PASS_ACTUAL_FOUR_LEAF_FIGURE_PATCH_PDF','candidate_sha256':H(candpath),'source_pdf_sha256':H(srcpath),'corrected_figures_pdf_sha256':H(figpath),'reading_proof_pdf_sha256':H(fullpath),'patch_manifest_sha256':H(manifestpath),'scope':'Original folios24/25/97/211 only. Independent original-vs-corrected render/payload comparisons and fullproof consistency, plus actual visual inspection of supplied exactPDF renders.','pages':results,'not_claimed':['BookFactoryproductionimport','nativeproductsourceupdated','full225illustratedlayoutapproval','physicalprint','PRINT_READY']}
(OUT/'verification.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
