"""Owner reading artifacts; never a replacement for the Book Factory renderer."""
from pathlib import Path
from io import BytesIO
import hashlib, html, json, re
import fitz
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, KeepInFrame

R=Path(__file__).resolve().parent; W=R.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
norm=lambda t:re.sub(r'\s+',' ',t).strip()
def dump(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
ch=sha(R/'candidate/candidate.json')
reviews=json.loads((R/'reviews/FINAL_REVIEW_BUNDLE.json').read_text())
assert reviews['candidate_sha256']==ch and reviews['status']=='PASS'
(R/'proof/renders').mkdir(parents=True,exist_ok=True)
font='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('Book',font+'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('BookBold',font+'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('Book',normal='Book',bold='BookBold',italic='Book',boldItalic='BookBold')
body=ParagraphStyle('book',fontName='Book',fontSize=10.5,leading=14.1,spaceAfter=7,textColor=HexColor('#20252a'))
heading=ParagraphStyle('head',parent=body,fontName='BookBold',fontSize=11.2,leading=14.8,spaceAfter=9)
source=(R/'candidate/reader-manuscript.md').read_text()
parts=re.split(r'^## Page (\d+)\s*$',source,flags=re.M)
assert len(parts)==451
buffer=BytesIO(); c=canvas.Canvas(buffer,pagesize=(612,792))
c.setTitle('Detective Academy EN V7 reading proof');c.setAuthor('Rise.Shine.Evolve.')
fits=[]
for k in range(1,len(parts),2):
    p=int(parts[k]);text=parts[k+1].strip()
    # Inline source portrait numbers are presentation furniture, not clues.
    # Give these literal dialogue runs the same speaker treatment as all
    # already separated Comms, especially the threshold scene on folio137.
    text=re.sub(r'(?m)^(?:\d+\s+)?(MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):[ \t]*',r'**\1:** ',text)
    text=re.sub(r'\n(?=\*\*(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):\*\*)','\n\n',text)
    # Adjacent speaker-label and speech paragraphs are one visual unit.
    text=re.sub(r'(\*\*(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):\*\*)\s*\n\s*\n',r'\1 ',text)
    text=re.sub(r'HAPPY MAKERS / DETECTIVE ACADEMY\s*\n\s*\d{3}\s*(?:\n\s*)?', '',text)
    text=re.sub(r'(?m)^HINT VAULT // LEVEL ([123])\n\s*\nHINT VAULT // LEVEL \1$',r'HINT VAULT // LEVEL \1',text)
    flow=[]
    for b in re.split(r'\n\s*\n',text):
        b=b.strip()
        if not b:continue
        b=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',b)
        b=re.sub(r' (?=(?:\d+ )?(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):)','\n',b)
        style=heading if len(b)<115 and b.upper()==b and re.search('[A-Z]',b) and not re.match(r'^(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):',b) else body
        value=html.escape(b)
        value=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',value)
        preserve=bool(re.search(r'(^|\n)(?:\d+ )?(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):',b)) or any(len(z.strip())>3 and z.strip().upper()==z.strip() and re.search('[A-Z]',z) for z in b.splitlines())
        value=value.replace('\n','<br/>') if preserve else re.sub(r'\s*\n\s*',' ',value)
        flow.append(Paragraph(value,style))
    height=sum(f.wrap(520,10000)[1]+f.getSpaceAfter() for f in flow)
    columns=[flow] if height<=850 else [flow[:len(flow)//2],flow[len(flow)//2:]]
    width=520 if len(columns)==1 else 250
    scales=[]
    c.setFillColor(HexColor('#283940'));c.setFont('BookBold',9)
    c.drawString(46,759,'DETECTIVE ACADEMY · READING PROOF V7')
    c.setFont('Book',8);c.drawRightString(566,759,'Source folio '+str(p))
    for j,col in enumerate(columns):
        box=KeepInFrame(width,682,col,mode='shrink',hAlign='LEFT',vAlign='TOP')
        bw,bh=box.wrapOn(c,width,682);box.drawOn(c,46+j*270,738-bh)
        scales.append(1/getattr(box,'_scale',1))
    assert min(scales)*10.5>=7.7,(p,scales)
    if p<=147:assert min(scales)*10.5>=9.0,(p,'narrative too small',scales)
    c.setFillColor(HexColor('#677278'));c.setFont('Book',7.5)
    c.drawString(46,26,'Reading proof · Final book layout pending')
    c.drawRightString(566,26,str(p));c.showPage()
    fits.append({'folio':p,'body_font_min':round(min(scales)*10.5,2),'columns':len(columns),'flow_height':round(height,2)})
c.save()
pure=fitz.open(stream=buffer.getvalue(),filetype='pdf')
v6=fitz.open(W/'detective-v6/proof/DETECTIVE_EN_V6_READING_PROOF.pdf')
original=fitz.open(W/'upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf')
boundary=json.loads((R/'qa/BOUNDARY_CHECK.json').read_text())
art=set(boundary['source_art_folios'])
original_intake=json.loads((W/'detective-upgrade/source/intake-v5.json').read_text())
original_text={s['id']:s['text'] for s in original_intake['segments']}
candidate=json.loads((R/'candidate/candidate.json').read_text())
page_of={s['id']:int(s['id'][4:7]) for s in candidate['segments']}
# These unchanged source leaves retain writable CaseWall/response spaces and a
# fully numbered index, whose furniture should not be lost in prose extraction.
designed_extras={13,26,148,149}
for s in candidate['segments']:
    if page_of[s['id']] in designed_extras:assert s['text']==original_text[s['id']]
final=fitz.open();donors={}
for p in range(1,226):
    donor=original if p in designed_extras else v6 if p in art else pure
    final.insert_pdf(donor,from_page=p-1,to_page=p-1)
    donors[p]='unchanged_designed_source' if p in designed_extras else 'v6_locked_evidence_art' if p in art else 'v7_editorial_text'
out=R/'proof/DETECTIVE_EN_V7_FULL_READING_PROOF.pdf'
final.set_metadata({'title':'Detective Academy: full English V7 reading proof','author':'Rise.Shine.Evolve.',
 'subject':'Full English editorial candidate with source puzzle art and all V6 source repairs. '+ch+'; final Book Factory layout pending.'})
book_bytes=final.tobytes(garbage=4,deflate=True);final.close()
assert len(book_bytes)>10_000_000
actual=fitz.open(stream=book_bytes,filetype='pdf');checks=[]
for p in range(1,226):
    donor=original if p in designed_extras else v6 if p in art else pure
    assert actual[p-1].get_text()==donor[p-1].get_text(),('copy text mismatch',p)
    if p in art|designed_extras:
        fitz.TOOLS.store_shrink(100)
        a=actual[p-1].get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
        b=donor[p-1].get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
        assert a.samples==b.samples,('evidence pixel mismatch',p)
    for b in actual[p-1].get_text('blocks'):
        if b[6]==0:assert fitz.Rect(b[:4]) in actual[p-1].rect,('offpage',p,b[:4])
    checks.append({'folio':p,'source':donors[p],'status':'PASS'})
assert len(actual)==225
for p in [19,23,27,53,65,68,69,99,109,113,120,121,129,133,137,141,143,144,148,149,154,212]:
    actual[p-1].get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False).save(R/f'proof/renders/book-{p:03d}.png')
dump(R/'proof/FIT_CHECK.json',{'candidate_sha256':ch,'folios':fits})

# Three-way owner comparison: original submitted dialogue / previous V6 / V7.
cmp=json.loads((R/'candidate/comms-comparison.json').read_text())
prior=json.loads((R/'diagnostic/PRIOR_COMMS_AUDIT.json').read_text())
comparison=R/'proof/HM_COMMS_ORIGINAL_V6_V7_COMPARISON.pdf'
q=canvas.Canvas(str(comparison),pagesize=(842,595))
q.setTitle('Happy Makers Comms: original, V6 and V7');q.setAuthor('Rise.Shine.Evolve.')
cmpbody=ParagraphStyle('compare',fontName='Book',fontSize=10.3,leading=14,spaceAfter=11,textColor=HexColor('#23313a'))
small=ParagraphStyle('small',parent=cmpbody,fontSize=9,leading=12)
cover=ParagraphStyle('cover',parent=cmpbody,fontSize=12,leading=18,spaceAfter=17)
compare_fits=[]
def para(t,x,y,width,style):
    z=Paragraph(t,style);w,h=z.wrap(width,10000);z.drawOn(q,x,y-h);return y-h-z.getSpaceAfter()
q.setFillColor(HexColor('#172e38'));q.rect(0,0,842,595,fill=1,stroke=0)
q.setFillColor(HexColor('#ecb66b'));q.setFont('BookBold',12);q.drawString(48,541,'DETECTIVE ACADEMY · HM COMMS')
q.setFillColor(HexColor('#ffffff'));q.setFont('BookBold',25);q.drawString(48,492,'Co faktycznie się zmieniło')
white=ParagraphStyle('white',parent=cover,textColor=HexColor('#ffffff'))
y=450
for t in [
 '<b>Trzy wersje obok siebie:</b> Twój pierwotny PDF → V6 → nowa V7.',
 '<b>Poprzednio:</b> zmiany w 15 z 30 głównych scen, łącznie 27 wypowiedzi. Drugie 15 scen bez zmian. Przejście V5 → V6 nie zmieniło żadnej z tych rozmów.',
 f'<b>Teraz:</b> zredagowano {sum(s["changed_v7"] for s in cmp["scenes"])} głównych scen. Pięć mocnych rozmów zachowano w całości: Cases 05, 11, 16, 17 i 27. Pozostałe mocne żarty także zachowano tam, gdzie działają.',
 '<b>Jak czytać:</b> każda kolejna strona pokazuje pełną scenę. Zielona kolumna to V7. Dopisek pod tytułem podaje, ile wypowiedzi zmieniło się na każdym etapie.',
 'Po 30 sprawach znajdziesz także rozmowy z Case Wall i mostów fabularnych. Pełna książka jest w osobnym, 225-stronicowym pliku do czytania.'
]:y=para(t,48,y,738,white)
assert y>58
q.setFillColor(HexColor('#d5e4e7'));q.setFont('Book',8.5);q.drawString(48,28,'Porównanie redakcyjne · teksty w języku książki · 21.10.2026');q.showPage()

def compare_page(title,location,rows,prior_changes,new_changes,golden=False):
    page=len(compare_fits)+2
    q.setFillColor(HexColor('#f8f8f5'));q.rect(0,0,842,595,fill=1,stroke=0)
    q.setFillColor(HexColor('#192f3a'));q.setFont('BookBold',17);q.drawString(36,555,title)
    q.setFont('Book',9);q.drawString(36,535,location)
    label=f'Oryginał → V6: {prior_changes} zmienionych wypowiedzi. V6 → V7: {new_changes}.'
    if golden:label+=' Mocna scena zachowana.'
    q.setFillColor(HexColor('#5b666b'));q.setFont('Book',8.7);q.drawString(36,516,label)
    xpositions=[36,300,564];width=242; bottoms=[]
    for col,(name,x) in enumerate(zip(['TWÓJ ORYGINAŁ','POPRZEDNIA V6','NOWA V7'],xpositions)):
        if col==2:q.setFillColor(HexColor('#e5eee6'));q.roundRect(x-10,48,width+20,446,8,fill=1,stroke=0)
        q.setFillColor(HexColor('#254334') if col==2 else HexColor('#44535c'));q.setFont('BookBold',10);q.drawString(x,477,name)
        y=451
        for row in rows:
            t='<b>'+html.escape(row['speaker'])+'</b><br/>'+html.escape(row[['source_text','v6_text','v7_text'][col]])
            y=para(t,x,y,width,cmpbody)
        assert y>=61,(title,name,'overflow',y)
        bottoms.append(round(y,2))
    q.setFillColor(HexColor('#667177'));q.setFont('Book',7.7)
    q.drawString(36,26,'Pełne wypowiedzi · zmiany oceniane po treści, z pominięciem samych podziałów wierszy')
    q.drawRightString(806,26,str(page));q.showPage()
    compare_fits.append({'title':title,'page':page,'column_bottoms':bottoms})

for s in cmp['scenes']:
    rows=s['turns']
    compare_page(f'CASE {s["case"]:02d}',f'Strona książki: {s["source_folio"]}',rows,
      sum(norm(r['source_text'])!=norm(r['v6_text']) for r in rows),
      sum(r['changed_v7'] for r in rows),not s['changed_v7'])

base=json.loads((R/'baseline/candidate-v6.json').read_text());bt={s['id']:s['text'] for s in base['segments']}
ct={s['id']:s['text'] for s in candidate['segments']}
def combined_rows(ids,speakers):
    rows=[]
    for i,name in zip(ids,speakers):
        rows.append({'speaker':name,'source_text':norm(original_text[i]),'v6_text':norm(bt[i]),'v7_text':norm(ct[i])})
    return rows
# p12 has literal speaker tags in one canonical segment in all three versions.
rows=[]
for a,b,d in zip(original_text['page012.block03'].splitlines(),bt['page012.block03'].splitlines(),ct['page012.block03'].splitlines()):
    name=a.split(':',1)[0];rows.append({'speaker':name,'source_text':a.split(':',1)[1].strip(),'v6_text':b.split(':',1)[1].strip(),'v7_text':d.split(':',1)[1].strip()})
compare_page('CASE WALL · ROZMOWA', 'Strona książki: 12',rows,sum(r['source_text']!=r['v6_text'] for r in rows),sum(r['v6_text']!=r['v7_text'] for r in rows))
rows=[]
for ids,name in [(['page034.block16'],'DILO'),(['page034.block18'],'LULI'),(['page035.block06','page035.block07'],'NINI'),(['page035.block09','page035.block10'],'BIBI')]:
    rows.append({'speaker':name,'source_text':norm(''.join(original_text[i] for i in ids)), 'v6_text':norm(''.join(bt[i] for i in ids)),'v7_text':norm(''.join(ct[i] for i in ids))})
compare_page('CZTERY ZNAKI · ROZMOWA','Strony książki: 34–35',rows,sum(r['source_text']!=r['v6_text'] for r in rows),sum(r['v6_text']!=r['v7_text'] for r in rows))
rows=[]
for mapping,key in [(original_text,'source_text'),(bt,'v6_text'),(ct,'v7_text')]:
    # Verified source boundaries: first speech ends after 'reason'; Dilo gets
    # the remainder. Luli's first sentence ends after 'methodology' in source.
    first=norm(mapping['page120.block15']);sep=first.index('I kept mine')
    middle=norm(mapping['page120.block16'])
    if key=='v7_text':sep2=middle.index('Useful evidence')
    else:sep2=middle.index('And the parcel')
    values=[first[:sep].strip(),first[sep:].strip(),middle[:sep2].strip(),middle[sep2:].strip(),norm(mapping['page120.block17'])]
    if not rows:rows=[{'speaker':n} for n in ['NINI','DILO','LULI','BIBI','MIMI']]
    for row,value in zip(rows,values):row[key]=value
compare_page('STARE SPRAWY WRACAJĄ','Strona książki: 120 · kolejność mówców sprawdzona z pierwotnym układem',rows,sum(r['source_text']!=r['v6_text'] for r in rows),sum(r['v6_text']!=r['v7_text'] for r in rows))
q.save()
# Persist the completed book after both documents have finished composing.
out.write_bytes(book_bytes)
assert out.stat().st_size==len(book_bytes)
cmpdoc=fitz.open(comparison)
assert len(cmpdoc)==34
for pg in cmpdoc:
    for b in pg.get_text('blocks'):
        if b[6]==0:assert fitz.Rect(b[:4]) in pg.rect,('comparison offpage',pg.number,b[:4])
for p in [1,2,4,7,14,15,22,25,27,29,30,31,32,33,34]:
    cmpdoc[p-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False).save(R/f'proof/renders/compare-{p:02d}.png')
dump(R/'proof/PROOF_QA.json',{'candidate_sha256':ch,'reading_proof_sha256':sha(out),'reading_folios':225,
 'v7_text_folios':225-len(art|designed_extras),'locked_art_and_designed_source_folios':len(art|designed_extras),
 'copy_checks':checks,'comparison_sha256':sha(comparison),'comparison_pages':len(cmpdoc),
 'comparison_fit':compare_fits,'offpage_text':'NONE','actual_visual_review':'PENDING',
 'content_review':'Four real independent stages PASS for exact candidate hash','production_layout':'NOT_RUN','print_ready':False})
print(json.dumps({'reading_proof':str(out),'comparison':str(comparison),'reading_folios':225,'comparison_pages':34,'candidate_sha256':ch},indent=2))
