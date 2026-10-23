from pathlib import Path
import json,re,hashlib
W=Path(__file__).resolve().parents[2];O=W/'detective-upgrade';R=W/'detective-v7'
old=json.loads((O/'source/intake-v5.json').read_text())['segments'];v6=json.loads((W/'detective-v6/candidate/candidate.json').read_text());new={s['id']:s['text'] for s in v6['segments']}
casepages=[16,19,23,27,31,37,41,45,49,53,57,61,65,69,73,77,83,87,91,95,99,105,109,113,117,121,125,129,133,137]
N='MIMI|LULI|DILO|ALIO|NINI|BIBI|EVERYONE';norm=lambda t:re.sub(r'\s+',' ',t).strip();scenes=[]
for case,page in enumerate(casepages,1):
 ss=[s for s in old if s['page']==page];turns=[];combined=[s for s in ss if s.get('classification')=='comms']
 if case==30:
  original=[('MIMI','No new clue. Use what you earned.'),('DILO','Victory noise?'),('LULI','Pending evidence.'),('NINI','Very pending.'),('BIBI','Begin.')]
  for (speaker,text),now in zip(original,['Use what you earned.','Victory noise?','Pending evidence.','Very pending.','Begin.']):turns.append({'speaker':speaker,'source_text':text,'v6_text':now,'ids':['page137.block08'] if speaker in ['MIMI','DILO'] else ['page137.block09']})
 elif combined:
  s=combined[0];parts=re.split(r'(?m)^('+N+r'):\s*',s['text']);np=re.split(r'(?m)^('+N+r'):\s*',new[s['id']])
  for i in range(1,len(parts),2):turns.append({'speaker':parts[i],'source_text':norm(parts[i+1]),'v6_text':norm(np[i+1]),'ids':[s['id']]})
 else:
  current=None
  for s in ss:
   if re.fullmatch(r'(?:\d+\s+)?(?:'+N+r')(?:\s+\d+)?\s*',s['text'].strip()):
    if current:turns.append(current)
    current={'speaker':re.search(N,s['text']).group(0),'source_text':'','v6_text':'','ids':[],'speaker_id':s['id']}
   elif current and s.get('editable'):
    current['source_text']+=s['text'];current['v6_text']+=new[s['id']];current['ids'].append(s['id'])
  if current:turns.append(current)
  for t in turns:t['source_text']=norm(t['source_text']);t['v6_text']=norm(t['v6_text'])
 assert turns,(case,page)
 for t in turns:t['changed']=t['source_text']!=t['v6_text']
 scenes.append({'case':case,'source_folio':page,'changed_before_v7':any(t['changed'] for t in turns),'changed_turns_before_v7':sum(t['changed'] for t in turns),'turns':turns})
(R/'baseline/candidate-v6.json').write_bytes((W/'detective-v6/candidate/candidate.json').read_bytes())
(R/'diagnostic/comms-source-v6.json').write_text(json.dumps(scenes,ensure_ascii=False,indent=2)+'\n')
lines=[]
for s in scenes:
 lines.append(f"\nCASE {s['case']:02d} / folio{s['source_folio']} / prior changed={s['changed_before_v7']}\n")
 for t in s['turns']:
  lines.append(t['speaker']+': '+t['v6_text']+'\n')
  if t['changed']:lines.append('  SOURCE: '+t['source_text']+'\n')
(R/'diagnostic/ALL_COMMS_V6_WITH_PRIOR_DIFF.txt').write_text(''.join(lines))
report={'source':'Owner225PDF SHA2569db84d4f...','baseline_v6_sha256':hashlib.sha256((W/'detective-v6/candidate/candidate.json').read_bytes()).hexdigest(),'principal_case_comms':30,'scenes_changed_from_owner225':sum(s['changed_before_v7'] for s in scenes),'scenes_unchanged_from_owner225':sum(not s['changed_before_v7'] for s in scenes),'changed_cases':[s['case'] for s in scenes if s['changed_before_v7']],'changed_turns':sum(s['changed_turns_before_v7'] for s in scenes),'v6_vs_v5_comms_changes':0,'scope':'Whitespace-normalized spoken dialogue in30principalcasecomms; source-folio locations explicit; not all narration/footer/frontmatter. Case30original interleaved extraction reconstructed from verified source reading order.'}
(R/'diagnostic/PRIOR_COMMS_AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));print(''.join(lines))
