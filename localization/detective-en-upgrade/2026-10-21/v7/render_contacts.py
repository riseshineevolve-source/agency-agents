from pathlib import Path
import fitz,json,math
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).resolve().parent
b=json.loads((r/'qa/FINAL_CONTENT_VERIFICATION.json').read_text())
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
(r/'proof/contact-sheets').mkdir(exist_ok=True)
sets=[('book',r/'proof/DETECTIVE_EN_V7_FULL_READING_PROOF.pdf',sorted(set(b['changed_folios']+[13,20,24,25,26,31,42,54,57,74,77,83,96,97,125,145,148,149,154,211,225])),4,4,330,448),
      ('compare',r/'proof/HM_COMMS_ORIGINAL_V6_V7_COMPARISON.pdf',list(range(1,35)),2,3,530,400)]
receipts=[]
for prefix,path,pages,cols,rows,tw,th in sets:
    doc=fitz.open(path);count=cols*rows
    for off in range(0,len(pages),count):
        batch=pages[off:off+count]
        sheet=Image.new('RGB',(cols*tw,rows*th),'#d9dddc');draw=ImageDraw.Draw(sheet)
        for j,p in enumerate(batch):
            page=doc[p-1];scale=min((tw-12)/page.rect.width,(th-31)/page.rect.height)
            pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
            im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
            x=(j%cols)*tw+(tw-im.width)//2;y=(j//cols)*th+23
            sheet.paste(im,(x,y));draw.text(((j%cols)*tw+8,(j//cols)*th+3),f'{prefix.upper()} {p:03d}',font=font,fill='#11292f')
        output=r/f'proof/contact-sheets/{prefix}-{off//count+1:02d}.png';sheet.save(output)
        receipts.append({'sheet':str(output.relative_to(r)),'folios':batch})
    print(prefix,'folios',len(pages),'sheets',math.ceil(len(pages)/count))
(r/'proof/CONTACT_INDEX.json').write_text(json.dumps(receipts,indent=2)+'\n')
