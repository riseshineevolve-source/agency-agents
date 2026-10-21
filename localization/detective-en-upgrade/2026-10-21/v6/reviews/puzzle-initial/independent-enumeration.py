"""Independent owner-authorized V6 repair enumeration.
Uses source-transcribed rooms/objects; printed expected positions are ONLY postchecks.
No production files or historical audit output is modified.
"""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'detective-upgrade/geometry-audit'
OUT=Path(__file__).parent

def xy(v):return ord(v[0])-65,int(v[1:])-1

def roomgrid(cols,rows):return {c+str(y):row[x] for y,row in enumerate(rows,1) for x,c in enumerate(cols)}

def near(a,b,rooms,same=True):
 ax,ay=xy(a);bx,by=xy(b)
 return abs(ax-bx)+abs(ay-by)==1 and (not same or rooms[a]==rooms[b])

def run(names,cells,domains,constraints,principal,rooms):
 order=sorted(names,key=lambda n:len(domains[n]));found=[]
 def recurse(placed,rows,cols):
  for need,pred in constraints:
   if all(n in placed for n in need) and not pred(placed):return
  if len(placed)==len(order):
   companions=[n for n,v in placed.items() if n!=principal and rooms[v]==rooms[placed[principal]]]
   if len(companions)==1:found.append(dict(placed))
   return
  n=order[len(placed)]
  for v in domains[n]:
   if v[0] in cols or v[1:] in rows:continue
   placed[n]=v;recurse(placed,rows|{v[1:]},cols|{v[0]});del placed[n]
 recurse({},set(),set())
 return found

def result(case,variant,solutions,expected,principal,rooms):
 assert len(solutions)==1,(case,variant,len(solutions))
 a=solutions[0]
 contact=next((n,v) for n,v in a.items() if n!=principal and rooms[v]==rooms[a[principal]])
 return {'case':case,'variant':variant,'complete_assignment_count':len(solutions),'assignment':a,'contact':list(contact),'matches_intended_roster_postcheck_only':a==expected}

rs=[]
# Case02: explicit OUTER GRID corner, beside = shared edge; same room toggled.
g=json.loads((D/'early-map-grids.json').read_text())['cases'][0]
assert g['case']==2
rooms=roomgrid(g['columns'],g['room_grid']);cells=[v for v in rooms if v not in g['blocked']];ob=g['objects']
for same in [False,True]:
 ns=['Nova','Dax','Rook','Atlas','Ivy','Max']
 dom={n:cells[:] for n in ns}
 dom.update(Nova=['B3'],Dax=[v for v in cells if rooms[v]=='D' and v[0]=='D'],Rook=[v for v in cells if v[0] in 'AF' and v[1:] in ['1','6'] and any(near(v,q,rooms,same) for q in ob['teacher_desk'])],Atlas=[v for v in cells if rooms[v]=='E' and v[0]=='F'],Ivy=[v for v in cells if v in ob['desk_chair']])
 sol=run(ns,cells,dom,[],'Max',rooms)
 rs.append(result(2,'outer_grid_corner_edge_beside_same_room_'+str(same),sol,g['expected_for_comparison_only'],'Max',rooms))
# Case07: owner-authorized explicit metal-frame anchor C2. Every visible wheeled case considered.
g=json.loads((D/'root-map-grids-06-07.json').read_text())['case07'];rooms=roomgrid(g['columns'],g['room_rows']);cells=[v for v in rooms if v not in g['blocked']]
for same in [False,True]:
 ns=['Blaze','Indigo','Willa','Zoe','Rocket','Gray'];dom={n:cells[:] for n in ns}
 dom.update(Blaze=[v for v in cells if rooms[v]=='R'],Indigo=[v for v in cells if rooms[v] in ['D','R']],Willa=[v for v in cells if sum(abs(x-y) for x,y in zip(xy(v),xy('C2')))==2],Zoe=[v for v in cells if (v[0] in 'AF' or v[1:] in ['1','6']) and any(near(v,q,rooms,same) for q in ['A1','D1','D6'])],Rocket=['E5'])
 cons=[([n],lambda a,n=n:rooms[a[n]]!='R') for n in ns if n!='Blaze']
 sol=run(ns,cells,dom,cons,'Gray',rooms)
 rs.append(result(7,'frame_C2_all_visible_carts_edge_same_room_'+str(same),sol,g['expected'],'Gray',rooms))
