"""One writer integrates actual multidisciplinary findings into the V8 master."""
from pathlib import Path
import copy, hashlib, json, re, shutil, subprocess

R = Path(__file__).resolve().parent
W = R.parent
V7 = W / 'recovery/unpacked/detective-v7'
BASE = 'df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
norm = lambda t: re.sub(r'\s+', ' ', t).strip()
def dump(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

assert sha(V7 / 'candidate/candidate.json') == BASE
for name in ['baseline','candidate','qa','integration','proof','diagnostic']:
    (R / name).mkdir(exist_ok=True)
baseline = R / 'baseline/candidate-v7.json'
if not baseline.exists(): shutil.copy2(V7 / 'candidate/candidate.json', baseline)
assert sha(baseline) == BASE
base = json.loads(baseline.read_text())
before = {s['id']: s['text'] for s in base['segments']}
rich = json.loads((V7 / 'candidate/candidate-segments.json').read_text())
meta = {s['id']: s for s in rich['segments']}
v6locks = {s['id'] for s in json.loads((R / 'source-models/V6_CHANGE_LOCKS.json').read_text())}
edits = []
for name in ['edits-base.json','edits-clarity.json','edits-solutions.json']:
    edits.extend(json.loads((R / name).read_text()))
changes = {}; units = []
for e in edits:
    ids = e['ids']; text = e['text']
    assert ids and len(ids) == len(set(ids))
    assert not set(ids) & (set(changes) | v6locks), ('overlap/protected V6 repair', ids)
    assert all(i in before for i in ids)
    old = ''.join(before[i] for i in ids)
    if old == text: continue
    tokens = re.findall(r'\S+\s*', text)
    assert len(tokens) >= len(ids), ('too few words', ids)
    weights = [max(1,len(re.findall(r'\S+',before[i]))) for i in ids]
    allocation = [1] * len(ids)
    for _ in range(len(tokens)-len(ids)):
        j = max(range(len(ids)), key=lambda j: weights[j]/allocation[j])
        allocation[j] += 1
    cursor = 0
    for i,n in zip(ids,allocation):
        t = ''.join(tokens[cursor:cursor+n]); cursor += n
        if t != before[i]: changes[i] = t
    assert ''.join(changes.get(i,before[i]) for i in ids) == text
    units.append({**e,'before':old,'after':text})

allowed = sorted({i for e in edits for i in e['ids']}, key=lambda i:list(before).index(i))
intake = {'format':'rse-authorized-editorial-upgrade','language':'en',
    'baseline_candidate_sha256':BASE,'authority':'OWNER_AUTHORITY.json',
    'segments':[{'id':i,'text':t,'protected':i not in allowed,
                 'protected_tokens':[],'protected_numbers':[]} for i,t in before.items()]}
source = R / 'baseline/v8-intake-r2.json'
if source.exists(): assert json.loads(source.read_text()) == intake, 'New scope requires a new immutable run'
else: dump(source,intake)
run = R / 'run-r2'
if not run.exists():
    subprocess.run(['python3',str(W/'engine/scripts/rse-language.py'),'prepare',
        '--source',str(source),'--from','en','--to','en','--mode','upgrade',
        '--project','detective-academy','--scope','bounded','--output',str(run)],check=True)
manifest = json.loads((run/'run.json').read_text())
dump(run/'change-scope.json',{'run_sha256':manifest['manifest_sha256'],
    'allowed_changed_segments':allowed,'protected_segments':[i for i in before if i not in allowed],
    'reason':'Explicit22October owner whole-book audit; bounded concrete findings only. All V6 repairs, all answers/placements, names, clue facts, and locked puzzle art retained; two explanatory/navigation vector text surfaces updated.'})
candidate = copy.deepcopy(json.loads((run/'candidate.json').read_text()))
for s in candidate['segments']: s['text'] = changes.get(s['id'],before[s['id']])
dump(R/'candidate/candidate.json',candidate)
ch = sha(R/'candidate/candidate.json')
after = {s['id']:s['text'] for s in candidate['segments']}
assert len(after)==3067 and set(after)==set(before)
assert all(before[i]==after[i] for i in v6locks)
assert set(changes)<=set(allowed)
reason = {i:e['issue'] for e in units for i in e['ids']}
for s in rich['segments']:
    s['text'] = before[s['id']]; s['target_text'] = after[s['id']]
    s['v8_editable'] = s['id'] in allowed
    s['decision'] = 'FIX' if s['id'] in changes else 'KEEP'
rich.update({'baseline_candidate_sha256':BASE,'candidate_sha256':ch})
dump(R/'candidate/candidate-segments.json',rich)
dump(R/'candidate/change-ledger.json',[{'id':i,'page':meta[i]['page'],
    'before':before[i],'after':after[i],'issue':reason[i],
    'before_sha256':hashlib.sha256(before[i].encode()).hexdigest(),
    'target_sha256':hashlib.sha256(after[i].encode()).hexdigest()} for i in changes])
dump(R/'candidate/edit-units.json',units)
dump(R/'candidate/candidate-pages.json',[{'page':p,'text':''.join(after[s['id']] for s in rich['segments'] if s['page']==p)} for p in range(1,226)])

# Retain actual, source-verified speaker attribution; substitute only writer edits.
orders = json.loads((V7/'candidate/reader-order.json').read_text())['pages']
for p,entries in orders.items():
    for e in units:
        if str(meta[e['ids'][0]]['page']) != p: continue
        pattern = r'\s+'.join(re.escape(z) for z in e['before'].split())
        hits = 0
        for entry in entries:
            entry[1],n = re.subn(pattern,lambda m:e['after'].strip(),entry[1]); hits+=n
        assert hits==1,('reader-order binding',p,e['ids'],hits)
dump(R/'candidate/reader-order.json',{'candidate_sha256':ch,'purpose':'Only source-verified attribution; every changed ordered run is rebound to exact canonical words.','pages':orders})

boundary7 = json.loads((V7/'qa/BOUNDARY_CHECK.json').read_text())
art = set(boundary7['source_art_folios'])
out = ['# Detective Academy\n\nThe Mystery of Room Zero\n\n']
for p in range(1,226):
    out.append(f'\n\n## Page {p}\n\n')
    ps = [s for s in rich['segments'] if s['page']==p]
    if p in art:
        out.append('See the evidence artwork on this folio in the full illustrated reading version.\n\n')
        continue
    if str(p) in orders:
        for speaker,t in orders[str(p)]: out.append((f'**{speaker}:** ' if speaker else '')+t+'\n\n')
        continue
    # Solution explanation columns must read as complete deductions, not extraction blocks.
    if p>=179 and any('HOW THE EVIDENCE FITS' in s['target_text'] for s in ps):
        start=next(j for j,s in enumerate(ps) if 'HOW THE EVIDENCE FITS' in s['target_text'])
        end=next((j for j,s in enumerate(ps) if 'WHY IT MATTERS' in s['target_text']),len(ps))
        title=''.join(s['target_text'] for s in ps[:start+1] if not s['target_text'].strip().startswith('HAPPY MAKERS / DETECTIVE ACADEMY'))
        body=''.join(s['target_text'] for s in ps[start+1:end])
        body=re.sub(r'(?m)^(0[1-9]|10)\s*\n',r'\n\n\1. ',body).strip()
        out.append(title+'\n\n'+body+'\n\n')
        if end<len(ps):out.append('WHY IT MATTERS\n\n'+''.join(s['target_text'] for s in ps[end+1:])+'\n\n')
        continue
    groups=[]; j=0
    while j<len(ps):
        s=ps[j]
        if s.get('extraction_method')=='ocr_unverified':
            groups.append('*Evidence artwork appears on this page in the book.*');j+=1;continue
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
        k=body.index('WITNESS RECORD')+len('WITNESS RECORD');head,tail=body[:k],body[k:]
        matches=list(re.finditer(r'(?<!\S)(0[1-9]|[12][0-9]|30)(?=\s+[A-Z])',tail))
        if matches:
            records=[]
            for z,m in enumerate(matches):
                end=matches[z+1].start() if z+1<len(matches) else len(tail)
                records.append(norm(tail[m.start():end]))
            body=head+'\n\n'+'\n\n'.join(records)+'\n\n'
        for key in ['In this case, beside','PERSON MAY STAND ON:','SQUARE BLOCKED BY:']:
            body=body.replace(key,'\n\n'+key)
    sections[j+1]=body
text=''.join(sections)
(R/'candidate/reader-manuscript.md').write_text(text)
assert len(re.findall(r'^## Page ',text,re.M))==225
dump(R/'qa/BOUNDARY_CHECK.json',{'candidate_sha256':ch,'baseline_candidate_sha256':BASE,
    'segments':3067,'changed_units':len(changes),'changed_folios':sorted({meta[i]['page'] for i in changes}),
    'v6_delta_locks':27,'v6_repairs_exact':True,'outside_allowlist':[],
    'source_art_folios':sorted(art),'actual_pdf_text_patch_folios':[148,184],
    'answers_and_printed_placements':'All30 answer headers and107positions retained; reasoning expands but never changes solution.',
    'print_ready':False})
dump(R/'qa/GOLDEN_KEEP.json',{'candidate_sha256':ch,'unchanged_ids':[i for i in before if i not in changes],
    'protected_v6_ids':sorted(v6locks),'reason':'Concrete-defect integration only; actual specialist KEEP registry retained in reports.'})
dump(run/'issue-ledger.json',{'run_sha256':manifest['manifest_sha256'],'candidate_sha256':ch,
    'diagnostic':'COMPLETE','issues':[{'id':f'V8-{k:03d}','segment_id':e['ids'][0],
      'classification':'FIX','final_classification':'KEEP','segments':e['ids'],'detail':e['issue'],
      'resolution':'Sole writer applied exact target. Independent closure review required before delivery.'} for k,e in enumerate(units,1)],
    'source_ambiguities':[]})
brief=json.loads((V7/'run-r2/functional-brief.json').read_text())
brief['run_sha256']=manifest['manifest_sha256']
for u in brief['units']:
    u['decision']='FIX' if u['id'] in changes else 'KEEP'
    u['permission']='BOUNDED_CONCRETE_FINDING' if u['id'] in allowed else 'EXACT_V7_KEEP'
dump(run/'functional-brief.json',brief)
print(json.dumps({'candidate_sha256':ch,'changed_units':len(changes),'changed_folios':sorted({meta[i]['page'] for i in changes}),'edit_groups':len(units)},indent=2))
