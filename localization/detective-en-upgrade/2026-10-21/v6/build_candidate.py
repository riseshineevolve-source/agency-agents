"""Owner-authorized bounded V6 repairs; V5 remains an immutable baseline."""
from pathlib import Path
import json, hashlib, subprocess, copy

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent / 'detective-upgrade'
CLI = ROOT.parent / 'rse/scripts/rse-language.py'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
dump = lambda p, o: p.write_text(json.dumps(o, ensure_ascii=False, indent=2) + '\n')

BASE_HASH = '9ebae1eabafe2f5ed92c38c2ad7b858a9c85d573b5a7e92c4fb08f1c5810a978'
assert sha(OLD/'candidate/candidate.json') == BASE_HASH
for sub in ['baseline','candidate','qa','art','proof','integration']:
    (ROOT/sub).mkdir(parents=True, exist_ok=True)
baseline_path = ROOT/'baseline/candidate-v5.json'
if baseline_path.exists():
    assert sha(baseline_path) == BASE_HASH
else:
    baseline_path.write_bytes((OLD/'candidate/candidate.json').read_bytes())
baseline = json.loads(baseline_path.read_text())
byid = {s['id']:s['text'] for s in baseline['segments']}

BESIDE = ('In this case, beside means one square up, down, left or right, in the same room. '
          'Diagonal squares and squares across a wall do not count.')
SYMBOLS = ('PERSON MAY STAND ON: clear floor and objects marked with an open circle.\n'
           'SQUARE BLOCKED BY: walls and objects marked with a black square.')
changes = {
 'page020.block04': 'Use the Standard Map Case Rules on page 11.\n'+BESIDE+'\n'+SYMBOLS+'\n',
 'page020.block08': "03\nRook was in one of the four corners of the whole grid, directly beside a teacher's desk.\n",
 'page024.block04': 'PHOTO A\n',
 'page025.block04': 'PHOTO B\n',
 'page027.block04': 'two copies of one room check. The number on the\nevidence case inside Photo A is 017. In Photo B,\n',
 'page027.block05': 'it is 071. The team checks the original paper\npacket: 017 is the current Trophy Hall reference.\nPhoto B belongs to the older 071 file. The\nphotographs belong to different records.\n',
 'page042.block04': 'Use the Standard Map Case Rules on page 11.\n'+BESIDE+'\n'+SYMBOLS+'\n',
 'page042.block08': '03\nWilla was exactly 2 grid steps from the metal frame at C2. Add the row difference\n',
 'page042.block09': 'and the column difference. This is grid distance, not a walking route.\n',
 'page042.block10': '04\nZoe was against an outer wall and directly beside a wheeled equipment case.\n',
 'page054.block03': 'Use the Standard Map Case Rules on page 11.\n'+BESIDE+'\n',
 'page054.block04': SYMBOLS+'\n',
 'page054.block08': '03\nWyatt was in column B, directly beside the wheeled robot arm in the Robotics Lab.\n',
 'page074.block04': 'Use the Standard Map Case Rules on page 11.\n'+BESIDE+'\n',
 'page074.block05': SYMBOLS+'\n',
 'page074.block07': "01\nHarper was at least one row above Cruz and at least one column to Cruz's right.\n",
 'page074.block08': "02\nPiper was at least one row above Duke and at least one column to Duke's right.\n",
 'page074.block10': '04\nCruz was directly beside a camp cot in the same room.\n',
 'page074.block12': '06\nInez shared a room with a cot but was not directly beside any cot in that room.\n',
 'page096.block03': ('Use the Standard Map Case Rules on page 11.\n'
     'PERSON MAY STAND ON: clear floor, cadet bunks and pilot seats.\n'
     'The bunk beds at E5, E7 and F7 are all usable cadet bunks, marked with open circles.\n'
     'SQUARE BLOCKED BY: walls and objects marked with a black square.\n'),
 'page096.block05': '01\nSid was in a lower row than Pax.\n',
 'page096.block06': "02\nPax was in a lower row than Mara and in a column to Mara's right.\n",
 'page096.block07': '03\nLuca was diagonally next to Asa: exactly one row and one column away.\n',
 'page154.block07': 'Start with Wyatt: column B and the wheeled robot arm in the Robotics Lab. Check the usable squares directly beside that arm.\n',
 'page164.block09': "Use both 'above and to the right' clues. Cruz must be beside a cot in the same room; a cot beyond a wall does not count.\n",
 'page165.block11': "Use Asa's same-room clue and Luca's one-row, one-column diagonal link. Then compare the rows and columns in the Mara-Pax-Sid chain.\n",
 'page190.block11': '05\nZoe is C6 beside a wheeled equipment case; Gray\n',
}
assert set(changes) <= set(byid)
assert all(t != byid[i] for i,t in changes.items())

