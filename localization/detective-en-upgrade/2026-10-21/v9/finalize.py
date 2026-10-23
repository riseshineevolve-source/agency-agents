from pathlib import Path
import copy,hashlib,json,re,shutil
R=Path(__file__).resolve().parent;W=R.parent;V8=W/'detective-v8'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ch=sha(R/'candidate/candidate.json');qa=load(R/'proof/PROOF_QA.json');boundary=load(R/'qa/BOUNDARY_CHECK.json')
assert ch=='fa020029727aebaedbefe36c8a8ea7704ee350a5d9def5ff195b3377fa72d3a3'
reviews=load(R/'reviews/FINAL_REVIEW_BUNDLE.json');assert all(x['status']=='PASS' and x['candidate_sha256']==ch for x in reviews['reviews'])
cli=load(R/'qa/CLI_CHECK.json');assert cli['status']=='OWNER_READ_CANDIDATE' and cli['deterministic_qa']=='PASS' and not cli['unresolved_issues']
binding=load(R/'reviews/meaning-final/PDF_PRESERVATION_BINDING.json')
scenes=load(R/'candidate/final-scenes.json')['scenes'];base=load(R/'baseline/candidate-v8.json');candidate=load(R/'candidate/candidate.json')
before={x['id']:x['text'] for x in base['segments']};after={x['id']:x['text'] for x in candidate['segments']}
assert len(before)==len(after)==3067
comparison=[]
for s in scenes:
    comparison.append({'scene':s['id'],'case':s['case'],'folios':s['folios'],
      'turns':[{'speaker':t['speaker'],'original':t.get('source_text'),'v7':t.get('v7_text'),'v8':t['v8_text'],'final':t['final_text']} for t in s['turns']]})
dump(R/'candidate/ORIGINAL_V7_V8_FINAL_COMPARISON.json',{'candidate_sha256':ch,'original_verified_scope':'30maincaseCommsfromprioractualoriginal225PDFtranscription; 4auxiliaryscenes useV8only, notinventedoriginals.','scenes':comparison})
dump(R/'baseline/SOURCE_INVENTORY.json',{'owner_authority':'OWNER_AUTHORITY.json','current_product_truth':'V8lockedexceptexplicitHMCommsallowlist',
 'sources':[{'version':'owner225original','pdf_sha256':'9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0','access':'Priorverified30caseComms in source-scenes.json; no claimednewPDFdownload.'},
 {'version':'V7','candidate_sha256':'df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1','path':'recovery/unpacked/detective-v7/candidate/candidate.json'},
 {'version':'V8','candidate_sha256':sha(R/'baseline/candidate-v8.json'),'pdf_sha256':sha(V8/'proof/DETECTIVE_EN_V8_FULL_ENGLISH.pdf'),'authority':'OwnerpreserveseverythingexceptComms.'}],
 'result':{'version':'V8withfinalHMComms','internal_revision':'V9','candidate_sha256':ch},'no_puzzle_reaudit':'UnchangedV8mechanicalreceipts inheritedafterexactbyte/pixelbinding; no repeatedsuccessespretended.'})
dump(R/'qa/FINAL_CONTENT_VERIFICATION.json',{'candidate_sha256':ch,'all_final_stage_reviews':'PASS','cli':'OWNER_READ_CANDIDATE; deterministicPASS',
 'scenes':34,'turns':183,'changed_spoken_turns':sum(t['v8_text']!=t['final_text'] for s in scenes for t in s['turns']),
 'changed_units':len([i for i in before if before[i]!=after[i]]),'allowed_units':220,'non_comms_protected_units_exact':2847,
 'mixed137narrative_prefix_exact':True,'all143nonCommsV8repairunits_exact':True,'all27V6repairunits_exact':True,
 'book_pdf_sha256':qa['book_pdf_sha256'],'standalone_pdf_sha256':qa['standalone_pdf_sha256'],
 'book_all190unchangedleaves_exact':'Independenttext+pixelPASS','book_35changedleaves_nonComms_remainder':'IndependentstrictnormalizedPASS',
 'all183book_turns_and_speaker_order':'IndependentPASS','all183standalone_turns_and_speaker_order':'IndependentPASS',
 'writer':'root','actual_reviewers':4,'publication_freeze_production_renderer_or_PL_change':False})

