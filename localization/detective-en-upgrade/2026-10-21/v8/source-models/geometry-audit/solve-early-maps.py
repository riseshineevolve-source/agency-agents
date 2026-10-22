"""Enumerate original Case02/04 clues; expected rosters are postchecks only."""
import argparse,json,hashlib,collections
from pathlib import Path

def adjacent(a,b,diagonal=False):
 dx=abs(ord(a[0])-ord(b[0]));dy=abs(int(a[1:])-int(b[1:]))
 return max(dx,dy)==1 if diagonal else dx+dy==1

def solve(g,diagonal=False,beside_same_room=False,objective_fact=True,room_corner=False):
 room={g['columns'][c]+str(r):code for r,row in enumerate(g['room_grid'],1) for c,code in enumerate(row)}
 floor=[p for p in room if p not in g['blocked']];objects=g['objects'];case=g['case'];names=['Nova','Dax','Rook','Atlas','Ivy','Max'] if case==2 else ['Echo','Kai','Zuri','Briar','Clover','Pixel']
 def beside(p,object_key):
  return any(adjacent(p,q,diagonal) and (not beside_same_room or room[p]==room[q]) for q in objects[object_key])
 if case==2:
  def corner(p):
   if not room_corner:return p[0] in 'AF' and p[1] in '16'
   c,r=ord(p[0]),int(p[1:]);code=room[p]
   return (room.get(chr(c-1)+str(r))!=code or room.get(chr(c+1)+str(r))!=code) and (room.get(chr(c)+str(r-1))!=code or room.get(chr(c)+str(r+1))!=code)
  domains={'Nova':['B3'],'Dax':[p for p in floor if room[p]=='D' and p[0]=='D'],'Rook':[p for p in floor if corner(p)],
           'Atlas':[p for p in floor if room[p]=='E' and p[0]=='F'],'Ivy':[p for p in floor if p in objects['desk_chair']],'Max':floor}
  domains['Rook']=[p for p in domains['Rook'] if p in floor and beside(p,'teacher_desk')]
 else:
  domains={'Echo':['A2'],'Kai':[p for p in floor if room[p]=='K'],'Zuri':[p for p in floor if room[p]=='T' and p[1]=='4'],
           'Briar':[p for p in floor if beside(p,'ring_toss_stand')],'Clover':[p for p in floor if room[p]=='P' and p[1]=='5'],
           'Pixel':[p for p in floor if room[p]=='T'] if objective_fact else floor}
 order=sorted(names,key=lambda n:len(domains[n]));assignments=[];visited=0
 def rec(placed,rows,cols):
  nonlocal visited
  visited+=1
  if len(placed)==len(names):
   principal='Max' if case==2 else 'Pixel'
   if sum(room[p]==room[placed[principal]] for n,p in placed.items() if n!=principal)!=1:return
   if case==4 and any(room[p]=='K' for n,p in placed.items() if n!='Kai'):return
   assignments.append(dict(placed));return
  name=order[len(placed)]
  for p in domains[name]:
   if p[0] in cols or p[1:] in rows:continue
   if case==4 and name!='Kai' and room[p]=='K':continue
   placed[name]=p;rec(placed,rows|{p[1:]},cols|{p[0]});placed.pop(name)
 rec({},set(),set())
 answers=[]
 principal='Max' if case==2 else 'Pixel'
 for a in assignments:
  companions=[(n,p) for n,p in a.items() if n!=principal and room[p]==room[a[principal]]]
  assert len(companions)==1;answers.append(companions[0][0]+' at '+companions[0][1])
 return {'full_assignment_count':len(assignments),'assignments':assignments,'answers':dict(collections.Counter(answers)),
         'search_nodes':visited,'domain_sizes':{n:len(v) for n,v in domains.items()},
         'matches_expected_post_enumeration':len(assignments)==1 and assignments[0]==g['expected_for_comparison_only']}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--grid',type=Path,default=Path(__file__).with_name('early-map-grids.json'));p.add_argument('--output',type=Path,default=Path(__file__).with_name('early-map-solver-results.json'));a=p.parse_args();data=json.loads(a.grid.read_text());out=[]
 for g in data['cases']:
  variants={}
  for name,diag,same,obj in [('edge_beside',False,False,True),('edge_beside_same_room',False,True,True),('eight_neighbour_beside',True,False,True),('eight_neighbour_same_room',True,True,True),('edge_witness_clues_only',False,False,False),('eight_neighbour_witness_clues_only',True,False,False)]:variants[name]=solve(g,diag,same,obj)
  if g['case']==2:
   for name,diag,same in [('room_corner_edge_beside',False,False),('room_corner_eight_neighbour_beside',True,False),('room_corner_eight_neighbour_same_room',True,True)]:variants[name]=solve(g,diag,same,True,True)
  out.append({'case':g['case'],'variants':variants})
 result={'source_pdf_sha256':data['source_pdf_sha256'],'candidate_sha256':data['candidate_sha256'],'grid_sha256':hashlib.sha256(a.grid.read_bytes()).hexdigest(),'cases':out,'scope':'Literal unsolvedmap/clue enumeration; expected solutions comparison only. Beside interpretation sensitivities explicit; no physical print or fullbook approval.'};a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({str(c['case']):{n:v['full_assignment_count'] for n,v in c['variants'].items()} for c in out},indent=2))

