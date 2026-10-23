"""Exhaustive source Case10/15 enumeration; expected rosters used only as postchecks."""
import json,hashlib,collections
from pathlib import Path
ROOT=Path(__file__).parent

def solve(g,diag=False,same_room=False,equal_ne=False,charging_tall=False):
 room={g['columns'][c]+str(r):code for r,row in enumerate(g['room_grid'],1) for c,code in enumerate(row)}
 floor=[p for p in room if p not in g['blocked']];obj=g['objects'];case=g['case']
 def dist(p,q):return abs(ord(p[0])-ord(q[0]))+abs(int(p[1:])-int(q[1:]))
 def adj(p,q):
  dx=abs(ord(p[0])-ord(q[0]));dy=abs(int(p[1:])-int(q[1:]))
  return (max(dx,dy)==1 if diag else dx+dy==1) and (not same_room or room[p]==room[q])
 def beside(p,key):return any(adj(p,q) for q in obj[key])
 def ne(p,q):
  dx=ord(p[0])-ord(q[0]);dy=int(q[1:])-int(p[1:])
  return dx>0 and dy>0 and (not equal_ne or dx==dy)
 if case==10:
  names=['Ember','Nico','Wyatt','Finn','Beck','Vera','Dash'];principal='Dash'
  charging='bunk' if charging_tall else 'charging_pod'
  console_rooms={room[q] for q in obj['control_console']}
  domains={'Ember':[p for p in floor if p in obj['demo_seat'] and beside(p,'demo_seat')],
   'Nico':[p for p in floor if p[0]=='F' and p in obj['demo_seat']],
   'Wyatt':[p for p in floor if p[0]=='B' and beside(p,charging)],
   'Finn':[p for p in floor if dist(p,obj['coolant_tank'][0])==7],
   'Beck':[p for p in floor if (p[0] in 'AG' or p[1:] in ['1','7']) and beside(p,'parts_crate')],
   'Vera':[p for p in floor if room[p] in console_rooms and not any(adj(p,q) for q in obj['control_console'] if room[p]==room[q])],
   'Dash':floor}
 else:
  names=['Harper','Piper','Duke','Cruz','Jett','Inez','Milo'];principal='Milo'
  cot_rooms={room[q] for q in obj['cot']}
  domains={'Harper':floor,'Piper':floor,'Duke':[p for p in floor if room[p]=='F' and p[1:]=='5'],
   'Cruz':[p for p in floor if beside(p,'cot')],
   'Jett':[p for p in floor if room[p]=='W'],
   'Inez':[p for p in floor if room[p] in cot_rooms and not any(adj(p,q) for q in obj['cot'] if room[p]==room[q])],
   'Milo':floor}
 order=sorted(names,key=lambda n:len(domains[n]));solutions=[];nodes=0
 def rec(a,rows,cols):
  nonlocal nodes
  nodes+=1
  if case==15:
   if 'Harper' in a and 'Cruz' in a and not ne(a['Harper'],a['Cruz']):return
   if 'Piper' in a and 'Duke' in a and not ne(a['Piper'],a['Duke']):return
  if len(a)==len(names):
   if sum(room[p]==room[a[principal]] for n,p in a.items() if n!=principal)!=1:return
   solutions.append(dict(a));return
  n=order[len(a)]
  for p in domains[n]:
   if p[0] in cols or p[1:] in rows:continue
   if case==15 and n!='Jett' and room[p]=='W':continue
   a[n]=p;rec(a,rows|{p[1:]},cols|{p[0]});a.pop(n)
 rec({},set(),set())
 answers=collections.Counter()
 for a in solutions:
  companion=[(n,p) for n,p in a.items() if n!=principal and room[p]==room[a[principal]]];assert len(companion)==1
  answers[companion[0][0]+' at '+companion[0][1]]+=1
 return {'full_assignment_count':len(solutions),'assignments':solutions,'answers':dict(answers),'search_nodes':nodes,'domain_sizes':{n:len(p) for n,p in domains.items()},'matches_expected_post_enumeration':len(solutions)==1 and solutions[0]==g['expected_for_comparison_only']}

if __name__=='__main__':
 grid=ROOT/'mid-map-grids.json';data=json.loads(grid.read_text());cases=[]
 for g in data['cases']:
  variants={}
  for name,diag,same in [('edge_beside',False,False),('edge_same_room',False,True),('eight_neighbour_beside',True,False),('eight_neighbour_same_room',True,True)]:variants[name]=solve(g,diag,same)
  if g['case']==10:
   variants['charging_pod_as_circle_marked_tall_box_edge']=solve(g,charging_tall=True)
   variants['charging_pod_as_circle_marked_tall_box_diagonal']=solve(g,diag=True,charging_tall=True)
  else:
   variants['equal_diagonal_NE_edge_beside']=solve(g,equal_ne=True)
   variants['equal_diagonal_NE_eight_neighbour_beside']=solve(g,diag=True,equal_ne=True)
  cases.append({'case':g['case'],'variants':variants})
 out={'source_pdf_sha256':data['source_pdf_sha256'],'candidate_sha256':data['candidate_sha256'],'grids_sha256':hashlib.sha256(grid.read_bytes()).hexdigest(),'cases':cases,'scope':'Literal clues and original figure only; no source solution coordinates enter domains or constraints; no print/layout approval.'}
 (ROOT/'mid-map-solver-results.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({str(c['case']):{n:[v['full_assignment_count'],v['answers']] for n,v in c['variants'].items()} for c in cases},indent=2))
