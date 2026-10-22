"""V8 independent constraint enumeration; fresh solver and constraints from visible V7.
Historical grid transcriptions are explicitly corrected/checked against folio PNGs.
No answer fields are ever supplied as solver inputs.
"""
import json,itertools,pathlib,hashlib,time,collections
ROOT=pathlib.Path('/workspace/scratch/e6eabdc4c3a0/detective-v8')
SRC=ROOT/'source-models/geometry-audit'; OUT=ROOT/'reviews/puzzles-r1'
def read(f): return json.load(open(SRC/f))
def coord(p):return chr(65+p[0])+str(p[1]+1)
def cell(s):return (ord(s[0])-65,int(s[1:])-1)
def dist(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
def diag(a,b):return abs(a[0]-b[0])==abs(a[1]-b[1])==1
class Model:
 def __init__(self,n,m,people,rows=None,blocked=None):
  self.n=n;self.m=m;self.people=people.split();self.rows=rows or m.get('room_rows') or m.get('grid_rows_north_to_south') or [''.join(x) for x in m.get('room_grid',[])];self.w=len(self.rows);self.blocks=set(cell(s) for s in (blocked if blocked is not None else m.get('blocked',m.get('blocked_squares',[]))));self.floor={(x,y) for x in range(self.w) for y in range(self.w)}-self.blocks;self.dom={v:set(self.floor) for v in self.people};self.binary=[];self.counts=[];self.description=[]
  for a,b in itertools.combinations(self.people,2):self.binary.append((a,b,lambda p,q:p[0]!=q[0] and p[1]!=q[1],'different row and column'))
 def room(self,p):return self.rows[p[1]][p[0]]
 def un(self,v,fun,desc):self.dom[v]={p for p in self.dom[v] if fun(p)};self.description.append((v,desc,[coord(p) for p in sorted(self.dom[v])]))
 def fix(self,v,c):self.un(v,lambda p:p==cell(c),'exact '+c)
 def bi(self,a,b,fun,desc):self.binary.append((a,b,fun,desc))
 def same(self,a,b):self.bi(a,b,lambda p,q:self.room(p)==self.room(q),'same room')
 def solo(self,v):
  for q in self.people:
   if q!=v:self.bi(v,q,lambda p,q:self.room(p)!=self.room(q),'only person in room')
 def companion(self,v):self.counts.append(v)
 def adj(self,p,objects,mode='edge',same=True):return any((dist(p,cell(o))==1 if mode=='edge' else max(abs(p[0]-cell(o)[0]),abs(p[1]-cell(o)[1]))==1) and (not same or self.room(p)==self.room(cell(o))) for o in objects)
 def propagate(self,D,trace=None):
  changed=True
  while changed:
   changed=False
   for a,b,fun,desc in self.binary:
    for u,v,rev in [(a,b,False),(b,a,True)]:
     old=D[u];new={p for p in old if any(fun(q,p) if rev else fun(p,q) for q in D[v])}
     if not new:return False
     if new!=old:
      D[u]=new;changed=True
      if trace is not None:trace.append({'person':u,'constraint':desc+' / '+v,'before':[coord(p) for p in sorted(old)],'after':[coord(p) for p in sorted(new)]})
   # Row/column Hall subsets. Each roster has exactly n people / n rows.
   for axis in [0,1]:
    # Eliminate exhausted Hall groups to provide child-readable propagation trace.
    for k in range(1,len(self.people)):
     groups=itertools.combinations(range(self.w),k)
     for values in groups:
      ids=[v for v in self.people if {p[axis] for p in D[v]}<=set(values)]
      if len(ids)>len(values):return False
      if len(ids)!=len(values):continue
      for v in self.people:
       if v in ids:continue
       old=D[v];new={p for p in old if p[axis] not in values}
       if not new:return False
       if old!=new:
        D[v]=new;changed=True
        if trace is not None:trace.append({'person':v,'constraint':('columns' if axis==0 else 'rows')+' reserved by '+','.join(ids),'before':[coord(p) for p in sorted(old)],'after':[coord(p) for p in sorted(new)]})
   for who in self.counts:
    other=[v for v in self.people if v!=who]
    options=set()
    for p in D[who]:
     r=self.room(p);lo=sum(all(self.room(q)==r for q in D[v]) for v in other);hi=sum(any(self.room(q)==r for q in D[v]) for v in other)
     if lo<=1<=hi:options.add(p)
    if not options:return False
    if options!=D[who]:D[who]=options;changed=True
    rooms={self.room(p) for p in D[who]}
    if len(rooms)!=1:continue
    r=next(iter(rooms));forced=[v for v in other if all(self.room(q)==r for q in D[v])];possible=[v for v in other if any(self.room(q)==r for q in D[v])]
    for v in other:
     old=D[v]
     if len(forced)==1 and v not in forced:new={p for p in old if self.room(p)!=r}
     elif len(possible)==1 and v in possible:new={p for p in old if self.room(p)==r}
     else:continue
     if not new:return False
     if new!=old:D[v]=new;changed=True
  return True
 def solve(self):
  sols=[];nodes=0;initial={v:set(x) for v,x in self.dom.items()};trace=[];ok=self.propagate(initial,trace)
  def search(D):
   nonlocal nodes
   nodes+=1
   if not self.propagate(D):return
   if all(len(D[v])==1 for v in D):
    s={v:next(iter(q)) for v,q in D.items()}
    if all(sum(self.room(s[v])==self.room(s[who]) for v in s if v!=who)==1 for who in self.counts):sols.append(s)
    return
   v=min((v for v in D if len(D[v])>1),key=lambda v:len(D[v]))
   for p in sorted(D[v]):
    nxt={u:set(s) for u,s in D.items()};nxt[v]={p};search(nxt)
  if ok:search(initial)
  return {'case':self.n,'solution_count':len(sols),'nodes':nodes,'initial_domains':{v:[coord(p) for p in sorted(d)] for v,d in self.dom.items()},'after_initial_propagation':{v:[coord(p) for p in sorted(d)] for v,d in initial.items()},'propagation_trace':trace,'solutions':[{v:coord(p) for v,p in s.items()} for s in sols],'room_occupancy':[dict(collections.Counter(self.room(p) for p in s.values())) for s in sols]}
def make_models(adjmode='edge',missing_circle_blocked=False):
 models={};x=read('spatial-intro-29-grid.json');m=Model(1,x['intro_case01'],'Quill Pip Morse Knox');m.un('Quill',lambda p:p[1]==0,'row1');m.un('Pip',lambda p:p[1]==2,'row3');m.un('Morse',lambda p:p[0]==2,'columnC');m.un('Knox',lambda p:p[0]==3,'columnD');m.bi('Pip','Quill',lambda p,q,m=m:p[0]<q[0],'left');m.bi('Morse','Knox',lambda p,q,m=m:p[1]>q[1],'lower');models[1]=m
 em={a['case']:a for a in read('early-map-grids.json')['cases']}
 m=Model(2,em[2],'Nova Dax Rook Atlas Ivy Max',blocked=em[2]['blocked']+(['C3'] if missing_circle_blocked else []));m.fix('Nova','B3');m.un('Dax',lambda p:m.room(p)=='D' and p[0]==3,'Display,columnD');m.un('Rook',lambda p:p[0] in [0,5] and p[1] in [0,5] and m.adj(p,m.m['objects']['teacher_desk'],same=True),'whole-grid corner beside teacher desk');m.un('Atlas',lambda p:m.room(p)=='E' and p[0]==5,'Equipment,columnF');m.un('Ivy',lambda p:coord(p) in m.m['objects']['desk_chair'],'on desk chair');m.companion('Max');models[2]=m
 m=Model(4,em[4],'Echo Kai Zuri Briar Clover Pixel');m.fix('Echo','A2');m.un('Kai',lambda p:m.room(p)=='K','Kitchen');m.solo('Kai');m.un('Zuri',lambda p:m.room(p)=='T' and p[1]==3,'Pickup,row4');m.un('Briar',lambda p:m.adj(p,m.m['objects']['ring_toss_stand'],mode=adjmode,same=True),'beside ring toss');m.un('Clover',lambda p:m.room(p)=='P' and p[1]==4,'Packing,row5');m.un('Pixel',lambda p:m.room(p)=='T','objective: Pixel Pickup Tent');m.companion('Pixel');models[4]=m
 x=read('root-map-grids-06-07.json');m=Model(6,x['case06'],'Scout Hugo Arlo Vale Wren Uma');m.fix('Scout','E3');m.un('Hugo',lambda p:m.room(p)=='D' and m.adj(p,m.m['display_cases'],mode=adjmode),'Dinosaur beside display case');m.un('Arlo',lambda p:m.room(p)=='F' and p[1]==1,'Foyer,row2');m.un('Vale',lambda p:m.room(p)=='G' and m.adj(p,m.m['statues'],mode=adjmode),'Gallery beside statue');m.un('Wren',lambda p:coord(p) in m.m['benches'] and m.adj(p,m.m['skeletons'],mode=adjmode),'bench beside skeleton');m.companion('Uma');models[6]=m
 m=Model(7,x['case07'],'Blaze Indigo Willa Zoe Rocket Gray');m.un('Blaze',lambda p:m.room(p)=='R','Rehearsal');m.solo('Blaze');m.un('Indigo',lambda p:m.room(p) in ['D','R'],'Dressing or Rehearsal');m.un('Willa',lambda p:dist(p,cell('C2'))==2,'Manhattan2 from C2');m.un('Zoe',lambda p:(p[0] in [0,5] or p[1] in [0,5]) and m.adj(p,m.m['visible_roadcases_or_carts']),'outer wall beside wheeled case');m.fix('Rocket','E5');m.companion('Gray');models[7]=m
 mid={a['case']:a for a in read('mid-map-grids.json')['cases']}
 m=Model(10,mid[10],'Ember Nico Wyatt Finn Beck Vera Dash');seats=m.m['objects']['demo_seat'];m.un('Ember',lambda p:coord(p) in seats and m.adj(p,seats),'seat beside another seat');m.un('Nico',lambda p:p[0]==5 and coord(p) in seats,'columnF demo seat');m.un('Wyatt',lambda p:p[0]==1 and m.room(p)=='R' and m.adj(p,['B6']),'columnB beside wheeled robot arm in Robotics');m.un('Finn',lambda p:dist(p,cell('C7'))==7,'Manhattan7 coolant tank');m.un('Beck',lambda p:(p[0] in [0,6] or p[1] in [0,6]) and m.adj(p,m.m['objects']['parts_crate']),'outer wall beside parts crate');m.un('Vera',lambda p:any(m.room(cell(q))==m.room(p) for q in m.m['objects']['control_console']) and not m.adj(p,m.m['objects']['control_console']),'room with console,not beside console');m.companion('Dash');models[10]=m
 # New manual visual transcription of folio63, not an inherited model.
 mm={'room_rows':['TTTSSSS','TTTTRSS','CTRRRSS','CCRRRGS','CBRBBGG','CBBBBGG','CCBGGGG'],'blocked':['B1','E1','F1','C4','C6','E7','F7'],'room_codes':{'T':'Training Room','S':'Stage Wing','C':'Costume Room','R':'Rehearsal Room','B':'Bird Room','G':'Green Room'}}
 m=Model(12,mm,'Kira Nell Iris Eli Cove Sage Winter');m.un('Kira',lambda p:m.room(p)=='B','BirdRoom');m.solo('Kira');m.un('Nell',lambda p:m.room(p)=='S' and p[1]==1,'StageWing,row2');m.un('Iris',lambda p:p[1]==4,'third from south = row5 with 7 distinct rows');m.un('Eli',lambda p:m.room(p) in ['G','B'],'Green or Bird');m.un('Cove',lambda p:p[0]==1 and(p[0] in [0,6] or p[1] in [0,6]),'columnB outerwall');m.bi('Sage','Kira',lambda p,q,m=m:(m.room(p)=='R')!=(m.room(q)=='R'),'exactly one in Rehearsal');m.companion('Winter');models[12]=m
 x=read('case13-grid.json');m=Model(13,x,'Juno Skye Eden Willow Bodhi Moxie Remy');m.bi('Juno','Skye',diag,'corners touch');m.un('Skye',lambda p:m.room(p)=='R','Ranger');m.same('Eden','Juno');m.bi('Willow','Bodhi',lambda p,q,m=m:p[0]<q[0] and p[1]<q[1],'NW anydistance');m.bi('Bodhi','Moxie',lambda p,q,m=m:p[0]<q[0] and p[1]>q[1],'SW anydistance');m.un('Moxie',lambda p:m.room(p)=='R' and p[1]==4,'Ranger,row5');m.companion('Remy');models[13]=m
 m=Model(15,mid[15],'Harper Piper Duke Cruz Jett Inez Milo');m.bi('Harper','Cruz',lambda p,q,m=m:p[0]>q[0] and p[1]<q[1],'above and right');m.bi('Piper','Duke',lambda p,q,m=m:p[0]>q[0] and p[1]<q[1],'above and right');m.un('Duke',lambda p:m.room(p)=='F' and p[1]==4,'FirstAid,row5');m.un('Cruz',lambda p:m.adj(p,m.m['objects']['cot']),'same-room beside cot');m.un('Jett',lambda p:m.room(p)=='W','Welcome');m.solo('Jett');m.un('Inez',lambda p:any(m.room(cell(q))==m.room(p) for q in m.m['objects']['cot']) and not m.adj(p,m.m['objects']['cot']),'room containing cot,not beside cot');m.companion('Milo');models[15]=m
 late=read('late-map-17-19-grid.json');m=Model(17,late['case17'],'Otis Mika Koa Sunny Luna Axel Reed');m.un('Otis',lambda p:m.room(p) in ['T','B'],'Ticket or Baggage');m.un('Mika',lambda p:m.room(p)=='T' and p[0]==1,'Ticket,columnB');m.un('Koa',lambda p:m.room(p)=='W' and p[1]==5,'Waiting,row6');m.un('Sunny',lambda p:coord(p) in m.m['benches'],'on bench');m.un('Luna',lambda p:m.room(p)=='W' and p[0]==6,'Waiting,columnG');m.bi('Axel','Koa',lambda p,q,m=m:p[1]==q[1]-3,'exactly3 rows north');m.companion('Reed');models[17]=m
 m=Model(19,late['case19'],'Avery Theo Ollie Dex Mack Kian Sasha',blocked=late['case19']['blocked']+['F7']);m.bi('Avery','Mack',lambda p,q,m=m:p[1]==q[1]-2,'exactly2 rows north');m.un('Theo',lambda p:dist(p,cell(m.m['piano']))==7,'Manhattan7 piano');m.bi('Ollie','Avery',lambda p,q,m=m:(m.room(p)=='A')!=(m.room(q)=='A'),'exactlyone Archive');m.same('Dex','Theo');m.bi('Mack','Ollie',lambda p,q,m=m:p[0]<q[0] and p[1]>q[1],'SW anydistance');m.un('Kian',lambda p:m.room(p)=='S' and p[0]==5,'StudyHall,columnF');m.companion('Sasha');models[19]=m
 x=read('spatial-20-22-grid.json');m=Model(20,x['case20'],'Sid Pax Luca Mara Asa Toby Demi',blocked=[s for s in x['case20']['blocked'] if s not in ['E7','F7']]);m.bi('Sid','Pax',lambda p,q,m=m:p[1]>q[1],'lowerrow');m.bi('Pax','Mara',lambda p,q,m=m:p[1]>q[1] and p[0]>q[0],'lowerrow and rightcolumn');m.bi('Luca','Asa',diag,'diagonal one-row one-column');m.un('Mara',lambda p:m.room(p)=='M' and p[1]==3,'MainStudio,row4');m.same('Asa','Mara');m.un('Toby',lambda p:m.room(p)=='W','WorkshopHall');m.solo('Toby');m.companion('Demi');models[20]=m
 m=Model(22,x['case22'],'Lex Imani Cody Nia Gia Wes Zara');m.bi('Lex','Imani',diag,'diagonal nextto');m.same('Imani','Nia');m.bi('Cody','Wes',diag,'diagonal nextto');m.bi('Nia','Lex',lambda p,q,m=m:(m.room(p)=='P')!=(m.room(q)=='P'),'exactlyone PracticeHall');m.un('Gia',lambda p:dist(p,cell(m.m['piano']))==7,'Manhattan7 piano');m.un('Wes',lambda p:any(m.room(cell(q))==m.room(p) for q in m.m['instrument_lockers']) and not m.adj(p,m.m['instrument_lockers'],mode=adjmode),'roomwithlocker,notbeside same-room locker');m.companion('Zara');models[22]=m
 x=read('spatial-23-25-grid.json');m=Model(23,x['case23'],'Vivi Cora Ozzy Rae Mae Pia Jude');m.un('Vivi',lambda p:dist(p,cell(m.m['gondola']))==7,'Manhattan7 gondola');m.bi('Cora','Mae',lambda p,q,m=m:p[0]>q[0] and p[1]<q[1],'NE anydistance');m.bi('Ozzy','Cora',lambda p,q,m=m:p[0]<q[0] and p[1]>q[1],'SW anydistance');m.bi('Rae','Cora',lambda p,q,m=m:p[0]==q[0]+2,'exactly2 columns east');m.bi('Mae','Ozzy',lambda p,q,m=m:(m.room(p)==m.room(q)) if coord(q) in m.m['benches'] else True,'bench person if Ozzy');m.bi('Mae','Pia',lambda p,q,m=m:(m.room(p)==m.room(q)) if coord(q) in m.m['benches'] else True,'bench person if Pia');m.bi('Ozzy','Pia',lambda p,q,m=m:(coord(p) in m.m['benches']) or (coord(q) in m.m['benches']),'one of Ozzy/Pia on bench');m.bi('Pia','Vivi',lambda p,q,m=m:(m.room(p)=='S')!=(m.room(q)=='S'),'exactlyone SnackStand');m.companion('Jude');models[23]=m
 m=Model(25,x['case25'],'Gabe Casey Rio Tate Sol Wynn Nori');m.bi('Gabe','Rio',diag,'diagonalnextto');m.un('Casey',lambda p:m.room(p)=='L' and p[0]==3,'Lobby,columnD');m.bi('Rio','Gabe',lambda p,q,m=m:p[0]<q[0] and p[1]<q[1],'NW anydistance');m.bi('Tate','Wynn',diag,'diagonalnextto');m.bi('Sol','Gabe',lambda p,q,m=m:p[0]>q[0] and p[1]<q[1],'NE anydistance');m.un('Wynn',lambda p:m.room(p)=='A' and coord(p) in m.m['bar_stools'],'Laundry barstool');m.companion('Nori');models[25]=m
 x=read('spatial-intro-29-grid.json');m=Model(29,x['case29'],'Mavis Cato Jules Bryn Vega Ren Poppy Wade Seth');m.bi('Mavis','Vega',lambda p,q,m=m:p[0]<q[0] and p[1]<q[1],'NW anydistance');m.bi('Cato','Ren',lambda p,q,m=m:p[0]>q[0] and p[1]<q[1],'NE anydistance');m.bi('Jules','Wade',diag,'diagonalnextto');m.same('Bryn','Jules');m.bi('Vega','Cato',lambda p,q,m=m:p[0]<q[0] and p[1]<q[1],'NW anydistance');m.un('Ren',lambda p:m.room(p)=='C','ControlRoom');m.same('Poppy','Mavis');m.un('Wade',lambda p:m.room(p)=='O' and m.adj(p,m.m['teacher_desks'],mode=adjmode),'Operations beside same-room teachersdesk');m.companion('Seth');models[29]=m
 return models
if __name__=='__main__':
 start=time.time();models=make_models();results=[]
 for n,m in models.items():
  r=m.solve();results.append(r);print(n,r['solution_count'],r['nodes'],r['solutions'][:2],flush=True)
 output={'format':'independent-all-spatial-audit-v1','canonical_sha256':'df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1','evidence':'V7 PDF visible folios individually reviewed; inherited geometry transcriptions crosschecked; fresh solver + constraint modeling. Case12 newly transcribed. Case19 F7 added blocker from actual black marker. Case20 E7/F7 made usable per corrected art.','results':results}
 (OUT/'spatial-enumerations.json').write_text(json.dumps(output,indent=2));print('seconds',time.time()-start)
