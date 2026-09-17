# RSE Recovery Index

Status: active recovery / continuity source
Last reconciled: 2026-09-17
Purpose: prevent already-created RSE work from being rediscovered, overwritten, silently downgraded, or lost when execution moves between ChatGPT chats, Library files, local Windows folders, Codex, and GitHub.

## Access / trust model

The Orchestrator must never assume that chat history is the durable source of truth. Recovery uses four evidence classes, in this order:

1. current repository files and validated branches / PRs,
2. owner-provided current manifests, checkpoints and source-manager files,
3. current Project / Library artifacts recovered from prior chats,
4. recalled chat context only when it does not conflict with files or repository state.

A recovered older brief remains useful as history, but it must not override a newer explicit manifest or locked repository file.

## Recovery labels

- `CANONICAL` - current source of truth. New work must follow it.
- `CURRENT_SUPPORT` - current supporting artifact, tool, test or evidence.
- `ARCHIVAL` - useful history/reference, not current product truth.
- `SUPERSEDED` - explicitly replaced by a newer source.
- `OWNER_GATE` - exists but cannot be promoted/replaced automatically.
- `LOCAL_ONLY` - confidential or machine-local source that must not be copied to cloud/GitHub.

---

## 1. RSE Core / Website / AI Discovery

Repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
Branch: `main`
Status: active.

### Preserve

- `RSE_AI_DISCOVERY_COMMERCE_IMPLEMENTATION_BRIEF_2026-09-16.md` - `CURRENT_SUPPORT`.
- AI Discovery production baseline already shipped through PRs #573, #575, #577, #579, #581 and #583.
- Current follow-up issue: #584 recrawl/index inspection.
- Android / Google Play is the current app direction. Old PWA/Paddle/SaaS/365-day-access language is `SUPERSEDED`.
- Seniors surface after Adults is already-settled behavior.

### Do not rediscover

- RSE Agency v2 already exists; do not rebuild the agent library.
- Do not generate more intent pages merely because generation is cheap; post-recrawl evidence must justify expansion.
- Do not invent Google Play URLs, prices, launch dates, identifiers or store badges.

---

## 2. Polish Localization Engine

Repository: `riseshineevolve-source/agency-agents`
Branch / PR: `rse/polish-localization-engine-v1`, draft PR #6.
Status: active calibration.

### Preserve

- pl-PL style guide and forbidden translationese / AI-ism library - `CANONICAL` for Polish voice.
- 12-gate localization QA pipeline - `CANONICAL`.
- Golden corpus: frozen published 244-page Happy Makers paperback - `CANONICAL` calibration source.
- `localization/pl-PL/golden-tests/published-book-calibration-v1.md` - `CANONICAL` regression set.
- Golden Calibration Round 1 defects and engine patches - `CURRENT_SUPPORT`.
- Golden Calibration Round 2 - PASS under patched rules.
- recurring-label glossary lock - `CANONICAL`; Dilo intentionally remains provisional until all uses are reconciled.

### Do not rediscover

- Do not translate all 244 pages until regression quality is stable.
- Do not localize changing website English before English freeze.
- Preserve meaning/claim strength before wit. Native Polish may restructure syntax but not silently change claims.

---

## 3. Happy Makers Detective Academy

Repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
Branch / PR: `feature/detective-book-factory`, draft PR #571.
Production area: `tools/detective-book-factory/`.
Status: active book production / map visual gate.

### Current source hierarchy

1. `content/spatial_source_manifest_final.yml` - `CANONICAL` production source selection.
2. `HMDA_checkpoint_19_HMDA20_UPGRADE.shigai.json` - `CANONICAL` native Shigai geometry / raw-board authority for selected cases.
3. `HMDA_SHIGAI_SOURCE_15_MODULES_FINAL.pdf` - `CURRENT_SUPPORT` visual/source export and solution-map evidence.
4. Book Factory editorial/content files - current English book production source.
5. hybrid pilot outputs and prior test-case PDFs - supporting visual evidence only.

### Recovered native source facts

