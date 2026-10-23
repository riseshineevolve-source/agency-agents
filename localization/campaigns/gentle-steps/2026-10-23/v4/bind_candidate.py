from pathlib import Path
import json,hashlib,copy
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'pl':['01_grudzien_bez_pospiechu_PL.md','02_kalendarz_z_zadaniami_PL.md'],'en':['01_december_family_time_EN.md','02_advent_activities_EN.md']}
for lang,fs in files.items():
 c=copy.deepcopy(json.loads((R/'run'/lang/'candidate.json').read_text()))
 for u,f in zip(c['segments'],fs):u['text']=(R/'candidate'/f).read_text()
 p=R/'candidate'/('candidate-'+lang+'.json');p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 print(lang,sha(p),[(f,len((R/'candidate'/f).read_text().split())) for f in fs])
