#!/usr/bin/env python3
"""Original-map exact-cover placement audit. Expected answers are comparison-only."""
import json, itertools, hashlib, pathlib, collections, time
BASE=pathlib.Path(__file__).resolve().parent
path=BASE/'spatial-intro-29-grid.json'; data=json.loads(path.read_text())
def xy(s): return ord(s[0])-65,int(s[1:])-1
def room(g,s): x,y=xy(s);return g['room_rows'][y][x]
def cells(g): return [c+str(r+1) for r in range(len(g['room_rows'])) for c in g['columns'] if c+str(r+1) not in g['blocked']]
def solve(g,mode,strict45=False):
 names=['Mavis','Cato','Jules','Bryn','Vega','Ren','Poppy','Wade','Seth'];allc=cells(g)
 def nw(a,b):
  x,y=xy(a);u,v=xy(b)
  return x<u and y<v and (not strict45 or u-x==v-y)
 def ne(a,b):x,y=xy(a);u,v=xy(b);return x>u and y<v and (not strict45 or x-u==v-y)
 def diag(a,b):x,y=xy(a);u,v=xy(b);return abs(x-u)==abs(y-v)==1
 def beside(a,b):x,y=xy(a);u,v=xy(b);return abs(x-u)+abs(y-v)==1 if mode=='edge' else max(abs(x-u),abs(y-v))==1
 pairs=[('Mavis','Vega',nw),('Cato','Ren',ne),('Vega','Cato',nw),('Jules','Wade',diag),('Bryn','Jules',lambda a,b:room(g,a)==room(g,b)),('Poppy','Mavis',lambda a,b:room(g,a)==room(g,b))]
 domains={n:list(allc) for n in names}
 domains['Ren']=[a for a in allc if room(g,a)=='C']
 domains['Wade']=[a for a in allc if room(g,a)=='O' and any(beside(a,b) for b in g['teacher_desks'])]
 # Source label ROOM/ZONE has no special exclusions here: all eight named areas count as spaces.
 links={n:[] for n in names}
 for a,b,f in pairs:
  rel={v:{w for w in domains[b] if f(v,w)} for v in domains[a]}
  rev={w:{v for v in domains[a] if f(v,w)} for w in domains[b]}
  links[a].append((b,rel));links[b].append((a,rev))
 count=0; assignments=[];answers=collections.Counter();nodes=0
 def rec(assign,dom):
  nonlocal count,nodes
  nodes+=1
  if len(assign)==len(names):
   rr=room(g,assign['Seth']); others=[(n,a) for n,a in assign.items() if n!='Seth' and room(g,a)==rr]
   if len(others)!=1:return
   count+=1;answers['%s at %s'%others[0]]+=1
   if len(assignments)<200:assignments.append(dict(assign))
   return
  n=min((n for n in names if n not in assign),key=lambda n:len(dom[n]))
  for v in dom[n]:
   x,y=xy(v);new={};valid=True
   for m in names:
    if m in assign or m==n:continue
    dd=[w for w in dom[m] if xy(w)[0]!=x and xy(w)[1]!=y]
    for other,rel in links[n]:
     if other==m:dd=[w for w in dd if w in rel.get(v,set())]
    if not dd:valid=False;break
    new[m]=dd
   if not valid:continue
   aa=dict(assign);aa[n]=v
   # Don't allow more than two people in Seth's area once known.
   if 'Seth' in aa and sum(room(g,w)==room(g,aa['Seth']) for w in aa.values())>2:continue
   rec(aa,new)
 rec({},domains)
 return {'mode':mode,'direction_45_degree_sensitivity':strict45,'full_assignment_count':count,'stored_assignments':assignments,'answers':dict(answers),'search_nodes':nodes,'matches_expected_post_enumeration':count==1 and assignments[0]==g['expected_comparison_only']}
def intro(g):
 out=[]
 for perm in itertools.permutations(cells(g),4):
  a=dict(zip(['Quill','Pip','Morse','Knox'],perm));q,p,m,k=map(xy,perm)
  if len({x for x,y in map(xy,perm)})!=4 or len({y for x,y in map(xy,perm)})!=4:continue
  if q[1]==0 and p[1]==2 and m[0]==2 and k[0]==3 and p[0]<q[0] and m[1]>k[1]:out.append(a)
 return {'full_assignment_count':len(out),'assignments':out,'answers':[{n:s for n,s in a.items() if room(g,s)=='D'} for a in out],'matches_expected_post_enumeration':len(out)==1 and out[0]==g['expected_comparison_only']}
if __name__=='__main__':
 result={'source_pdf_sha256':data['source_pdf_sha256'],'candidate_sha256':data['candidate_sha256'],'grid_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'intro_case01':intro(data['intro_case01']),'case29':[solve(data['case29'],mode,strict) for mode,strict in [('edge',False),('eight_neighbour',False),('edge',True),('eight_neighbour',True)]]}
 (BASE/'spatial-intro-29-results.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'intro':result['intro_case01'], 'case29':[{k:v for k,v in x.items() if k!='stored_assignments'} for x in result['case29']]},indent=2))

