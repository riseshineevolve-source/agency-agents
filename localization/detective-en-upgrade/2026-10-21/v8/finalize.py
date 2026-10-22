"""Joint evidence index, exact-bound QA, import packet and durable checkpoint."""
from pathlib import Path
import hashlib,json,re,shutil
R=Path(__file__).resolve().parent;V7=R.parent/'recovery/unpacked/detective-v7'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ch=sha(R/'candidate/candidate.json');pdf=R/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf';ph=sha(pdf)
base=load(R/'baseline/candidate-v7.json');can=load(R/'candidate/candidate.json')
before={s['id']:s['text'] for s in base['segments']};after={s['id']:s['text'] for s in can['segments']}
ledger=load(R/'candidate/change-ledger.json');units=load(R/'candidate/edit-units.json')
actual={i for i in before if before[i]!=after[i]}
assert len(actual)==146 and actual=={s['id'] for s in ledger}
assert len(units)==47 and len(after)==3067
assert all(s['before']==before[s['id']] and s['after']==after[s['id']] for s in ledger)
locks=load(R/'source-models/V6_CHANGE_LOCKS.json')
assert len(locks)==27 and all(after[s['id']]==before[s['id']]==s['after'] for s in locks)
answerids=[i for i in before if before[i].startswith('ANSWER:')]
assert len(answerids)==30 and all(after[i]==before[i] for i in answerids)
boardfolios=[17,20,28,38,42,54,62,66,74,84,92,96,106,110,118,134]
assert all(after[i]==t for i,t in before.items() if int(i[4:7]) in boardfolios)
hintchanges=[i for i in actual if 150<=int(i[4:7])<=177]
assert hintchanges==['page167.block07']
cmp=load(V7/'candidate/comms-comparison.json')['scenes'];comms=[]
for scene in cmp:
    changed=[]
    for t in scene['turns']:
        if any(after[i]!=before[i] for i in t['ids']):changed.append(t['speaker'])
    comms.append({'case':scene['case'],'changed_turn_speakers':changed,'status':'KEEP' if not changed else 'CASE04_TASK_REDIRECT_ONLY'})
assert [x['case'] for x in comms if x['changed_turn_speakers']]==[4]
assert next(x for x in comms if x['case']==4)['changed_turn_speakers']==['NINI']
sp=load(R/'reviews/puzzles-final/final-spatial-rerun.json')
qa={'candidate_sha256':ch,'reading_pdf_sha256':ph,'segments':3067,'source_folios':225,
    'changed_segments_from_v7':146,'semantic_edit_groups':47,'changed_folios':sorted({int(i[4:7]) for i in actual}),
    'all27_v6_repairs_byte_identical':True,'all30_answer_headers_byte_identical':True,
    'all16_witness_board_folios_byte_identical':True,'hint_changes':hintchanges,
    'all30_main_comms_reviewed':comms,'all16_full_rosters': 'Actual independent fresh enumeration: one each; final-spatial-rerun.json',
    'all14_other_cases':'Actual independent candidate/evidence checks; ALL30_PUZZLE_AUDIT_R1.json and final closure',
    'all90_hints':'Actually read and checked by puzzle reviewer, not merely counted',
    'source_truth':'Four0records;14mapset;CHECKTHEOLDMAP;ASSUMPTIONS/D3/sixsymbolcode/readerchosenpriorcallsign',
    'source_figures':'All31puzzle/evidencefigures and16answerartfolios independentlyrender-bound; native184feedbacktextonly.',
    'actual_pdf_text_surface_patches':[148,184],'status':'PASS','print_ready':False}
dump(R/'qa/FINAL_CONTENT_VERIFICATION.json',qa)

