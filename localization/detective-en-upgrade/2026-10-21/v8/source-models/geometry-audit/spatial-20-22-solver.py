import json,hashlib,pathlib,collections
D=pathlib.Path(__file__).resolve().parent
raw=(D/'spatial-20-22-grid.json').read_bytes();g=json.loads(raw)
def xy(s):return ord(s[0])-65,int(s[1])-1
def diag(a,b):
 x,y=xy(a);u,v=xy(b);return abs(x-u)==abs(y-v)==1
def near(a,b,mode):
 x,y=xy(a);u,v=xy(b);return abs(x-u)+abs(y-v)==1 if mode=='edge' else max(abs(x-u),abs(y-v))==1

def solve(k,adj='edge',south='any_distance',bunks=False):
 c=g[k]; cells=[f'{x}{y}' for y in range(1,8) for x in c['columns']];blocked=set(c['blocked'])
 if bunks:blocked-=set(c.get('black_marked_bunk_shapes',[]) if bunks is True else bunks)
 cells=[x for x in cells if x not in blocked]
 def room(x):a,b=xy(x);return c['room_rows'][b][a]
 if k=='case20':
  ns=['Mara','Asa','Luca','Pax','Sid','Toby','Demi'];dom={n:cells[:] for n in ns}
  dom['Mara']=[x for x in cells if room(x)=='M' and x[1]=='4'];dom['Asa']=[x for x in cells if room(x)=='M'];dom['Toby']=[x for x in cells if room(x)=='W']
 else:
  ns=['Wes','Cody','Gia','Imani','Lex','Nia','Zara'];dom={n:cells[:] for n in ns}
  dom['Wes']=[x for x in cells if any(room(z)==room(x) for z in c['instrument_lockers']) and not any(room(z)==room(x) and near(x,z,adj) for z in c['instrument_lockers'])]
  dom['Gia']=[x for x in cells if sum(abs(a-b) for a,b in zip(xy(x),xy(c['piano'])))==7]
 def valid(a,full=False):
  if k=='case20':
   if any(n!='Toby' and room(v)=='W' for n,v in a.items()):return False
   if 'Luca'in a and 'Asa'in a and not diag(a['Luca'],a['Asa']):return False
   if 'Mara'in a and 'Pax'in a:
    mx,my=xy(a['Mara']);px,py=xy(a['Pax'])
    if not(px>mx and py>my):return False
    if south=='same_ray' and px-mx!=py-my:return False
   if 'Sid'in a and 'Pax'in a:
    sx,sy=xy(a['Sid']);px,py=xy(a['Pax'])
    if not sy>py:return False
   who='Demi'
  else:
   if 'Wes'in a and 'Cody'in a and not diag(a['Wes'],a['Cody']):return False
   if 'Imani'in a and 'Lex'in a and not diag(a['Imani'],a['Lex']):return False
   if 'Imani'in a and 'Nia'in a and room(a['Imani'])!=room(a['Nia']):return False
   if 'Nia'in a and 'Lex'in a and (room(a['Nia'])=='P')+(room(a['Lex'])=='P')!=1:return False
   who='Zara'
  if who in a:
   count=sum(room(v)==room(a[who]) for v in a.values())
   if count>2 or full and count!=2:return False
  return True
 answers=collections.Counter();sol=[];nodes=0
 def rec(a,cols,rows):
  nonlocal nodes
  nodes+=1
  if len(a)==len(ns):
   if valid(a,True):
    sol.append(dict(a));who='Demi'if k=='case20' else'Zara'; contact=[(n,v)for n,v in a.items()if n!=who and room(v)==room(a[who])];answers[str(contact[0])]+=1
   return
  poss=[]
  for n in ns:
   if n not in a:
    opts=[v for v in dom[n] if v[0]not in cols and v[1]not in rows and valid(dict(a,**{n:v}))]
    poss.append((len(opts),n,opts))
  _,n,opts=min(poss)
  for v in opts:rec(dict(a,**{n:v}),cols|{v[0]},rows|{v[1]})
 rec({},set(),set())
 return {'full_assignment_count':len(sol),'answers':dict(answers),'assignments':sol[:200],'search_nodes':nodes,'truncated_assignments':len(sol)>200,'domain_sizes':{n:len(v)for n,v in dom.items()}}
out={'source_pdf_sha256':g['source_pdf_sha256'],'candidate_sha256':g['candidate_sha256'],'grid_sha256':hashlib.sha256(raw).hexdigest(),'cases':{}}
for k in ['case20','case22']:
 out['cases'][k]={}
 if k=='case20':
  for south in ['any_distance','same_ray']:
   out['cases'][k][south]=solve(k,south=south)
  out['cases'][k]['printed_furniture_list_bunks_usable_sensitivity']=solve(k,bunks=True)
  out['cases'][k]['only_E7_unblocked_sensitivity']=solve(k,bunks=['E7'])
  out['cases'][k]['only_F7_unblocked_sensitivity']=solve(k,bunks=['F7'])
 else:
  for adj in ['edge','eight']:
   out['cases'][k][adj]=solve(k,adj=adj)
# Read source solution comparison ONLY after all enumerations; never added to domains or predicates.
expected={'case20':{'Mara':'D4','Asa':'B2','Luca':'A1','Toby':'C6','Pax':'F5','Sid':'E7','Demi':'G3'},'case22':{'Gia':'B1','Wes':'D3','Cody':'C4','Imani':'F7','Lex':'E6','Nia':'G5','Zara':'A2'}}
for k,variants in out['cases'].items():
 for result in variants.values():
  result['expected_full_roster_present_post_enumeration']=expected[k] in result['assignments']
  result['unique_expected_full_roster_post_enumeration']=result['full_assignment_count']==1 and result['assignments'][0]==expected[k]
(D/'spatial-20-22-results.json').write_text(json.dumps(out,indent=2)+'\n')
for k,vs in out['cases'].items():
 for n,v in vs.items():print(k,n,v['full_assignment_count'],v['answers'])

