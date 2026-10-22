"""Render the exact English master with retained evidence and bounded native PDF text repairs."""
from pathlib import Path
from io import BytesIO
import hashlib, html, json, re
import fitz
from PIL import Image, ImageChops
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph, KeepInFrame, Table, TableStyle, Spacer

R=Path(__file__).resolve().parent; W=R.parent
V7=W/'recovery/unpacked/detective-v7'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ch=sha(R/'candidate/candidate.json')
canon=json.loads((R/'candidate/candidate.json').read_text())
ct={s['id']:s['text'] for s in canon['segments']}
source=fitz.open(V7/'proof/DETECTIVE_EN_V7_FULL_READING_PROOF.pdf')
untouched=fitz.open(V7/'proof/DETECTIVE_EN_V7_FULL_READING_PROOF.pdf')
(R/'proof/renders').mkdir(parents=True,exist_ok=True)
(R/'proof/fonts').mkdir(exist_ok=True)
fontdir='/usr/share/fonts/truetype/dejavu/'
for name,file in [('Book','DejaVuSans.ttf'),('BookBold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,fontdir+file))
pdfmetrics.registerFontFamily('Book',normal='Book',bold='BookBold',italic='Book',boldItalic='BookBold')
body=ParagraphStyle('body',fontName='Book',fontSize=10.5,leading=14.1,spaceAfter=7,textColor=HexColor('#20252a'))
head=ParagraphStyle('head',parent=body,fontName='BookBold',fontSize=11.2,leading=14.8,spaceAfter=9)
tablebody=ParagraphStyle('table',parent=body,spaceAfter=0,leading=13.2)
tablehead=ParagraphStyle('tablehead',parent=tablebody,fontName='BookBold',textColor=white)
smallhead=ParagraphStyle('smallhead',parent=tablehead,fontSize=9.5,leading=12)

def para(text,style=body,preserve=False):
    text=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',text)
    value=html.escape(text)
    value=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',value)
    value=value.replace('\n','<br/>') if preserve else re.sub(r'\s*\n\s*',' ',value)
    return Paragraph(value,style)

def table(rows,widths):
    cells=[[para(v,tablehead if i==0 else tablebody) for v in row] for i,row in enumerate(rows)]
    t=Table(cells,colWidths=widths,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#243f46')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[white,HexColor('#edf2ef')]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,0),.4,HexColor('#243f46'))]))
    return t

def flow_for(text):
    text=re.sub(r'(?m)^(?:\d+\s+)?(MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):[ \t]*',r'**\1:** ',text)
    text=re.sub(r'\n(?=\*\*(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):\*\*)','\n\n',text)
    text=re.sub(r'(\*\*(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):\*\*)\s*\n\s*\n',r'\1 ',text)
    text=re.sub(r'HAPPY MAKERS / DETECTIVE ACADEMY\s*\n\s*\d{3}\s*(?:\n\s*)?','',text)
    text=re.sub(r'(?m)^HINT VAULT // LEVEL ([123])\n\s*\nHINT VAULT // LEVEL \1$',r'HINT VAULT // LEVEL \1',text)
    result=[]
    for b in re.split(r'\n\s*\n',text):
        b=b.strip()
        if not b:continue
        if 'CHECK YOUR FOURTEEN MAPS' in b:
            lines=b.splitlines();rows=[['CASE','EMPTY ROOM','LETTER']]
            caption=[]
            for line in lines:
                m=re.fullmatch(r'(\d{2}) — (.+) — ([A-Z])',line)
                if m:rows.append(list(m.groups()))
                else:caption.append(line)
            assert len(rows)==15
            result.extend([para(' '.join(caption),head),table(rows,[57,400,63]),Spacer(1,8)])
            continue
        if "THEO / DEX / MACK / SASHA / SASHA'S COMPANIONS" in b:
            before,tail=b.split('THEO / DEX / MACK / SASHA / SASHA\'S COMPANIONS',1)
            if before.strip():result.append(para(before.strip()))
            rows=[['THEO','DEX','MACK','SASHA',"SASHA'S COMPANIONS"]]
            for line in tail.strip().splitlines():rows.append([x.strip() for x in line.split('/')])
            assert len(rows)==3 and all(len(x)==5 for x in rows)
            result.extend([table(rows,[65,65,65,65,260]),Spacer(1,8)])
            continue
        ishead=len(b)<115 and b.upper()==b and re.search('[A-Z]',b) and not b.startswith('**')
        preserve=any(len(z.strip())>3 and z.strip().upper()==z.strip() and re.search('[A-Z]',z) for z in b.splitlines())
        result.append(para(b,head if ishead else body,preserve))
    return result

def furniture(c,p):
    c.setFillColor(HexColor('#283940'));c.setFont('BookBold',9)
    c.drawString(46,759,'DETECTIVE ACADEMY · ENGLISH READING EDITION V8')
    c.setFont('Book',8);c.drawRightString(566,759,str(p))
    c.setFillColor(HexColor('#677278'));c.setFont('Book',7.5)
    c.drawString(46,26,'The Happy Makers · The Mystery of Room Zero')
    c.drawRightString(566,26,str(p))

def draw_flow(c,flow,x,y,width,height):
    raw=sum(f.wrap(width,10000)[1]+f.getSpaceAfter() for f in flow)
    box=KeepInFrame(width,height,flow,mode='shrink',hAlign='LEFT',vAlign='TOP')
    bw,bh=box.wrapOn(c,width,height);box.drawOn(c,x,y-bh)
    scale=1/getattr(box,'_scale',1)
    return {'body_font_min':round(scale*10.5,2),'raw_height':round(raw,2)}

parts=re.split(r'^## Page (\d+)\s*$',(R/'candidate/reader-manuscript.md').read_text(),flags=re.M)
assert len(parts)==451
buf=BytesIO();c=canvas.Canvas(buf,pagesize=(612,792));fits=[]
c.setTitle('Detective Academy — English V8');c.setAuthor('Rise.Shine.Evolve.')
for k in range(1,len(parts),2):
    p=int(parts[k]);text=parts[k+1].strip();furniture(c,p)
    if p==11:
        cflow=flow_for('MAP CASES\nREAD THIS ONCE')
        draw_flow(c,cflow,46,736,520,48)
        rules=ct['page011.block02']
        sections=re.split(r'(?m)^(1 COORDINATES|2 PLACE THE WITNESSES|3 CLUE WORDS|4 READ EACH CASE\'S MAP KEY)\n',rules)
        draw_flow(c,[para(sections[0].strip())],46,694,520,65)
        columns=[[],[]]
        for j in range(1,len(sections),2):
            which=0 if j<5 else 1
            columns[which].append(para(sections[j],head))
            for line in sections[j+1].strip().splitlines():
                line=re.sub(r'^([A-Z /-]+:)',r'**\1**',line)
                columns[which].append(para(line))
        ff=[draw_flow(c,fl,46+j*270,635,250,594) for j,fl in enumerate(columns)]
        fits.append({'folio':p,'columns':2,'body_font_min':min(x['body_font_min'] for x in ff),'details':ff})
    else:
        flow=flow_for(text)
        ff=draw_flow(c,flow,46,738,520,682)
        fits.append({'folio':p,'columns':1,**ff})
    c.showPage()
c.save();pure=fitz.open(stream=buf.getvalue(),filetype='pdf')

# Two native text repairs. No image pixels, numbered difference markers or map geometry are redrawn.
patches={148:fitz.Rect(93.5,363.5,292,374),184:fitz.Rect(65,646,547,700)}
def embed_source_font(page,fontname,alias):
    clean=lambda x:re.sub('[^a-z0-9]','',x.lower())
    font=next(f for f in page.get_fonts() if clean(f[3])==clean(fontname))
    _,ext,_,data=source.extract_font(font[0])
    path=R/'proof/fonts'/('source-'+alias+'.'+ext);path.write_bytes(data)
    page.insert_font(fontname=alias,fontfile=str(path))
    return alias,str(path)
pg=source[147];bold,boldfile=embed_source_font(pg,'RobotoCondensed-Bold','IndexRepair')
pg.add_redact_annot(patches[148],fill=(1,1,1));pg.apply_redactions(images=0,graphics=0)
pg.insert_text((94,371.2),ct['page148.block15'].strip(),fontname=bold,fontfile=boldfile,fontsize=7.9,color=(0,0,0))
pg=source[183];regular,regularfile=embed_source_font(pg,'RobotoCondensed-Regular','FeedbackRepair')
pg.add_redact_annot(patches[184],fill=(1,1,1));pg.apply_redactions(images=0,graphics=0)
feedback=''.join(ct[f'page184.block{i:02d}'] for i in [15,16,17]).strip()
left=pg.insert_textbox(fitz.Rect(72,648,540,700),feedback,fontname=regular,fontfile=regularfile,fontsize=12.5,align=1,color=(0,0,0))
assert left>=0,('feedback overflow',left)

boundary=json.loads((R/'qa/BOUNDARY_CHECK.json').read_text())
art=set(boundary['source_art_folios']);designed={13,26,148,149};preserved=art|designed
book=fitz.open();donors={}
for p in range(1,226):
    donor=source if p in preserved else pure
    book.insert_pdf(donor,from_page=p-1,to_page=p-1)
    donors[p]='native_text_patch' if p in patches else 'retained_evidence_or_designed' if p in preserved else 'v8_canonical_text'
book.set_metadata({'title':'Detective Academy: The Mystery of Room Zero — complete English V8',
    'author':'Rise.Shine.Evolve.','subject':'Editorial reading edition. Exact candidate SHA256 '+ch+'. Final production typesetting and print preflight are separate.'})
data=book.tobytes(garbage=4,deflate=True);book.close()
actual=fitz.open(stream=data,filetype='pdf');checks=[]
for p in range(1,226):
    donor=source if p in preserved else pure
    assert actual[p-1].get_text()==donor[p-1].get_text(),('serialization text drift',p)
    for b in actual[p-1].get_text('blocks'):
        if b[6]==0:assert fitz.Rect(b[:4]) in actual[p-1].rect,('offpage',p,b[:4])
    if p in preserved:
        fitz.TOOLS.store_shrink(100)
        a=actual[p-1].get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
        b=untouched[p-1].get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
        if p not in patches:assert a.samples==b.samples,('retained evidence drift',p)
        else:
            aa=Image.frombytes('RGB',[a.width,a.height],a.samples)
            bb=Image.frombytes('RGB',[b.width,b.height],b.samples)
            bbox=ImageChops.difference(aa,bb).getbbox()
            assert bbox
            allowed=fitz.Rect(patches[p]);allowed=fitz.Rect(allowed.x0/2-2,allowed.y0/2-2,allowed.x1/2+2,allowed.y1/2+2)
            assert fitz.Rect(bbox) in allowed,('patch escaped text surface',p,bbox,allowed)
    checks.append({'folio':p,'donor':donors[p],'status':'PASS'})
changed=set(boundary['changed_folios'])
for p in sorted(changed|{1,3,13,24,25,79,97,123,127,131,135,139,145,147,149,211}):
    fitz.TOOLS.store_shrink(100)
    actual[p-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False).save(R/f'proof/renders/book-{p:03d}.png')
out=R/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf'
temp=out.with_suffix('.writing.pdf');temp.write_bytes(data);temp.replace(out)
assert out.stat().st_size==len(data)>10_000_000 and len(fitz.open(out))==225
usedfits=[x for x in fits if x['folio'] not in preserved]
assert min(x['body_font_min'] for x in usedfits)>=9.5,('font too small',sorted(usedfits,key=lambda x:x['body_font_min'])[:3])
dump(R/'proof/FIT_CHECK.json',{'candidate_sha256':ch,'minimum_regenerated_body_font':min(x['body_font_min'] for x in usedfits),'folios':usedfits})
dump(R/'proof/PROOF_QA.json',{'candidate_sha256':ch,'pdf_sha256':sha(out),'folios':225,
    'regenerated_text_folios':225-len(preserved),'unchanged_evidence_designed_folios':len(preserved)-len(patches),
    'native_text_patch_folios':sorted(patches),'patch_rectangles':{str(p):list(r) for p,r in patches.items()},
    '225serialization_and_offpage_checks':checks,'unchanged_evidence_pixel_identity':'PASS',
    'two_patch_changed_pixels_inside_text_rectangles':'PASS','actual_visual_review':'PENDING',
    'production_typesetting_and_physical_print':'NOT_RUN','print_ready':False})
print(json.dumps({'pdf':str(out),'sha256':sha(out),'pages':225,'min_body_font':min(x['body_font_min'] for x in usedfits),'candidate_sha256':ch},indent=2))
