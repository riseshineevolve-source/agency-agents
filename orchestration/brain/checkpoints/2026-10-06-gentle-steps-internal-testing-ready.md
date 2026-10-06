# Gentle Steps — repository-side internal testing handoff

Date: 2026-10-06
Role: dedicated Gentle Steps execution owner
Central RSE priority mutation: NONE

## Validated application truth

Repository:
`riseshineevolve-source/RISE.SHINE.EVOLVE`

Branch:
`gentle-steps/app-en-full24-purple-gold`

Exact validated application HEAD:
`86a20876c5b5d706ac5c2042d39e1f7f830d82fa`

## Exact-head CI

- Gentle Steps English App #155 — PASS
- Gentle Steps Android Build #109 — PASS
- SEO/privacy/Lighthouse #1063 — PASS

## Multi-agent QA board applied

- Accessibility Auditor
- Test Automation Engineer
- Performance Benchmarker
- Engineering Code Reviewer
- Privacy Engineer
- Application Security Engineer
- Mobile Release Engineer
- UI Finish-Gate Reviewer
- Reality Checker
- Evidence Collector / Test Results Analyzer

## Repository-side verdict

**READY FOR INTERNAL TESTING: YES**

**PRODUCTION / GOOGLE PLAY RELEASE: HOLD**

The app is ready for a real-device internal smoke test. This is not a production certification.

## Closed in the current slice

- English 24-day / 72-activity source contract retained.
- Owner-approved Christmas Happy-Makers identity is now active throughout runtime using the verified five Christmas portraits derived from the locked Christmas Family V1 source:
  - Mimi
  - Luli
  - Dilo
  - Alio
  - Nini
- No Grandma Bibi.
- No Detective Academy / Room 0 imagery or language.
- Home uses exactly five Christmas Happy-Makers.
- Family dialog uses exactly five Christmas profiles/cameos.
- Daily Happy-Makers notes use the verified Christmas portraits.
- Dilo and Alio remain distinct.
- Main app shell is no longer one giant live region.
- Calendar/day/next/previous navigation resets scroll and moves focus to the day heading.
- Completion re-render restores focus to the completion action.
- Deterministic browser smoke covers all 24 days.
- Completion save, reload persistence and undo pass.
- Offline service-worker reload passes.
- 320px / 390px / 768px no-horizontal-overflow checks pass.
- No uncaught runtime exceptions in smoke.
- Advent boundary tests pass for Nov 30, Dec 1, Dec 12, Dec 24 and Dec 31.
- Android lintDebug and release lint vital pass.
- Debug APK and unsigned AAB produced.
- Dedicated Gentle Steps Lighthouse remains green after Christmas visual integration.

## Evidence

Visual artifact:
- workflow run #155
- artifact ID `11415352340`
- name `gentle-steps-en-full24-visual-v2`

Lighthouse artifact:
- workflow run #155
- artifact ID `11415937889`

Android artifact:
- workflow run #109
- artifact ID `11415422497`
- name `gentle-steps-android-preplay-build`

Build hashes:
- APK `8ed5cebe30ac075126f6acd9c2e2c19d881f3aa6e22d92644db8f5a4bbae0156`
- AAB `3d05b50b9b685c4ee612e292e38b7554cc52f58f005be733f9af0c1c8240bf18`

## Current non-blocking watches

1. `npm audit --audit-level=high` passes, but npm reports 3 moderate `uuid` advisories via `xcode -> @capacitor/cli`. Do not force-fix across Capacitor versions without compatibility evidence.
2. Android npm dependencies are version-pinned in package.json but no committed package-lock is present yet; use a deliberate compatibility/reproducibility slice before final Play release.
3. Current Advent behavior is annual: locked Jan-Nov, unlocks day-by-day Dec 1-24, all open Dec 25-31, then resets for the next Advent season.
4. Package ID / branding metadata remain explicitly provisional pre-Play.

## Real-device gate

Required next evidence:
1. install exact validated debug APK;
2. verify icon and splash;
3. verify Home / Family / five Christmas Happy-Makers;
4. inspect several normal days plus Days 22-24;
5. mark complete -> kill app -> reopen -> verify persistence;
6. airplane-mode reopen;
7. notification permission + actual scheduled delivery + notification tap opens correct day;
8. increase Android system font one step and inspect layout;
9. short TalkBack navigation pass.

## Owner / external release gates after device PASS

- final package ID decision;
- upload signing / Play App Signing;
- Play Console creation;
- Data Safety / Families / privacy/legal declarations;
- listing/regions/pricing;
- publication.

Do not merge main, publish, sign, spend money or cross Play/legal gates automatically.
