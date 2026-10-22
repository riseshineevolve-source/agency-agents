"""Enumerate original printed constraints; expected roster is comparison-only."""
import json,hashlib,pathlib,collections
ROOT=pathlib.Path(__file__).resolve().parent
GP=ROOT/'spatial-23-25-grid.json';grid=json.loads(GP.read_text())
def xy(s):return ord(s[0])-65,int(s[1])-1
def cell(x,y):return chr(x+65)+str(y+1)
def solve(k):
 g=grid[f'case{k}']; room=lambda s:g['room_rows'][xy(s)[1]][xy(s)[0]]
 cells=[cell(x,y) for y in range(7) for x in range(7) if cell(x,y) not in g['blocked']]
 names=list(g['expected']);domains={n:cells[:] for n in names}
 if k==23:
  domains['Vivi']=[s for s in cells if sum(abs(a-b) for a,b in zip(xy(s),xy(g['gondola'])))==7]
 else:
  domains['Casey']=[s for s in cells if room(s)=='L' and s[0]=='D']
  domains['Wynn']=[s for s in g['bar_stools'] if s in cells and room(s)=='A']
 def valid(a,final=False):
  def relation(n,m,fn):return n not in a or m not in a or fn(xy(a[n]),xy(a[m]))
  if k==23:
   if not relation('Cora','Mae',lambda p,q:p[0]>q[0] and p[1]<q[1]):return False
   if not relation('Ozzy','Cora',lambda p,q:p[0]<q[0] and p[1]>q[1]):return False
   if not relation('Rae','Cora',lambda p,q:p[0]==q[0]+2):return False
   if 'Pia' in a and 'Vivi' in a and ((room(a['Pia'])=='S')+(room(a['Vivi'])=='S')!=1):return False
   if all(n in a for n in ['Mae','Ozzy','Pia']):
    if not any(a[n] in g['benches'] and room(a[n])==room(a['Mae']) for n in ['Ozzy','Pia']):return False
  else:
   if not relation('Gabe','Rio',lambda p,q:abs(p[0]-q[0])==abs(p[1]-q[1])==1):return False
   if not relation('Rio','Gabe',lambda p,q:p[0]<q[0] and p[1]<q[1]):return False
   if not relation('Tate','Wynn',lambda p,q:abs(p[0]-q[0])==abs(p[1]-q[1])==1):return False
   if not relation('Sol','Gabe',lambda p,q:p[0]>q[0] and p[1]<q[1]):return False
  target='Jude' if k==23 else 'Nori'
  if target in a:
   count=sum(room(s)==room(a[target]) for s in a.values())
   if count>2 or (final and count!=2):return False
  return True
 out=[];nodes=0
 def rec(a,rows,cols):
  nonlocal nodes
  nodes+=1
  if len(a)==len(names):
   if valid(a,True):out.append(dict(a))
   return
  options=[]
  for n in names:
   if n in a:continue
   vals=[s for s in domains[n] if xy(s)[0] not in cols and xy(s)[1] not in rows and valid(dict(a,**{n:s}))]
   options.append((len(vals),n,vals))
  _,n,vals=min(options)
  for s in vals:
   x,y=xy(s);rec(dict(a,**{n:s}),rows|{y},cols|{x})
 rec({},set(),set())
 target='Jude' if k==23 else 'Nori'
 answers=collections.Counter()
 for a in out:
  for n,s in a.items():
   if n!=target and room(s)==room(a[target]):answers[f'{n} at {s}']+=1
 return {'case':k,'full_assignment_count':len(out),'assignments':out,'answers':dict(answers),'search_nodes':nodes,'matches_expected_post_enumeration':len(out)==1 and out[0]==g['expected']}
result={'source_pdf_sha256':grid['source_pdf_sha256'],'candidate_sha256':grid['candidate_sha256'],'grid_sha256':hashlib.sha256(GP.read_bytes()).hexdigest(),'solver_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'conventions':{'grid_steps':'Manhattan distance row difference + column difference, not wall-constrained walking path','north_east_south_west':'Strict quadrant any distance, not necessarily equal coordinate differences','diagonally_next_to':'Exactly one row and one column apart','global':'Every witness once; different row and column; printed blocked squares excluded'},'cases':[solve(23),solve(25)]}
(ROOT/'spatial-23-25-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

