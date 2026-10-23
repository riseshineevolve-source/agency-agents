"""Bounded source-PDF amendments and a reading proof, not a production renderer."""
from pathlib import Path
import json, hashlib, re
import fitz

R=Path(__file__).resolve().parent
W=R.parent
O=W/'detective-upgrade'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dump=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
SOURCE=W/'upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf'
candidate_hash=sha(R/'candidate/candidate.json')
assert candidate_hash=='d9dcc50eaccea03f693b1ade4ea001d522379d9def9f0467dd2e21ddd7e9fedc'
assert sha(SOURCE)=='9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0'
(R/'tmp').mkdir(exist_ok=True)
(R/'proof/renders').mkdir(parents=True,exist_ok=True)

# Reuse the accepted reader-order adapter. Story/finale text is unchanged.
reader_code=(O/'candidate/build_reader.py').read_text()
reader_code=reader_code.replace("R=Path('detective-upgrade');", "R=Path('detective-v6');")
reader_code=reader_code.replace("(R/'qa/source-page-map.json')", "(Path('detective-upgrade')/'qa/source-page-map.json')")
exec(compile(reader_code,str(R/'tmp/reused-reader-adapter.py'),'exec'),{})
reader=R/'candidate/reader-manuscript.md'
text=reader.read_text()
# Separate numbered witness statements even when source extraction split a
# statement across PDF blocks. This changes presentation, never wording.
sections=re.split(r'(^## Page \d+\s*$)',text,flags=re.M)
for j in range(1,len(sections),2):
    page_body=sections[j+1]
    if 'WITNESS RECORD' in page_body:
        pos=page_body.index('WITNESS RECORD')+len('WITNESS RECORD')
        head,body=page_body[:pos],page_body[pos:]
        matches=list(re.finditer(r'(?<!\S)(0[1-9]|[12][0-9]|30)(?=\s+[A-Z])',body))
        if matches:
            records=[]
            for k,m in enumerate(matches):
                end=matches[k+1].start() if k+1<len(matches) else len(body)
                records.append(re.sub(r'\s+',' ',body[m.start():end]).strip())
            page_body=head+'\n\n'+'\n\n'.join(records)+'\n\n'
        # Let the reader scan local rules and map keys on separate paragraphs.
        page_body=page_body.replace('In this case, beside','\n\nIn this case, beside')
        page_body=page_body.replace('PERSON MAY STAND ON:', '\n\nPERSON MAY STAND ON:')
        page_body=page_body.replace('SQUARE BLOCKED BY:', '\n\nSQUARE BLOCKED BY:')
        sections[j+1]=page_body
text=''.join(sections)
for page,caption in [(24,'PHOTO A'),(25,'PHOTO B')]:
    pattern=rf'(## Page {page}\n\n)(.*?)(?=\n\n## Page )'
    text=re.sub(pattern,lambda m:m.group(1)+caption+'\n\nSee the photograph on this page in the illustrated reading proof.\n\n',text,flags=re.S)
for page in [97,211]:
    pattern=rf'(## Page {page}\n\n)(.*?)(?=\n\n## Page )'
    text=re.sub(pattern,lambda m:m.group(1)+'See the Case 20 map on this page in the illustrated reading proof.\n\n',text,flags=re.S)
reader.write_text(text)

