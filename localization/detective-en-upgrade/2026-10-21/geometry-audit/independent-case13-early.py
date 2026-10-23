"""Independent complete row/column-permutation check of Cases02/04/13.
Never reads expected assignments; checks original-grid literal constraints.
"""
from pathlib import Path
import itertools,json,collections
ROOT=Path(__file__).resolve().parent

def summarize(answers,target,rooms):
 return {'full_assignment_count':len(answers),'assignments':answers,'answers':dict(collections.Counter(next(n+' at '+p for n,p in a.items() if n!=target and rooms[p]==rooms[a[target]]) for a in answers))}

def case13(room_only):
 g=json.loads((ROOT/'case13-grid.json').read_text());names=['Juno','Skye','Eden','Willow','Bodhi','Moxie','Remy'];out=[]
 rooms={c+str(y):r[x] for y,r in enumerate(g['grid_rows_north_to_south'],1) for x,c in enumerate('ABCDEFG')}
 for cols in itertools.permutations('ABCDEFG'):
  if not cols[3]<cols[4]<cols[5]:continue
  if abs(ord(cols[0])-ord(cols[1]))!=1:continue
  for rows in itertools.permutations('1234567'):
   if rows[5]!='5' or not(rows[3]<rows[4] and rows[4]>rows[5]):continue
   if abs(int(rows[0])-int(rows[1]))!=1:continue
   positions=[c+r for c,r in zip(cols,rows)]
   if any(p in g['blocked_squares'] for p in positions):continue
   J,S,E,W,B,M,R=positions
   if rooms[M]!='R' or rooms[S]!='R' or rooms[E]!=rooms[J]:continue
   if room_only and any(rooms[p] in g['zone_codes'] for p in [J,E,R]):continue
   if sum(rooms[p]==rooms[R] for p in positions[:-1])!=1:continue
   out.append(dict(zip(names,positions)))
 return summarize(out,'Remy',rooms)

def early(g,diag=False,same=False,obj=True,roomcorner=False):
 n=g['case'];names=['Nova','Dax','Rook','Atlas','Ivy','Max'] if n==2 else ['Echo','Kai','Zuri','Briar','Clover','Pixel'];out=[]
 rooms={c+str(y):r[x] for y,r in enumerate(g['room_grid'],1) for x,c in enumerate('ABCDEF')}
 def near(p,key):
  for q in g['objects'][key]:
   dx=abs(ord(p[0])-ord(q[0]));dy=abs(int(p[1])-int(q[1]))
   if (max(dx,dy)==1 if diag else dx+dy==1) and (not same or rooms[p]==rooms[q]):return True
  return False
 def corner(p):
  if not roomcorner:return p[0] in 'AF' and p[1] in '16'
  x=ord(p[0]);y=int(p[1]);r=rooms[p]
  horizontal=any(rooms.get(chr(x+d)+str(y))!=r for d in [-1,1])
  vertical=any(rooms.get(chr(x)+str(y+d))!=r for d in [-1,1])
  return horizontal and vertical
 for cols in itertools.permutations('ABCDEF'):
  if cols[0]!=('B' if n==2 else 'A'):continue
  if n==2 and (cols[1]!='D' or cols[3]!='F'):continue
  for rows in itertools.permutations('123456'):
   if rows[0]!=('3' if n==2 else '2'):continue
   if n==4 and (rows[2]!='4' or rows[4]!='5'):continue
   ps=[c+r for c,r in zip(cols,rows)]
   if any(p in g['blocked'] for p in ps):continue
   a,b,c,d,e,f=ps
   if n==2:
    if rooms[b]!='D' or rooms[d]!='E' or not corner(c) or not near(c,'teacher_desk') or e not in g['objects']['desk_chair']:continue
   else:
    if rooms[b]!='K' or any(rooms[p]=='K' for p in [a,c,d,e,f]):continue
    if rooms[c]!='T' or rooms[e]!='P' or not near(d,'ring_toss_stand'):continue
    if obj and rooms[f]!='T':continue
   if sum(rooms[p]==rooms[f] for p in ps[:-1])!=1:continue
   out.append(dict(zip(names,ps)))
 return summarize(out,'Max' if n==2 else 'Pixel',rooms)

def sig(v):return sorted(tuple(sorted(a.items())) for a in v['assignments'])
if __name__=='__main__':
 r={'case13':{'room_only':case13(True),'any_named_area':case13(False)},'early':{}}
 source13=json.loads((ROOT/'case13-solver-result.json').read_text())
 assert sig(r['case13']['room_only'])==sig(source13['baseline_room_only'])
 assert sig(r['case13']['any_named_area'])==sig(source13['sensitivity_companion_means_any_named_area'])
 data=json.loads((ROOT/'early-map-grids.json').read_text());root=json.loads((ROOT/'early-map-solver-results.json').read_text())
 for g,rootcase in zip(data['cases'],root['cases']):
  variants={}
  for name,diag,same,obj in [('edge_beside',False,False,True),('edge_beside_same_room',False,True,True),('eight_neighbour_beside',True,False,True),('eight_neighbour_same_room',True,True,True),('edge_witness_clues_only',False,False,False),('eight_neighbour_witness_clues_only',True,False,False)]:variants[name]=early(g,diag,same,obj)
  if g['case']==2:
   for name,diag,same in [('room_corner_edge_beside',False,False),('room_corner_eight_neighbour_beside',True,False),('room_corner_eight_neighbour_same_room',True,True)]:variants[name]=early(g,diag,same,True,True)
  for name,v in variants.items():assert sig(v)==sig(rootcase['variants'][name]),(g['case'],name)
  r['early'][str(g['case'])]=variants
 r['all_assignment_sets_equal_original_solvers']=True
 (ROOT/'independent-case13-early-results.json').write_text(json.dumps(r,indent=2)+'\n')
 print('Independent permutations: all Case13 and Case02/04 assignment sets match.')