The current checkpoint contains **20 unique Shigai candidate modules**, represented by 40 scene/clue pages. The 60-page PDF contains those 40 source pages plus 20 solution pages.

However, production is intentionally locked to **15 selected modules**, not all 20. This is explicit in `content/spatial_source_manifest_final.yml`. The remaining five checkpoint modules are backups/challengers and must not be silently promoted into the production source set.

Current selected-production checkpoint/PDF hashes:

- `HMDA_checkpoint_19_HMDA20_UPGRADE.shigai.json`
  - SHA-256 `cdc6de5b60117fe19e89fc4a13e2b9c1d92657f5e7fdb8ec69a18ae85ba8723e`
- `HMDA_SHIGAI_SOURCE_15_MODULES_FINAL.pdf`
  - SHA-256 `6662c292642f3d66148e41eef180bb7d2b15a0975ca822981f4f33aa7153aada`

The five checkpoint candidates excluded from the locked 15-source production manifest are:

- `The Secret Alarm Record and the Unclaimed Relic`
- `The Tiny Display Card and the Forgotten Relic`
- `The Secret Adventure for Lisa`
- `The Faint Velvet Thread and the Missing Treasure`
- `The Telltale Ledger Note and the Priceless Prize`

They are not deleted. They remain recovery/challenger assets.

### Recovered tools / work that must not be lost

- `render_book.py`
- `scripts/render_editorial_preview.py`
- `scripts/preflight.py`
- `scripts/build_spatial_map_pilot_manifest.py`
- `scripts/render_spatial_map.py` / validated code-drawn map fallback
- `scripts/render_spatial_map_hybrid.py`
- `scripts/validate_spatial_map_pilot.py`
- `scripts/validate_spatial_source_manifest.py`
- `content/spatial_source_manifest_final.yml`
- `content/spatial_map_pilots.yml`
- `content/spatial_room_skin.yml`
- `SPATIAL_SOURCE_LOCK.md`
- `EDITORIAL_LOCK_v4.md`

The HMDA_10 and HMDA_17 hybrid pilot is `CURRENT_SUPPORT` and already validated. It reuses original Shigai raster art byte-for-byte for the source image, wraps it in HMDA layout, and preserves geometry. Validation previously passed topology, constraints and unique-solution checks for both pilots.

Recovered Library artifacts include `HMDA_10_hybrid.pdf` and `Happy-Makers-Detective-Academy-Test-Cases.pdf`; these are evidence/reference artifacts, not replacements for the manifest/checkpoint.

### Current gate

- Hybrid/code-drawn visual standard remains owner-gated before mass conversion.
- Production renderer remains strict; editorial preview may use explicit missing-map placeholders.
- Do not change source geometry to make a page prettier.
- English master first; Polish only after English freeze.

---

## 4. Happy Me Adventures

Repository: `riseshineevolve-source/riseshineevolve`
Active branch: `mobile/mobile-first-rebuild`
Package: `com.riseshineevolve.happyme`
Issue: #15 custody audit / mobile rebuild completion.
Status: active Android release hardening.

### Preserve

- existing 200+ commit mobile rebuild - `CANONICAL`; do not restart from the empty similarly named repository.
- `MOBILE_RELEASE_READINESS_MATRIX.md` - `CANONICAL` current release control surface.
- Android/release/auth/privacy docs already in branch - `CURRENT_SUPPORT`.
- shared-device cache isolation hardening and invariant test - `CURRENT_SUPPORT`.
- offline queue mutation/revision design and its deterministic replay-safety test - `CURRENT_SUPPORT` once current CI is green.

### Known verified baseline

Recent Mobile Quality evidence has already verified typecheck, lint, production build, production dependency audit, Android project generation, release identity, API 36, production Supabase target, signing fail-closed behavior, debug APK and unsigned release AAB.

### Do not rediscover

- Do not revive old PWA/commercial assumptions.
- External dashboard/device gates must not be marked PASS from static source alone.
- Final store publication, price/commercial model and material child/parent scope changes remain owner gates.

---

