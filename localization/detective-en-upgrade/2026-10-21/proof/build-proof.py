from pathlib import Path
import re,json,hashlib,html
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph,Spacer,KeepInFrame
R=Path('detective-upgrade');font='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('Proof',font+'DejaVuSans.ttf'));pdfmetrics.registerFont(TTFont('ProofBold',font+'DejaVuSans-Bold.ttf'))
source=(R/'candidate/reader-manuscript.md').read_text();parts=re.split(r'^## Page (\d+)\s*$',source,flags=re.M);assert len(parts)==451
out=R/'proof/DETECTIVE_EN_V5_EDITORIAL_TEXT_PROOF.pdf';c=canvas.Canvas(str(out),pagesize=(612,792));c.setTitle('Detective Academy: EN editorial text proof V5');c.setAuthor('Rise.Shine.Evolve.')
body=ParagraphStyle('body',fontName='Proof',fontSize=10.5,leading=14.2,spaceAfter=7,textColor='#191919');heading=ParagraphStyle('heading',parent=body,fontName='ProofBold',fontSize=11.2,leading=15,spaceAfter=9)
checks=[]
for i in range(1,len(parts),2):
 page=int(parts[i]);text=parts[i+1].strip();flow=[]
 for block in re.split(r'\n\s*\n',text):
  block=block.strip()
  block=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',block)
  block=re.sub(r' (?=(?:\d+ )?(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):)', '\n', block)
  if not block:continue
  style=heading if (len(block)<110 and block.upper()==block and re.search('[A-Z]',block) and not re.match(r'^(MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):',block)) else body
  # PDF line breaks inside prose are normalized; dialogue turns and headings stay separate.
  value=html.escape(block)
  value=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',value)
  if re.search(r'(^|\n)(?:\d+ )?(?:MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE):',block) or any(len(line.strip())>3 and line.strip().upper()==line.strip() and re.search('[A-Z]',line) for line in block.splitlines()):value=value.replace('\n','<br/>')
  else:value=re.sub(r'\s*\n\s*',' ',value)
  flow.append(Paragraph(value,style))
 height=sum(x.wrap(520,10000)[1]+x.getSpaceAfter() for x in flow);scale=min(1,682/max(height,1))
 c.setFillColorRGB(.15,.15,.15);c.setFont('ProofBold',9);c.drawString(46,759,'DETECTIVE ACADEMY · EDITORIAL TEXT PROOF')
 c.setFont('Proof',8);c.drawRightString(566,759,'Source folio '+str(page))
 columns=[flow] if height<=850 else [flow[:len(flow)//2],flow[len(flow)//2:]]
 width=520 if len(columns)==1 else 250;actual_scales=[]
 for column_index,content in enumerate(columns):
  box=KeepInFrame(width,682,content,mode='shrink',hAlign='LEFT',vAlign='TOP');w,h=box.wrapOn(c,width,682);box.drawOn(c,46+column_index*270,738-h);actual_scales.append(1/getattr(box,'_scale',1))
 assert min(actual_scales)*10.5>=7.7,(page,actual_scales)
 scale=min(actual_scales)
 c.setFont('Proof',7.5);c.setFillColorRGB(.4,.4,.4);c.drawString(46,26,'Text review only · Original puzzle artwork remains in the source PDF');c.drawRightString(566,26,str(page));c.showPage();checks.append({'source_folio':page,'estimated_scale':scale,'flow_height':height})
c.save();(R/'proof/FIT_CHECK.json').write_text(json.dumps({'pages':225,'candidate_sha256':hashlib.sha256((R/'candidate/candidate.json').read_bytes()).hexdigest(),'manuscript_sha256':hashlib.sha256((R/'candidate/reader-manuscript.md').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'page_fit':checks,'status':'EDITORIAL_PROOF_NOT_PRODUCT_LAYOUT'},indent=2)+'\n');print(out)
