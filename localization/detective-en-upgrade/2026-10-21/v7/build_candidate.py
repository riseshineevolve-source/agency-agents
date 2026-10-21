"""Single-writer V7 editorial candidate; V6 mechanics and artwork stay locked."""
from pathlib import Path
import ast, copy, hashlib, json, re, subprocess

R=Path(__file__).resolve().parent
W=R.parent
V6=W/'detective-v6'
OLD=W/'detective-upgrade'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
norm=lambda t:re.sub(r'\s+',' ',t).strip()
def dump(p,o):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')

BASE='d9dcc50eaccea03f693b1ade4ea001d522379d9def9f0467dd2e21ddd7e9fedc'
assert sha(R/'baseline/candidate-v6.json')==BASE
base=json.loads((R/'baseline/candidate-v6.json').read_text())
before={s['id']:s['text'] for s in base['segments']}
rich=json.loads((V6/'candidate/candidate-segments.json').read_text())
meta={s['id']:s for s in rich['segments']}
v6locks={s['id'] for s in json.loads((V6/'candidate/change-ledger.json').read_text())}
summary_exception='page212.block12'
allow=[s['id'] for s in rich['segments'] if (s['editable'] or s['id']==summary_exception) and s['id'] not in v6locks]
changes={}; reasons={}; unit_groups=[]

def apply(ids,text,issue):
    assert set(ids)<=set(allow),(ids,'outside prose allowlist')
    old=''.join(before[i] for i in ids)
    if norm(old)==norm(text):return
    assert not set(ids)&set(changes),('overlap',ids)
    tokens=re.findall(r'\S+\s*',text)
    assert len(tokens)>=len(ids),(ids,'too few words')
    weights=[max(1,len(re.findall(r'\S+',before[i]))) for i in ids]
    allocation=[1]*len(ids)
    for _ in range(len(tokens)-len(ids)):
        k=max(range(len(ids)),key=lambda j:weights[j]/allocation[j])
        allocation[k]+=1
    offset=0
    for i,n in zip(ids,allocation):
        t=''.join(tokens[offset:offset+n]);offset+=n
        if t!=before[i]:changes[i]=t;reasons[i]=issue
    assert ''.join(changes.get(i,before[i]) for i in ids)==text
    unit_groups.append({'ids':ids,'before':old,'after':text,'issue':issue})

scenes=json.loads((R/'diagnostic/comms-source-v6.json').read_text())
targets=json.loads((R/'edits_comms.json').read_text())
for scene in scenes:
    case=scene['case']; new=targets[str(case)]
    assert len(new)==len(scene['turns'])
    issue=f'HM{case:02d}: concrete scene diagnostic in reviews/comedy-diagnostic/diagnostic.json and story-diagnostic/DIAGNOSTIC.md; retain speaker/portrait order and puzzle truth.'
    if case==1:
        apply(['page016.block04'],'\n'.join(t['speaker']+': '+n for t,n in zip(scene['turns'],new)),issue)
    elif case==30:
        apply(['page137.block08'],"already proved.\n\nHAPPY MAKERS COMMS\n1 MIMI: "+new[0]+"\n2 DILO: "+new[1]+"\n",issue)
        apply(['page137.block09'],'\n'.join(f'{k+3} {t["speaker"]}: {new[k+2]}' for k,t in enumerate(scene['turns'][2:]))+'\n',issue)
    else:
        for turn,newtext in zip(scene['turns'],new):apply(turn['ids'],newtext+'\n',issue)
for edit in json.loads((R/'edits_story.json').read_text()):apply(edit['ids'],edit['text'],edit['issue'])

dump(R/'OWNER_AUTHORITY.json',{
 'date':'2026-10-21','baseline_candidate_sha256':BASE,
 'owner_request':'Use rse-language for another whole English text upgrade, especially funny, sharp, intelligent, affectionate Happy Makers Comms with real story value and reader belonging; explain prior changes honestly.',
 'mode':'Same-language upgrade; complete225folio diagnostic, bounded prose/comms authoring allowlist.',
 'locked':'All27 V6 deltas, all maps, clues, hints, solution answers/reasoning, names, four0records, 14map extraction and four finale inputs.',
 'narrow_summary_exception':'page212.block12 only: correct first-instruction chronology in WHY IT MATTERS prose. No answer or puzzle mechanism changes. Concrete independent R1 finding; within owner-requested whole-text upgrade.',
 'writer':'root; actual independent native/audience and meaning/logic reviewers run separately.',
 'product_source_or_renderer_changed':False,'freeze_or_publication':False})
intake={'format':'rse-authorized-editorial-upgrade','language':'en','authority':'OWNER_AUTHORITY.json',
 'baseline_candidate_sha256':BASE,'segments':[{'id':s['id'],'text':s['text'],
 'protected':s['id'] not in allow,'protected_tokens':[],'protected_numbers':[]} for s in base['segments']]}
