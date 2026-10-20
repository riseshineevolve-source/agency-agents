# Book Factory — exclusive writer implementation checkpoint —20 October2026

## Authority and current truth

The owner explicitly transferred exclusive Book Factory/Detective product writing to codex_work_29b36a8d7861 in this conversation. Ownership commit2aa8adccfc2078aaa1c4b04cc9d4e0dd5030c82d is authoritative. Continue repairs, tests and full builds without asking for permission again. Other old writers must not overwrite this lane. No publication, KDP submission or main-product merge was requested.

Current status: implementation and real full225-page UI export work, but FINAL DELIVERY IS NOT COMPLETE. A verified content loss on folio143 still needs its final repair and rerun. The whole Work executor then disconnected: file operations and commands return409 environment_offline / Environment is not connected. This is an execution-environment blocker, not an owner gate or permission request.

Product branch feature/rse-book-factory-v2 remains observed c8046bf7dc435617e296936398c172a0a3ceb0f7. The newly recovered and repaired Python Studio source is currently LOCAL ONLY, not yet committed to that branch. Do not falsely describe a product implementation commit or packaged release as completed.

## Workspace and authoritative inputs

Workspace:/workspace/scratch/29b36a8d7861

Working package:book-factory/RSE_BOOK_FACTORY_CASE01
Original current code archive:current-source/RSE_BOOK_FACTORY_CASE01_SOURCE_MAP_AXES_FIXED_20261020.zip
Archive SHA256:7a509d15ae781c00523126fcee998e7d85a055de1390531b7c061931de6434d8

Inputs relative to workspace:
- production-inputs/HMDA_Book1_EN_Premium_V12_EXACT_TEXT.md
  SHA256 b39215cb5e26cfb53e624b01fe7e5913654645774fccde8c7ef46b12d5c4001e
- upload/dla codexa finalne grafiki (4).zip
  SHA256 daf0e1e82e4980ab0b73688f713d1602efb01cae93c3d8cfcc9a4b79658f4ba1
- upload/DETECTIVE_EN_SOURCE_VERIFIED_MAPS_OWNER_REVIEW(1).pdf
 225Letter pages;SHA25653c4c92bfff44bf38f30c014d746ce9b1ade472e7e78745d1e414e38c24d26fb
- production-inputs/DETECTIVE_ACADEMY_BOOK1_EN_RC23_OWNER_REVIEW.pdf
 225Letter pages;SHA25678f60c66e8adc236b44c6c8a2211cbf47f7d8064d4f4e4f850444

All original inputs remained unchanged in the verified completed run. The current PDF has flattened headers; original RC23 supplies authentic native witness facts and solved-map layers. Do not guess those from raster labels.

## What has actually been implemented locally

- Full production engine: rse_factory/full_gold_volume.py::production_build(reference_dir,canon_path,art_path,current_pdf,output_dir,source_pdf).
- Real /gold FastAPI interface for4inputs, immutable sessions, inputSHA, full build in background, status and current/result preview of any physicalfolio, PDF/QA/recipe download, restart/resume, concurrent-build409, result-tamper409 and code/input/reference fingerprint invalidation.
- Main generic studio still offers story/art/illustrated/calendar/style profiles. It is not proof of arbitrary-book perfection.
- Cache: source/code/font/reference/content-addressed leaf PDFs and whole output reuse. Atomic verified leaf write using tobytes, fsync, partial-to-final rename, receipt hash; zero-byte interrupted cache entries rerender. First debug assembly found7zero cache files, so this was repaired before the actual UI pass.
- Exact embedded Roboto Condensed regular/bold restored from currentPDF without network font install. requirements now matches actual PyMuPDF1.26.6 and Pillow12.3.0; FastAPI0.128.2/uvicorn0.48.0/python-multipart0.0.29 tested.
- Gold Case Files, circular undistorted official avatars, bounded two-line titles and unruled Notes.
- Native Witness Boards1–9clues: one equal14–12pt font, individual measured rows and blank Notes. Dense7–9clue variant removes redundant roster. ActualCase29 has9distinct14pt rows and57.63pt blankNotes; Case02 has6rows14pt and69.34pt Notes.
- CompactWitness seam cleaned by cropping sourceWitness ribbon635..724 instead of620..724.
- opening_family.py repairs Squad pages7/8: correct role portraits, no sticky/photo intersections, no oldDilo silhouette.8actual-art testsPASS and root independently viewed proofs.
- evidence_families.py whole-owner families:33(code05,one6-slot row),47(route08),51(four-zero-record09),59(timestamp11). No nested generic wrappers. Source masks and immutable image regions recorded;7testsPASS.
- editorial_reconciliation.py applies9audited derived-copy spans to exact originalV12, without modifying it. Case03 actualA017/B071 photos contradict old textual difference list; hints/solution/callbacks corrected using actual10objects. Original4plain0records remain4; Case05six-symbolcode remains separate.4testsPASS.
- Source axes preserved correctly for6x6/7x7/9x9; old spatial_map alternate no longer blindly adds6x6.
- render_solution_map now imports full native map panel (axes+107numbered markers across16maps), separate native occupant/coordinate roster, legible9.5pt compact legend. All16actual source pages verified,3testsPASS. Root viewed Gold180and224 proofs.
- PhotoA/B25/26 now sameGoldchrome with EXACT unchanged originalphoto assets, as opposed to older unrelated frame.
- Source-special boards88/122/126/130 now one authenticWitness header + tight complete source cards (no legacy outer-frame nesting), unruledNotes.
- Seven Witness pages whose “clues” were exact duplicates of their InvestigationRules (24,46,50,58,100,114,138) now preserve those rules once and provide a blankDETECTIVEWORKSPACE. No unique puzzle facts removed.
- rare_semantic_page SPECIAL_EVIDENCE fullimage panel on115 fixed: completeFOOTPRINT EVIDENCE, all4cards, originalFROM/TO response labels/guides.2testsPASS and visualproof viewed.
- Generic illustrated compile previously discarded _embed PPI/hash metadata. Repaired quickstart.py now records actual source image hash/fit/PPI and blocks strict print for ~50PPI; ≥300PPItestPASS.
- Current README.md, START_HERE_POLSKI.txt and START_FULL_BOOK_POLSKI.md describe full workflow,4inputs, output/download/cache/resume. SOURCE_LOCKS.json and.gitignore added. Source repo must not receive private inputPDF/art/manuscript/font/job/cache binaries. ReleaseZIP should include its3owner referencePNGmasters.
- CLI full_gold_volume.main now routes production_build, original legacy full_build remains compatibility API.

