# Gentle Steps EN app — runtime closing checkpoint 02

Date: 2026-10-03
Authority: dedicated Gentle Steps execution lane
Status: MOBILE CACHE HARDENED / CALENDAR A11Y FIX COMMITTED / CHRISTMAS FAMILY V1 SOURCE BYTES VERIFIED / EXACT-HEAD CI RUNNING

## Source of truth

Execution bootstrap:
`orchestration/bootstrap/GENTLE_STEPS_EXECUTION_BOOTSTRAP.md`

App repository:
`riseshineevolve-source/RISE.SHINE.EVOLVE`

Branch:
`gentle-steps/app-en-full24-purple-gold`

Current HEAD:
`6ae46c35906158323c2a435f4954ab15bfc581c0`

Owner-approved Christmas family lock:
`gentle-steps-app/brand/concepts/HAPPY_MAKERS_CHRISTMAS_FAMILY_V1_LOCK.json`

## Durable work completed in this slice

Three bounded runtime hardening commits were created in order:

1. `7eba6f0112a0bf8bb022e5442c78f457a1098dd7` — `Harden Gentle Steps mobile cache and accessibility`
   - advanced PWA cache to `gentle-steps-en-full24-v7`;
   - runtime cache now writes only exact approved APP_SHELL URLs instead of every successful same-origin GET;
   - cross-origin requests remain ignored;
   - this prevents accidental persistence of legacy/heavy same-origin art if it is ever requested;
   - calendar button aria-label punctuation was simplified.

2. `ac7904eea865f79930b578a19d48c829706ff861` — `Keep consent policy compatible while retaining cache hardening`
   - the first hardening pass added a deferred analytics-consent include;
   - global SEO consent validation correctly rejected that form because the repository policy expects the canonical privacy-first include;
   - index + local validator were restored by blob identity while preserving the cache and app hardening;
   - no attempt was made to weaken the global consent validator.

3. `6ae46c35906158323c2a435f4954ab15bfc581c0` — `Fix Gentle Steps calendar accessible naming`
   - Lighthouse evidence showed the visible `1 / Open` text was still not contained in the explicit accessible name;
   - explicit calendar button aria-label override was removed;
   - a screen-reader-only `Day ` prefix was added so the computed control name becomes e.g. `Day 1 Open` while keeping visible `1 / Open`;
   - deterministic EN app validation now checks the spoken prefix and sr-only utility.

No final English content, Polish localization, pricing, legal state, package identity, signing, publication or central RSE priority was changed.

## Exact-head CI now running

For HEAD `6ae46c35906158323c2a435f4954ab15bfc581c0`:

- Gentle Steps English App: run `37155578470` — IN PROGRESS at checkpoint write.
- Gentle Steps Android Build: run `37155578417` — IN PROGRESS at checkpoint write.
- SEO Validation: run `37155578412` — IN PROGRESS at checkpoint write.

The immediately preceding exact source head `ac7904eea865f79930b578a19d48c829706ff861` already produced a successful Gentle Steps English App job and fresh visual/Lighthouse evidence. Current-head validation must supersede it before readiness status advances.

## Current visual evidence from immediately preceding source-equivalent UI

Visual proof artifact:
- `gentle-steps-en-full24-visual-v2`
- artifact id `11285675866`
- digest `sha256:1ec43337ac80069508b2ad01041909f85e3e4bf85eb389dc8584bf1a9eb58dc0`

Proof set includes:
- Home 390x844;
- Family 390x1000;
- Day 01 390x1200;
- Day 12 390x1200;
- Day 22 390x1600;
- Day 23 390x1600;
- Day 24 390x1200;
- brand-assets preview.

Observed:
- no obvious horizontal overflow or sticky-action obstruction;
- long-content Days 22/23 remain readable at the proof viewport;
- Day 24 remains readable;
- current proof still shows the pre-Christmas-V1 runtime character set and therefore is not final visual identity proof.

