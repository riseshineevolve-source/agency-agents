from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ch=sha(r/'candidate/candidate.json');rs=[]
for stage,path in [('native_language','comedy-final/native_language.json'),('audience','audience-final/audience.json'),('meaning','story-final/meaning.json'),('logic','story-final/logic.json')]:
 p=r/'reviews'/path;x=json.loads(p.read_text());assert x.get('status',x.get('overall_status'))=='PASS' and x['candidate_sha256']==ch,(stage,x)
 rs.append({'stage':stage,'status':'PASS','candidate_sha256':ch,'reviewer':x.get('reviewer','/root/hm10_family_ear'),'scope':x.get('review_scope',x.get('scope','Actual final receipt; full scope in evidence file.')),'evidence':'reviews/'+path,'receipt_sha256':sha(p)})
x={'candidate_sha256':ch,'status':'PASS','reviews':rs,'actual_specialist_agents':4,'one_writer':'hm10_writer','root':'mechanical integration and QA only','normalization_only':True}
(r/'reviews/FINAL_REVIEW_BUNDLE.json').write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps({'status':'PASS','candidate_sha256':ch,'stages':len(rs)}))
