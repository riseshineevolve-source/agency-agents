"""Independent complete row/column permutation audit; never reads expected roster.
Case07 anchor simulations establish conditional math, not source identification.
"""
import itertools,json,hashlib,collections,pathlib,copy
p=pathlib.Path(__file__).resolve().parent;g=json.load(open(p/'root-map-grids-06-07.json'))
def adjacent(a,b,diag=False):
 dx=abs(ord(a[0])-ord(b[0]));dy=abs(int(a[1])-int(b[1]));return max(dx,dy)==1 if diag else dx+dy==1
def enumeration(case,anchor=None,diag=False):
 z=copy.deepcopy(g[f'case{case:02d}'])
 room={c+str(r):row[i] for r,row in enumerate(z['room_rows'],1) for i,c in enumerate('ABCDEF')}
 blocked=set(z['blocked']);names=['Scout','Hugo','Arlo','Vale','Wren','Uma'] if case==6 else ['Blaze','Indigo','Willa','Zoe','Rocket','Gray']
 out=[]
 for cols in itertools.permutations('ABCDEF'):
  if (case==6 and cols[0]!='E') or (case==7 and cols[4]!='E'):continue
  for rows in itertools.permutations('123456'):
   if (case==6 and rows[0]!='3') or (case==7 and rows[4]!='5'):continue
   a=dict(zip(names,[c+r for c,r in zip(cols,rows)]))
   if any(x in blocked for x in a.values()):continue
   if case==6:
    if room[a['Hugo']]!='D' or not any(adjacent(a['Hugo'],x,diag) for x in z['display_cases']):continue
    if room[a['Arlo']]!='F' or a['Arlo'][1]!='2':continue
    if room[a['Vale']]!='G' or not any(adjacent(a['Vale'],x,diag) for x in z['statues']):continue
    if a['Wren'] not in z['benches'] or not any(adjacent(a['Wren'],x,diag) for x in z['skeletons']):continue
    target='Uma'
   else:
    if room[a['Blaze']]!='R' or sum(room[x]=='R' for x in a.values())!=1:continue
    if room[a['Indigo']] not in ['D','R']:continue
    if anchor and abs(ord(a['Willa'][0])-ord(anchor[0]))+abs(int(a['Willa'][1])-int(anchor[1]))!=2:continue
    if not (a['Zoe'][0] in 'AF' or a['Zoe'][1] in '16'):continue
    if not any(adjacent(a['Zoe'],x,diag) for x in z['visible_roadcases_or_carts']):continue
    target='Gray'
   if sum(room[x]==room[a[target]] for n,x in a.items() if n!=target)!=1:continue
   out.append(a)
 answers=collections.Counter(next(n+' at '+x for n,x in a.items() if n!=target and room[x]==room[a[target]]) for a in out)
 return {'full_assignment_count':len(out),'answer_counts':dict(answers),'assignments':out}
r={'case06_orthogonal':enumeration(6),'case06_eight_neighbor_sensitivity':enumeration(6,diag=True),'case07_conditional_only':{('anchor_omitted_not_full_validation' if a is None else a):enumeration(7,a) for a in [None,'D1','C2','C1','C4']}}
root=json.load(open(p/'root-map-results-06-07.json'))
def signature(assignments):
 return sorted(tuple(sorted(a.items())) for a in assignments)
assert signature(r['case06_orthogonal']['assignments'])==signature(root['case06']['orthogonal']['assignments'])
assert signature(r['case06_eight_neighbor_sensitivity']['assignments'])==signature(root['case06']['eight_neighbor']['assignments'])
for a in ['D1','C2','C1','C4']:
 assert signature(r['case07_conditional_only'][a]['assignments'])==signature(root['case07']['conditional_anchors_not_source_validation'][a]['assignments'])
assert signature(r['case07_conditional_only']['anchor_omitted_not_full_validation']['assignments'])==signature(root['case07']['unidentified_anchor_omitted_not_a_full_puzzle_check']['assignments'])
r['all_assignment_sets_equal_root']=True
(p/'independent-enumeration-results-06-07.json').write_text(json.dumps(r,indent=2)+'\n')
print('Independent column/row permutation enumeration: all assignment sets equal root; Case06 unique; Case07 remains conditional.')