Lighthouse artifact:
- artifact id `11285790567`
- digest `sha256:f19794ef5014b957c6131da8d2f1b0ed7a8ae998988213cf64dab06fcca181bc`

Immediately preceding proof scores:
- Home: Performance 100 / Accessibility 100 / SEO 100 / Best Practices 96; LCP 1.7s, TBT 0ms, CLS 0.
- Day 22: Performance 100 / Accessibility 100 / SEO 100 / Best Practices 96; LCP 1.5s, TBT 0ms, CLS 0.

The home report specifically exposed:
- calendar label-content-name mismatch, addressed by current HEAD;
- favicon.ico 404, still open;
- analytics-consent request in the critical dependency tree, intentionally left canonical because consent policy takes precedence over local defer optimization.

## Owner-approved Christmas Family V1 source verified

The actual owner-approved conversation raster named in the lock was materialized successfully in this execution environment.

Source:
`świąteczny_portret_rodziny_w_fioletach_i_złocie.png`

Verified:
- dimensions: 1254x1254;
- SHA-256: `9d4ee560fffecdc30867cffb1aa60511f0242bdfb98990548ee7f948fbebda0d`;
- exact cast visible: Mimi, Luli, Alio, Nini, Dilo;
- no Grandma Bibi;
- no Detective Academy / Room 0 motifs.

Exact source-derived square crop mapping was tested locally without redraw:
- Mimi crop: (350,55)-(710,415), 192x192 WebP candidate SHA-256 `6fce57d6e6bb4e6503c4879c1e14c88678928e3b0ae5cdb865e48062eb7c5455`;
- Luli crop: (85,185)-(445,545), candidate SHA-256 `3f3fffdd1202478aadba80680d85e7c4ca9cf0da388c817845cf4e1f3e170f2a`;
- Alio crop: (90,535)-(470,915), candidate SHA-256 `2a105cfaca325ce1fe2f5368eb402e8599bd4820a5c29a3ca230fcfedbd7149c`;
- Nini crop: (430,560)-(810,940), candidate SHA-256 `da0bbbc689517203e4c7411de680e0731b26297477a9825d580e2c99674db14e`;
- Dilo crop: (795,430)-(1185,820), candidate SHA-256 `8fda988a4ad6fbe2024e9c88d63e188f26c30a59f88e37eb55855447358609ed`.

The derived crops were visually inspected and preserve the approved Christmas identities, including the younger purple-hoodie Alio and older purple-gold-jacket Dilo.

Binary promotion of those exact source-derived WebPs into `brand/generated/` is NOT yet committed. Current runtime generated assets therefore remain stale relative to Christmas Family V1. Do not claim final family visual identity until those bytes are promoted and a fresh Home/Family/day proof passes.

## Remaining safe repository-side work

1. wait for exact-head CI on `6ae46c...`;
2. inspect fresh Lighthouse and confirm label-content-name mismatch is gone;
3. promote exact source-derived Christmas Family V1 WebPs to runtime without redraw;
4. rerun Home / Family / Day 01 / 12 / 22 / 23 / 24 proof and reject any wrong identity/crop;
5. close favicon 404 with a valid small local icon asset without weakening analytics consent policy;
6. rerun dependency audit + Android lintDebug + debug APK + unsigned AAB;
7. prepare exact real-device/internal-testing smoke matrix.

## Readiness

READY FOR INTERNAL TESTING: NO at this checkpoint.

Blocking repository-side items:
- exact Christmas Family V1 runtime asset promotion;
- fresh exact-head visual proof after that promotion;
- current-head CI must complete green.

Owner/device/external gates remain:
- final package ID;
- final Play icon/splash choice;
- signing / Play App Signing;
- monetization/regions;
- Data Safety/privacy/legal declarations;
- physical-device notification/offline/progress/font-scaling/TalkBack smoke;
- Play upload/publication decision.
