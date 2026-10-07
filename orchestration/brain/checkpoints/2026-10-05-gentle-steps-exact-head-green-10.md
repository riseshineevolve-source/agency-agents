# Gentle Steps EN app — exact-head green + browser smoke checkpoint 10

Date: 2026-10-05
Status: exact-head green; accessibility/browser-smoke closing slice verified; exact Christmas Family V1 source remains raw-byte gated

## Exact app state
- repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
- branch: `gentle-steps/app-en-full24-purple-gold`
- exact HEAD: `192fd304b59232b2bc48deb4babd9e89d6da032b`
- HEAD message: `Test Gentle Steps Advent date-lock boundaries`
- compared with prior checkpoint baseline `444d619c43ccd73472109991bc1ecbd3fb0f4b01`: current branch is 11 commits ahead / 0 behind

## Material repository-side progress since checkpoint 09
- Deterministic browser interaction smoke suite is now committed and runs in Gentle Steps CI.
- Critical browser journeys verified on exact HEAD:
  - Home renders 24 Advent day tiles without horizontal overflow.
  - Family dialog opens/closes and contains exactly five Happy-Makers profiles.
  - Calendar -> day navigation resets scroll to top.
  - Day 01 renders all three ordered activities without horizontal overflow.
  - completion action preserves focus, persists locally across reload, and undo persists.
  - previous/next navigation works and starts at top.
  - all 24 direct day routes render three ordered activities without horizontal overflow.
  - long Day 22 renders and scrolls correctly.
  - Family review deep link works.
  - cached Home/content survive deterministic offline reload.
  - 320px and 768px resilience checks pass.
  - no uncaught runtime exceptions.
- Accessibility source fixes are present:
  - the whole app is no longer a polite live region; the dedicated toast remains `role=status aria-live=polite`;
  - day navigation explicitly scrolls to top and transfers focus to the primary heading;
  - completion rerender restores focus to the completion control.
- Advent boundary regression tests are committed and PASS:
  - Nov 30 locked;
  - Dec 1 unlocks Day 1 only;
  - Dec 12 unlocks through Day 12;
  - Dec 24 unlocks Day 24;
  - Dec 31 remains fully available.
- Test-only preview guard remains constrained to loopback/non-native runtime.

## Exact-head CI
All three workflows for `192fd304b59232b2bc48deb4babd9e89d6da032b` are completed SUCCESS:
- Gentle Steps Android Build run `37370754649` / #85
- Gentle Steps English App run `37370754677` / #131
- SEO Validation run `37370754724` / #1013 (final attempt successful)

### Gentle Steps English App evidence
- visual proof artifact `11370892003`
  - digest `sha256:5d07994cd3ee4f6f1551c3b95ec4e04de2530aed6604f2c127fa706f839796b7`
  - non-expired
- dedicated Lighthouse artifact `11370496995`
  - digest `sha256:c2404d249c2ef70d725d8a81d13342b49511fdc93fcab2ceadc00ef5c476ea19`
  - non-expired
- Home: Performance 100 / Accessibility 100 / Best Practices 100 / SEO 100
  - FCP ~1.0 s; LCP ~1.5 s; TBT 0 ms; CLS 0; Speed Index ~1.0 s
- Day 22: Performance 100 / Accessibility 100 / Best Practices 100 / SEO 100
  - FCP ~0.9 s; LCP ~1.5 s; TBT 0 ms; CLS 0; Speed Index ~0.9 s

### Android evidence
- artifact `11370701293` (`gentle-steps-android-preplay-build`)
  - digest `sha256:15cd1c33b24fe2122ad18b592cea76b695d853c6cf1ef7f080b96fd6f82eb4ca`
  - non-expired
- SDK 36 setup PASS
- `lintDebug` PASS
- release lint vital PASS
- debug APK PASS
  - SHA-256 `74448fdf75499a8ac95e7715b3713f012b6aeca0dc219aeac0847d9c0a4d155a`
- unsigned release AAB PASS
  - SHA-256 `c72d4cc202fbfbc937f682082b7a46520a89dbe3a4aec552b8ccd7c686ce4718`
- native `npm audit --audit-level=high` gate PASS
  - 3 moderate transitive findings remain in the Capacitor toolchain; available automatic fix is breaking/force and was not applied
- Android branding remains explicitly `PROVISIONAL_INTERNAL_TEST_BRANDING`; no package/signing/store decisions were changed.

### SEO evidence
- final exact-head run `37370754724`: SUCCESS
- SEO status artifact `11370653252`
  - digest `sha256:0c536a424e10feb87c01054b6d81e05700d3658db9163986d7376e11497fe895`
- main-site Lighthouse artifact `11370713409`
  - digest `sha256:e780856cee9a03023cd937deb56f75a8726ee0963e51ee4fc1a01f525a909a7e`
- SEO validation: 1377 checks PASS
- SEO audit: 117 checks PASS

## Christmas Family V1 production gate
Owner lock remains:
- `gentle-steps-app/brand/concepts/HAPPY_MAKERS_CHRISTMAS_FAMILY_V1_LOCK.json`
- source file id: `file_00000000689881f4a1ed4b9ba414ce08`
- cast: Mimi, Luli, Dilo, Alio, Nini only

The exact source is now durably enumerated in Library:
- file: `Świąteczny portret rodziny w fioletach i złocie.png`
- Library path: `/AI AGENTS/Świąteczny portret rodziny w fioletach i złocie.png`
- library file id: `libfile_4635ff872ea88191a81b8dcec725bbf9`
- size: 2,683,485 bytes

However, fresh raw-file materialization of the exact file id still fails with:
- `This Project file does not have an authorized raw-byte materialization path.`

Therefore:
- do not redraw;
- do not reconstruct from preview pixels;
- do not substitute a generated lookalike;
- keep the current `happy-makers-christmas-v1.webp` derivative quarantined because prior exact-browser evidence showed it as an empty cream strip.

Fresh exact-head visual proof confirms Home and Family still show the older casual/non-Christmas portrait set. The main visual gap is therefore real and unchanged.

## Readiness
READY FOR INTERNAL TESTING: NO.

Remaining material repository-side gap:
- lossless promotion of the exact owner-approved Christmas Family V1 into Home / Family / daily cameos, followed by fresh identity proof and exact-head CI.

Non-blocking/toolchain hardening still tracked:
- Android npm dependency lock/reproducibility can be tightened before Play release if not already supplied by a later commit.
- three moderate native-toolchain audit findings remain; do not use `npm audit fix --force` without a bounded Capacitor-compatible upgrade.

## Genuine owner/device/external gates
- real-device Android smoke
- TalkBack / physical assistive-technology testing
- real notification delivery + tap + cold-start verification
- final package ID
- final production icon/splash owner approval
- signing
- Play Console / regions / monetization decisions
- privacy / Data Safety / legal declarations
- Play upload / publication

## Next safe action
On the next run:
1. reconstruct exact current HEAD first and accept later GitHub truth over this checkpoint;
2. retry only the authorized raw-byte path for the exact approved Christmas Family source or use a newly appearing durable owner-approved source;
3. if source bytes remain gated and HEAD is unchanged/green, stay in verification mode and do not manufacture replacement visual work.