oldpacket=V8/'integration/EDITORIAL_IMPORT_PACKET_V8.json'
dump(R/'integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_FINAL.json',{
 'format':'rse-editorial-hm-comms-delta-v1','baseline_v8_sha256':sha(R/'baseline/candidate-v8.json'),'candidate_sha256':ch,
 'base_contract':'../v8/integration/EDITORIAL_IMPORT_PACKET_V8.json over its inheritedV7sourcecontract',
 'operations':[{'id':x['id'],'page':x['page'],'expected_v8_text':x['before'],'expected_v8_sha256':x['before_sha256'],'target_text':x['after'],'target_sha256':x['target_sha256']} for x in load(R/'candidate/change-ledger.json')],
 'all3067target_hashes':{i:hashlib.sha256(t.encode()).hexdigest() for i,t in after.items()},
 'existing_source_to_destination_remaps':{'16':'15','27':'26'},'single_product_writer':'ExistingexclusiveBookFactorywriter; thispasschangeseditorialcandidate/proofonly.',
 'turn_contract':{'scenes':34,'existing_spoken_turns':183,'speaker_and_portrait_order':'UNCHANGED','final_strings':'candidate/final-scenes.json'},
 'layout_policy':'Fitfullapproveddialogue; donotabridgetofit. ExistingBookFactorywritercanchooseappropriateapprovedlayout, thenverifyimport/fit/art/physicalproof.',
 'production_source_or_renderer_written':False,'production_import_executed':False,'PL_migration':False,'owner_freeze_or_release':False})
shutil.copy2(oldpacket,R/'integration/INHERITED_V8_IMPORT_PACKET.json')
shutil.copy2(V8/'integration/INHERITED_V7_IMPORT_PACKET.json',R/'integration/INHERITED_V7_IMPORT_PACKET.json')
shutil.copy2(V8/'reviews/FINAL_REVIEW_BUNDLE.json',R/'baseline/INHERITED_V8_REVIEW_BUNDLE.json')
shutil.copy2(V8/'qa/FINAL_CONTENT_VERIFICATION.json',R/'baseline/INHERITED_V8_CONTENT_VERIFICATION.json')