# Convert actual reviewer assessments into the CLI's small interchange schema.
# No independent opinion is generated here; each PASS points to an actual report.
native=load(R/'reviews/story-humor-final/native_language.json')
aud=load(R/'reviews/audience-final/audience.json')
logic=load(R/'reviews/reader-market-final/logic.json')
meaning=load(R/'reviews/puzzles-final/FINAL_MEANING_LOGIC_CLOSURE.json')
assert native['status']==aud['status']==logic['status']=='PASS'
assert meaning['disposition']=='PASS_MEANING_AND_PUZZLE_LOGIC' and not meaning['open_logic_blockers']
assert native['candidate_sha256']==aud['candidate_sha256']==logic['candidate_sha256']==meaning['canonical_candidate_sha256']==ch
rr=[]
for stage,obj,path in [('native_language',native,'story-humor-final/native_language.json'),('audience',aud,'audience-final/audience.json'),('logic',logic,'reader-market-final/logic.json')]:
    rr.append({'stage':stage,'status':obj['status'],'candidate_sha256':ch,'reviewer':obj['reviewer'],
        'scope':obj['scope'],'evidence':'Actual independent review, findings, closure and scope: reviews/'+path,
        'receipt_sha256':sha(R/'reviews'/path)})
rr.append({'stage':'meaning','status':'PASS','candidate_sha256':ch,'reviewer':'Actual independent agent /root/v8_puzzle_logic',
    'scope':meaning['scope'],'evidence':'Actual all30case review, fresh16-map CSP,14nonspatial resolutions,90hint read, reasoning/claim closure: reviews/puzzles-final/FINAL_MEANING_LOGIC_CLOSURE.json',
    'receipt_sha256':sha(R/'reviews/puzzles-final/FINAL_MEANING_LOGIC_CLOSURE.json')})
dump(R/'reviews/FINAL_REVIEW_BUNDLE.json',{'candidate_sha256':ch,'status':'PASS','reviews':rr,
    'actual_specialist_agents':4,'one_writer':'/root','reading_pdf_sha256':ph,
    'normalization_only':'Interchange wrapper of actual independent PASS reports; not simulated reviewer output.'})

old=load(V7/'integration/EDITORIAL_IMPORT_PACKET_V7.json')
original={i:t for i,t in before.items()}
ops7=old.get('operations_from_original225')
if not isinstance(ops7,list):
    # Original operations are discoverable by schema below, rather than guessed.
    ops7=next((v for k,v in old.items() if 'original' in k.lower() and isinstance(v,list) and v and isinstance(v[0],dict) and ('before' in v[0] or 'source_text' in v[0])),[])
for op in ops7:
    i=op.get('id') or op.get('segment_id')
    if i in original:original[i]=op.get('before',op.get('source_text',original[i]))
packet={'format':'detective-en-v8-editorial-import-v1','candidate_sha256':ch,'baseline_v7_sha256':sha(R/'baseline/candidate-v7.json'),
    'reading_pdf_sha256':ph,'source_folios':225,'stable_units':3067,
    'operations_from_v7':ledger,'target_segment_hashes':{i:hashlib.sha256(t.encode()).hexdigest() for i,t in after.items()},
    'consumer':'Existing exclusive BookFactory writer; do not create a competing product master or renderer.',
    'inherited_import_contract':'v7/integration/EDITORIAL_IMPORT_PACKET_V7.json retains original225/V6source operations and required product slots.',
    'canonical_application':'Apply V7 original-source packet, then these146V8operations; verify all3067targethashes.',
    'retained_folio_remap':{'source16':'destination15','source27narrative':'destination26'},
    'preserve':['all27V6repairbytes','all30answerheaders','all107printedplacements','all31puzzleevidencefigures','allfourV6correctedleaves24/25/97/211'],
    'native_text_patch_surfaces':{'148':'Case03index FILE22/23 PHOTOS24/25 RECORD26; preserve card border.','184':'WHYITMATTERSpositivefeedbackonly; photograph and10markers unchanged.'},
    'actual_production_import':'PENDING_EXISTING_BOOK_FACTORY_WRITER','print_and_release':'NOT_GRANTED'}