## Real HTTP end-to-end evidence, not a synthetic renderer test

Session:27a3702991a442f3
Session directory:book-factory/RSE_BOOK_FACTORY_CASE01/studio_jobs/gold_locked/27a3702991a442f3
Actual initial upload+preview used exact4files (~402MB), inputSHAallmatch, HTTP201/200;2.26s.

Actual fullUIrun (before last143fix):
book-factory/RSE_BOOK_FACTORY_CASE01/studio_jobs/gold_locked/27a3702991a442f3/production_results/DETECTIVE_ACADEMY_EN_38877457a762f1d2e854.pdf
97,733,779bytes;225Letter pages
SHA25614f7b2650f49204c87d24a723c0640e03c1e06364eda898502d62fc453d8f429
187rendered,38preserved,cache0 onfirstbuild.
RepeatPOST+fullPDFdownload PASS in0.764s: zeroadditionalproduction_build calls, cachedTrue, identicalSHA/bytes and outputmtime.

User-readable copy:
analysis/real-ui-build/20261020-200635/DETECTIVE_UI_FULL_225P.pdf
ActualHTTPevidence:
analysis/real-ui-build/20261020-200635/REAL_HTTP_FULL_BUILD_QA.json

Script:
analysis/run_real_ui_build.py --allow-build
Starts actualUvicorn+HTTPclient in one process/thread, uses saved session, waits, downloadsPDF/QA/recipe+previews, verifies all225leaf sizes, repeatscachedownload. This script wraps observer only; it DOES call the real renderer.

All-folio preflight on debug225:0nativeplaceholdermarkers,0out-of-trim text,0blankpages. Low-source-PPIhold remains; no invented300PPIclaim. Later UIrun report is alongside PDF; inspect that exact final candidate separately.

Browser screenshot end-to-end not proven: Chromium absent and officialdownloadtruncated. RealHTTP PASS is proven; do not label it visual-browserPASS.

## Tests and visual QA already completed

- UI11testsPASS before final attempted rerun lost executor; synthetic225fixtures and mock build cover session/cache/state/race, while actualfullHTTPabove covers real renderer.
- Owner-lock+Case02+nativepostflight23PASS, including actual9clues and actualofficial portraitSHA.
- Generic/support bounded groups:48PASS,2SKIP(outdated/mnt/data privatefixtures),0FAIL. Optionalopencv/pytesseract not installed/exercised.
- Semanticmapping6new+2legacyPASS.
- Source/editorial/solved-map owned groups13PASS after envpaths updated.
- Opening8actualartPASS; evidence7PASS; completeevidencepanel2PASS.
- JSsyntax and PythoncompilePASS.
- Do not add these overlapping groups into a fictitious uniquegrandtotal. One giant unittest discover earlier stopped midlog withoutsummary; do not claim an entirelygreenfullsuite.
- Root contacts1–40 and selectedfullpages; delegated contacts41–80,81–160,161–225 and enlarged proofs reviewed. No remaining obvious placeholder or textcollision in those snapshots.
- Final repaired variants rootviewed25,54,88,126,180,224 after additional fixes. Proof:analysis/final-variants-proof.pdf;PNGvariant-###.png.
- Fullbody sourcecoverage found true143loss, so visualcontactPASS was insufficient. Do not claim finalperfection or printapproval.

## Precise blocker remaining in source and minimal next repair

