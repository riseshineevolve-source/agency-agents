# Gentle Steps EN app — repair-head exact green checkpoint 12

Date: 2026-10-06
Status: repair HEAD fully green; Christmas Family V1 raw source bytes still gated; monitor/verification mode until source gate changes

## Exact app state
- repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
- branch: `gentle-steps/app-en-full24-purple-gold`
- exact HEAD: `98c351050ecc99b9d3a5674528fee1629ba3b738`
- HEAD message: `Revert corrupt Christmas Family runtime asset promotion`
- compare against this branch from the same SHA: identical / 0 ahead / 0 behind

## Exact-head CI
All push-triggered workflows for the repair HEAD are complete and green:
- Gentle Steps English App: run `37379079280` / #133 — SUCCESS
- Gentle Steps Android Build: run `37379079282` / #87 — SUCCESS
- SEO Validation: run `37379079286` / #1015 — SUCCESS

English App validation includes PASS for:
- full 24-day / 72-activity EN-only contract
- deterministic browser interaction smoke
- Home and all 24 direct day routes
- Family dialog exactly five Happy-Makers
- completion persistence + undo
- focus preservation after completion
- navigation scroll/focus reset
- Day 22 long-content scroll
- offline reload
- 320px and 768px horizontal-overflow guards
- no uncaught runtime exceptions

## Lighthouse exact-head evidence
Artifact:
- `11373510091` `lighthouse-results`
- digest: `sha256:02d96476a32b9866b742b1d914fe46b04d1d7f2ddecdc357ec71df4fc5626ec3`

Parsed exact reports:
- Home `/?preview=1`: Performance 100 / Accessibility 100 / Best Practices 100 / SEO 100
  - LCP 1.5 s (1532 ms)
  - TBT 0 ms
  - CLS 0
- Day 22 `/?preview=1&day=22`: Performance 100 / Accessibility 100 / Best Practices 100 / SEO 100
  - LCP 1.5 s (1452 ms)
  - TBT 0 ms
  - CLS 0

## Fresh visual proof
Artifact:
- `11372304951` `gentle-steps-en-full24-visual-v2`
- digest: `sha256:8a769a0735605f0ec084e2f19987af6df187725766db782e50fa2c273db4f1e5`

Fresh inspection:
- Home: no clipping/overflow, but family portrait set is still the stale casual/non-Christmas identity
- Family dialog: complete five-person rendering and readable layout, but still stale casual/non-Christmas identity
- Day 22/23/24 full-height proof: Family Connection and final completion actions are visible and unobstructed
- Day 24 correctly shows no Next action beyond the final day
- `brand-assets-preview-820x1150.png` still shows the quarantined empty cream-strip Christmas derivative and the current purple/gold icon + splash direction; the corrupt/empty derivative is not promoted into runtime

## Android exact-head evidence
Artifact:
- `11373640214` `gentle-steps-android-preplay-build`
- artifact ZIP digest: `sha256:9e3144848c496b682e3a26b7b3f2a74eb471fcae596cf1e70c82a609caa60004`
- debug APK SHA-256: `8e34c3d8991cd38a0ba4cf4b66e312c6d136040fd53f8763fba1bf9cb345b1ca`
- unsigned AAB SHA-256: `c72d4cc202fbfbc937f682082b7a46520a89dbe3a4aec552b8ccd7c686ce4718`
- SDK 36: PASS
- `lintDebug`: PASS
- debug APK: PASS
- unsigned release AAB: PASS
- local-notifications plugin present: `@capacitor/local-notifications@8.3.1`

Current Android branding source hashes recorded by CI:
- app icon source SHA-256: `a6cc004e117230326b796fa1a8c5fb75d7178dbcbd7afd097a8b68490899712b`
- adaptive foreground source SHA-256: `ba33efc187305db6f45ddeecbe0c695d1ba2715d135623192683a362cdc560d6`
- splash mark source SHA-256: `a4860eb56ad538e733ec37a168b0733a95c0a796125fa09d059696c7d068b5ad`

## Dependency audit
Exact-head Android job ran `npm audit --audit-level=high` successfully.
Current findings remain only 3 moderate transitive vulnerabilities in `uuid -> xcode -> @capacitor/cli`.
The offered fix requires breaking `npm audit fix --force`; it was not applied.

## SEO exact-head evidence
SEO Validation run `37379079286` / #1015 — SUCCESS.
- 1377 validation checks passed
- 117 SEO audit checks passed
- SEO status artifact `11372577317`, digest `sha256:0fbbc2b1c19b1dcea6a1a641d68bcd849ecbd6f88e8b13331f8490cfc81d4a50`
- SEO Lighthouse artifact `11372339737`, digest `sha256:6f5aed9510431b33ff1ea7acadabc31a6cc01656ec325b020265852723625c99`

## Christmas Family V1 source gate
Owner lock remains:
`gentle-steps-app/brand/concepts/HAPPY_MAKERS_CHRISTMAS_FAMILY_V1_LOCK.json`

Exact approved source remains:
- conversation/project file id: `file_00000000689881f4a1ed4b9ba414ce08`
- owner-approved cast: Mimi, Luli, Dilo, Alio, Nini
- no Grandma Bibi
- no Detective Academy / Room 0 universe

Fresh raw-file materialization attempt on 2026-10-06 still fails with:
`This Project file does not have an authorized raw-byte materialization path.`

Therefore:
- do not redraw
- do not reconstruct from preview pixels
- do not substitute lookalikes
- do not retry the previously corrupt/truncated runtime asset

## Readiness
READY FOR INTERNAL TESTING: NO.

Single material repo-side gap:
- obtain an authorized complete byte path for the exact owner-approved Christmas Family V1
- derive deterministic valid family/cameo WebP assets with recorded hashes
- wire Home / Family / daily note cameos
- refresh Home / Family / Day 01 / Day 12 / Day 22 / Day 23 / Day 24 + brand proof
- run exact-head CI again

Genuine owner/device/external gates:
- real-device Android smoke
- TalkBack / physical assistive-tech verification
- real local-notification delivery + tap + cold-start verification
- final package ID
- final production icon/splash approval
- signing
- Play Console / pricing / regions / monetization
- privacy / Data Safety / legal declarations
- Play upload/publication

## Next safe action
At the next run:
1. reconstruct exact branch HEAD and verify CI freshness;
2. retry only the authorized raw-byte path for the exact owner-approved Family V1 source;
3. if still gated, remain in verification mode and do not manufacture replacement art or speculative code.