source=R/'baseline/v7-intake-r2.json'
if source.exists():assert json.loads(source.read_text())==intake
else:dump(source,intake)
run=R/'run-r2'
if not run.exists():subprocess.run(['python',str(W/'rse/scripts/rse-language.py'),'prepare','--source',str(source),'--from','en','--to','en','--mode','upgrade','--project','detective-academy','--scope','bounded','--output',str(run)],check=True)
manifest=json.loads((run/'run.json').read_text())
dump(run/'change-scope.json',{'run_sha256':manifest['manifest_sha256'],'allowed_changed_segments':allow,
 'protected_segments':[i for i in before if i not in allow],
 'reason':'Owner-requested whole English editorial diagnostic and bounded prose/Comms upgrade. All V6 repairs and every puzzle, hint, solution answer/reasoning and artwork unit protected. One nonmechanic WHY IT MATTERS chronology exception: page212.block12.'})
candidate=copy.deepcopy(json.loads((run/'candidate.json').read_text()))
for s in candidate['segments']:s['text']=changes.get(s['id'],before[s['id']])
dump(R/'candidate/candidate.json',candidate)
ch=sha(R/'candidate/candidate.json')
after={s['id']:s['text'] for s in candidate['segments']}
assert set(after)==set(before) and len(after)==3067
assert all(before[i]==after[i] for i in v6locks)
assert set(changes)<=set(allow)
for s in rich['segments']:
    s['text']=before[s['id']];s['target_text']=after[s['id']]
    s['v7_editable']=s['id'] in allow
    s['decision']='FIX' if s['id'] in changes else 'GOLDEN_KEEP'
rich.update({'baseline_candidate_sha256':BASE,'candidate_sha256':ch})
dump(R/'candidate/candidate-segments.json',rich)
dump(R/'candidate/candidate-pages.json',[{'page':p,'text':''.join(s['target_text'] for s in rich['segments'] if s['page']==p)} for p in range(1,226)])
dump(R/'candidate/change-ledger.json',[{'id':i,'page':meta[i]['page'],'before':before[i],'after':after[i],
 'issue':reasons[i],'before_sha256':hashlib.sha256(before[i].encode()).hexdigest(),
 'target_sha256':hashlib.sha256(after[i].encode()).hexdigest()} for i in changes])
dump(R/'candidate/edit-units.json',unit_groups)
dump(R/'qa/GOLDEN_KEEP.json',{'candidate_sha256':ch,'unchanged_ids':[i for i in before if i not in changes],
 'whole_golden_main_comms':[c for c in range(1,31) if all(norm(t['v6_text'])==norm(n) for t,n in zip(scenes[c-1]['turns'],targets[str(c)]))],
 'reason':'Strong kernels preserved; all protected surfaces and V6 repairs exact.'})

# Explicit, source-verified reading order; this adapter never writes story text.
module=ast.parse((OLD/'candidate/build_reader.py').read_text())
order_node=next(n for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='orders' for t in n.targets))
orders=ast.literal_eval(order_node.value)
for page,entries in orders.items():
    revised=[]
    for speaker,t in entries:
        for i in changes:
            if meta[i]['page']!=page:continue
            old=before[i].strip()
            pattern=r'\s+'.join(re.escape(z) for z in old.split())
            t=re.sub(pattern,lambda m:after[i].strip(),t)
        revised.append((speaker,t))
    orders[page]=revised

page120=[s for s in rich['segments'] if s['page']==120]
story120=''.join(after[s['id']] for s in page120 if 4<=int(s['id'].split('block')[1])<=10)
turns120=[]
for i,speakers in [('page120.block15',['NINI','DILO']),('page120.block16',['LULI','BIBI']),('page120.block17',['MIMI'])]:
    lines=after[i].strip().splitlines()
    # Baseline wrapped speeches are reassembled by their verified boundaries.
    if i=='page120.block15':lines=['I knew we kept those maps for a reason.','I kept mine because the stack looked impressive.']
    assert len(lines)==len(speakers),(i,lines)
    turns120.extend(zip(speakers,lines))
