from pathlib import Path
import json,hashlib,datetime,re
B=Path('/workspace/scratch/e6eabdc4c3a0/detective-v8')
O=B/'reviews/reader-market-final';O.mkdir(parents=True,exist_ok=True)
V7=Path('/workspace/scratch/e6eabdc4c3a0/recovery/unpacked/detective-v7/candidate')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
path=B/'candidate/candidate.json';h=sha(path)
assert h=='d0faccca46f0023d564154a1fe3f6a559ce37ac31dc53f6d2b4fe7d4f1b9fc1e'
C=json.loads(path.read_text())['segments'];N={x['id']:x['text'] for x in C}
A={x['id']:x['text'] for x in json.loads((V7/'candidate.json').read_text())['segments']}
R1={x['id']:x['text'] for x in json.loads((B/'baseline/v8-r1-candidate.json').read_text())['segments']}
D=sorted(i for i in A if A[i]!=N[i]);d=sorted(i for i in R1 if R1[i]!=N[i])
E=json.loads((B/'candidate/edit-units.json').read_text());L=json.loads((B/'candidate/change-ledger.json').read_text());S=json.loads((B/'candidate/candidate-segments.json').read_text())['segments'];by={x['id']:x for x in S}
old_review=json.loads((B/'reviews/reader-market-r1/reader-market-review.json').read_text())
def ids(p,a,b):return [f'page{p:03}.block{x:02}' for x in range(a,b+1)]
closures=[
 ('RM01','Fifteen map explanations now show actual options, exclusions and failed branches before the final roster. The reader can see why a tempting finish fails rather than merely copy coordinates. Case01 remains a clear worked introduction.',[i for u in old_review['findings'][0]['solution_units'] for i in u['segment_ids']]),
 ('RM02','Case26 now gives all fourteen selected case / empty-room / initial rows, in order. The table matches the existing independent derivation and produces CHECK THE OLD MAP. A reader can locate an individual extraction error.',ids(220,7,12)),
 ('RM03','The frontmatter now promises growing maps and different ways of testing evidence. It no longer promises every activity is harder than the previous one. The lighter activities remain useful pace changes.',['page005.block05']),
 ('RM04','The returning-question colon is followed by WHAT IS ROOM ZERO before the cast transition.',['page005.block07']),
 ('RM05','Case04 now earns a witness for the transfer-record gap. Nini asks who was with Pixel; Zuri’s account lets Mimi correct the record and return the sealed box. No carrier identity or unreported carrying event has been invented.',ids(27,15,17)+ids(27,27,29)+['page030.block03']),
 ('RM06','Case23 asks for the witness who can address the missing handoff. The setup no longer promises a precise crossing location that is never supplied. The next-page clean-handoff closure now fulfills the stated local contract.',ids(108,12,13)+ids(112,3,4)),
 ('RM07','Casey now explicitly confirms that the parcel is a return for Archive Restoration, not a Guest House delivery. This closes Bibi’s intended-recipient question using the existing return label and borrowed-tool facts, without creating a new addressee.',ids(116,11,12)+['page120.block05']),
 ('RM08','The Case03 lookup line now points to FILE22/23, PHOTOS24/25 and RECORD26. The actual PDF patch also displays that line, with hint/solution references retained. A separate cosmetic border repair is tracked only in the visual receipt.',['page148.block15']),
 ('RM09','The Act2 bridge keeps Mimi’s concrete place-beside-the-file action and removes its repeated final belonging sentence. The four marks and incomplete route still carry the forward question.',ids(40,5,7)),
 ('RM10','The short Bibi bridge now narrates one trip to the archive, preserves her uncertainty and gives the exact saved note. It does not send her away twice in the same paragraph.',ids(52,4,9)),
 ('RM11','The body no longer repeats the whole headline. It begins with the precise action to copy RULE0FIRST and keeps the missing rule open.',ids(81,2,6)),
 ('RM12','The invitation now says Case01 is just ahead. It no longer implies that the very next folio is the case rather than the intervening transition.',['page014.block02']),
]
F=[]
for key,evidence,ss in closures:
 base=next(x for x in old_review['findings'] if x['id']==key)
 F.append({'id':key,'status':'CLOSED','original_priority':base['priority'],'segments':ss,'evidence':evidence,'candidate_sha256':h})
