# Gentle Steps EN app — exact-head green + splash source history audit checkpoint 13

Date: 2026-10-06
Status: runtime/source exact-head green; Christmas Family runtime identity integrated; owner-approved city-family splash source remains unrecoverable from current durable sources.

## Exact app state
- repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
- branch: `gentle-steps/app-en-full24-purple-gold`
- exact HEAD: `9993837d35c8eecc49ab4e8eaff893358e21384e`
- HEAD message: `Gentle Steps: wait for lazy family portraits in smoke QA`

## Exact-head CI
All push workflows for this exact HEAD are complete and green:
- Gentle Steps English App: run `37499799411` / #157 — SUCCESS
- Gentle Steps Android Build: run `37499799392` / #111 — SUCCESS
- SEO Validation: run `37499799311` / #1065 — SUCCESS

Browser smoke artifact assertions PASS for:
- Home at 390px
- 24 Advent tiles
- Christmas Family V1 hero: exactly five Happy-Makers, portraits load
- Family dialog: exactly five Christmas cameos, verified Christmas portrait assets
- Day notes: Christmas character cameos
- completion persistence + undo + focus preservation
- all 24 direct day routes: 3 ordered activities, no horizontal overflow
- Day 24 shared Happy-Makers note: exactly five Christmas portraits, only approved Christmas portrait assets, no overflow
- Day 22 long content scroll
- offline reload
- 320px and 768px overflow guards
- no uncaught runtime exceptions

## Lighthouse exact-head evidence
Artifact:
- `11428603501` `lighthouse-results`
- digest: `sha256:969b40db241fb118ffd65757f4c9900d33a1d64aa8041ebf3abb56efe386bc8c`

Parsed reports:
- Home `/?preview=1`: Performance 100 / Accessibility 100 / Best Practices 100 / SEO 100
  - LCP 1531.5 ms
  - TBT 0 ms
  - CLS 0
- Day 22 `/?preview=1&day=22`: Performance 100 / Accessibility 100 / Best Practices 100 / SEO 100
  - LCP 1452.36 ms
  - TBT 0 ms
  - CLS 0
- Lighthouse assertion results: empty failure set

## Visual proof
Artifact:
- `11429581405` `gentle-steps-en-full24-visual-v2`
- digest: `sha256:6706c641c01bea50462443e3f1e53b4f1303f89152223c82a884a454f360bcdb`

Fresh inspection confirms:
- Home renders the five-person Christmas Family V1 cluster
- Family modal renders Mimi, Luli, Dilo, Alio, Nini in Christmas identity; no Grandma Bibi
- Day 24 shared Warm-Eve note shows the five-person Christmas mini-cameo
- Day 24 completion action is visible and unobstructed
- no Detective Academy / Room 0 visual motifs in these proof surfaces

## Android exact-head evidence
Artifact:
- `11429980178` `gentle-steps-android-preplay-build`
- artifact digest: `sha256:cacff813fb9ba446bfbc21e20306b5d58be0e35498932e895a8698c5fc5414e7`
- debug APK SHA-256: `9738d620d27448c77b9c36b6c4cbd854773b120b463dd35951882839a4ee6d42`
- unsigned AAB SHA-256: `68dc4368bf86b9a440bce70ca80328fc0e569f4be3e17d82b6a5d42eb56c7ed1`
- Android build: SUCCESS
- SDK 36 source ready
- lintDebug/build path: PASS
- local notifications plugin: `@capacitor/local-notifications@8.3.1`

Current native build metadata still marks package ID as `PROVISIONAL_PRE_PLAY`; no final package ID decision was made.

## Dependency audit
Exact-head Android run executed `npm audit --audit-level=high` successfully.
Remaining findings:
- 3 moderate transitive vulnerabilities in `uuid -> xcode -> @capacitor/cli`
- available npm fix requires breaking `--force`; not applied.

## Current runtime splash
Android artifact contains a deterministic purple/gold simplified city splash generated from validated mark assets.
Branding manifest status:
- `PROVISIONAL_INTERNAL_TEST_BRANDING`
- `splash_direction: OWNER_APPROVED_V2_CITY_SIMPLIFIED_RUNTIME`
- `final_owner_approval_required_before_play_creation: true`

Fresh visual inspection confirms the runtime splash is a purple/gold city/star mark, not the full owner-locked everyday-family/home-life cinematic splash.

## Owner-approved splash source history audit
Owner-approved reference metadata:
- `gentle-steps-app/brand/concepts/splash-v2-city-family.json`
- status: `OWNER_APPROVED_REFERENCE`
- source filename: `a_cozy_polished_festive_animated_3d_rendered_po.png`
- intended repo asset: `gentle-steps-app/brand/concepts/splash-v2-city-family.webp`

Git history proves the repo WebP has been truncated from its first commit:
- introduction commit: `a5124e021c605caa62d9d97907b7b120e7ebd0f5`
- commit date: 2026-10-02
- blob SHA: `2210680abddef5a751fb1b1084f9d1002263f908`
- blob size at introduction: 7,525 bytes
- there are no earlier revisions of this path in the branch history

Therefore there is no valid full splash raster recoverable from Git history.

Targeted Library/current-conversation search on 2026-10-06 found no exact source file named `a_cozy_polished_festive_animated_3d_rendered_po.png` and no exact `splash-v2-city-family` raster source.

## Christmas Family V1 exact source gate
Owner lock remains:
- generation id: `2b2548ee-8880-40ae-a66a-7605520e869f`
- exact project file id: `file_00000000689881f4a1ed4b9ba414ce08`
- cast: Mimi, Luli, Dilo, Alio, Nini
- no Grandma Bibi
- no Detective Academy / Room 0 universe

Fresh raw-byte materialization attempt on 2026-10-06 still fails:
`This Project file does not have an authorized raw-byte materialization path.`

Do not redraw, reconstruct from preview, or substitute a lookalike.

## Readiness
READY FOR INTERNAL TESTING: NO under the current strict owner-lock standard.

Runtime/app logic and CI are green. Remaining repo/visual gap:
- exact full owner-approved family/city/home-life splash source is not recoverable from repo history or current Library search
- current runtime splash remains the approved-direction simplified provisional city mark
- after exact source becomes available: derive production splash deterministically, record hashes, refresh brand proof and exact-head Android/English CI

Genuine owner/device/external gates:
- real-device Android smoke
- TalkBack / physical assistive-tech verification
- real local-notification permission/delivery/tap/cold-start verification
- final package ID owner decision
- final icon/splash approval
- signing
- Play Console / pricing / regions / monetization
- privacy / Data Safety / legal declarations
- Play upload/publication

## Next safe action
At the next run:
1. reconstruct exact branch HEAD and exact-head CI;
2. check whether a new durable exact splash source has appeared in repo/project/Library;
3. if not, remain in monitor/verification mode and repair only new regressions or materially stale evidence;
4. do not generate substitute family art or silently broaden scope.
