# Project Unstoppable / Unstoppable Me — Revival Checkpoint

Date: 2026-09-27
Authority: Central RSE Technical Orchestrator
Status: ACTIVE PARALLEL REVIVAL LANE / NO RELEASE AUTHORIZATION

## Canonical code source

Repository:
`riseshineevolve-source/unstoppable-me`

Canonical main at revival start:
`df1014c7318d6b14a97ef183790c8b3c7b3ad0c2`

Revival branch:
`codex/unstoppable-me-revival`

Current revival branch head after Central setup:
`651f28ceb09070354394a36deac97df98441ecc1`

The separate repository:
`riseshineevolve-source/Unstoppable-Me-Edit`
is currently empty and is NOT a source of truth.

Git history on `unstoppable-me` contains Lovable-generated commits, confirming this is the historical Lovable-connected codebase. GitHub is the durable authority for revival.

## Product pair

Project Unstoppable exists as two complementary forms:

1. **Amazon KDP / workbook**
   - owner supplied source: `Project_Unstoppable_6x10_Fixed.pdf`
   - 191 pages
   - 31-day program
   - recurring day system: intro / briefing / workbench / system reboot / glitch & puzzle / free roam
   - ends with Day 31 Unstoppable Contract and Superpower First-Aid Kit

2. **Interactive app**
   - React/Vite/TypeScript
   - Supabase auth/data
   - same 31-day content universe in `src/data/adventureData.ts`
   - interactive responses, drawings, mini-games
   - progress, section tracking, achievements, streaks, weekly summaries, mission log
   - TTS, profile/settings, leaderboard, privacy, account deletion

Full KDP/app parity has NOT yet been proven; a structured day-by-day parity audit is required before canonical content lock.

## Strategic positioning

Owner reactivated this project because the adjacent market/niche work identified strong opportunity around **teen coping skills**.

Current content already overlaps strongly with:
- self-regulation
- emotion awareness
- overload
- boundaries / saying no
- social pressure
- bullying / mean comments
- parent communication
- focus
- procrastination
- rest/reset
- resilience after failure
- confidence
- relationships and support

Direction:
**modern game-like teen life-skills / coping toolkit**, not therapy.

Do not use clinical CBT/DBT/diagnostic positioning without a separate evidence/legal/product decision.

## Revival actions already completed by Central

On `codex/unstoppable-me-revival`:
- removed tracked `.env` from the revival branch without exposing its contents;
- added `.env` / `.env.*` protection to `.gitignore`;
- added safe `.env.example` using only:
  - `VITE_SUPABASE_URL`
  - `VITE_SUPABASE_PUBLISHABLE_KEY`
- added `.github/workflows/unstoppable-ci.yml`;
- added `CODEX_START_HERE.md` with the bounded recovery contract.

Important:
historical git may still contain previous environment-file contents. Do not echo secret values. If a privileged/service-role secret is discovered, report only the key type/name and require owner rotation.

## Known current inconsistencies / release blockers

### Code / product truth
- README is generic Lovable boilerplate and still contains `REPLACE_WITH_PROJECT_ID`.
- PWA manifest says **8-day adventure**, while source content is 31 days.
- `/install` actively promotes browser/PWA installation.
- Current RSE release direction is Android / Google Play; PWA may remain technical fallback but should not be marketed as the current released product unless owner re-authorizes it.
- latest main commit explicitly says test signup / auto-confirm was temporarily enabled; production auth configuration must be revalidated before release.

### Privacy / minors / release
- app stores account/progress/mission responses/drawings/preferences and game scores.
- Privacy page and account deletion path exist, including `delete_own_account` RPC.
- privacy copy/contact details must be revalidated before Play publication.
- intended teen age range and Google Play target-audience/Data Safety implications remain owner/release gates.
- leaderboard must remain privacy-minimized.

### Editorial / KDP + app
Publication-grade audit is required for:
- health-adjacent or psychology-adjacent claims;
- absolutist coping advice;
- bullying / harassment advice;
- finance generalizations;
- quote attribution;
- age suitability;
- privacy-sensitive sharing prompts.

Known source areas for review include Day 3, 5, 6, 8, 10, 16, 17 and 22.

## Dual-product contract

Avoid publishing the book and app as two copies of the same experience.

Target complementarity:
- **BOOK:** write / plan / reflect / draw / build a reusable personal toolkit.
- **APP:** do / interact / practice / get feedback / play / track / build streaks.

The same core concepts and Happy Makers world may be shared, but user responses/private journals must never be copied into public/book assets.

## Next safe work

1. Run app CI baseline: install, tests, build, lint.
2. Produce current-state audit.
3. Audit KDP/app parity Days 1–31 using owner PDF.
4. Audit teen coping/self-regulation editorial safety + claims.
5. Correct source-backed stale app facts (31 days, README, release direction).
6. Prepare release gates for Android/Google Play without publishing.
7. Decide after audit whether KDP source needs a bounded content revision before final release metadata/cover work.

## No-go gates

No:
- main merge without Central/owner review;
- Google Play publication;
- KDP publication;
- paid services;
- production Supabase configuration changes;
- secret exposure;
- real-user QA data;
- medical/therapy positioning.

