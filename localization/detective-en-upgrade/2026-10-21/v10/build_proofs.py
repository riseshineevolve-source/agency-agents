"""Reading proof only: reflow authorised dialogue folios, retain all other V8 PDF leaves."""
from pathlib import Path
from io import BytesIO
import ast, hashlib, html, json, re
import fitz
from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph, KeepInFrame, Table, TableStyle, Spacer

R=Path(__file__).resolve().parent;W=R.parent;V8=W/'detective-v8'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
norm=lambda s:re.sub(r'\s+',' ',s).strip()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
for name,file in [('Book','DejaVuSans.ttf'),('BookBold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('Book',normal='Book',bold='BookBold',italic='Book',boldItalic='BookBold')
body=ParagraphStyle('body',fontName='Book',fontSize=10.5,leading=14.1,spaceAfter=7,textColor=HexColor('#20252a'))
head=ParagraphStyle('head',parent=body,fontName='BookBold',fontSize=11.2,leading=14.8,spaceAfter=9)
tablebody=ParagraphStyle('table',parent=body,spaceAfter=0,leading=13.2)
tablehead=ParagraphStyle('tablehead',parent=tablebody,fontName='BookBold',textColor=white)
smallhead=ParagraphStyle('smallhead',parent=tablehead,fontSize=9.5,leading=12)
# Reuse the verified editorial reading adapter, never the product renderer.
tree=ast.parse((V8/'build_book.py').read_text())
for node in tree.body:
    if isinstance(node,ast.FunctionDef) and node.name in ['para','table','flow_for','furniture','draw_flow']:
        exec(compile(ast.Module(body=[node],type_ignores=[]),str(V8/'build_book.py'),'exec'))
ch=sha(R/'candidate/candidate.json');boundary=json.loads((R/'qa/BOUNDARY_CHECK.json').read_text())
changes=boundary['changed_folios'];reader=(R/'candidate/reader-manuscript.md').read_text()
parts=re.split(r'^## Page (\d+)\s*$',reader,flags=re.M);pages={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)}
source=fitz.open(V8/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf')
assert len(source)==225 and sha(V8/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf')=='67278523fa587ed18799da5c3b8c0aeb5c4bf77294a5269e8b132fbe138ea230'
fits=[];generated={}
for p in changes:
    buf=BytesIO();c=canvas.Canvas(buf,pagesize=(612,792));furniture(c,p)
    fit=draw_flow(c,flow_for(pages[p]),46,738,520,682)
    fits.append({'folio':p,**fit});assert fit['body_font_min']>=10.5,(p,fit)
    c.showPage();c.save();generated[p]=fitz.open(stream=buf.getvalue(),filetype='pdf')
book=fitz.open(V8/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf')
for p in changes:
    book.delete_page(p-1)
    book.insert_pdf(generated[p],from_page=0,to_page=0,start_at=p-1)
book.set_metadata({'title':'Detective Academy: The Mystery of Room Zero - V10 Happy Makers family dialogue',
    'author':'Rise.Shine.Evolve.','subject':'Complete English editorial reading edition. V8 puzzle content retained; V10 HM Comms rhythm revision.'})
out=R/'proof/DETECTIVE_EN_V10_FULL_ENGLISH.pdf';out.write_bytes(book.tobytes(garbage=4,deflate=True))
actual=fitz.open(out);checks=[]
assert len(actual)==225
for p in range(1,226):
    if p not in generated:
        assert actual[p-1].get_text()==source[p-1].get_text(),('unchangedtext',p)
        fitz.TOOLS.store_shrink(100)
        assert actual[p-1].get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False).samples==source[p-1].get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False).samples,('unchangedpixels',p)
        checks.append({'folio':p,'text_and_render_identical_v8':True})
    else:
        assert actual[p-1].get_text()==generated[p][0].get_text(),('changedserialization',p)
        checks.append({'folio':p,'authorised_dialogue_reflow':True})
    for b in actual[p-1].get_text('blocks'):
        if b[6]==0:assert fitz.Rect(b[:4]) in actual[p-1].rect,('offpage',p,b[:4])

scenes=json.loads((R/'candidate/final-scenes.json').read_text())['scenes']
dialoguestyle=ParagraphStyle('dialogue',fontName='Book',fontSize=12.0,leading=17.0,textColor=HexColor('#20252a'))
speakerstyle=ParagraphStyle('speaker',fontName='BookBold',fontSize=8.7,leading=11,textColor=HexColor('#33454a'))
labels={'INTRO07':'MEET THE HAPPY MAKERS','CASEWALL12':'YOUR CASE WALL','THREAD34':'FOUR MATCHING MARKS','THREAD120':'THE OLD CASES COME BACK'}
buf=BytesIO();c=canvas.Canvas(buf,pagesize=(612,792));dialoguefits=[]
c.setTitle('Happy Makers Comms - complete final English dialogue');c.setAuthor('Rise.Shine.Evolve.')
for index,s in enumerate(scenes,1):
    c.setFillColor(HexColor('#20353d'));c.rect(0,748,612,44,fill=1,stroke=0)
    c.setFillColor(white);c.setFont('BookBold',11);c.drawString(44,765,'HAPPY MAKERS COMMS')
    c.setFont('Book',8);c.drawRightString(568,766,'THE MYSTERY OF ROOM ZERO')
    label=('CASE '+str(s['case']).zfill(2)) if s['case'] else labels[s['id']]
    c.setFillColor(HexColor('#20353d'));c.setFont('BookBold',15);c.drawString(44,714,label)
    c.setFont('Book',8.5);c.setFillColor(HexColor('#6b7377'));c.drawString(44,695,'BOOK FOLIO '+', '.join(str(p) for p in s['folios']))
    y=670
    for t in s['turns']:
        p=Paragraph(html.escape(t['final_text']),dialoguestyle);_,h=p.wrap(494,1000)
        boxh=h+37
        assert y-boxh>=53,(s['id'],t['speaker'],'standaloneoverflow')
        c.setFillColor(HexColor('#f1f3f2'));c.roundRect(44,y-boxh,524,boxh,5,fill=1,stroke=0)
        label=Paragraph(t['speaker'],speakerstyle);label.wrap(494,100);label.drawOn(c,59,y-18)
        p.drawOn(c,59,y-23-h)
        y-=boxh+7
    c.setFont('Book',8);c.setFillColor(HexColor('#6b7377'));c.drawString(44,26,'The Happy Makers / Detective Academy');c.drawRightString(568,26,str(index))
    dialoguefits.append({'scene':s['id'],'folio':index,'bottom_y':round(y+7,2),'font_size':12.0})
    c.showPage()
c.save();hm=R/'proof/HAPPY_MAKERS_COMMS_V10_EN.pdf';hm.write_bytes(buf.getvalue())
standalone=fitz.open(hm);assert len(standalone)==34
for p,s in zip(standalone,scenes):
    text=norm(p.get_text())
    for t in s['turns']:assert norm(t['final_text']) in text,('dialogueroundtrip',s['id'],t['speaker'])
    for b in p.get_text('blocks'):
        if b[6]==0:assert fitz.Rect(b[:4]) in p.rect
contacts=[]
qa={'candidate_sha256':ch,'book_pdf_sha256':sha(out),'book_pages':225,'standalone_pdf_sha256':sha(hm),'standalone_pages':34,
 'changed_book_folios':changes,'unchanged_v8_text_and_pixel_identical_folios':225-len(changes),'all225_offpage_checks':'PASS',
 'standalone_all183_spoken_turn_roundtrips':'PASS','minimum_book_body_font':min(x['body_font_min'] for x in fits),'standalone_font':12.0,
 'book_fits':fits,'standalone_fits':dialoguefits,'all_page_checks':checks,'contact_sheets':contacts,'visual_review':'PENDING',
 'production_typesetting_or_physical_print':'NOT_RUN','print_ready':False,'candidate_author':'hm10_writer','integrator':'root'}
dump(R/'proof/PROOF_QA.json',qa)
print(json.dumps({k:v for k,v in qa.items() if k not in ['book_fits','standalone_fits','all_page_checks','contact_sheets']},indent=2))
