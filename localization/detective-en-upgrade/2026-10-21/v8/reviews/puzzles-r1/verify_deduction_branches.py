from independent_solver import *
late_targets={13:'Remy',15:'Milo',19:'Sasha',22:'Zara',25:'Nori',29:'Seth'}
receipts=[]
for case,target in late_targets.items():
 m=make_models()[case];m.counts=[];r=m.solve();rr=[]
 for s in r['solutions']:
  ps={v:cell(p) for v,p in s.items()}
  assert all(p in m.dom[v] for v,p in ps.items())
  assert all(f(ps[a],ps[b]) for a,b,f,d in m.binary)
  room=m.room(ps[target]);others=[v for v in s if v!=target and m.room(ps[v])==room]
  rr.append({'roster':s,'target_room':m.m['room_codes'][room],'other_people':others,'count':len(others),'passes_exactly_one_other':len(others)==1})
 assert sum(q['passes_exactly_one_other'] for q in rr)==1
 receipts.append({'case':case,'target':target,'pre_companion_count':len(rr),'verified_rosters':rr})
 # Assertions for claims used in prose, checked over every pre-companion candidate.
 if case==13:
  assert all(s['Juno']=='F3' and s['Skye']=='E4' and s['Eden']=='G2' for s in r['solutions'])
  assert all(s['Moxie']=='C5' for s,q in zip(r['solutions'],rr) if q['passes_exactly_one_other'])
 if case==15:
  assert all(s['Jett']=='G7' and s['Cruz']=='C3' and s['Piper']=='F4' for s in r['solutions'] if s['Milo']=='A1')
 if case==19:
  assert all(s['Kian']=='F4' and s['Avery']=='E5' and s['Ollie']=='D3' for s in r['solutions'])
 if case==29:
  assert all(s['Jules']=='E8' and s['Bryn'][1:]=='9' for s in r['solutions'])
  assert all(s['Wade']=='F7' for s,q in zip(r['solutions'],rr) if q['passes_exactly_one_other'])
print([(r['case'],r['pre_companion_count'],sum(q['passes_exactly_one_other'] for q in r['verified_rosters'])) for r in receipts])
(OUT/'verified-candidate-branches.json').write_text(json.dumps(receipts,indent=2))
# Literal example rosters in MAP_DEDUCTION_CHAINS, all checked with normal clues and objective count evaluated.
examples={
 13:[{'Juno':'F3','Skye':'E4','Eden':'G2','Willow':'A1','Bodhi':'B6','Moxie':'C5','Remy':'D7'}],
 19:[{'Avery':'E5','Theo':'B2','Ollie':'D3','Dex':'A1','Mack':'C7','Kian':'F4','Sasha':'G6'}],
 22:[{'Lex':'E6','Imani':'F7','Cody':'D4','Nia':'G5','Gia':'B1','Wes':'C3','Zara':'A2'}],
 25:[{'Gabe':'F3','Casey':'D4','Rio':'E2','Tate':'C6','Sol':'G1','Wynn':'B7','Nori':'A5'}, {'Gabe':'F4','Casey':'D5','Rio':'E3','Tate':'A6','Sol':'G1','Wynn':'B7','Nori':'C2'}]
}
for case,ss in examples.items():
 actual=next(r for r in receipts if r['case']==case)['verified_rosters']
 for s in ss:
  found=next(q for q in actual if q['roster']==s)
  assert not found['passes_exactly_one_other']
print('All literal failed-example rosters verified against full ordinary constraints; all fail exactly-one-companion.')