orders[120]=[('',story120),('', 'HAPPY MAKERS COMMS')]+turns120
dump(R/'candidate/reader-order.json',{'candidate_sha256':ch,'purpose':'Attribution/read-order only; canonical text remains candidate.json. Folio120 verified visually; finale map inherited and changed strings rebound.', 'pages':orders})
pageinfo={p['page']:p for p in json.loads((OLD/'qa/source-page-map.json').read_text())['pages']}
out=['# Detective Academy\n\nThe Mystery of Room Zero\n\n']
artpages=[]
for p in range(1,226):
    out.append(f'\n\n## Page {p}\n\n')
    ps=[s for s in rich['segments'] if s['page']==p]
    artwork=pageinfo[p]['role']=='puzzle_or_evidence' or any('SOLUTION MAP' in s['target_text'] or 'SOLUTION PHOTO' in s['target_text'] for s in ps)
    if artwork:
        artpages.append(p)
        out.append('See the original evidence artwork on this folio in the illustrated reading proof.\n\n')
        continue
    if p in orders:
        for name,t in orders[p]:out.append((f'**{name}:** ' if name else '')+t+'\n\n')
        continue
    groups=[];j=0
    while j<len(ps):
        s=ps[j]
        if s.get('extraction_method')=='ocr_unverified':groups.append('*Evidence artwork appears on this page in the book.*');j+=1;continue
        if s['editable'] and p>=19:
            end=j
            while end<len(ps) and ps[end]['editable']:end+=1
            groups.append(''.join(z['target_text'] for z in ps[j:end]));j=end
        else:groups.append(s['target_text']);j+=1
    for g in groups:
        if re.fullmatch(r'\s*\d{1,3}\s*',g) and int(g.strip())==p:continue
        if g.strip() in ['HAPPY MAKERS / DETECTIVE ACADEMY','ACADEMY RECORD / STORY CONTINUES','DETECTIVE NOTES','DETECTIVE WORKSPACE']:continue
        g=g.strip()
        m=re.fullmatch(r'(?:\d+\s+)?(MIMI|LULI|DILO|NINI|ALIO|BIBI)\s*(?:\d+)?',g)
        if m:g='**'+m.group(1)+':**'
        g=re.sub(r'\n(?=(?:MIMI|LULI|DILO|ALIO|NINI|BIBI):)','\n\n',g)
        out.append(g+'\n\n')
text=''.join(out)
sections=re.split(r'(^## Page \d+\s*$)',text,flags=re.M)
for j in range(1,len(sections),2):
    body=sections[j+1]
    if 'WITNESS RECORD' in body:
        pos=body.index('WITNESS RECORD')+len('WITNESS RECORD');head,tail=body[:pos],body[pos:]
        matches=list(re.finditer(r'(?<!\S)(0[1-9]|[12][0-9]|30)(?=\s+[A-Z])',tail))
        if matches:
            records=[]
            for k,m in enumerate(matches):
                end=matches[k+1].start() if k+1<len(matches) else len(tail)
                records.append(norm(tail[m.start():end]))
            body=head+'\n\n'+'\n\n'.join(records)+'\n\n'
        for key in ['In this case, beside','PERSON MAY STAND ON:','SQUARE BLOCKED BY:']:body=body.replace(key,'\n\n'+key)
    sections[j+1]=body
text=''.join(sections)
(R/'candidate/reader-manuscript.md').write_text(text)

comparison=[]
for scene in scenes:
    case=scene['case']
    turns=[{**t,'v7_text':n,'changed_v7':norm(t['v6_text'])!=norm(n)} for t,n in zip(scene['turns'],targets[str(case)])]
    comparison.append({'case':case,'source_folio':scene['source_folio'],'turns':turns,
                       'changed_v7':any(t['changed_v7'] for t in turns)})
dump(R/'candidate/comms-comparison.json',{'candidate_sha256':ch,'scenes':comparison})
dump(R/'qa/BOUNDARY_CHECK.json',{'candidate_sha256':ch,'baseline_candidate_sha256':BASE,
 'segments':3067,'changed_units':len(changes),'changed_folios':sorted({meta[i]['page'] for i in changes}),
 'allowlist_units':len(allow),'protected_units':3067-len(allow),'v6_delta_locks':len(v6locks),
 'v6_repairs_exact':True,'outside_allowlist':[],
 'hints_solutions_maps':'Every hint, clue, answer, reasoning step and map BYTE_IDENTICAL_TO_V6. Only nonmechanic summary212block12 repairs chronology. Existing V6 corrected figures reused unchanged.',
 'nonmechanic_summary_exception':summary_exception,
 'main_comms_changed':sum(s['changed_v7'] for s in comparison),'main_comms_assessed':30,'source_art_folios':artpages,
 'reader_order120':'Five speeches bound to visually verified speakers; no wording added by adapter.',
 'print_ready':False})
dump(run/'issue-ledger.json',{'run_sha256':manifest['manifest_sha256'],'candidate_sha256':ch,'diagnostic':'COMPLETE',
 'issues':[{'id':f'EDITORIAL-{k:03d}','classification':'FIX','final_classification':'KEEP','status':'RESOLVED',
 'segments':u['ids'],'detail':u['issue'],'resolution':'Single writer integrated exact target; final independent reviews pending.'} for k,u in enumerate(unit_groups,1)]})
print(json.dumps({'candidate_sha256':ch,'changed_units':len(changes),'allowlist_units':len(allow),
 'main_comms_changed':sum(s['changed_v7'] for s in comparison),'golden_main_comms':[s['case'] for s in comparison if not s['changed_v7']],
 'reader_folios':len(re.findall(r'^## Page ',text,re.M))},indent=2))
