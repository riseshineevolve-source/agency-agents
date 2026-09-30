# Gentle Steps — Days 01–03 Advent app vertical slice owner gate

Date: 2026-09-30
Role: dedicated Gentle Steps execution owner
Status: BOUNDED SLICE COMPLETE / OWNER VISUAL + PL VOICE GATE

## Source / authority

Execution started from:
- `orchestration/bootstrap/GENTLE_STEPS_EXECUTION_BOOTSTRAP.md`

Owner-authorized active lane:
- EN + PL mobile Advent app conversion
- existing EN book/ebook remain existing commercial assets
- no central RSE priority mutation in this slice

Canonical published content source:
- `24 Gentle Paperback ok.pdf`
- real Days 01–03 verified against source pages 21–29 before implementation

Polish rule applied:
- previous close-translation/calibration copy treated as reference only
- app PL copy for Days 01–03 was newly re-authored for contemporary Polish family language
- no full 24-day PL scale-out should occur until owner calibrates this new voice

## Product implementation

Code repo:
`riseshineevolve-source/RISE.SHINE.EVOLVE`

Branch:
`gentle-steps/app-days01-03-vertical-slice`

Verified HEAD:
`96ed14da0cbe87f127d03e07c969d60b1558e96d`

Base main used for the slice:
`3beea54060bd22d1c289458558ec2fb1f33f0f83`

Implemented:
- 24-day Advent calendar shell
- Days 01–03 active with real source content
- day detail
- Mindful Moment / Fun Spark / Family Connection structure
- EN canonical copy
- pl-PL native re-authoring candidate
- EN/PL switch
- local completion/progress persistence
- offline-first service worker
- installable web-app manifest
- privacy-first analytics-consent integration required by the host repo
- mobile review deep links for deterministic proof rendering
- no account requirement
- no new backend
- no social feed
- no AI dependency

Optional reminders are intentionally deferred to the Android/native packaging slice rather than approximated with an unreliable web-only reminder.

## Automated verification

Gentle Steps Vertical Slice:
- workflow run: `36745782403`
- HEAD: `96ed14da0cbe87f127d03e07c969d60b1558e96d`
- conclusion: PASS

The contract validator checks:
- exactly Days 01–03 in this slice
- EN + pl-PL locale presence
- stable semantic section IDs across locales
- exactly 3 ritual sections per day
- complete section copy + Happy-Makers note
- 24-day shell
- localStorage progress
- no Supabase/Firebase/OpenAI app dependency
- offline service-worker registration/cache contract
- standalone PWA manifest

Host-repo SEO / privacy / AI-discovery validation:
- workflow run: `36745782275`
- HEAD: `96ed14da0cbe87f127d03e07c969d60b1558e96d`
- conclusion: PASS

## Visual evidence

Generated automatically from the exact verified branch HEAD in CI.

Artifact:
- run: `36745782403`
- artifact id: `11112880942`
- name: `gentle-steps-days01-03-mobile-review`

Screens:
1. `home-en-390x844.png`
   - viewport: 390 × 844
   - SHA-256: `421675e012c307ac724c71e1bcf6abc246d65ee96dfa4f3ad4e1e7098e6fa27c`
   - visual audit: PASS for hierarchy, touch sizing, calendar readability, progress clarity and premium seasonal direction

2. `day1-pl-390x1000.png`
   - viewport: 390 × 1000
   - SHA-256: `41ec110cb26cd8540a097cec9d1089da580d9752de40685292febe9cd4da3cf0`
   - visual audit: PASS for Polish body readability, section hierarchy, sticky completion action and mobile spacing

The current visuals are production-quality direction evidence, not final brand/publication approval.

## Remaining path to 24 days / Play-ready

After owner calibration of this slice:

1. map real EN content for Days 04–24 into the same stable content contract;
2. re-author Days 04–24 in native pl-PL using the approved voice, rather than translating sentence-by-sentence;
3. run full content/safety/consent QA across all 24 days;
4. verify 24-day mobile overflow/accessibility and offline content integrity;
5. package Android shell (Capacitor or equivalent minimal wrapper);
6. implement optional local reminder/notification without requiring an account/backend;
7. add final app icon, splash and Play Store package assets;
8. real-device test install, offline mode, persistence, notification permission and accessibility;
9. Play preflight;
10. explicit owner release/publication gate.

## Real owner gate

STOP HERE before scaling the Polish rewrite across Days 04–24.

Owner decision required on the representative real slice:
1. visual direction — does the warm wine / cream / evergreen premium Advent UI feel right?
2. Polish voice — does Days 01–03 now feel like an original contemporary Polish family product rather than translated/coaching copy?
3. provisional Polish product naming shown in the slice (`24 małe kroki do Świąt`) — keep, change, or leave English title for V1.

EN source mechanics and app architecture do not require a new owner decision at this gate.
