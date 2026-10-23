import json,re,hashlib,difflib
from pathlib import Path
R=Path('detective-upgrade'); C=R/'candidate'
source=json.loads((R/'source/intake-v5.json').read_text()); pages=json.loads((R/'source/detective-225.pages.json').read_text()); edits=json.loads((C/'editorial-deltas.json').read_text())
texts={p['page']:p['text'] for p in pages}; errors=[]; accepted=[]
for e in edits:
 if texts[e['page']].count(e['old'])!=1:errors.append({'page':e['page'],'error':'replacement must match once','old':e['old']});continue
 texts[e['page']]=texts[e['page']].replace(e['old'],e['new'],1);accepted.append(e)
if errors:raise RuntimeError(errors)
def partition(oldparts,new):
 old=''.join(oldparts)
 if old==new:return oldparts
 ops=difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes()
 def mapped(pos):
  for tag,a,b,c,d in ops:
   if a<=pos<=b:
    if tag=='equal':return c+pos-a
    if b==a:return d
    return round(c+(pos-a)*(d-c)/(b-a))
  return len(new)
 bounds=[0];o=0
 for part in oldparts[:-1]:
  o+=len(part); k=mapped(o)
  if 0<k<len(new) and not (new[k-1].isspace() or new[k].isspace()):
   options=[i for i in range(max(bounds[-1]+1,k-24),min(len(new),k+24)) if new[i-1].isspace() or new[i].isspace()]
   if options:k=min(options,key=lambda i:abs(i-k))
  bounds.append(k)
 bounds.append(len(new))
 out=[new[a:b] for a,b in zip(bounds,bounds[1:])]
 if any(not x.strip() for x in out):
  words=re.findall(r'\S+\s*',new)
  if len(words)<len(oldparts):raise RuntimeError('cannot distribute nonempty blocks')
  counts=[len(re.findall(r'\S+',x)) for x in oldparts];total=sum(counts);splits=[0];used=0
  for i,n in enumerate(counts[:-1]):
   used+=n;k=round(len(words)*used/total);k=max(splits[-1]+1,min(k,len(words)-(len(oldparts)-i-1)));splits.append(k)
  splits.append(len(words));out=[''.join(words[a:b]) for a,b in zip(splits,splits[1:])]
 assert ''.join(out)==new
 return out
segments=[]
for page in range(1,226):
 ss=[dict(s) for s in source['segments'] if s['page']==page]
 if page<19 or page not in {e['page'] for e in accepted}:
  for s in ss:s['target_text']=s['text'];s['decision']='KEEP'
  segments+=ss;continue
 old=''.join(s['text'] for s in ss)
 assert old==next(p['text'] for p in pages if p['page']==page),(page,'intake extraction order mismatch')
 new=texts[page];cursor=0;i=0
 while i<len(ss):
  if not ss[i]['editable']:
   t=ss[i]['text'];assert new[cursor:cursor+len(t)]==t,(page,ss[i]['id'],'protected anchor drift',new[cursor:cursor+100],t)
   ss[i]['target_text']=t;cursor+=len(t);i+=1;continue
  j=i
  while j<len(ss) and ss[j]['editable']:j+=1
  if j==len(ss):end=len(new)
  else:
   anchor=ss[j]['text'];end=new.find(anchor,cursor);assert end>=0,(page,ss[j]['id'],'missing anchor')
  parts=partition([s['text'] for s in ss[i:j]],new[cursor:end])
  for s,t in zip(ss[i:j],parts):s['target_text']=t
  cursor=end;i=j
 assert cursor==len(new),(page,'trailing new text')
 for s in ss:s['decision']='FIX' if s['target_text']!=s['text'] else 'KEEP'
 segments+=ss
out={'source_sha256':source['source_sha256'],'language':'en','mode':'upgrade','status':'PREMIUM_WORKING','segments':segments}
front=json.loads((C/'front-editorial-deltas.json').read_text())
byid={s['id']:s for s in segments}
for e in front:
 assert byid[e['id']]['text']==e['old'],e['id']
 byid[e['id']]['target_text']=e['new'];byid[e['id']]['decision']='FIX'
accepted+=front
(C/'candidate-segments.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(C/'candidate-pages.json').write_text(json.dumps([{'page':p,'text':''.join(s['target_text'] for s in segments if s['page']==p)} for p in range(1,226)],ensure_ascii=False,indent=2)+'\n')
(C/'change-ledger.json').write_text(json.dumps(accepted,ensure_ascii=False,indent=2)+'\n')
print('segments',len(segments),'changed',sum(s['decision']=='FIX' for s in segments),'pages',len(set(e['page'] for e in accepted)))
