# RSE Product Asset Recovery Ledger

Status: active continuity ledger
Last reconciled: 2026-09-17

Purpose: distinguish a known RSE product/entity from an actually recovered production/master artifact. A website catalog record, a remembered project, and a final printable file are not interchangeable evidence.

## Evidence states

- `MASTER_RECOVERED` - concrete master/final artifact is accessible and identified.
- `PRODUCTION_SUPPORT_RECOVERED` - supporting build/test/source artifact is accessible, but not necessarily the final customer master.
- `CATALOG_CONFIRMED_MASTER_NOT_YET_RECOVERED` - product is confirmed in canonical RSE product inventory, but this recovery pass did not surface a unique final master file.
- `ARCHIVAL` - historical artifact, not current production truth.

## Books / printable products

### The Confident, Mindful & Happy Me Adventure book

State: `MASTER_RECOVERED`

Recovered Library file:
- `Paperback  final fixed print.pdf`

Role:
- frozen published English master,
- 244-page calibration corpus for the Polish Localization Engine.

Do not modify the English published master while using it for localization regression.

### Level Up Your Brain - World 01

State: `MASTER_RECOVERED`

Recovered Library file:
- `Paperback 10 STORIES WORLD 01 FINAL standard.pdf`

Recovered publication fact from the master:
- paperback ISBN: `9798247194682`

The master itself, not a website summary, is the stronger publication artifact for book-content facts.

### Level Up Your Brain - World 02

State: `CATALOG_CONFIRMED_MASTER_NOT_YET_RECOVERED`

The canonical RSE product inventory confirms the product, but the current Library recovery search did not surface a unique final/master filename. Do not infer its final PDF from World 01 or fabricate a path.

### 24 Gentle Steps to Christmas

State: `CATALOG_CONFIRMED_MASTER_NOT_YET_RECOVERED`

Canonical product naming is locked to `24 Gentle Steps to Christmas`; older/public generic labels such as `Christmas Family Book` are not the canonical product name.

The current recovery search did not surface a unique final/master file. Preserve the entity and continue looking when additional local/Library sources become available.

### Grandma Bibi / Grandma's Bibi Anti-Boredom Club

State: `CATALOG_CONFIRMED_MASTER_NOT_YET_RECOVERED`

Product/universe is confirmed in RSE product inventory. Final canonical project title and final master file must be recovered from stronger project/local evidence before any migration or republishing work.

### Happy Makers Detective Academy

State: `PRODUCTION_SUPPORT_RECOVERED`

Current source-of-truth lives in the Detective Book Factory and its locked Shigai source manifest/checkpoint. Recovered Library/support artifacts include:
- `Happy-Makers-Detective-Academy-Test-Cases.pdf`
- `HMDA_RECOVERY_11_CANDIDATES.zip`
- historical `HMDA_checkpoint_11.shigai.json`
- historical `HMDA_CHECKPOINT_STATUS.md`
- current uploaded `HMDA_checkpoint_19_HMDA20_UPGRADE.shigai.json`
- current uploaded `HMDA_SHIGAI_SOURCE_15_MODULES_FINAL.pdf`

The older recovery/test files are not allowed to override the current locked 15-module production manifest.

### Optical Animals

State: `PRODUCTION_SUPPORT_RECOVERED`

Recovered current source-manager bundle:
- `FINAL20_MANIFEST.json`
- `README_FIRST.txt`
- setup PowerShell/BAT
- promotion PowerShell/BAT

Recovered Library visual history includes:
- `Optical_Animals_20_page_preselection.pdf`
- historical `Optical_Animals_KDP_brief_i_prompty.docx`

Neither archival preselection nor old 30-animal brief may override the current exactly-20 owner manifest. Final production art must be promoted into `01_FINAL_20_SOURCE` before final assembly.

## Apps

### Happy Me Adventures

State: `PRODUCTION_SUPPORT_RECOVERED`

Canonical implementation is the substantial `mobile/mobile-first-rebuild` branch in `riseshineevolve-source/riseshineevolve`, not the empty similarly named repository. The release matrix, Android builds, state isolation and offline queue tests are repository-backed evidence.

### Senior / Hello Today

State: `PRODUCTION_SUPPORT_RECOVERED`

Canonical execution is in `riseshineevolve-source/hello-today-android.` with supporting project/chat reports. Recovered reports prove JVM/lint/debug/test-APK build work and define a managed-device accessibility gate, but compiling tests is not equivalent to completed real 90+ usability validation.

### Mind Bloom Assistant

State: `PRODUCTION_SUPPORT_RECOVERED`

Repository exists and Phase 0 audit/handoff was recovered. The audit explicitly stated `NO CODE CHANGED / NO COMMIT CREATED` for that audit snapshot, so it must never be misclassified as completed Inbox implementation.

### Project Unstoppable

State: `PRODUCTION_SUPPORT_RECOVERED`

Current public RSE site/product direction confirms the Android app is Coming Soon on Google Play. Existing Lovable/GitHub application assets are preserved in Wave 2. Do not confuse public Coming Soon copy with a completed Google Play release artifact.

## Recovery rule

A product is never dropped merely because a final master was not surfaced in one recovery pass. Conversely, a product is never marked release-ready merely because its entity exists on the website. Continue recovery from Project/Library/local/GitHub sources and promote evidence only when a concrete artifact is identified.