authority = {
 'owner_instruction_original': '1 case 03- wogole nie dawajmy podpisu w takim razie file 017 i file 071 ani older ani current . samo photo A i photo B zeby od razu nie wskazywac ze jest roznia 017 i 071. ok to zrob fixy wszystkich innych podanych cases tak zeby bylo jasno logicznie spojnie dobrze i dawalo tylko jedno mozliwe rozwiazanie i doprecyzuj tak wskazowki ze dziecko dokladnie rozumie wszystko',
 'date_local': '2026-10-21', 'timezone': 'Europe/Warsaw',
 'scope': 'Bounded source repairs Cases02/03/07/10/15/20, matching hints/solutions/callback, and Case20 usable-bunk symbols.',
 'baseline_candidate_sha256': BASE_HASH,
 'source_pdf_sha256': sha(ROOT.parent/'upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf'),
 'intended_witness_rosters': 'Preserved. Expected rosters may only be compared after enumeration.',
 'case07_anchor': 'New precise C2 metal-frame anchor chosen within explicit owner repair authority; not identified retrospectively as the old range marker.',
 'case20_art_decision': 'E5/E7/F7 visually identical bunk beds are all usable cadet bunks; E7/F7 require open circles on unsolved97 and solved211.',
 'caption_decision': 'External black-bar captions only PHOTO A and PHOTO B; photographic evidence017/071 is preserved inside the photos.',
 'production_writer': 'Existing exclusive BookFactory writer retains production source/renderer. This lane creates a localized candidate and bounded source-patch evidence.',
 'freeze_or_release': False,
}
dump(ROOT/'OWNER_AUTHORITY.json', authority)

specs = []
for s in baseline['segments']:
    specs.append({'id': s['id'], 'text': s['text'], 'protected':s['id'] not in changes,
                  'protected_tokens': [], 'protected_numbers': []})
source_path=ROOT/'baseline/v6-intake-r2.json'
intake={'format':'rse-owner-authorized-bounded-upgrade','language':'en',
        'authority':'OWNER_AUTHORITY.json', 'baseline_candidate_sha256': BASE_HASH,'segments': specs}
if not source_path.exists():
    dump(source_path,intake)
else:
    assert json.loads(source_path.read_text()) == intake

run=ROOT/'run-r2'
if not run.exists():
    subprocess.run(['python',str(CLI),'prepare','--source',str(source_path),'--from','en','--to','en',
                    '--mode','upgrade','--project','detective-academy','--scope','bounded','--output',str(run)],check=True)
manifest=json.loads((run/'run.json').read_text())
allowed=list(changes)
protected=[s['id'] for s in specs if s['id'] not in changes]
dump(run/'change-scope.json',{'run_sha256':manifest['manifest_sha256'],
     'allowed_changed_segments':allowed,'protected_segments':protected,
     'reason':'Exact owner-directed six-case source repairs; captions, clue/key clarity, dependency hints/solution and photo-to-archive callback only. All other V5 text GOLDEN_KEEP.'})
candidate=copy.deepcopy(json.loads((run/'candidate.json').read_text()))
for s in candidate['segments']:
    s['text']=changes.get(s['id'],byid[s['id']])
dump(ROOT/'candidate/candidate.json',candidate)
candidate_hash=sha(ROOT/'candidate/candidate.json')

old_rich=json.loads((OLD/'candidate/candidate-segments.json').read_text())
for s in old_rich['segments']:
    s['text']=byid[s['id']]
    s['target_text']=changes.get(s['id'],byid[s['id']])
    # Preserve the accepted reader's paragraph-grouping metadata. Permissions
    # for this revision live in the immutable run/change scope, not this hint.
    s['v6_editable']=s['id'] in changes
    s['decision']='FIX' if s['id'] in changes else 'GOLDEN_KEEP'
old_rich['baseline_candidate_sha256']=BASE_HASH
old_rich['candidate_sha256']=candidate_hash
dump(ROOT/'candidate/candidate-segments.json',old_rich)
pages=[]
for page in range(1,226):
    ss=[s for s in old_rich['segments'] if s['page']==page]
    pages.append({'page':page,'text':''.join(s['target_text'] for s in ss)})
dump(ROOT/'candidate/candidate-pages.json',pages)
ledger=[{'id':i,'page':int(i[4:7]),'before':byid[i],'after':t,
         'authority':'OWNER_AUTHORITY.json','baseline_sha256':hashlib.sha256(byid[i].encode()).hexdigest(),
         'target_sha256':hashlib.sha256(t.encode()).hexdigest()} for i,t in changes.items()]
dump(ROOT/'candidate/change-ledger.json',ledger)
dump(ROOT/'qa/BOUNDED_DELTA.json',{'candidate_sha256':candidate_hash,'baseline_candidate_sha256':BASE_HASH,
 'total_units':len(specs),'changed_units':len(allowed),'changed_folios':sorted({int(i[4:7]) for i in allowed}),
 'allowed_changed_ids':allowed,'protected_unchanged':len(protected),'outside_allowlist':[],
 'whole_book_reviews':'Inherited accepted V4/V5 for unchanged units; new V6 reviews only bounded delta and dependency closure.',
 'story_humor_and_other_cases':'BYTE_IDENTICAL_TO_V5','print_ready':False})
dump(run/'issue-ledger.json',{'run_sha256':manifest['manifest_sha256'],'diagnostic':'COMPLETE',
 'issues':[{'id':f'V6-CASE-{n:02d}','status':'FIX','source_conflict':False,
            'detail':'Owner-directed source correction implemented; pending exact candidate/figure review.'} for n in [2,3,7,10,15,20]]})
print(json.dumps({'candidate_sha256':candidate_hash,'changed':len(changes),'protected':len(protected)},indent=2))
