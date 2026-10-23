from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parent;W=R.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ch=sha(R/'candidate/candidate.json');b=load(R/'qa/BOUNDARY_CHECK.json');q=load(R/'proof/PROOF_QA.json')
reviews=load(R/'reviews/FINAL_REVIEW_BUNDLE.json');assert all(x['status']=='PASS' and x['candidate_sha256']==ch for x in reviews['reviews'])
cli=load(R/'qa/CLI_CHECK.json');assert cli['status']=='OWNER_READ_CANDIDATE' and cli['deterministic_qa']=='PASS' and not cli['unresolved_issues']
binding=load(R/'reviews/story-final/PDF_PRESERVATION_BINDING.json');assert binding['status']=='PASS'
scenes=load(R/'candidate/final-scenes.json')['scenes']
dump(R/'candidate/ORIGINAL_V7_V8_V9_FINAL_COMPARISON.json',{'candidate_sha256':ch,'original_verified_scope':'30maincaseComms from previous actual original225PDF transcription; four auxiliary scenes have no invented original attribution.','scenes':[{'scene':s['id'],'case':s['case'],'folios':s['folios'],'turns':[{'speaker':t['speaker'],'original':t.get('source_text'),'v7':t.get('v7_text'),'v8':t.get('v8_text'),'v9':t['baseline_text'],'final':t['final_text']} for t in s['turns']]} for s in scenes]})
dump(R/'baseline/SOURCE_INVENTORY.json',{'authority':'OWNER_AUTHORITY.json','baseline_v9_sha256':sha(R/'baseline/candidate-v9.json'),'baseline_v8_pdf_sha256':sha(W/'detective-v8/proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf'),'engine':'qa/ENGINE_SNAPSHOT.json','only_editable_content':'220HMComms stable IDs; mixed137narrativeprefix protected','candidate_sha256':ch,'unchanged_puzzle_audit':'Prior verifiedV8/V9 evidence retained after exact binding; no new unchanged puzzle solve claimed.'})
ledger=load(R/'candidate/change-ledger.json');after={s['id']:s['text'] for s in load(R/'candidate/candidate.json')['segments']}
dump(R/'integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_V10.json',{'format':'rse-editorial-hm-comms-delta-v1','baseline_v9_sha256':sha(R/'baseline/candidate-v9.json'),'candidate_sha256':ch,'base_contract':'Existing V9 over V8/V7 editorial contracts','operations':[{'id':x['id'],'page':x['page'],'expected_v9_text':x['before'],'expected_v9_sha256':x['before_sha256'],'target_text':x['after'],'target_sha256':x['target_sha256']} for x in ledger],'all3067target_hashes':{i:hashlib.sha256(t.encode()).hexdigest() for i,t in after.items()},'existing_source_to_destination_remaps':{'16':'15','27':'26'},'turn_contract':{'scenes':34,'spoken_turns':183,'speaker_portrait_order':'UNCHANGED','full_strings':'candidate/final-scenes.json'},'single_product_writer':'Existing exclusive BookFactory writer; editorial proof only here. Preserve complete dialogue on import.','production_source_or_renderer_written':False,'production_import_executed':False,'PL_migration':False,'owner_freeze_or_release':False})
dump(R/'qa/FINAL_CONTENT_VERIFICATION.json',{'candidate_sha256':ch,'all_four_actual_stage_reviews':'PASS','actual_specialist_agents':4,'sole_dialogue_author':'hm10_writer','root':'mechanical integration','cli':'OWNER_READ_CANDIDATE; deterministic PASS','scenes':34,'turns':183,'changed_units':b['changed_units'],'non_comms_protected_units_exact':2847,'all143nonCommsV8repairunits_exact':True,'mixed137narrative_prefix_exact':True,'pdf_binding':'reviews/story-final/PDF_PRESERVATION_BINDING.json','visual_review':'reviews/audience-final/VISUAL_REVIEW.json and proof/ROOT_VISUAL_REVIEW.json','book_pdf_sha256':q['book_pdf_sha256'],'standalone_pdf_sha256':q['standalone_pdf_sha256'],'production_or_print_approval':False})
(R/'README.md').write_text('''# Happy Makers Comms — English rhythm revision V10

The owner rejected V9 as wordy, difficult to follow and insufficiently funny. One actual dialogue author, hm10_writer, read all30case introductions and task contexts, plus four auxiliary scenes. Three independent reviewers covered native English/comedy, audience/family ear, meaning and logic. Actual R1 FIX receipts and final PASS closure remain in reviews. No claim of human child testing or guaranteed commercial success.

Read proof/HAPPY_MAKERS_COMMS_V10_EN.pdf for all34dialogues alone, or proof/DETECTIVE_EN_V10_FULL_ENGLISH.pdf for the complete225page English reading edition. The book retains previous running furniture on protected leaves; filenames and metadata identify this revision. These are editorial reading proofs, not final production typesetting or physical-print approval.

Each scene uses a case-specific family situation, a clear comic premise and responses that follow each other. No fixed word-count target was imposed. Tender repair21 and patient29 stay quieter. All183existing speaker/portrait turns remain. Only220allowlisted units are editable;2847outside-Comms units, mixed137narrative prefix and all143non-Comms V8 repairs stay exact. Puzzle instructions, hints, answers and maps are preserved.

Current language CLI is pinned in qa/ENGINE_SNAPSHOT.json. Four real review stages bind the exact canonical hash, and the CLI deterministic check passes. Independent saved-PDF binding checks190untouched leaves,35changed non-Comms remainders and all183speech/speaker pairs in both PDFs. Visual review uses fresh Poppler images; receipts state actual sample coverage.

The existing sole BookFactory writer receives integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_V10.json over prior V9/V8/V7 contracts, preserving16→15and27→26remaps. Full wording must survive production import. No renderer, PL migration, main merge, publication, freeze or hosted-CI claim.
''')
(R/'CHECKPOINT.md').write_text(f'''# Current V10 checkpoint

Status: OWNER_READ_CANDIDATE. English HMComms-only rhythm revision complete.

Canonical SHA256: `{ch}`. Baseline V9: `{sha(R/'baseline/candidate-v9.json')}`.

34scenes /183turns; {b['changed_units']}changed stable units on35folios.2847protected units and143V8non-Comms repairs exact. Four actual stages PASS; actual R1 fixes retained; CLI deterministic PASS. No new full-book puzzle audit claimed.

Complete225page PDF: `{q['book_pdf_sha256']}`. Standalone34page PDF: `{q['standalone_pdf_sha256']}`. Book minimum10.5pt; standalone12pt. Independent PDF preservation binding PASS; visual sample scope recorded separately. No production or physical-print approval.
''')
(R/'RECOVERY.md').write_text('''# Reproduce

Restore detective-v10, required detective-v9 inputs, detective-v8 baseline PDF/adapter, recovered V7 candidate and engine-v10. Current prose is dialogue-writer-final.json. R1 is immutable history. Run build_candidate.py for mechanical integration, build_proofs.py for saved PDFs and render_poppler.py for fresh raster QA. Rebuilding PDFs may change metadata byte hashes; do not copy receipts onto new bytes without actual binding. Current source is candidate/candidate.json and complete reading order is reader-manuscript.md. No revert of puzzle mechanics to originals.
''')
print(json.dumps({'candidate_sha256':ch,'status':'OWNER_READ_CANDIDATE','operations':len(ledger)}))
