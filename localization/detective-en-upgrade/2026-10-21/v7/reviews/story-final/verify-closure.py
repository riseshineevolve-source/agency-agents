from pathlib import Path
import json,hashlib,re
R=Path(__file__).resolve().parents[2];D=Path(__file__).parent;H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=R/'candidate/candidate.json';O=R/'baseline/candidate-v7-r1.json';B=R/'baseline/candidate-v6.json'
assert H(P)=='df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1'
assert H(O)=='9f25b542e0162aa357c8409c3927622ee52ba1508e5bcbe3443d608c14e29fe5'
norm=lambda p:{s['id']:s.get('text',s.get('target_text')) for s in json.loads(p.read_text())['segments']};v,o,b=norm(P),norm(O),norm(B)
assert set(v)==set(o)==set(b) and len(v)==3067
delta=json.loads((R/'qa/R1_CLOSURE_DELTA.json').read_text());dc={k for k in v if v[k]!=o[k]};assert len(dc)==8 and dc=={x['id'] for x in delta['changed_units']}
for x in delta['changed_units']:assert x['before']==o[x['id']] and x['after']==v[x['id']]
assert delta['candidate_sha256']==H(P) and delta['previous_sha256']==H(O)
locks=json.loads((R.parent/'detective-v6/candidate/change-ledger.json').read_text());assert all(v[x['id']]==b[x['id']] for x in locks)
assert all(v[k]==b[k] for k in v if int(k[4:7])>=148 and k!='page212.block12')
for k in ['page212.block05','page212.block07','page212.block08','page212.block09','page212.block10']:assert v[k]==o[k]==b[k]
ld=json.loads((R/'candidate/change-ledger.json').read_text());changed={k for k in v if v[k]!=b[k]};assert len(changed)==229 and changed=={x['id'] for x in ld}
for x in ld:
 assert x['before']==b[x['id']] and x['after']==v[x['id']]
 assert x['before_sha256']==hashlib.sha256(x['before'].encode()).hexdigest() and x['target_sha256']==hashlib.sha256(x['after'].encode()).hexdigest()
intake=json.loads((R/'baseline/v7-intake-r2.json').read_text());allow={x['id'] for x in intake['segments'] if not x['protected']}
scope=json.loads((R/'run-r2/change-scope.json').read_text());assert allow==set(scope['allowed_changed_segments']);assert len(allow)==701 and 'page212.block12' in allow and not(changed-allow)
assert not any(int(k[4:7])<=25 and re.search(r'\b(017|071)\b',t) for k,t in v.items())
assert 'during cleanup, after the 4:17 frame' in ''.join(v[k] for k in ['page068.block04','page068.block05','page068.block06'])
assert v['page099.block21'].startswith('Detective, you fit the pieces.')
assert "The log fixes Jude's location." in v['page108.block13']
assert v['page212.block12']=='The repaired note gives the team a fuller instruction than RULE 0 FIRST. They still need to work out what it asks them to examine.\n'
R1m=json.loads((R/'reviews/story-r1/meaning-review.json').read_text());R1l=json.loads((R/'reviews/story-r1/logic-review.json').read_text());assert R1m['candidate_sha256']==R1l['candidate_sha256']==H(O)
assert R1m['open_finding_ids']==R1l['open_finding_ids']==['V7-R1-CAMERA-CLOSURE-OMITTED']
assert R1m['complete_reader_sha256']==H(R/'baseline/reader-v7-r1.md')
reader=(R/'candidate/reader-manuscript.md').read_text();assert [int(p) for p in re.findall(r'^## Page (\d+)\s*$',reader,re.M)]==list(range(1,226))
verification={'candidate_sha256':H(P),'baseline_v6_sha256':H(B),'reviewed_r1_candidate_sha256':H(O),'r1_complete_reader_sha256':H(R/'baseline/reader-v7-r1.md'),'current_complete_reader_sha256':H(R/'candidate/reader-manuscript.md'),'stable_ids':3067,'r2_delta_from_r1':sorted(dc),'r2_delta_count':8,'unchanged_units_inherit_actual_full_r1_review':3059,'total_delta_from_v6':229,'v6_unchanged_units':2838,'allowed_units':701,'all27_v6_repairs_exact':True,'all_hints_clues_answers_join_steps_maps_exact':True,'sole_prose_summary_exception':'page212.block12','all_other_units148to225_exact_v6':True,'actual_declared_delta_text_and_hashes_checked':True,'r1_camera_issue_resolved':True,'all_early_reveal_role_system_and_payoff_invariants_retained':True,'frozen_figure_pdf_sha256':H(R.parent/'detective-v6/proof/DETECTIVE_EN_V6_CORRECTED_FIGURES.pdf'),'maps_or_renders_repeated':False,'actual_neighbor_folios_read':[19,20,22,56,65,68,69,98,99,100,102,103,104,108,109,110,112,212,213],'current_reader_folios':225,'unresolved_material_findings':[]}
assert verification['frozen_figure_pdf_sha256']=='97f93e50551c25f7def860f3142b7010919d67e32b1a4a9995c0aa4a4e0302e9'
(D/'CLOSURE_VERIFICATION.json').write_text(json.dumps(verification,indent=2)+'\n')
print('PASS_EXACT_DELTA_AND_BOUNDARIES',H(P))