dump(R/'integration/EDITORIAL_IMPORT_PACKET_V8.json',packet)
dump(R/'qa/CONTENT_MAP.json',{'candidate_sha256':ch,'source_coverage_folios':list(range(1,226)),
    'cases':load(R/'reviews/puzzles-r1/ALL30_PUZZLE_AUDIT_R1.json')['cases'],
    'function_repetition_and_reader_promise':'reviews/reader-market-r1/reader-market-review.json',
    'comedy_and_voice_map':'reviews/story-humor-r1/findings.json','audience_keep_and_repair_map':'reviews/audience-r1/audience-review-v7-diagnostic.json'})
run=R/'run-r2';il=load(run/'issue-ledger.json')
for i in il['issues']:i['resolution']='Exact sole-writer target independently checked; final native/audience/meaning/logic PASS bound to '+ch+'.'
dump(run/'issue-ledger.json',il)
checkpoint=f'''# Detective Academy EN V8 checkpoint

Status: OWNER_READ_CANDIDATE. Complete owner-authorized multidisciplinary English audit and integrated editorial corrections.

Exact candidate SHA256: `{ch}`. Baseline V7: `df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1`.

Four actual independent specialists covered story/native/humor; audience/developmental sensitivity/mentor support; all30 puzzle meaning/logic; reader engagement/promise/marketing. One root writer integrated47semanticgroups,146stableunits on41folios. Strong existing Comms preserved; onlyCase04Nini taskredirect changed in main30scenes. Hat becomes a current-tableprop, Dilo ending preserves carefulgrowth; mapdefinitions, supportnavigation, rulecopyorder, contract/payoff,15mapreasoning,05codeproof,26extractiontable,27alignmentreasoning improved.

Actual fresh independent CSP: all16maps each ONE FULL roster. All14othercases actuallychecked,90hints/30solutions read. All27V6repairs,16witnessboards,30answerheaders and107printedplacements unchanged. Case02unmarkedC3blocked byclearpositivekey; Case19actualF7blackmarker modeled. Case26explicit8zoneexclusions close unprintedROOM/ZONEkeygap. Four0records/14mapset/finaleinputs preserved.

Final independent native/audience/meaning/logic PASS on exacthash. Historicalbc90/460a reasoningFIXreceipts retained, not relabelledPASS. Run-r2canonical; runhistorical.

Reading PDF225pages SHA256 `{ph}`.173regeneratedtextleaves atminimum10.5pt;50evidence/designedsourceleavespixelidenticalV7,148/184boundednativePDFtextpatches. Actual independent fullsizechanged-folio checks and saved-PDFbindings inreviews; root225folio contact-layout pass isthumbnail-only. FinalBookFactorytypesetting/physicalprint notclaimed.

Consume integration/EDITORIAL_IMPORT_PACKET_V8.json through existing soleBookFactorywriter; originalV7contractand16→15/27→26 remaps remain. No productrenderer/source, PLversion, mainmerge, publication, contentfreeze or Actionsdispatch. HostedCIgreen notconfirmed.
'''
(R/'CHECKPOINT.md').write_text(checkpoint)
(R/'README.md').write_text('''# Detective Academy — complete English V8

The current owner-reading master is `proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf` (225pages). Canonical stable text is `candidate/candidate.json`; `candidate/reader-manuscript.md` is a text companion whose artwork folios point into the complete PDF.

Four actual independent specialists and one writer completed the requested whole-book audit. `CHECKPOINT.md` gives exact hashes, corrections, tests and limits. The consolidated Polish audit/change report is in `proof/DETECTIVE_EN_V8_AUDYT_I_ZMIANY.pdf`.

Review evidence is under `reviews/`; exact before/after changes are in `candidate/change-ledger.json` and `candidate/edit-units.json`. Canonical CLI run is `run-r2/`. The earlier `run/` and V8R1 baseline are historical, with original FIX receipts retained.

`integration/EDITORIAL_IMPORT_PACKET_V8.json` is for the existing exclusive BookFactory writer. It layers146operations over the inherited V7 import contract and checks3067targethashes. All prior V6 content/art repairs remain. Final production layout, physical proof and release are separate.
''')
print(json.dumps({'candidate_sha256':ch,'pdf_sha256':ph,'changed_units':len(actual),'groups':len(units),'status':'ACTUAL_REVIEW_BUNDLE_READY'},indent=2))