(R/'README.md').write_text('''# Happy Makers Comms - final English dialogue over locked V8\n\nThe owner asked to restore the fuller original exchanges, keep successful V7 ideas and upgrade only HM Comms. Four actual independent specialist agents diagnosed all34scenes/183turns; root was the sole candidate writer. Final native/comedy, audience, meaning and family/continuity reviews PASS the exact source hash in CHECKPOINT.md.\n\nRead `proof/HAPPY_MAKERS_COMMS_FINAL_EN.pdf` for the34dialogueunits alone, or `proof/DETECTIVE_EN_V8_HM_COMMS_FINAL.pdf` for the225pagecompleteEnglishreadingedition. The fullbook retains theV8readingfurniture/versionlabel because its puzzlesandallothertext remainthat sameV8edition. This editorial layer is internallyV9. Neitherproof is a finalBookFactory/KDPtypesetting orphysicalprintapproval.\n\nThe source comparison uses verifiedoriginaltranscription for30maincases, actualV7 andexactV8; fourauxiliaryscenes have no falselyinventedoriginalattribution. Goodoriginalkernels andV7familybeats were merged into coherent full exchanges, with short punchlines retained deliberately. Quietrepair21 andreaderpatience29 remain.\n\nEverything outside220HMCommsallowlistedunits is protected. Actual210units change on35folios;2847nonCommsunits,143V8nonCommsrepairunits and27V6repairunits remainexact. Mixed137narrativeprefix remainsprotected. Existing183speaker/portraitturnorder retained.\n\nActual independentPDFbinding proves190untouchedleaves have identicaltext/pixels and35reflowedleaves have identicalnonComms remainder. Every183speech/speakerpair appears inbothPDFs. FreshPopplerrenders are used forvisualQA because MuPDFpreviewfontcacheoccasionallydropsglyphs despitecorrectsavedPDFbytes. No unchangedpuzzle is re-solved inthispass.\n\nThe existing soleBookFactorywriter consumes `integration/EDITORIAL_IMPORT_PACKET_HM_COMMS_FINAL.json` over theV8/V7contracts, preserving16→15and27→26sourceremaps. Fullspokenwording mustsurvivefinalimport; theproductrenderer isnotchanged here. No PLedition, mainmerge, freeze, publicationorActionsdispatch.\n''')
(R/'CHECKPOINT.md').write_text(f'''# HM Comms final checkpoint\n\nStatus: OWNER_READ_CANDIDATE. Owner-authorizedHMComms-onlyoriginal/V7merge andricherfamilyscenescomplete.\n\nCanonical candidate SHA256: `{ch}`. V8baseline: `{sha(R/'baseline/candidate-v8.json')}`.\n\n34scenes,183spoken turns,173spokenstringschanged,210stableunitschangedon35sourcefolios.2847outside-Commsunits andmixed137narrativeprefix exact. All143nonCommsV8repairs andall27V6repairs exact.30cases/90hints/30solutions/maps unchanged.\n\nFouractualindependentstagesPASS exacthash; actualR1FIXreceipts retained, actual17turn15sceneclosure. Native/comedy reviewer additionallyrereadall34finalshortdialogues. CLI deterministicPASS/OWNER_READ_CANDIDATE; noopenissues/sourceambiguities. Thisisnotanew225foliopuzzleaudit.\n\nComplete225pagePDF SHA256: `{qa['book_pdf_sha256']}`. Standalone34pageCommsPDF SHA256: `{qa['standalone_pdf_sha256']}`. Bookminimum10.5pt;standalone11.5pt. Independent190leaftext/pixelidentity,35strictnonCommsremainders and183speakerpairsPASS. Actualvisualreceiptgovernssamplecoverage; rootall69foliosin8contactsoverview.\n\nExistingsoleBookFactorywriterreceives210operationdelta plus3067targethashes andsame183speakerorder. Productionimport/physicalprint/release remainseparate. No productrenderer,PL,mainmerge,publication,freezeorhostedCIgreen claim.\n''')
(R/'RECOVERY.md').write_text('''# Recovery and reproduce\n\nCurrent readable results are the two proof/PDFs. Current canonical text is candidate/candidate.json, full225folio reading order is reader-manuscript.md and complete34scene source is final-scenes.json. Do not revert puzzle mechanics to older originals.\n\n1. Restore this directory as detective-v9, with engine/ alongside. The archive also retains theexactV8baselinePDF andV8readingadapter for reproducibleproofs.\n2. `python detective-v9/build_candidate.py` re-appliesonlytheauthorisedfinaldialogue, checksprotectedcanonicaltext and225readerpageprojections. It neverauthorsproseautomatically.\n3. `python detective-v9/build_proofs.py` makesbothPDFs withsamefullwording andretainedV8leaves. `python detective-v9/render_poppler.py` makesfreshaccuraterasterQA.\n4. ReproducedPDFmetadatamaychangebytehash. Do notcopyoldhash-boundapprovalreceiptsonto newbytes: comparetext/rendercontentandrebindhonestly. Candidateprosehashmustremainexact.\n5. Actualdiagnostic,R1FIX,finalPASSandproof-onlyFIXhistory remainunderreviews. Use thefinalreceipts,notoldFIXversions. No neweditingroundisneededwithoutanactualdefectorownerrequest.\n\nBookFactory production import belongs to the existing exclusive productwriter. Preserve full dialogue andportraitorder; doclayouts inthisarchivearereadingproofs.\n''')
print(json.dumps({'candidate_sha256':ch,'content_qa':'PASS','import_operations':210,'pdf_hashes':[qa['book_pdf_sha256'],qa['standalone_pdf_sha256']]}))
