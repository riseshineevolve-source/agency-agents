"""Audit literal6x6clues; expected answer never restricts search.
Case07 anchor simulations are explicitly conditional, not source validation.
"""
from pathlib import Path
import json,hashlib,collections
ROOT=Path(__file__).resolve().parent

def adjacent(a,b,kind):
 dx=abs(ord(a[0])-ord(b[0]));dy=abs(int(a[1])-int(b[1]));return dx+dy==1 if kind=='orthogonal' else max(dx,dy)==1

def search(domains,final):
 names=sorted(domains,key=lambda n:len(domains[n]));out=[]
 def step(p,cols,rows):
  if len(p)==len(names):
   if final(p):out.append(dict(p))
   return
  n=names[len(p)]
  for x in domains[n]:
   if x[0] in cols or x[1] in rows:continue
   p[n]=x;step(p,cols|{x[0]},rows|{x[1]});del p[n]
 step({},set(),set());return out

def evaluate(grid,case,kind='orthogonal',anchor=None):
 areas={c+str(r):line[i] for r,line in enumerate(grid['room_rows'],1) for i,c in enumerate(grid['columns'])};floor=[p for p in areas if p not in grid['blocked']]
 close=lambda p,objects:any(adjacent(p,x,kind) for x in objects)
 if case==6:
  domains={'Scout':['E3'],'Hugo':[p for p in floor if areas[p]=='D' and close(p,grid['display_cases'])],
   'Arlo':[p for p in floor if areas[p]=='F' and p[1]=='2'],
   'Vale':[p for p in floor if areas[p]=='G' and close(p,grid['statues'])],
   'Wren':[p for p in floor if p in grid['benches'] and close(p,grid['skeletons'])],'Uma':floor}
  check=lambda p:sum(areas[x]==areas[p['Uma']] for n,x in p.items() if n!='Uma')==1
  target='Uma'
 else:
  domains={'Blaze':[p for p in floor if areas[p]=='R'],'Indigo':[p for p in floor if areas[p] in ('D','R')],
   'Willa':floor if anchor is None else [p for p in floor if abs(ord(p[0])-ord(anchor[0]))+abs(int(p[1])-int(anchor[1]))==2],
   'Zoe':[p for p in floor if (p[0] in ('A','F') or p[1] in ('1','6')) and close(p,grid['visible_roadcases_or_carts'])],
   'Rocket':['E5'],'Gray':floor}
  def check(p):
   return all(areas[x]!='R' for n,x in p.items() if n!='Blaze') and sum(areas[x]==areas[p['Gray']] for n,x in p.items() if n!='Gray')==1
  target='Gray'
 out=search(domains,check);answers=[]
 for p in out:answers.append(next(n+' at '+x for n,x in p.items() if n!=target and areas[x]==areas[p[target]]))
 return {'full_assignment_count':len(out),'answer_counts':dict(collections.Counter(answers)),
  'assignments':out[:30],'assignments_truncated':len(out)>30,'expected_is_among_results':grid['expected'] in out,
  'unique_full_expected':len(out)==1 and out[0]==grid['expected']}

if __name__=='__main__':
 path=ROOT/'root-map-grids-06-07.json';g=json.loads(path.read_text());result={
  'source_pdf_sha256':g['source_pdf_sha256'],'candidate_sha256':g['candidate_sha256'],'grid_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
  'case06':{k:evaluate(g['case06'],6,k) for k in ('orthogonal','eight_neighbor')},
  'case07':{'unidentified_anchor_omitted_not_a_full_puzzle_check':evaluate(g['case07'],7),
    'conditional_anchors_not_source_validation':{a:evaluate(g['case07'],7,anchor=a) for a in ['D1','C2','C1','C4']}}
 }
 (ROOT/'root-map-results-06-07.json').write_text(json.dumps(result,indent=2)+'\n')
 print('Case06',[(k,v['full_assignment_count'],v['answer_counts']) for k,v in result['case06'].items()])
 print('Case07 conditional',[(k,v['full_assignment_count'],v['answer_counts']) for k,v in result['case07']['conditional_anchors_not_source_validation'].items()])
