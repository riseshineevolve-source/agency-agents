from pathlib import Path
import hashlib,html,json,re
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
import fitz

R=Path(__file__).resolve().parent
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ch=sha(R/'candidate/candidate.json');booksha=sha(R/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf')
bundle=load(R/'reviews/FINAL_REVIEW_BUNDLE.json');assert bundle['status']=='PASS' and bundle['candidate_sha256']==ch
for n,f in [('Audit','DejaVuSans.ttf'),('AuditBold','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
pdfmetrics.registerFontFamily('Audit',normal='Audit',bold='AuditBold',italic='Audit',boldItalic='AuditBold')
S={
 'body':ParagraphStyle('body',fontName='Audit',fontSize=10.1,leading=14.4,spaceAfter=6,textColor=HexColor('#23323a')),
 'h1':ParagraphStyle('h1',fontName='AuditBold',fontSize=21,leading=26,spaceAfter=14,textColor=HexColor('#203c43')),
 'h2':ParagraphStyle('h2',fontName='AuditBold',fontSize=13,leading=17,spaceBefore=13,spaceAfter=8,textColor=HexColor('#203c43')),
 'h3':ParagraphStyle('h3',fontName='AuditBold',fontSize=10.6,leading=14.5,spaceBefore=10,spaceAfter=6,textColor=HexColor('#203c43')),
 'small':ParagraphStyle('small',fontName='Audit',fontSize=8.6,leading=11.5,spaceAfter=6,textColor=HexColor('#58676c')),
 'old':ParagraphStyle('old',fontName='Audit',fontSize=9.4,leading=13.3,spaceAfter=8,textColor=HexColor('#687277'),leftIndent=9,borderColor=HexColor('#d5dcda'),borderWidth=.4,borderPadding=7),
 'new':ParagraphStyle('new',fontName='Audit',fontSize=9.8,leading=13.8,spaceAfter=10,textColor=HexColor('#203d32'),leftIndent=9,borderColor=HexColor('#b8cdc1'),borderWidth=.6,borderPadding=7),
 'cell':ParagraphStyle('cell',fontName='Audit',fontSize=8.4,leading=11.7,spaceAfter=0),
 'white':ParagraphStyle('white',fontName='AuditBold',fontSize=8.4,leading=11.7,textColor=white,spaceAfter=0)}
S['label']=ParagraphStyle('label',parent=S['small'],keepWithNext=True)
flow=[]
def p(t,style='body',br=False):
    t=html.escape(t)
    if br:t=t.replace('\n','<br/>')
    flow.append(Paragraph(t,S[style]))
def table(rows,widths):
    cells=[[Paragraph(html.escape(str(v)),S['white' if i==0 else 'cell']) for v in row] for i,row in enumerate(rows)]
    t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#243f46')),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,HexColor('#eff3f1')]),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7)]))
    flow.append(t);flow.append(Spacer(1,10))

p('DETECTIVE ACADEMY','small')
p('Wspólny audyt i poprawki V8','h1')
p('The Mystery of Room Zero · pełna angielska wersja redakcyjna\n22 października 2026','body',True)
p('Sprawdzono całą książkę: 225 stron, 30 spraw, 90 podpowiedzi i 30 rozwiązań. Czterech niezależnych recenzentów pracowało w uzupełniających się rolach; jeden autor redakcji połączył ich uwagi w jeden tekst. Powstało 47 spójnych pakietów poprawek: 146 fragmentów na 41 stronach.')
p('Raport dla autorki. Zawiera odpowiedzi i szczegóły zakończenia.','small')
p('Kto sprawdzał i czego szukał','h2')
table([['Perspektywa','Zakres'],
 ['Fabuła, pisanie i humor','Cała opowieść i 30 HM Comms; naturalny angielski, rytm, głosy postaci, cel żartu, zapowiedzi i ich domknięcia.'],
 ['Dziecko, nastolatek, wsparcie i mentoring','Jasność działań, dostęp do pomocy, reakcje na pomyłkę, przynależność, docinki bez zawstydzania, czytanie samodzielne i rodzinne.'],
 ['Zagadki, znaczenie i logika','Wszystkie zadania i rysunki, pełne ustawienia postaci, reguły, 90 podpowiedzi, odpowiedzi, 14 map i finał.'],
 ['Czytelnik, marketing i sprzedaż','Zgodność obietnic z zawartością, wciągnięcie w historię, różnorodność, powtórzenia, satysfakcja z końca tomu i oczekiwanie na kolejny.'],
 ['Wspólna redakcja','Jeden tekst końcowy; rozstrzygnięcia oparte na dowodach, zachowanych faktach, działaniu zagadki i rzeczywistym problemie czytelnika.']], [145,365])
p('Najważniejsze wyniki','h2')
p('Każda z 16 map ma dokładnie jedno pełne ustawienie wszystkich świadków przy jawnie zapisanych zasadach. Pozostałe 14 spraw sprawdzono niezależnie z ich rzeczywistymi ilustracjami i danymi. Dla kodu sprawdzono wszystkie 720 kolejności; dla notatki wszystkie 24 kolejności czterech nieobracanych fragmentów. Wiadomość z pustych pomieszczeń wyprowadzono ponownie z 14 rozwiązanych map.')
p('Pozostały wszystkie 27 wcześniejszych napraw V6, wszystkie plansze ze wskazówkami, 30 nagłówków odpowiedzi i 107 wydrukowanych pozycji postaci. Nowa redakcja dopowiada reguły i drogę rozumowania. Cztery znaki 0, zestaw 14 map, CHECK THE OLD MAP i cztery dane finału są spójne.')
flow.append(PageBreak())
p('Co audyt rzeczywiście poprawił','h1')
summary=[
 ('Jasne zasady map','Dodano wspólne definicje sąsiedztwa, przekątnej, kierunków, odległości na siatce i pierwszeństwa znaczników. Warunek „dokładnie jedna inna osoba” jest teraz wyraźnie wskazówką używaną podczas rozwiązywania.'),
 ('Pełniejsze rozwiązania','Piętnaście późniejszych map pokazuje odrzucane pola, zajęte rzędy i kolumny oraz przykłady nieudanych ustawień. Kod z Case 05 ma krótki dowód oparty na czwartym miejscu HEART. Case 27 korzysta z trzech rzeczywistych punktów odniesienia.'),
 ('Puste pomieszczenia bez domysłów','Case 26 ma jawną listę ośmiu wykluczonych stref i informację, że biura, laboratoria, Observation Car oraz Music Archive także liczą się jako pomieszczenia. Rozwiązanie zawiera tabelę: numer sprawy → puste pomieszczenie → litera.'),
 ('Zdjęcie i kapelusz','Na fotografii Case 16 nie ma kapelusza. Bibi kładzie teraz swój kapelusz obok pudełka przy obecnym stole. Udana rozmowa o „architekturze” zostaje i pasuje do obrazu.'),
 ('Obietnice i domknięcia','Cases 04 i 23 proszą o kontakt, którego faktycznie pozwalają ustalić. Case 25 dopowiada istniejący w danych kierunek zwrotu do Archive Restoration. Otwarcie opisuje większe mapy i różne wyzwania, zamiast obiecywać równy wzrost trudności każdego zadania.'),
 ('Czytelnik wie, co zrobić','Call sign jest wyjaśniony na początku. Można skorzystać z pomocy przy pisaniu, pauzy, wspólnego rozwiązywania i podpowiedzi. Indeks pomocy jest podany od razu; pełną Rule Zero kopiuje się z właściwej strony.'),
 ('Wsparcie i rozwój postaci','Dilo przy końcowym archiwalnym mechanizmie zatrzymuje się, sprawdza i otwiera klapkę delikatnie. Jego ciekawość pozostaje; zachowanie wynika z doświadczenia z porwaną notatką.'),
 ('Dokładność pliku','Indeks Case 03 prowadzi do obu zdjęć i strony zapisu. Podpis przy rozwiązaniu zdjęć tłumaczy sens obserwacji bez przytyku do dziecka. Przywrócono pełny tytuł PHOTOGRAPH w eksporcie i sprawdzono kolejność mówców.')]
for title,text in summary:p(title,'h3');p(text)
flow.append(PageBreak())
p('Humor i HM Comms','h1')
p('Wszystkie 30 głównych rozmów przeczytano ponownie. Zachowano mocne sceny i żarty: telefon „undercover” przy batoniku, kapelusz Bibi, kask zmieniający wydział, rywalizację Dilo z wynikiem „In a tone”, nerwową gruszkę z „Strong alibi” i końcowe „Now the paperwork agrees”. Rodzina potrafi też odłożyć żart, kiedy Dilo rozrywa notatkę.')
p('Względem V7 zmienia się jedna główna wypowiedź Comms: Nini w Case 04 kieruje pytanie na świadka, którego rzeczywiście ustala mapa. Reszta pracy V8 wzmacnia kontekst, wyjaśnienia i spójność. Wcześniejsza V7 zawierała już 105 zmienionych wypowiedzi w 25 głównych scenach względem V6; tych dwóch etapów nie należy sumować jako nowych zmian V8.')
p('Kontrola wszystkich 30 spraw','h1')
p('„1 pełny układ” oznacza jedno ustawienie wszystkich osób, a nie tylko jednego oczekiwanego świadka. Przy zadaniach opisowych może różnić się sformułowanie odpowiedzi; sprawdzano jeden właściwy zestaw obserwacji lub wynik przy podanych zasadach. Call sign w finale odtwarza własny pseudonim wpisany wcześniej przez czytelnika.','small')
audit=load(R/'reviews/puzzles-r1/ALL30_PUZZLE_AUDIT_R1.json')
answers={1:'Knox D2',2:'Dax D2',3:'10 kontrolowanych zmian',4:'Zuri F4',5:'BALL–STAR–BOLT–HEART–KEY–MOON',6:'Arlo D2',7:'Zoe C6',8:'C',9:'4 znaki 0; 3 wykluczenia',10:'Ember D5',11:'D / 08:07',12:'Nell G2',13:'Bodhi B7',14:'Noah',15:'Harper D2',16:'Old Academy Annex / 2002',17:'Axel E3',18:'A–B–C–D',19:'Mack A7',20:'Pax F5',21:'B–D–A–C; instrukcja',22:'Cody C4',23:'Rae F6',24:'East Path → West Gate',25:'Casey D5',26:'CHECK THE OLD MAP',27:'Za obecną ścianą Archive',28:'ASSUMPTIONS; pełna Rule Zero',29:'Vega D3',30:'ASSUMPTIONS / D3 / kod / własny call sign'}
methods={3:'Dwa zdjęcia; 10 miejsc zmian',5:'720 kolejności → 1',8:'Trzy trasy; tylko C spełnia zasady',9:'7 kart; 4 pasujące znaki',11:'Cztery czasy; jeden poza oknem',14:'Czasy przejść po krawędziach',16:'Budynek i przecięcie zakresów dat',18:'Korekta trzech zegarów',21:'24 kolejności; jeden łańcuch krawędzi',24:'Jeden kierunek zanikania błota',26:'14 pełnych map; 14 liter',27:'Trzy zgodne punkty na dwóch planach',28:'Sześć twierdzeń i bank słów',30:'Cztery wcześniej zdobyte dane'}
rows=[['Case','Wynik','Jak sprawdzono']]
for case in audit['cases']:
 n=case['case'];rows.append([f'{n:02d}',answers[n],'1 pełny układ; niezależne wyliczenie' if case['kind']=='spatial' else methods[n]])
table(rows,[38,220,252])
p('Granice tych sprawdzeń','h2')
p('Fotografie oceniono jako dziesięć zamierzonych zmian obiektów, a nie jako pikselowo identyczne obrazy poza dziesięcioma punktami. Siatki przepisano z widocznych rysunków i rozwiązywano osobnym programem. To konkretne dowody kontroli treści; nie są obietnicą wyniku sprzedaży ani potwierdzeniem fizycznej próby drukarskiej.')
flow.append(PageBreak())
p('Dokładny rejestr 47 zmian','h1')
p('Numery stron odpowiadają pełnemu, 225-stronicowemu plikowi V8. Poniżej są rzeczywiste fragmenty przed i po redakcji; krótkie urywki mogą zaczynać się w środku zdania, bo zachowują granice źródła. Pełny kontekst jest w książce.','small')
labels={
 'V8-OPENING-PROMISE':'Obietnica rozwoju trudności', 'V8-OPENING-QUESTION':'Pytanie otwierające',
 'V8-ACCESSIBLE-CREDENTIAL':'Pomoc przy karcie rekruta','V8-CALLSIGN-DEFINITION':'Wyjaśnienie call sign',
 'V8-EARLY-SUPPORT':'Podpowiedzi i wsparcie od początku','V8-CASE04-PROMISE':'Zgodność zadania z ustaleniem świadka',
 'V8-CASE04-PAYOFF':'Domknięcie zapisu przekazania','V8-FUNCTION-REPETITION':'Usunięcie powtórzenia tej samej funkcji',
 'V8-HAT-ART-CLOSURE':'Kapelusz zgodny z fotografią','V8-CASEWALL-CLARITY':'Jasny zapis na Case Wall',
 'V8-PAINT-SYNTAX':'Jasność opisu zdarzeń przed i po','V8-CASE23-PROMISE':'Zgodność zapowiedzi z domknięciem',
 'V8-PARCEL-DESTINATION':'Cel zwrotu paczki','V8-PLAN-PLAYABILITY':'Porównanie planów bez dodatkowych materiałów',
 'V8-RULE-COPY-ORDER':'Właściwa strona pełnej reguły','V8-READER-AGE':'Otwarcie dla różnych czytelników',
 'V8-DILO-ARC':'Spójny rozwój Dilo','V8-PHOTO-NAVIGATION':'Indeks obu zdjęć i zapisu',
 'V8-PHOTO-FEEDBACK':'Wspierające objaśnienie zdjęć','V8-MARK-KEY-COMPLETENESS':'Pełny klucz wykluczonych kart',
 'V8-OPENING-NAVIGATION':'Dokładna nawigacja otwarcia','V8-GLOBAL-MAP-CLARITY':'Wspólne definicje map',
 'V8-ROOM-ZONE-KEY':'Jawny klucz pomieszczeń i stref','V8-ROOM-ZONE-HINT':'Zgodna podpowiedź do klucza',
 'V8-EXTRACTION-EXPLANATION':'Tabela czternastu pustych pomieszczeń','V8-CODE-PROOF':'Dowód kolejności kodu',
 'V8-OVERLAY-PROOF':'Poprawne rozumowanie przy trzech punktach planu'}
for k,e in enumerate(load(R/'candidate/edit-units.json'),1):
 key=e['issue'].split(':',1)[0];m=re.fullmatch(r'V8-WORKED-MAP(\d+)',key)
 label='Rozwiązanie mapy Case '+m.group(1)+' krok po kroku' if m else labels.get(key,key)
 folios=sorted({int(i[4:7]) for i in e['ids']})
 flow.append(KeepTogether([Paragraph(f'{k:02d}. {html.escape(label)}',S['h2']),Paragraph('Strona '+', '.join(map(str,folios)),S['small'])]))
 p('PRZED','label');p(e['before'].strip(),'old',True)
 p('V8','label');p(e['after'].strip(),'new',True)

flow.append(PageBreak())
p('Weryfikacja wersji końcowej','h1')
p('Końcowe recenzje języka, znaczenia, odbiorcy i logiki są zgodne z tym samym tekstem. Pierwsze uwagi do skrótów rozumowania w Cases 13 i 20 pozostały zapisane jako uwagi do wcześniejszego szkicu; po poprawieniu zdań recenzenci sprawdzili ich dokładną wersję ponownie.')
p('Pełny PDF ma 225 stron. Sprawdzono zapis i granice tekstu na każdej stronie. Wszystkie nowe strony tekstowe mają podstawowy tekst co najmniej 10,5 pt. Pięćdziesiąt stron z dowodami lub zachowanym projektem odpowiada pikselowo V7; na stronach 148 i 184 zmieniono tylko wskazane powierzchnie tekstu. Recenzenci obejrzeli w pełnym rozmiarze zmienione strony, a przegląd kontaktowy całej książki służył kontroli układu.')
p('Załączona książka jest kompletną wersją redakcyjną do czytania. Końcowy skład produkcyjny, próba drukarska i decyzja o publikacji pozostają odrębnymi etapami.')
p('Identyfikacja dokładnych plików','h2')
p('Tekst V8 SHA-256:\n'+ch,'small',True)
p('PDF książki SHA-256:\n'+booksha,'small',True)
p('Szczegółowe raporty czterech recenzentów, dowody wyliczeń i źródłowy rejestr zmian znajdują się w paczce redakcyjnej V8.','body')

out=R/'proof/DETECTIVE_EN_V8_AUDYT_I_ZMIANY.pdf'
doc=SimpleDocTemplate(str(out),pagesize=A4,leftMargin=42,rightMargin=43,topMargin=49,bottomMargin=43,title='Detective Academy — wspólny audyt i poprawki V8',author='Rise.Shine.Evolve.')
def furniture(c,doc):
 c.saveState();c.setFont('Audit',8);c.setFillColor(HexColor('#62716f'))
 c.drawString(42,817,'DETECTIVE ACADEMY · WSPÓLNY AUDYT V8');c.drawRightString(552,25,str(doc.page));c.restoreState()
doc.build(flow,onFirstPage=furniture,onLaterPages=furniture)
d=fitz.open(out)
for pg in d:
 for b in pg.get_text('blocks'):
  if b[6]==0:assert fitz.Rect(b[:4]) in pg.rect,(pg.number,b[:4])
(R/'proof/audit-renders').mkdir(exist_ok=True)
for pg in d:
 fitz.TOOLS.store_shrink(100)
 pg.get_pixmap(matrix=fitz.Matrix(.65,.65),alpha=False).save(R/f'proof/audit-renders/page-{pg.number+1:03d}.png')
(R/'proof/AUDIT_REPORT_QA.json').write_text(json.dumps({'candidate_sha256':ch,'pdf_sha256':sha(out),'report_pages':len(d),'copy':'All47semanticbeforeaftergroupsfromcanonicaleditunits.','offpage':'NONE','actual_visual_review':'PENDING'},indent=2)+'\n')
print(json.dumps({'report':str(out),'pages':len(d),'sha256':sha(out)},indent=2))