# Amend only the two external photo labels and four Case20 object markers.
source=fitz.open(SOURCE)
patches=[]
font_bytes=source.extract_font(223)[3]
for folio,caption in [(24,'PHOTO A'),(25,'PHOTO B')]:
    page=source[folio-1]
    rect=fitz.Rect(63,151.5,265,170.3)
    swatch=page.get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(270,156,272,158),colorspace=fitz.csGRAY)
    bar_grey=sorted(swatch.samples)[len(swatch.samples)//2]/255
    page.add_redact_annot(rect,fill=(bar_grey,bar_grey,bar_grey))
    page.apply_redactions(images=0,graphics=0,text=0)
    page.insert_font(fontname='V6Caption',fontbuffer=font_bytes)
    page.insert_text((66,165.2),caption,fontname='V6Caption',fontsize=12.6,color=(1,1,1))
    patches.append({'source_folio':folio,'kind':'external_photo_caption','new_text':caption,'rect':list(rect),
                    'photograph_pixels':'PRESERVED','font':'Original embedded Roboto Condensed Bold, 12.6pt'})

for folio in [97,211]:
    page=source[folio-1]
    # First source-map invocation is the visible axes-aligned grid. A second
    # clipped historical invocation on211 lies under the black MAP KEY bar;
    # it must not be mistaken for a second visible map or patched there.
    info=next(i for i in page.get_image_info(xrefs=True) if (i['width'],i['height'])==(1028,1090))
    bounds=fitz.Rect(info['bbox']); sx=bounds.width/1028;sy=bounds.height/1090
    for cell,(x,y,w,h) in [('E7',(595,1059,13,13)),('F7',(736,1059,12,12))]:
        rect=fitz.Rect(bounds.x0+x*sx,bounds.y0+y*sy,bounds.x0+(x+w)*sx,bounds.y0+(y+h)*sy)
        # Read existing local floor colour; no raster art is regenerated.
        sample=page.get_pixmap(matrix=fitz.Matrix(4,4),clip=fitz.Rect(rect.x0-.8,rect.y0-1.4,rect.x0+.8,rect.y0-.6),colorspace=fitz.csGRAY)
        bg=sorted(sample.samples)[len(sample.samples)//2]/255
        erase=rect+(-.45,-.45,.45,.45)
        page.draw_rect(erase,color=None,fill=(bg,bg,bg),overlay=True)
        page.draw_oval(rect,color=(0,0,0),fill=(bg,bg,bg),width=.6,overlay=True)
        patches.append({'source_folio':folio,'kind':'blocked_square_to_usable_circle','cell':cell,
                        'rect':list(rect),'affected_rect':list(erase),'source_map_bbox':list(bounds),
                        'map_image_xref':info['xref'],'classification':'usable cadet bunk',
                        'native_marker_bbox':[x,y,w,h],'new_shape':'open circle','floor_grey':bg})

figure_path=R/'proof/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf'
figures=fitz.open()
for folio in [24,25,97,211]:figures.insert_pdf(source,from_page=folio-1,to_page=folio-1)
figures.set_metadata({'title':'Detective Academy EN V6: corrected photo labels and Case20 map markers',
                      'author':'Rise.Shine.Evolve.','subject':'Bounded owner-authorized source corrections; not a release proof'})
figures.save(figure_path,garbage=4,deflate=True)
figures.close()
dump(R/'art/FIGURE_PATCH_MANIFEST.json',{'source_pdf_sha256':sha(SOURCE),'candidate_sha256':candidate_hash,
     'owner_authority':'../OWNER_AUTHORITY.json','patches':patches,'corrected_figures_pdf':figure_path.name,
     'corrected_figures_pdf_sha256':sha(figure_path),'source_folios':[24,25,97,211],
     'room_geometry_and_all_witness_coordinates':'UNCHANGED','production_renderer_modified':False})

# Reuse the existing approved text-proof builder; then substitute original
# evidence pages. This is an owner reading proof with source puzzle artwork,
# not a competing BookFactory layout or a claim of final print fit.
proof_code=(O/'proof/build-proof.py').read_text().replace("R=Path('detective-upgrade')", "R=Path('detective-v6')")
proof_code=proof_code.replace("out=R/'proof/DETECTIVE_EN_V5_EDITORIAL_TEXT_PROOF.pdf'", "out=R/'tmp/V6_TEXT_ONLY_INTERMEDIATE.pdf'")
proof_code=proof_code.replace('text proof V5','reading proof V6')
proof_code=proof_code.replace('DETECTIVE ACADEMY · EDITORIAL TEXT PROOF','DETECTIVE ACADEMY · READING PROOF V6')
proof_code=proof_code.replace('Text review only · Original puzzle artwork remains in the source PDF','Reading proof · Final book layout pending')
exec(compile(proof_code,str(R/'tmp/reused-text-proof-builder.py'),'exec'),{})
pure=fitz.open(R/'tmp/V6_TEXT_ONLY_INTERMEDIATE.pdf')
pages=json.loads((R/'candidate/candidate-pages.json').read_text())
roles={p['page']:p['role'] for p in json.loads((O/'qa/source-page-map.json').read_text())['pages']}
art_pages=[]
final=fitz.open()
for p in range(1,226):
    t=pages[p-1]['text']
    artwork=roles[p]=='puzzle_or_evidence' or 'SOLUTION MAP' in t or 'SOLUTION PHOTO' in t
    donor=source if artwork else pure
    final.insert_pdf(donor,from_page=p-1,to_page=p-1)
    if artwork:art_pages.append(p)
out=R/'proof/DETECTIVE_EN_V6_READING_PROOF.pdf'
final.set_metadata({'title':'Detective Academy: full English V6 reading proof', 'author':'Rise.Shine.Evolve.',
 'subject':'Full V6 editorial text with original puzzle artwork and authorized source corrections. Final BookFactory typesetting and print proof pending.'})
final.save(out,garbage=4,deflate=True)
final.close()

# Exact proof checks: every leaf is either the new text leaf or the amended
# original illustration leaf. Every copied evidence leaf is pixel-compared.
actual=fitz.open(out);checks=[]
pristine=fitz.open(SOURCE)
saved_figures=fitz.open(figure_path)
figure_index={24:0,25:1,97:2,211:3}
for p in range(1,226):
    a=actual[p-1]
    b=(saved_figures[figure_index[p]] if p in figure_index else pristine[p-1]) if p in art_pages else pure[p-1]
    assert a.get_text()==b.get_text(),('text copy mismatch',p)
    if p in art_pages:
        pa=a.get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
        pb=b.get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
        assert pa.samples==pb.samples,('evidence pixel copy mismatch',p)
    for block in a.get_text('blocks'):
        if block[6]==0:assert fitz.Rect(block[:4]) in a.rect,('off-page text',p,block[:4])
    checks.append({'folio':p,'source':'amended_original_artwork' if p in art_pages else 'exact_v6_text_proof','status':'PASS'})
assert len(actual)==225
for p,label in [(24,'PHOTO A'),(25,'PHOTO B')]:
    t=actual[p-1].get_text()
    assert label in t and not any(s in t for s in ['017','071','OLDER','LATER','ARCHIVED','CURRENT'])
for p in [20,24,25,27,42,54,74,96,97,154,164,165,190,211]:
    actual[p-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(R/f'proof/renders/p{p:03d}.png')
dump(R/'proof/PROOF_QA.json',{'candidate_sha256':candidate_hash,'reading_proof_sha256':sha(out),
     'reading_proof_pages':225,'exact_text_leaf_checks':225-len(art_pages),'exact_evidence_pixel_checks':len(art_pages),
     'photo_caption_checks':'PASS; only PHOTO A/B, original photo images untouched',
     'page_checks':checks,'changed_page_visual_review':'PENDING','production_layout':'NOT_RUN','print_ready':False})
print(json.dumps({'reading_proof':str(out),'pages':225,'artwork_pages':len(art_pages),'corrected_figures':str(figure_path),'patches':len(patches)},indent=2))