1. category in family_registry.py formerly classified nativeNARRATIVE143 asSPECIAL_EVIDENCE because the prose says “your verdicts”. Root ALREADY APPLIED explicitNARRATIVEinfirst8lines ->STORY_BRIDGE before broadbodyfallback. Confirm after runtime returns.
2. Agent preparing a full nativeNARRATIVEbody import in detective_native_production.py::rare_semantic_page. This runtimebranch WAS NOT APPLIED before environmentwentoffline. The agent cancelled a pending apply_patch that only targeted analysis/patch_native_story.py, not runtime. Check for this analysisfile onresume; do not assume the patch ran.
3. Add branch before “# Story bridges/physical indices/act interludes”:
   if any(line.strip().upper()=='NARRATIVE' for line in lines[:8]):
     clip=fitz.Rect(43,143,569,718)
     target=fitz.Rect(43,145,569,720)
     p.show_pdf_page(target,doc,folio-1,clip=clip,keep_proportion=True)
     return {'story_import':'COMPLETE_NATIVE_TEXT_VECTOR_AND_AVATARS','native_story_clip':list(clip),'story_target':list(target),'source_native_text_sha256':sha256(text.encode()).hexdigest(),'body_copy_reflowed':False}
   Validate all source body content lies within clip and failclosed if otherwise.
   This preserves exactsource text, speechcards,46sourceavatars/vectorobjects across15NARRATIVEfolios instead of flattening their readingorder.
4. The15sourceNARRATIVEfolios are34,35,52,80,81,102,120,140,141,142,143,144,145,146,147. Maxbodybottom691.45pt; lowestavatar663pt.143..718contains allbody, not sourcefooter. Per-page bodyavatarcounts2,2,0,0,0,0,5,0,8,9,5,0,5,4,6. Production34/35 customcanonicalfour-record bridge overrides rarebranch, so13actualleaves use newbranch.
5. New tests/test_native_story_source.py planned: syntheticinterleavedprose/speech/“yourverdict”/lowerparagraph preservewordsequence+avatar+vector; outofclipmusthold; envRSE_SOURCE_PDF all15source nativewordsequence+avatarcount/hash+vectors+sourceSHA.
6. Fix/confirm analysis/source_coverage_qa.py map duplicate methodology: show_pdf_page mapclip and rosterclip can expose two resource refs to same bitmap; require ≥1exactbitmaphash AND actual source axes match, retaining independent107marker/107occupantroster checks. Do not falsely require exactlyone image resource. Manualevidence33/47/51/59 and rasterfolios are already checked through exact unmaskedownerpixels+nativeoverlays/sourceSHA instead of demanding nativeOCR or stalegenericRC23labels. Verify latest saved script after resume.
7. analysis/pre-final-source-coverage.json contains46failures: true143nativebodyloss, plus then-unfixedmethodology above (manualrasterfolios,duplicateimage refs,oldgenericmanualevidencecopy). Canonical29story/allComms/objectives/rules/90hints/30solutions alreadyPASS. Do not claim this QAoverallPASS.
8. Re-run actualUIbuild after codefreeze (sourcefingerprint deliberately invalidates oldsessioncache on any.pychange), then secondcachedownload. Full.pyhashdependencies currently invalidate most185+pages for smallrendererchanges; safe~90s, not optimalfinegrainedinvalidations.
9. Run sourcecoverage on THAT exported finalPDF:
   python analysis/source_coverage_qa.py FINAL.pdf --build-report FINAL_BUILD_REPORT.json --out analysis/final-source-coverage.json
   Inspect all225contact and enlarged143+affectednativeNARRATIVEleaves,115,4specialboards,PhotoA/B,all16solvedmaps before finaldelivery.

## Persistence and delivery still outstanding

After runtime recovery:
- Commit current Python Studio source into EXISTING productbranch at tools/rse-book-factory-v2/studio/, preserve historicReact/v2 files. Update CODEX_CONTROL.md/CODEX_STATUS.md/CHECKPOINT.yml to current ownertransfer +225source/proof; oldRC24gate is superseded by explicitownerfeedback/transfer.
- Productbasec8046bf7...tree9a120dc018d5f4da737bfa21b23a6eff23f94e6c observed beforefailure. Re-readHEADand use expected_sha lease. No mainmerge.
- Source inventory saved analysis/git-source-inventory.json:82textsourcefiles~731KB. Exclude studio_jobs/runtime_fonts/privatePNGs/sourcePDFs fromGit. Include sourcehashlocks+hydrationREADME.
- Package usableStudioZIP with scripts+tests+3owner_case01_locked PNGs and currentinstructions; exclude402MBinputs/cache/jobs. ReleaseZIP not yet created.
- Save finalPDF (~98MB), toolZIP and optionally compactQAcontacts to persistentfiles. CurrentLibraryhelpers freshlyread in private-library-current/ include library_upload.py/library_hosted_apps.py/library_file_transfer.py. Required multiple/large prepared helper cannot run while executoroffline. No newfinalartifacts saved persistently this turn. Prior audit PDF is not the requestedtool/book and must not be redelivered as completion.
- Keep originalsources/previousPDFs intact. Generatedimageupscale is not a cure for sourcePPI. Do not labelKDP-ready without actualappropriateprintproof.
- Resume the work; no new ownerpermission for these repairs is needed. No need ask owner to relay messages or regrant writerownership.