## 5. Optical Animals

Authoritative code repository: `riseshineevolve-source/riseshineevolve`
Draft PR: #14 `Optical Animals: reusable book + seek-and-find creator`
Branch: `feat/optical-animals-book-creator`
Tool area: `tools/optical-book-creator/`.
Current local art source-manager root: `C:\Users\danie\Desktop\Asia\KDP\coloring\optical animals`.
Status: active visual curation + tool reconciliation.

### New source-manager bundle - current truth

Owner-provided bundle recovered 2026-09-17:

- `FINAL20_MANIFEST.json` - `CANONICAL` roster/status manifest.
- `README_FIRST.txt` - `CANONICAL` source-manager operating rule.
- `setup_optical_final.ps1` + `SETUP_OPTICAL_FINAL_FOLDERS.bat` - `CURRENT_SUPPORT` setup tooling.
- `promote_new_renders.ps1` + `PROMOTE_NEW_RENDERS.bat` - `CURRENT_SUPPORT` promotion tooling.

SHA-256 snapshots of the recovered source-manager files:

- `FINAL20_MANIFEST.json` `7fdcedea311fa10a6bf3df0c19e5c154fe8b1fae4c72a2d0050e767a0ba6a1c7`
- `setup_optical_final.ps1` `dee08430f79fcdbdcf8693c54a746a4382c26474c65a81e61d7f051141cfd48d`
- `promote_new_renders.ps1` `8fd2b6dd6152c7cc6ec4928a60ee7c66f52da4251a7207f62f49cb7515da85fb`
- `README_FIRST.txt` `1aa6b6fd76d21c6efb5b3d49203faee728eb222bb25438a704c8e47063902dc4`

### Canonical local folder contract

- `00_NEW_RENDERS_INBOX` - new candidate renders using canonical filenames.
- `01_FINAL_20_SOURCE` - **only input allowed for final book/PDF assembly**.
- `02_WORKING_CANDIDATES_20` - working current candidates.
- `99_ARCHIVE_REPLACED` - replaced final versions.

The source-manager setup copies byte-for-byte and does not delete or rewrite the historical `wszystkie` collection. Promotion archives an existing final, copies the new approved PNG byte-for-byte, moves the inbox copy to `_PROMOTED`, and warns below 2550x3300 px.

### Current roster state from FINAL20_MANIFEST

Approved (12):

1. fox
3. hummingbird
4. elephant
6. cockatoo
9. peacock
10. lion
11. heron
13. toucan
14. unicorn
15. cheetah
17. swan
19. decorative bird

Still owner-gated / unresolved (8):

- `02_zebra.png` - REDO
- `05_panda.png` - WAITING_NEW_APPROVED_FILE
- `07_tiger.png` - IMPROVE
- `08_giraffe.png` - IMPROVE
- `12_maned_wolf.png` - REPLACE old red panda
- `16_arabian_oryx.png` - REPLACE old duck
- `18_markhor.png` - REPLACE old chameleon
- `20_okapi.png` - REPLACE old `cos 1`

### Critical recovered conflict

PR #14 currently contains an older `config/final_20_selection.json` that still treats duck, red panda, chameleon and `cos 1`/owl as approved and tells the tool to use filenames from the local `wszystkie` folder.

That configuration is now `SUPERSEDED` by `FINAL20_MANIFEST.json` and the source-manager folder contract. It must be reconciled before any final PDF is generated.

### Preserve style sources

- latest Master Style Lock / coloring-surface rules - `CANONICAL` creative constraints.
- `MASTER ORNAMENT LOCK V2` / Signature Ornament Constellation rule - `CANONICAL`: 3-7 coordinated engraved/inlaid details, one hero ornament, different identity per animal, no sticker/crown/necklace treatment.
- historical `Optical_Animals_KDP_brief_i_prompty.docx` - `ARCHIVAL`; its older 30-animal / 82-page concept must not override current exactly-20 roster.

### Owner gate

No candidate image is promoted to FINAL merely because a matching file exists in Library. Visual approval remains owner-gated. Do not mass-regenerate or silently replace approved art.

