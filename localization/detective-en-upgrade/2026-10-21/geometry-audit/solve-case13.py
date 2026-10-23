"""Enumerate all literal Case13 placements, independent of expected answer.

Uses visually transcribed unsolved map; expected roster is comparison only.
"""
import argparse,collections,hashlib,json
from pathlib import Path

def solve(grid,room_only=True,blocked_override=None):
 cols=grid['columns_west_to_east'];rooms={cols[c]+str(r):room for r,line in enumerate(grid['grid_rows_north_to_south'],1) for c,room in enumerate(line)}
 assert len(rooms)==49
 blocked=set(grid['blocked_squares'] if blocked_override is None else blocked_override);floor=[p for p in rooms if p not in blocked]
 xy=lambda p:(cols.index(p[0]),int(p[1:]))
 names=['Moxie','Skye','Juno','Eden','Bodhi','Willow','Remy'];domains={n:floor for n in names};domains['Moxie']=[p for p in floor if rooms[p]=='R' and p[1:]=='5'];domains['Skye']=[p for p in floor if rooms[p]=='R']
 if room_only:
  for n in ('Juno','Eden','Remy'):domains[n]=[p for p in domains[n] if rooms[p] not in grid['zone_codes']]
 solutions=[];visited=0
 def valid(a):
  if 'Juno' in a and 'Skye' in a:
   x,y=xy(a['Juno']);u,v=xy(a['Skye'])
   if abs(x-u)!=1 or abs(y-v)!=1:return False
  if 'Eden' in a and 'Juno' in a and rooms[a['Eden']]!=rooms[a['Juno']]:return False
  if 'Willow' in a and 'Bodhi' in a:
   x,y=xy(a['Willow']);u,v=xy(a['Bodhi'])
   if not(x<u and y<v):return False
  if 'Bodhi' in a and 'Moxie' in a:
   x,y=xy(a['Bodhi']);u,v=xy(a['Moxie'])
   if not(x<u and y>v):return False
  if 'Remy' in a and len(a)==7 and sum(rooms[p]==rooms[a['Remy']] for n,p in a.items() if n!='Remy')!=1:return False
  return True
 def search(a,columns,rows):
  nonlocal visited
  visited+=1
  if len(a)==7:solutions.append(a.copy());return
  name=names[len(a)]
  for p in domains[name]:
   if p[0] in columns or p[1:] in rows:continue
   a[name]=p
   if valid(a):search(a,columns|{p[0]},rows|{p[1:]})
   a.pop(name)
 search({},set(),set());answers=[]
 for a in solutions:
  companions=[(n,p) for n,p in a.items() if n!='Remy' and rooms[p]==rooms[a['Remy']]];assert len(companions)==1;answers.append(companions[0])
 return {'full_assignment_count':len(solutions),'assignments':solutions,'answer_counts':dict(collections.Counter(n+' at '+p for n,p in answers)),'search_nodes':visited,'expected_assignment_matches':len(solutions)==1 and solutions[0]==grid['expected_assignment_for_comparison_only']}

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--grid',type=Path,default=Path(__file__).with_name('case13-grid.json'));a.add_argument('--output',type=Path,default=Path(__file__).with_name('case13-solver-result.json'));v=a.parse_args();g=json.loads(v.grid.read_text());out={'source_pdf_sha256':g['source_pdf_sha256'],'candidate_sha256':g['candidate_sha256'],'grid_sha256':hashlib.sha256(v.grid.read_bytes()).hexdigest(),'method':'All row/column-distinct seven-witness placements checked against all seven literal clues on unsolved visually transcribed map. Expected roster used only after enumeration.','baseline_room_only':solve(g,True),'sensitivity_companion_means_any_named_area':solve(g,False),'limits':['Formal result depends on explicitly stored visual grid/object transcription.','Not a production render, physical print proof or all-case uniqueness approval.']};v.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
