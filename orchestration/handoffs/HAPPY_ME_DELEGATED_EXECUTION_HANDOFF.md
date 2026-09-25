# RSE Delegated Execution Handoff — Happy Me Adventures

Status: ACTIVE DELEGATED EXECUTION OWNER
Updated: 2026-09-25
Central authority: RSE Technical Orchestrator / `orchestration/brain/RSE_BRAIN_MASTER.md`

## Ownership

This delegated execution lane owns **Happy Me Adventures only**.

It may:
- inspect and change Happy Me source on its dedicated task branch;
- use Codex for bounded implementation;
- run tests and CI;
- create project-specific checkpoints;
- prepare Google Play/internal-test readiness;
- push its dedicated task branch after green verification when useful.

It must NOT:
- edit the central RSE Brain / Commercial Priority Stack / portfolio registry;
- touch Detective Academy, Optical Animals, Gentle Steps, Senior, Mind Bloom, Opinie or Marketing source;
- merge to main;
- publish/deploy to Google Play;
- activate paid services;
- reactivate Supabase if billing may change without owner approval;
- create/sign/store secrets or upload keys on behalf of the owner;
- answer Families/Data Safety/legal declarations beyond engineering facts.

Cross-project decisions or central-priority changes are reported back to the central Orchestrator.

## Source of truth

Repository:
`riseshineevolve-source/riseshineevolve`

Canonical source branch:
`mobile/mobile-first-rebuild`

Current source head observed at transfer:
`de6ebbbec20a3766156dba07b25317cd9acc76a1`

Last fully verified code head:
`e356262231ec4e9114d93ab341ae8b125c80f7b2`

Latest known full code evidence:
`Mobile quality #231 PASS`

The current source branch is three documentation/release-gate commits ahead of the last fully verified code head; compare evidence found no app-code drift in those three commits.

## Local workspace

Project folder:
`C:\Users\danie\.codex\worktrees\happy-me-production\happy-me-adventures`

Dedicated local task branch:
`codex/happy-me-production-hardening`

The branch was created from:
`origin/mobile/mobile-first-rebuild`

Do not reset, clean, rebase or switch this worktree onto unrelated branches without first inspecting:
`git status`
`git diff`

An untracked `CODEX_START_HERE.md` may exist from workspace bootstrap; preserve it until the execution owner intentionally commits or replaces it.

## First files to read

1. `MOBILE_RELEASE_READINESS_MATRIX.md`
2. `HAPPY_ME_EXTERNAL_RELEASE_GATE_PACKET.md`
3. `PLAY_RELEASE_GATES.md`
4. `RELEASE_TEST_MATRIX.md`
5. `NATIVE_AUTH_RELEASE_CHECKLIST.md`
6. `PRODUCT_STRATEGY.md`
7. `STORE_CONVERSION_PLAN.md`
8. `MOBILE_MIGRATION.md`
9. `PAID_APP_SETUP.md`

## Product state

Happy Me Adventures is a 31-day family experience packaged for Android with Capacitor.

Package:
`com.riseshineevolve.happyme`

Known machine-verifiable release baseline is strong:
- clean dependency install PASS;
- TypeScript PASS;
- lint PASS;
- production build PASS;
- dependency audit PASS;
- Android generation PASS;
- package/version/SDK invariants PASS;
- debug APK PASS;
- unsigned release AAB PASS;
- signing fail-safe PASS;
- user-data isolation PASS;
- offline persistence/replay safety PASS;
- destructive-action fail-safe PASS;
- native deep-link source contract PASS;
- Data Safety engineering inventory PASS.

Do not redo these from scratch unless source/config changes.

## Current owner goal

Finish the existing app to a production-quality standard so it can move to Google Play as soon as the external account/configuration gates are available.

The work is **hardening and polish**, not a redesign.

Priority:
1. full UI/UX visual audit on phone/tablet;
2. all 31 days / all important flows regression;
3. responsive + safe-area + text overflow + orientation;
4. accessibility and reduced motion;
5. onboarding / Day 1 / journey / rewards / Parent Mode / auth source / offline states;
6. exact Google Play store-asset gap;
7. owner visual review packet;
8. only concrete reproducible fixes;
9. full CI after source changes.

## External gates — do not misclassify as code bugs

Production Supabase project currently recorded:
`fgmividxlwmvhlltwabd`

Latest durable status:
INACTIVE.

Do not silently reactivate it if billing may change.

Still external/human:
- Supabase Auth dashboard verification;
- upload keystore / Play App Signing;
- Play Console/internal testing;
- real-device auth callback testing;
- real-device offline/shared-device/destructive-action testing;
- Families / Target Audience;
- Data Safety final questionnaire;
- content rating;
- privacy/support/store listing approval;
- price/regions/publication.

## Working method

Use:
`CURRENT TRUTH -> AUDIT -> SMALLEST FIX -> TEST -> VISUAL VERIFY -> CHECKPOINT -> NEXT GATE`

No broad speculative refactor.
No autonomous visual redesign.
No fake screenshots.
No claim of device PASS from static analysis.

## Done for delegated lane

The delegated lane can report READY FOR DEVICE/PLAY INTERNAL TESTING only when:
- current source head has green full source CI;
- no known source/UX/visual blocker remains;
- owner review pack is ready;
- remaining blockers are genuinely external/device/owner gates.

Final Play publication remains owner-controlled.


## Remote task branch checkpoint

Confirmed on GitHub 2026-09-25:
- remote branch: `codex/happy-me-production-hardening`
- remote head: `4690d5700674a2e58ac88c9067f43fa9ea1e75ee`
- parent source head: `de6ebbbec20a3766156dba07b25317cd9acc76a1`
- commit: `docs(happy-me): add production hardening handoff`

Local bootstrap baseline before delegated execution:
- Node 24.19.0 available;
- npm 11.17.0 via `npm.cmd`;
- Microsoft OpenJDK 21.0.12.1 active;
- `npm ci` completed;
- TypeScript PASS;
- lint completed with 0 errors / 67 warnings;
- production Vite build PASS;
- working tree was clean before push.

The delegated Happy Me chat should continue from this remote task branch, not recreate the workspace.