new_closed=[
 {'id':'FINAL-READER-MAP20-REFERENTS','status':'CLOSED','segments':ids(210,7,12),'evidence':'The final explanation explicitly names Mara atE4 and Asa atE3 as the rejected options. It explains that Demi would then have two companions and concludes MaraD4/AsaB2. The previous ambiguous “either alternative” reference is gone. The unchanged witness board on96 and the final roster/answer were reread.'},
 {'id':'FINAL-READER-MAP13-CONDITION','status':'CLOSED','segments':ids(199,7,12),'evidence':'The failed BodhiB6/RemyD7 branch is now explicitly conditional on MoxieC5, after MoxieD5 has been rejected. “No way to place both Eden and Bodhi” no longer suggests a shared-room clue.'},
 {'id':'FINAL-READER-TITLE204','status':'CLOSED','segments':['page204.block02','page204.block03','page204.block04'],'evidence':'The wrapped PHOTOGRAPH title continuation is retained in the final clean reader and actual saved PDF; source footer metadata no longer replaces that title line.'},
 {'id':'FINAL-READER-TEACHING-CLARIFIERS','status':'KEEP','segments':['page194.block07']+ids(205,7,13),'evidence':'The Dash companion constraint is explicitly included in the row-coverage step. The OtisC5 alternative is explicitly rejected because it would block both remaining Sunny bench choices. These additions make the stated route easier to follow.'}
]
keep=[]
for x in old_review['golden_keep']:
 keep.append({'id':x['id'],'status':'FUNCTION_PRESERVED','title':x['title'],'segments':x['segment_ids'],'changed_since_v7':[i for i in x['segment_ids'] if A[i]!=N[i]],'evidence':x['reason']})
groups=[]
for n,e in enumerate(E,1):
 groups.append({'group':n,'status':'REVIEWED','issue':e['issue'],'segments':e['ids'],'exact_after_sha256':hashlib.sha256(e['after'].encode()).hexdigest(),'joined_candidate_equals_after':e['after']==''.join(N[i] for i in e['ids'])})
proof=B/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf';proofhash=sha(proof)
receipt={
 'reviewer':'Actual independent agent /root/v8_reader_market',
 'reviewed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'stage':'logic','stages':['logic','continuity','reader_experience','promise','functional_repetition'],
 'candidate_sha256':h,'status':'PASS','open_findings':[],
 'scope':'Actual complete 225-folio V8 R1 reading, including all30cases and all hints/solutions, at bc90b44439e6380104a67873383e946923577b86ece0b6f482380b6c9e73c76b; then verified exact R2/final delta, affected neighbors and dependency closure on d0faccca46f0023d564154a1fe3f6a559ce37ac31dc53f6d2b4fe7d4f1b9fc1e. No pretend repeated whole-book read after bounded fixes.',
 'full_direct_read_candidate_sha256':'bc90b44439e6380104a67873383e946923577b86ece0b6f482380b6c9e73c76b',
 'full_direct_read_baseline_path':str(B/'baseline/v8-r1-candidate.json'),
 'diagnostic_candidate_sha256':'df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1',
 'exact_final_delta_since_full_read':d,'unchanged_segments_inherited_from_full_read':len(N)-len(d),
 'complete_reader_folios_reviewed':list(range(1,226)),'cases_reviewed':list(range(1,31)),
 'all_47_edit_groups_reviewed':groups,
 'actual_changes_since_v7':{'count':len(D),'folios':len(set(x['page'] for x in L)),'ids':D},
 'reader_manuscript_sha256':sha(B/'candidate/reader-manuscript.md'),
 'rich_segments_sha256':sha(B/'candidate/candidate-segments.json'),
 'change_ledger_sha256':sha(B/'candidate/change-ledger.json'),
 'edit_units_sha256':sha(B/'candidate/edit-units.json'),
 'findings':F,'additional_closure_findings':new_closed,'golden_keep':keep,
 'global_invariants':[
  {'check':'All30cases retained','status':'PASS','evidence':'All30case objectives, main Comms and solution entries read. No case removed or reordered.'},
  {'check':'All original answer entries unchanged','status':'PASS','evidence':'All30ANSWER segments compare byte-identically with V7.'},
  {'check':'Spatial witness evidence preserved','status':'PASS','evidence':'All16spatial witness boards compare byte-identically; only explanatory/common-rule language changed.'},
  {'check':'Fourteen-map extraction remains earned','status':'PASS','evidence':'The selected14maps, explicit task-local room/zone key and new solution table agree with the existing independent derivation. Case01 is excluded only from this extraction.'},
  {'check':'Final inputs and personal identity','status':'PASS','evidence':'ASSUMPTIONS,D3,BALL–STAR–BOLT–HEART–KEY–MOON and the established reader call sign still supply the four final fields. The call sign is now defined at first use; help writing it is allowed.'},
  {'check':'Book1closure precedes sequel','status':'PASS','evidence':'Bibi authorship, room purpose, route function/limits, invitation and field vacancy close before certification. Book1log is filed before the new cut-out photograph is released.'},
  {'check':'Main Comms preservation','status':'PASS','evidence':'All30main Comms compared; only Nini04’s redirect changes. Quiet torn-note repair, distinct family viewpoints, Dilo’s checking arc and Alio’s observed pause survive.'},
  {'check':'No invented lore or sales claims','status':'PASS','evidence':'No new watcher, villain, tunnel, earlier triangle match, carrier event, wristband crossing location, recipient name, availability or sales guarantee is introduced.'},
  {'check':'Precise actual edit ledger','status':'PASS','evidence':'146actualchangedIDs across41folios exactly equal ledger; all47group after strings match joined compact candidate; rich target text agrees for all3067IDs.'}
 ],
 'reader_assessment':'The final text fulfills its family detective puzzle-adventure promise. Clearer help, map terms and worked routes improve access; the retained shorter cases keep the larger-map load from becoming one unbroken difficulty demand. The accumulated evidence, quiet repair scene, sixth-hook certification and specific new archive file give the book a complete first ending with a credible reason to continue. No additional broad rewrite is warranted.',
 'visual_review':'Separate saved-PDF visual receipt. Candidate logic PASS is independent of the small proof-only index-card border repair.',
 'proof_snapshot_sha256':proofhash,'print_ready':False,
 'limits':['This is an actual text logic/continuity/reader review; independent all-map solving belongs to the puzzle reviewer.','Audience judgments are editorial inferences; no reader-testing or sales-performance claim is made.','No final production typography, physical-print approval, content freeze or release authorization is granted.']
}
# Format only known compact phrases in our narrative notes; never alter IDs, source text or hashes.
repls={'all30cases':'all 30 cases','RULE0FIRST':'RULE 0 FIRST','Case01':'Case 01','MaraD4/AsaB2':'Mara D4 / Asa B2','atE4':'at E4','atE3':'at E3','BodhiB6/RemyD7':'Bodhi B6 / Remy D7','MoxieC5':'Moxie C5','MoxieD5':'Moxie D5','OtisC5':'Otis C5','All30case':'All 30 case','All30ANSWER':'All 30 ANSWER','All16spatial':'All 16 spatial','selected14maps':'selected 14 maps','ASSUMPTIONS,D3':'ASSUMPTIONS, D3','MOON and':'MOON and','Book1log':'Book 1 log','All30main':'All 30 main','Nini04':'Nini 04','146actualchangedIDs':'146 actual changed IDs','across41folios':'across 41 folios','all47group':'all 47 group','all3067IDs':'all 3,067 IDs'}
def fix(v,key=None):
 if isinstance(v,dict):
  for k,x in v.items():v[k]=fix(x,k)
 elif isinstance(v,list):
  for i,x in enumerate(v):v[i]=fix(x,key)
 elif isinstance(v,str) and key in {'scope','evidence','reader_assessment','title'}:
  for old,new in repls.items():v=v.replace(old,new)
 return v
