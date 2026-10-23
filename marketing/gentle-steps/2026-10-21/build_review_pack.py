"""Export reviewed marketing text; this is a reader proof, never a KDP cover renderer."""
import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether


BASE = Path(__file__).resolve().parent
PLUM = colors.HexColor('#34203F')
CREAM = colors.HexColor('#FAF6EE')
GOLD = colors.HexColor('#AE8449')
INK = colors.HexColor('#302833')
MUTED = colors.HexColor('#726477')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    pl = json.loads((BASE / 'copy.pl.final.json').read_text())
    en = json.loads((BASE / 'copy.en.final.json').read_text())
    texts = {s['id']: s['text'] for data in [pl, en] for s in data['segments']}
    pdfmetrics.registerFont(TTFont('RSE', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('RSE-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('RSE-Serif', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'))
    pdfmetrics.registerFontFamily('RSE', normal='RSE', bold='RSE-Bold', italic='RSE', boldItalic='RSE-Bold')
    styles = {
        'title': ParagraphStyle('title', fontName='RSE-Serif', fontSize=25, leading=31, textColor=PLUM, spaceAfter=14),
        'subtitle': ParagraphStyle('subtitle', fontName='RSE', fontSize=10.5, leading=15, textColor=MUTED, spaceAfter=18),
        'body': ParagraphStyle('body', fontName='RSE', fontSize=11.1, leading=16, textColor=INK, spaceAfter=9, alignment=TA_LEFT),
        'a_body': ParagraphStyle('a_body', fontName='RSE', fontSize=10.6, leading=14.5, textColor=INK, spaceAfter=5.5, alignment=TA_LEFT),
        'back': ParagraphStyle('back', fontName='RSE', fontSize=11.6, leading=17, textColor=INK, spaceAfter=9),
        'small': ParagraphStyle('small', fontName='RSE', fontSize=9, leading=13, textColor=MUTED, spaceAfter=9),
        'card': ParagraphStyle('card', fontName='RSE-Bold', fontSize=11.8, leading=16, textColor=PLUM, spaceAfter=6),
        'kicker': ParagraphStyle('kicker', fontName='RSE-Bold', fontSize=8.6, leading=12, textColor=GOLD, spaceAfter=7),
    }
    story = []
    def para(value, style='body'):
        return Paragraph(escape(value).replace('\n', '<br/>'), styles[style])

    def heading(kicker, title, subtitle=None):
        story.extend([para(kicker, 'kicker'), para(title, 'title')])
        if subtitle:
            story.append(para(subtitle, 'subtitle'))

    def body(value, style='body', first_bold=False):
        result=[]
        for index, chunk in enumerate(value.split('\n\n')):
            marked = escape(chunk).replace('\n', '<br/>')
            if first_bold and index == 0:
                marked = '<b>' + marked + '</b>'
            for label in ['ZŁAPMY CHWILĘ','ZRÓBMY COŚ RAZEM','POGADAJMY','LET’S TAKE A MOMENT','LET’S DO THIS TOGETHER','LET’S TALK']:
                if marked == label or marked.startswith(label+'<br/>'):
                    marked=marked.replace(label, '<b>'+label+'</b>',1)
            result.append(Paragraph(marked, styles[style]))
        return result

    heading('01 / TYŁ OKŁADKI / PL', texts['PL_TITLE'], texts['PL_SUBTITLE'])
    story.extend(body(texts['PL_BACK'], 'back', True))
    story.append(PageBreak())

    heading('02 / AMAZON DESCRIPTION / EN', texts['EN_TITLE'], texts['EN_SUBTITLE'])
    story.extend(body(texts['EN_AMAZON'], first_bold=False))
    story.append(PageBreak())

    for language, title, prefix in [('PL','A+ / Pięć modułów','PL'),('EN','A+ / Five modules','EN')]:
        heading(('03' if language=='PL' else '04')+' / A+ / '+language, title)
        for n in range(1,6):
            pieces=[para(f'0{n}', 'kicker')]+body(texts[f'{prefix}_A{n}'], 'a_body')+[Spacer(1,8)]
            story.append(KeepTogether(pieces))
        story.append(PageBreak())

    for language, title, prefix in [('PL','Trzy pomysły na posty','PL'),('EN','Three social masters','EN')]:
        heading(('05' if language=='PL' else '06')+' / SOCIAL / '+language, title)
        for n in range(1,4):
            pieces=[para(f'0{n}', 'kicker'),para(texts[f'{prefix}_S{n}_HOOK'],'card')]+body(texts[f'{prefix}_S{n}'])+[Spacer(1,13)]
            story.append(KeepTogether(pieces))
        if language=='PL':
            story.append(PageBreak())

    def page(canvas, document):
        canvas.saveState()
        width,height=A4
        canvas.setFillColor(CREAM);canvas.rect(0,0,width,height,fill=1,stroke=0)
        canvas.setStrokeColor(GOLD);canvas.setLineWidth(.7);canvas.line(48,height-37,width-48,height-37)
        canvas.setFillColor(MUTED);canvas.setFont('RSE',8)
        canvas.drawString(48,28,'Rise.Shine.Evolve. / DO AKCEPTACJI / 21.10.2026')
        canvas.drawRightString(width-48,28,str(document.page))
        canvas.restoreState()

    target=args.output/'RSE_GENTLE_STEPS_MARKETING_OWNER_REVIEW_20261021.pdf'
    doc=SimpleDocTemplate(str(target),pagesize=A4,rightMargin=48,leftMargin=48,topMargin=56,bottomMargin=48,
                          title='Gentle Steps - Marketing copy for owner review',author='Rise.Shine.Evolve.',
                          subject='Polish back cover, English Amazon description, bilingual A+ and social copy',creator='Rise.Shine.Evolve.')
    doc.build(story,onFirstPage=page,onLaterPages=page)

    # Reader export preserves final segment text and stable IDs; no hidden copy tightening.
    reader=['# Gentle Steps - marketing copy / 21 October 2026','', 'Status: OWNER_READ_CANDIDATE. Final art and public release remain separate gates.','']
    for data in [pl,en]:
        for segment in data['segments']:
            reader.extend(['## '+segment['id'],'',segment['text'],''])
    (BASE/'COPY_PACK.md').write_text('\n'.join(reader),encoding='utf-8')
    (args.output/'BACK_COVER_PL.txt').write_text(texts['PL_BACK']+'\n',encoding='utf-8')
    (args.output/'AMAZON_DESCRIPTION_EN.txt').write_text(texts['EN_AMAZON']+'\n',encoding='utf-8')
    print(target)


if __name__ == '__main__':
    main()