---

## 6. Senior / Hello Today

Execution repository: `riseshineevolve-source/hello-today-android.`
Related repository: `riseshineevolve-source/Happy-Senior`.
Execution remains in dedicated chat/workstream; central Orchestrator tracks milestones only.

### Recovered implementation evidence

- JVM/unit tests, lint, debug APK and instrumented-test APK compilation were previously reported green.
- later device-accessibility work defines `Android Device Accessibility`, managed Pixel 6 API 36 + Pixel C API 36, with accessibility, large-font, touch-target, rapid-Next and repeated-Stop coverage.
- local/offline content direction and no hidden cloud dependency must be preserved unless deliberately changed in the dedicated Senior project.

Do not restart the Senior implementation from the small `Happy-Senior` repository merely because it is easier to inspect.

---

## 7. Mind Bloom Assistant

Repository: `riseshineevolve-source/mind-bloom-assistant`
Execution remains in dedicated project/chat.

### Recovered Phase 0 handoff

- security gate first, including stored-XSS remediation and separate environment-file handling.
- first recommended feature slice after security: Authenticated Universal Inbox v0.
- existing audit explicitly ended with `NO CODE CHANGED / NO COMMIT CREATED` for that snapshot.

Do not mistake the audit document for completed implementation. Central orchestration tracks milestone/blocker state only.

---

## 8. Opinie - local confidential workbench

Local root: `C:\Users\danie\AI_LOCAL\opinie`
Status: post-planning / pre-validated implementation.
Classification: `LOCAL_ONLY` for all real case/archive data.

### Preserve

- current `PROJECT_BRIEF.md` is decision handoff authority.
- original case material is primary forensic source.
- original ~40-year archive is historical-knowledge authority.
- derived summaries/embeddings/model outputs are never primary evidence.
- required workbench shape: case folder, evidence/provenance, timeline, scene/reconstruction structure, deterministic calculations, explicit variants, review queue.
- review actions: `APPROVE / POPRAW / SEARCH DEEPER / REJECT / PAUSE`.

### Never copy remotely

Confidential source documents, case facts, archive files, indexes/embeddings and real-case analyses must remain local/offline. GitHub may contain sanitized code and status metadata only.

---

## 9. Wave 2 / deferred apps - preserve, do not reactivate silently

Existing non-empty repositories recovered from GitHub:

- `happy-makers-quest`
- `family-mission-control`
- `unstoppable-me`
- `night-command`
- `family-hearth-stories`
- `spark-joy-fam`
- `neon-wonder-world` (commercial role still unclassified)

Small RSE gifts/tools also exist:

- `word-search-puzzle`
- `Happy-Makers-Calm-Wheel`
- `1-minute-challange`

These are real assets, not forgotten ideas. They remain outside current Wave 1 budget until explicitly promoted.

Additional support repositories recovered:

- `monochrome-map-master`
- `robot-voice-maker`

Do not delete or rebuild them merely because their relationship to a current product is not yet fully documented.

---

## Recovery invariants

1. Never treat an older chat summary as stronger evidence than a newer owner manifest or repository lock file.
2. Before rebuilding a tool, search GitHub + Library + current Project files for an existing implementation.
3. Before replacing a visual asset, check its canonical status and owner gate.
4. Before changing Detective geometry, validate against the locked Shigai source manifest/checkpoint.
5. Before building Optical PDFs, require `01_FINAL_20_SOURCE`; `wszystkie` is archive/candidate history, not production input.
6. Before changing Happy Me release state, update `MOBILE_RELEASE_READINESS_MATRIX.md` with reproducible evidence.
7. Senior and Mind Bloom execute in their dedicated workstreams; central orchestration does not duplicate implementation.
8. Opinie confidential data never enters remote tooling.
9. Every recovered-but-not-current artifact should be marked `ARCHIVAL` or `SUPERSEDED`, not deleted merely to make the workspace tidy.
10. Whenever a contradiction is found, record it here and resolve it against the strongest source before continuing execution.