# Case10: Wyatt beside visible robot arm at B6. Other beside relationships use shared edge in same room.
g=json.loads((D/'mid-map-grids.json').read_text())['cases'][0];assert g['case']==10
rooms=roomgrid(g['columns'],g['room_grid']);cells=[v for v in rooms if v not in g['blocked']];ob=g['objects']
for same in [False,True]:
 ns=['Ember','Nico','Wyatt','Finn','Beck','Vera','Dash'];dom={n:cells[:] for n in ns};beside=lambda v,k:any(near(v,q,rooms,same) for q in ob[k])
 dom.update(Ember=[v for v in cells if v in ob['demo_seat'] and beside(v,'demo_seat')],Nico=[v for v in cells if v[0]=='F' and v in ob['demo_seat']],Wyatt=[v for v in cells if v[0]=='B' and near(v,'B6',rooms,same)],Finn=[v for v in cells if sum(abs(x-y) for x,y in zip(xy(v),xy('C7')))==7],Beck=[v for v in cells if (v[0] in 'AG' or v[1:] in ['1','7']) and beside(v,'parts_crate')],Vera=[v for v in cells if any(rooms[v]==rooms[q] for q in ob['control_console']) and not any(rooms[v]==rooms[q] and near(v,q,rooms,same) for q in ob['control_console'])])
 sol=run(ns,cells,dom,[],'Dash',rooms)
 rs.append(result(10,'robot_arm_B6_edge_beside_same_room_'+str(same),sol,g['expected_for_comparison_only'],'Dash',rooms))
# Case15: shared-edge beside in SAME ROOM; NE has independent positive offsets.
g=json.loads((D/'mid-map-grids.json').read_text())['cases'][1];assert g['case']==15
rooms=roomgrid(g['columns'],g['room_grid']);cells=[v for v in rooms if v not in g['blocked']];ob=g['objects']
ns=['Harper','Piper','Duke','Cruz','Jett','Inez','Milo'];dom={n:cells[:] for n in ns}
dom.update(Duke=[v for v in cells if rooms[v]=='F' and v[1:]=='5'],Cruz=[v for v in cells if any(near(v,q,rooms,True) for q in ob['cot'])],Jett=[v for v in cells if rooms[v]=='W'],Inez=[v for v in cells if any(rooms[v]==rooms[q] for q in ob['cot']) and not any(near(v,q,rooms,True) for q in ob['cot'])])
def northeast(a,b):ax,ay=xy(a);bx,by=xy(b);return ax>bx and ay<by
cons=[(['Harper','Cruz'],lambda a:northeast(a['Harper'],a['Cruz'])),(['Piper','Duke'],lambda a:northeast(a['Piper'],a['Duke']))]+[([n],lambda a,n=n:rooms[a[n]]!='W') for n in ns if n!='Jett']
sol=run(ns,cells,dom,cons,'Milo',rooms)
rs.append(result(15,'edge_beside_same_room_and_any_positive_NE_offsets',sol,g['expected_for_comparison_only'],'Milo',rooms))
# Case20: owner-authorized E7/F7 usable cadet bunks; both and E7-only tested. Sid lower row, Pax lower+right.
g=json.loads((D/'spatial-20-22-grid.json').read_text())['case20'];rooms=roomgrid(g['columns'],g['room_rows'])
expected={'Mara':'D4','Asa':'B2','Luca':'A1','Toby':'C6','Pax':'F5','Sid':'E7','Demi':'G3'}
for unblocked in [['E7'],['E7','F7']]:
 cells=[v for v in rooms if v not in (set(g['blocked'])-set(unblocked))]
 ns=['Mara','Asa','Luca','Pax','Sid','Toby','Demi'];dom={n:cells[:] for n in ns}
 dom.update(Mara=[v for v in cells if rooms[v]=='M' and v[1:]=='4'],Asa=[v for v in cells if rooms[v]=='M'],Toby=[v for v in cells if rooms[v]=='W'])
 def dia(a,b):ax,ay=xy(a);bx,by=xy(b);return abs(ax-bx)==1 and abs(ay-by)==1
 def southeast(a,b):ax,ay=xy(a);bx,by=xy(b);return ax>bx and ay>by
 cons=[(['Luca','Asa'],lambda a:dia(a['Luca'],a['Asa'])),(['Sid','Pax'],lambda a:xy(a['Sid'])[1]>xy(a['Pax'])[1]),(['Pax','Mara'],lambda a:southeast(a['Pax'],a['Mara']))]+[([n],lambda a,n=n:rooms[a[n]]!='W') for n in ns if n!='Toby']
 sol=run(ns,cells,dom,cons,'Demi',rooms)
 rs.append(result(20,'usable_bunks_'+','.join(unblocked),sol,expected,'Demi',rooms))
res={'status':'PASS_INDEPENDENT_OWNER_AUTHORIZED_REPAIR_MODELS','method':'Independent new backtracking implementation from transcribed source grids. One witness per distinct row/column; all witness clues and exactly-one same-room objective. Expected rosters comparison only. No original report/production/candidate mutation.','cases':rs}
(OUT/'independent-results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
