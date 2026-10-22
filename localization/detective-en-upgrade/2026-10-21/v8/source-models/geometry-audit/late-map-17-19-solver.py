"""Independent finite enumeration: expected rosters are checked only afterward."""
import json,hashlib,collections
from pathlib import Path
B=Path(__file__).parent

def solve(g,case,distance='manhattan',sw='strict_quadrant',row_north='row_difference'):
 c=g[case];cols=g['columns'];rooms={cols[x]+str(y):r for y,line in enumerate(c['room_rows'],1) for x,r in enumerate(line)}
 floor=[p for p in rooms if p not in c['blocked']];xy=lambda p:(cols.index(p[0]),int(p[1:]))
 if case=='case17':
  order=['Mika','Koa','Luna','Sunny','Axel','Otis','Reed'];domains={n:floor for n in order}
  domains.update(Mika=[p for p in floor if rooms[p]=='T' and p[0]=='B'],Koa=[p for p in floor if rooms[p]=='W' and p[1:]=='6'],Luna=[p for p in floor if rooms[p]=='W' and p[0]=='G'],Sunny=c['benches'],Otis=[p for p in floor if rooms[p] in ['T','B']])
 else:
  order=['Kian','Theo','Dex','Avery','Mack','Ollie','Sasha'];domains={n:floor for n in order}
  domains['Kian']=[p for p in floor if rooms[p]=='S' and p[0]=='F']
  def dist(p):
   x,y=xy(p);u,v=xy(c['piano']);dx,dy=abs(x-u),abs(y-v)
   return dx+dy if distance=='manhattan' else max(dx,dy)
  domains['Theo']=[p for p in floor if dist(p)==7]
 solutions=[];visited=0
 def valid(a):
  if case=='case17':
   if 'Axel' in a and 'Koa' in a:
    x,y=xy(a['Axel']);u,v=xy(a['Koa'])
    if y!=v-3 or (row_north=='same_column' and x!=u):return False
   final='Reed'
  else:
   if 'Avery' in a and 'Mack' in a:
    x,y=xy(a['Avery']);u,v=xy(a['Mack'])
    if y!=v-2 or (row_north=='same_column' and x!=u):return False
   if 'Dex' in a and 'Theo' in a and rooms[a['Dex']]!=rooms[a['Theo']]:return False
   if 'Ollie' in a and 'Avery' in a and sum(rooms[a[n]]=='A' for n in ['Ollie','Avery'])!=1:return False
   if 'Mack' in a and 'Ollie' in a:
    x,y=xy(a['Mack']);u,v=xy(a['Ollie'])
    if not(x<u and y>v):return False
    if sw=='exact_diagonal' and u-x!=y-v:return False
    if sw=='touching_diagonal' and (u-x!=1 or y-v!=1):return False
   final='Sasha'
  if len(a)==7 and sum(rooms[p]==rooms[a[final]] for n,p in a.items() if n!=final)!=1:return False
  return True
 def search(a,usedcols,usedrows):
  nonlocal visited
  visited+=1
  if len(a)==7:solutions.append(a.copy());return
  name=order[len(a)]
  for p in domains[name]:
   if p[0] in usedcols or p[1:] in usedrows:continue
   a[name]=p
   if valid(a):search(a,usedcols|{p[0]},usedrows|{p[1:]})
   a.pop(name)
 search({},set(),set())
 final='Reed' if case=='case17' else 'Sasha';answers=collections.Counter()
 for a in solutions:
  companions=[(n,p) for n,p in a.items() if n!=final and rooms[p]==rooms[a[final]]];assert len(companions)==1;answers[f'{companions[0][0]} at {companions[0][1]}']+=1
 return {'full_assignment_count':len(solutions),'assignments':solutions,'answer_counts':dict(answers),'search_nodes':visited,'expected_roster_present':c['expected_comparison_only'] in solutions,'sole_roster_matches_expected':len(solutions)==1 and solutions[0]==c['expected_comparison_only']}

if __name__=='__main__':
 p=B/'late-map-17-19-grid.json';g=json.loads(p.read_text())
 r={'source_pdf_sha256':g['source_pdf_sha256'],'candidate_sha256':g['candidate_sha256'],'grid_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'baseline_semantics':{'grid_steps':'Manhattan row difference plus column difference; no routefinding or diagonal steps.','south_west':'Strictly west and strictly south, any positive row/column distance.','rows_north':'Exact specified row difference, without same-column requirement; distinct-column rule still applies.'},'case17':{'baseline':solve(g,'case17'),'sensitivity_north_means_same_column':solve(g,'case17',row_north='same_column')},'case19':{'baseline':solve(g,'case19'),'sensitivity_sw_means_exact_diagonal':solve(g,'case19',sw='exact_diagonal'),'sensitivity_sw_means_touching_diagonal':solve(g,'case19',sw='touching_diagonal'),'sensitivity_grid_steps_include_diagonal':solve(g,'case19',distance='chebyshev'),'sensitivity_north_means_same_column':solve(g,'case19',row_north='same_column')}}
 (B/'late-map-17-19-results.json').write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({k:{s:{t:v for t,v in a.items() if t!='assignments'} for s,a in r[k].items()} for k in ['case17','case19']},indent=2))

