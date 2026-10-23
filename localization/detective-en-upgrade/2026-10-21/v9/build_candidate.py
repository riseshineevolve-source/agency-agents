"""Root sole-writer: dialogue-only layer over the exact accepted V8 mechanics."""
from pathlib import Path
import copy, hashlib, json, re, shutil, subprocess

R=Path(__file__).resolve().parent; W=R.parent; V8=W/'detective-v8'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
norm=lambda t:re.sub(r'\s+',' ',t).strip()
def dump(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(R/'baseline/candidate-v8.json')=='d0faccca46f0023d564154a1fe3f6a559ce37ac31dc53f6d2b4fe7d4f1b9fc1e'
base=json.loads((R/'baseline/candidate-v8.json').read_text())
before={s['id']:s['text'] for s in base['segments']}
scenes=json.loads((R/'diagnostic/source-scenes.json').read_text())
targets=json.loads((R/'dialogue-r1.json').read_text())
if (R/'dialogue-final.json').exists():targets=json.loads((R/'dialogue-final.json').read_text())
authority=json.loads((R/'OWNER_AUTHORITY.json').read_text());allowed=authority['scope']['allowed_ids']
updates={}; edit_units=[]
def apply(ids,text,scene):
    assert set(ids)<=set(allowed) and not set(ids)&set(updates)
    old=''.join(before[i] for i in ids)
    if old==text:return
    tokens=re.findall(r'\S+\s*',text)
    weights=[max(1,len(re.findall(r'\S+',before[i]))) for i in ids]
    allocation=[1]*len(ids)
    for _ in range(len(tokens)-len(ids)):
        j=max(range(len(ids)),key=lambda j:weights[j]/allocation[j]);allocation[j]+=1
    cursor=0
    for i,n in zip(ids,allocation):updates[i]=''.join(tokens[cursor:cursor+n]);cursor+=n
    assert ''.join(updates[i] for i in ids)==text
    edit_units.append({'scene':scene,'ids':ids,'before':old,'after':text})

for s in scenes:
    sid=s['id'];tt=targets[sid];turns=s['turns']
    assert len(tt)==len(turns) and all(t.strip()==t and t for t in tt)
    if sid in ['INTRO07','CASEWALL12','CASE01']:
        apply(turns[0]['ids'],'\n'.join(t['speaker']+': '+n for t,n in zip(turns,tt)),sid)
    elif sid=='CASE30':
        prefix=before['page137.block08'].split('HAPPY MAKERS COMMS',1)[0]
        assert prefix=='already proved.\n\n'
        apply(['page137.block08'],prefix+'HAPPY MAKERS COMMS\n1 MIMI: '+tt[0]+'\n2 DILO: '+tt[1]+'\n',sid)
        apply(['page137.block09'],'\n'.join(f'{k+3} {t["speaker"]}: {n}' for k,(t,n) in enumerate(zip(turns[2:],tt[2:])))+'\n',sid)
    elif sid=='THREAD120':
        apply(['page120.block15'],tt[0]+'\n'+tt[1]+'\n',sid)
        apply(['page120.block16'],tt[2]+'\n'+tt[3]+'\n',sid)
        apply(['page120.block17'],tt[4]+'\n',sid)
    else:
        for t,n in zip(turns,tt):apply(t['ids'],n+'\n',sid)

intake={'format':'rse-authorized-editorial-upgrade','language':'en','baseline_candidate_sha256':sha(R/'baseline/candidate-v8.json'),
 'authority':'OWNER_AUTHORITY.json','segments':[{'id':i,'text':t,'protected':i not in allowed,'protected_tokens':[],'protected_numbers':[]} for i,t in before.items()]}
source=R/'baseline/v9-intake.json'
if source.exists():assert json.loads(source.read_text())==intake
else:dump(source,intake)
run=R/'run'
if not run.exists():subprocess.run(['python3',str(W/'engine/scripts/rse-language.py'),'prepare','--source',str(source),'--from','en','--to','en','--mode','upgrade','--project','detective-academy','--scope','bounded','--output',str(run)],check=True)
manifest=json.loads((run/'run.json').read_text())
dump(run/'change-scope.json',{'run_sha256':manifest['manifest_sha256'],'allowed_changed_segments':allowed,'protected_segments':[i for i in before if i not in allowed],
 'reason':'Explicit owner unlock ONLY34HMComms, 183existingturns; allothertextexactV8 plusmixed137narrativeprefix retained.'})
candidate=copy.deepcopy(json.loads((run/'candidate.json').read_text()))
for x in candidate['segments']:x['text']=updates.get(x['id'],before[x['id']])
dump(R/'candidate/candidate.json',candidate);ch=sha(R/'candidate/candidate.json')
after={x['id']:x['text'] for x in candidate['segments']};actual=[i for i in before if after[i]!=before[i]]
assert set(actual)<=set(allowed) and len(after)==3067
assert after['page137.block08'].split('HAPPY MAKERS COMMS',1)[0]=='already proved.\n\n'
rich=json.loads((V8/'candidate/candidate-segments.json').read_text());meta={s['id']:s for s in rich['segments']}
for x in rich['segments']:
    x['text']=before[x['id']];x['target_text']=after[x['id']];x['v9_editable']=x['id'] in allowed;x['decision']='FIX' if x['id'] in actual else 'GOLDEN_KEEP'
rich.update({'baseline_candidate_sha256':sha(R/'baseline/candidate-v8.json'),'candidate_sha256':ch})
dump(R/'candidate/candidate-segments.json',rich)
dump(R/'candidate/candidate-pages.json',[{'page':p,'text':''.join(after[x['id']] for x in rich['segments'] if x['page']==p)} for p in range(1,226)])
dump(R/'candidate/edit-units.json',edit_units)
dump(R/'candidate/change-ledger.json',[{'id':i,'page':meta[i]['page'],'before':before[i],'after':after[i],
 'before_sha256':hashlib.sha256(before[i].encode()).hexdigest(),'target_sha256':hashlib.sha256(after[i].encode()).hexdigest()} for i in actual])

# Replace only each spoken string in the already verified complete V8 reading order.
reader=(V8/'candidate/reader-manuscript.md').read_text();parts=re.split(r'(^## Page (\d+)\s*$)',reader,flags=re.M)
page_offsets={int(parts[k+1]):k+2 for k in range(1,len(parts),3)}
replacements={}
for s in scenes:
    for t,new in zip(s['turns'],targets[s['id']]):
        p=int(t['ids'][0][4:7]);body=parts[page_offsets[p]]
        pattern=r'\s+'.join(re.escape(z) for z in t['v8_text'].split())
        matches=list(re.finditer(pattern,body));assert len(matches)==1,(s['id'],t['speaker'],t['v8_text'],len(matches))
        m=matches[0];replacements.setdefault(p,[]).append((m.start(),m.end(),new))
for p,rs in replacements.items():
    body=parts[page_offsets[p]];rs.sort(reverse=True)
    assert all(rs[i][0]>=rs[i+1][1] for i in range(len(rs)-1))
    for a,b,text in rs:body=body[:a]+text+body[b:]
    parts[page_offsets[p]]=body
# The inner numeric capture locates pages; it is metadata, never book body text.
final_reader=''.join(value for k,value in enumerate(parts) if k%3!=2)
fp=re.split(r'^## Page (\d+)\s*$',final_reader,flags=re.M)
original_pages=re.split(r'^## Page (\d+)\s*$',reader,flags=re.M)
assert len(fp)==len(original_pages)==451
for k in range(1,len(fp),2):
    p=int(fp[k]);oldbody=original_pages[k+1];newbody=fp[k+1]
    for s in scenes:
        for turn,new in zip(s['turns'],targets[s['id']]):
            if int(turn['ids'][0][4:7])!=p:continue
            marker='[SPOKEN_'+s['id']+'_'+str(s['turns'].index(turn))+']'
            oldbody,n=re.subn(r'\s+'.join(re.escape(z) for z in turn['v8_text'].split()),lambda m:marker,oldbody)
            assert n==1
            newbody,n=re.subn(re.escape(new),lambda m:marker,newbody)
            assert n==1
    assert oldbody==newbody,('nonCommsreaderdrift',p)
(R/'candidate/reader-manuscript.md').write_text(final_reader)
orders=json.loads((V8/'candidate/reader-order.json').read_text())
for s in scenes:
    for p in s['folios']:
        if str(p) not in orders['pages']:continue
        if s['id']=='THREAD120':
            speechiter=iter(targets[s['id']]);orders['pages'][str(p)]=[(speaker,next(speechiter) if speaker else text) for speaker,text in orders['pages'][str(p)]]
orders['candidate_sha256']=ch;dump(R/'candidate/reader-order.json',orders)
clean=['# Happy Makers Comms\n\nThe Mystery of Room Zero\n\n']
final_scenes=[]
for s in scenes:
    final_scenes.append({**s,'turns':[{**t,'final_text':n} for t,n in zip(s['turns'],targets[s['id']])]})
    label=f'Case {s["case"]:02d}' if s['case'] else {'INTRO07':'Meet the Happy Makers','CASEWALL12':'Your Case Wall','THREAD34':'Four Matching Marks','THREAD120':'The Old Cases Come Back'}[s['id']]
    clean.append('\n## '+label+'\n\n')
    for t,new in zip(s['turns'],targets[s['id']]):clean.append('**'+t['speaker']+':** '+new+'\n\n')
(R/'candidate/HAPPY_MAKERS_COMMS_FINAL_EN.md').write_text(''.join(clean))
dump(R/'candidate/final-scenes.json',{'candidate_sha256':ch,'scenes':final_scenes})
unchanged=[i for i in before if i not in actual]
dump(R/'qa/GOLDEN_KEEP.json',{'candidate_sha256':ch,'protected_outside_comms':[i for i in before if i not in allowed],
 'unchanged_ids':unchanged,'protected_mixed_unit_prefix':{'page137.block08':'already proved.\n\n'},'puzzle_truth':'ExactV8retained; no newunchangedpuzzlesolve claimed.'})
v8delta=json.loads((V8/'candidate/change-ledger.json').read_text())
protected_repairs=[x['id'] for x in v8delta if x['id'] not in allowed]
assert all(after[i]==before[i] for i in protected_repairs)
dump(R/'qa/BOUNDARY_CHECK.json',{'candidate_sha256':ch,'baseline_v8_sha256':sha(R/'baseline/candidate-v8.json'),'segments':3067,
 'scenes':34,'turns':183,'allowlisted_units':len(allowed),'changed_units':len(actual),'changed_folios':sorted(replacements),
 'outside_allowlist':[],'protected_outside_comms_unchanged':3067-len(allowed),'protected_mixed137prefix':'PASS',
 'all_non_comms_v8_repairs_exact':True,'speaker_turn_order_unchanged':True,'all_unedited_folios_exact':True,
 'puzzles_hints_solutions_figures':'UNCHANGED_FROM_V8; inheritedverifiedV8receipts, no needlessre-solving','print_ready':False})
dump(run/'issue-ledger.json',{'run_sha256':manifest['manifest_sha256'],'candidate_sha256':ch,'diagnostic':'COMPLETE',
 'issues':[{'id':'HM9-'+s['id'],'classification':'FIX','final_classification':'KEEP','status':'RESOLVED','segments':sorted(set(i for t in s['turns'] for i in t['ids'])),
 'detail':'Owner-requested original/V7merge, full conversational response and warmfamilyvoice; actual4diagnosticreviews refer toscopedscene.','resolution':'Rootwriter authored actualdialogue; finalindependentreviewstored separately.'} for s in scenes]})
print(json.dumps({'candidate_sha256':ch,'changed_units':len(actual),'changed_folios':len(replacements),'scenes':34,'turns':183,
 'v8_words':sum(len(t['v8_text'].split()) for s in scenes for t in s['turns']),
 'target_words':sum(len(t.split()) for ts in targets.values() for t in ts)},indent=2))
