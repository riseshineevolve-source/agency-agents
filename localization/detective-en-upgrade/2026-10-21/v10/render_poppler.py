"""Fresh saved-PDF raster QA; avoids the observed MuPDF font-cache preview artefact."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;qa=json.loads((R/'proof/PROOF_QA.json').read_text())
dest=R/'proof/renders';dest.mkdir(exist_ok=True)
book=R/'proof/DETECTIVE_EN_V10_FULL_ENGLISH.pdf';hm=R/'proof/HAPPY_MAKERS_COMMS_V10_EN.pdf'
def render(p):
    prefix=dest/f'book-{p:03d}'
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-scale-to','1100','-png',str(book),str(prefix)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
with ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(render,qa['changed_book_folios']))
def render_comms(p):
    prefix=dest/f'comms-{p:02d}'
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-scale-to','1100','-png',str(hm),str(prefix)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
with ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(render_comms,range(1,35)))
for p in dest.glob('*.png'):
    try:Image.open(p).load()
    except OSError:
        if p.stem.startswith('comms-'):render_comms(int(p.stem.split('-')[1]))
        else:render(int(p.stem.split('-')[1]))
        Image.open(p).load()
contacts=[]
for kind,files in [('book',sorted(dest.glob('book-*.png'))),('comms',sorted(dest.glob('comms-*.png')))]:
    for start in range(0,len(files),9):
        sheet=Image.new('RGB',(1050,1440),'#b8bdc0');draw=ImageDraw.Draw(sheet)
        for j,f in enumerate(files[start:start+9]):
            im=Image.open(f);im.thumbnail((330,433));x=10+j%3*350;y=22+j//3*480;sheet.paste(im,(x,y));draw.text((x,y+436),f.stem,fill='black')
        p=R/'proof'/f'contact-{kind}-{start//9+1}.png';sheet.save(p);contacts.append(str(p))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt={'candidate_sha256':qa['candidate_sha256'],'book_pdf_sha256':sha(book),'comms_pdf_sha256':sha(hm),'renderer':'Poppler pdftoppm, fresh saved PDF bytes; scale-to1100',
    'book_folios':qa['changed_book_folios'],'standalone_folios':list(range(1,35)),
    'rendered_pngs':[{'name':p.name,'sha256':sha(p)} for p in sorted(dest.glob('*.png'))],
    'contacts':contacts,'visual_review':'PENDING'}
(R/'proof/POPPLER_RENDER_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'book_pdf_sha256':sha(book),'comms_pdf_sha256':sha(hm),'book_renders':35,'comms_renders':34,'contact_sheets':len(contacts)}))
