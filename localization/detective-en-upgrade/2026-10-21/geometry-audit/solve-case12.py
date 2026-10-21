"""Independent finite enumeration of the visually transcribed Case12 grid.

Expected source assignment is comparison-only, not a solver constraint.
"""
import argparse, collections, hashlib, itertools, json
from pathlib import Path

def solve(grid,blocked):
 rooms={grid['columns_west_to_east'][col]+str(row):code
        for row,codes in enumerate(grid['grid_rows_north_to_south'],1)
        for col,code in enumerate(codes)}
 assert len(rooms)==49
 floor=[p for p in rooms if p not in blocked]
 # Domain restrictions follow clues1,2,3,4,5. Clue6 checked literally below.
 domains={
  'Kira':[p for p in floor if rooms[p]=='B'],
  'Nell':[p for p in floor if rooms[p]=='S' and p[1]=='2'],
  'Iris':[p for p in floor if p[1]=='5'],
  'Eli':[p for p in floor if rooms[p] in ('G','B')],
  'Cove':[p for p in floor if p[0]=='B' and p[1] in ('1','7')],
  'Sage':floor,
  'Winter':floor}
 names=sorted(domains,key=lambda n:len(domains[n]));results=[];visited=0
 def search(placed,columns,rows):
  nonlocal visited
  visited+=1
  if len(placed)==7:
   if any(rooms[p]=='B' for n,p in placed.items() if n!='Kira'):return
   if sum(rooms[placed[n]]=='R' for n in ('Sage','Kira'))!=1:return
   if sum(rooms[p]==rooms[placed['Winter']] for n,p in placed.items() if n!='Winter')!=1:return
   results.append(placed.copy());return
  name=names[len(placed)]
  for p in domains[name]:
   if p[0] in columns or p[1] in rows:continue
   # Safe closure from clue1: no other witness may be in Bird Room.
   if name!='Kira' and rooms[p]=='B':continue
   # Safe closure from clue6 and already explicit clue1.
   if name=='Sage' and rooms[p]!='R':continue
   placed[name]=p;search(placed,columns|{p[0]},rows|{p[1]});placed.pop(name)
 search({},set(),set())
 answers=[]
 for result in results:
  companions=[(n,p) for n,p in result.items() if n!='Winter' and rooms[p]==rooms[result['Winter']]]
  assert len(companions)==1;answers.append(companions[0])
 return {'full_assignment_count':len(results),'assignments':results,
         'answer_counts':dict(collections.Counter(n+' at '+p for n,p in answers)),
         'search_nodes':visited,'expected_assignment_matches':len(results)==1 and results[0]==grid['expected_assignment_for_comparison_only']}

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--grid',type=Path,default=Path(__file__).with_name('case12-grid.json'));a.add_argument('--output',type=Path,default=Path(__file__).with_name('case12-solver-result.json'));v=a.parse_args();g=json.loads(v.grid.read_text());blocked=set(g['blocked_squares']);result=solve(g,blocked);variants={}
 for count in (1,2):
  for cells in itertools.combinations(g['figure_shape_sensitivity_cells'],count):variants['treat_as_usable:'+','.join(cells)]=solve(g,blocked-set(cells))
 out={'source_pdf_sha256':g['source_pdf_sha256'],'grid_sha256':hashlib.sha256(v.grid.read_bytes()).hexdigest(),
      'method':'Enumerate every row/column-distinct placement satisfying all seven literal clues on the human-transcribed map. Expected roster comparison is post-enumeration only.',
      'baseline':result,'silhouette_sensitivity_variants':variants,
      'scope':'Current Case12 source logical geometry; not production render or print approval.'}
 v.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