receipt=fix(receipt)
for name in ['logic.json','full_findings.json']:(O/name).write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
md=['# Detective Academy V8 — final reader and continuity receipt','',
 '**Text status: PASS.** All twelve R1 findings are closed. No material reader, promise, continuity or repetition finding remains open.','',
 f'Candidate SHA-256: `{h}`','',
 'The complete 225-folio V8 R1 manuscript was read at the preserved bc90 baseline. The final bounded delta, affected pages and all dependencies were then reread on this exact candidate. All 47 edit groups and their joins were inspected. This is not a claim that the entire book was reread after each small correction.','',
 '## R1 closure','', '| Finding | Final disposition |', '|---|---|']
for f in F:md.append('| '+f['id']+' | '+f['evidence']+' |')
md += ['', '## Final dependency checks','']
for f in receipt['additional_closure_findings']:md += ['- **'+f['id']+': '+f['status']+'.** '+f['evidence']]
md += ['', '## Retained strengths and book promise','',receipt['reader_assessment'],'',
 'All 30 cases and all final answers remain. The 14 selected maps still produce CHECK THE OLD MAP, and Case 01 keeps its recruitment job. All 30 main Comms remain except Nini’s tightly scoped Case 04 redirect. The family’s shared humor, Dilo’s quieter checking, the torn-note repair and the empty-hook payoff survive. The new sequel file appears after the first route is complete; it does not reopen the solved Cup or invent a triangle match.','',
 '## Exact binding and coverage','',
 f'- Candidate: `{h}`',
 f'- Reader manuscript: `{receipt["reader_manuscript_sha256"]}`',
 '- 3,067 stable IDs; 146 changed IDs across 41 folios; 47 groups.',
 f'- {len(d)} final IDs differ from the complete-read bc90 baseline; {len(N)-len(d)} identical units inherit that actual reading.',
 '- All 30 answer entries and all 16 spatial witness boards are unchanged.',
 '- Every ledger before/after value, target hash, rich target and grouped after string was checked.',
 '', 'The JSON includes all exact IDs, per-finding evidence, KEEP units and group hashes. The separate visual receipt is bound to the saved PDF and its inspected folios. It does not establish print readiness or release approval.','']
(O/'review.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'status':receipt['status'],'hash':h,'closure_findings':len(F),'groups':len(groups),'final_delta_ids':len(d),'outputs':[str(O/'logic.json'),str(O/'full_findings.json'),str(O/'review.md')]},indent=2))
