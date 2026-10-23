"""Recheck V5 against its actual accepted V4 baseline and real delta receipts."""
from pathlib import Path
import json,hashlib,subprocess
r=Path(__file__).resolve().parents[1];h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
old=load(r/'history/candidate-v4.json');new=load(r/'candidate/candidate.json');assert h(r/'history/candidate-v4.json')=='ec93cfc7a99257113fe33d6536574d2d6889c969ec68dac69ca97ad26010a55e'
assert [s['id'] for s in old['segments']]==[s['id'] for s in new['segments']]
delta=[(a,b) for a,b in zip(old['segments'],new['segments']) if a['text']!=b['text']]
assert {a['id'] for a,b in delta}=={'page207.block05','page212.block05'}
assert all(a['text'].count('\0')==3 and b['text']==a['text'].replace('\0','-') for a,b in delta)
ch=h(r/'candidate/candidate.json');receipts=[]
for stage,name in [('native_language','review-separator-native-audience.json'),('audience','review-separator-native-audience.json'),('meaning','review-separator-truth-logic.json'),('logic','review-separator-truth-logic.json')]:
 p=r/'geometry-audit'/name;d=load(p);assert d['candidate_sha256']==ch and d['status']=='PASS';receipts.append({'stage':stage,'status':'PASS','candidate_sha256':ch,'reviewer':d['reviewer'],'evidence':'Actual source-bound two-unit delta/closure review; unchanged3065units retain explicit accepted V4whole-book review baseline.','evidence_file':'../geometry-audit/'+name,'evidence_sha256':h(p)})
p=r/'qa/reviews-v5.cli.json';p.write_text(json.dumps({'candidate_sha256':ch,'reviews':receipts},indent=2)+'\n')
choices=[Path('rse/scripts/rse-language.py').resolve()]+[p/'scripts/rse-language.py' for p in r.parents]
cli=next((p for p in choices if p.exists()),None)
if cli is None:raise SystemExit('Recover reviewed scripts/rse-language.py first; no fabricated QA.')
subprocess.run(['python3',str(cli),'check','--run',str(r/'run-v5'),'--candidate',str(r/'candidate/candidate.json'),'--reviews',str(p),'--output',str(r/'qa/FINAL_LANGUAGE_CHECK_V5.json')],check=True)
