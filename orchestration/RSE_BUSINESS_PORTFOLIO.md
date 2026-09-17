# RSE Business Portfolio Orchestrator

Status: active control document
Owner: Rise.Shine.Evolve
Operating model: CORE-first, specialists on demand, English-first, source-of-truth in project files/repositories rather than chat history.

## Purpose

This document is the portfolio control layer for RSE business projects that are intended to become books, apps, digital products, or supporting commercial infrastructure. It exists to prevent duplicate work, conflicting changes, abandoned branches, repeated audits, and expensive multi-agent overuse.

The central Orchestrator coordinates projects. Large execution projects may keep their own specialist chat/workstream, but their status, dependencies and gates are reconciled here.

## Portfolio rules

1. Use the project's `PROJECT_BRIEF.md` as the first source of project context whenever it exists.
2. Do not restart architecture, redesign a product, or repeat completed audits unless a verified blocker requires it.
3. Use CORE agents first. Add specialists only when a concrete task needs them.
4. Prefer one implementation owner per file/surface. Parallel agents may review, test or research, but must not independently rewrite the same source.
5. Every implementation loop should be: plan -> minimal change -> automated checks -> targeted review -> correction -> verification -> checkpoint.
6. English master first. Polish localization begins only after source content is stable, except for frozen/published materials used as Polish Engine calibration corpora.
7. Major decisions remain owner-gated: product scope, pricing/payments, legal/compliance, brand identity, final visual selection, publication/store launch, destructive migration, crawler policy, and production deployment when not already covered by an approved release process.
8. Do not ask the owner to perform repetitive copy/paste or approval clicks when the connected toolchain can safely do the work.
9. GitHub/repository checkpoints are preferred over chat-only state.
10. Confidential local-only data must never be copied into GitHub or remote agent contexts.

## ACTIVE portfolio

### 1. RSE Core Platform / Website / Business

Role: commercial umbrella and canonical brand/product source.
Repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
State: active.
Current tracks:
- brand/business/site strategy consolidation,
- AI Discovery measurement and recrawl/index inspection,
- canonical product/entity truth layer,
- English-site stabilization,
- Polish localization after English freeze.

Important completed baseline:
- retired PWA/SaaS/Paddle positioning removed,
- Google Play Coming Soon positioning and Seniors surface shipped,
- AI product/entity truth layer shipped,
- first four C1 intent guides shipped,
- measurement harness shipped,
- live production parity verified.

Guardrail: do not create additional intent pages merely because they are easy to generate. Expansion requires evidence from post-recrawl measurement.

### 2. Polish Localization Engine

Role: shared localization/transcreation infrastructure for RSE books, sites, apps, metadata and store copy.
Repository: `riseshineevolve-source/agency-agents`
Active branch/PR: `rse/polish-localization-engine-v1`, draft PR #6.
State: active calibration.
Current golden corpus: frozen published 244-page Happy Makers paperback.
Strategy: calibrate on difficult representative segments before full-book translation; feed accepted corrections back into style rules, routing and QA gates; then run regression tests before scaling.

### 3. Happy Makers Detective Academy

Product: Book 1 and reusable automated Book Factory.
Execution repository/source: `riseshineevolve-source/RISE.SHINE.EVOLVE`, branch `feature/detective-book-factory`, draft PR #571; local working copy historically named `detective-academy`.
Production area: `tools/detective-book-factory/`.
State: active production.
Locked direction:
- English master before Polish,
- 15 Shigai BASIC results are VERIFIED SPATIAL DEDUCTION MODULES, not final cases,
- Book Factory remains code-driven; Canva is finishing only,
- preserve puzzle logic/geometry while rebuilding presentation.
Current blockers/gates:
- spatial-map visual standard is not yet approved for mass conversion,
- final solution-map art and full visual reskin remain,
- hidden `CHECK THE OLD MAP` meta-letter validation must remain correct,
- final print QA is still required.
Agent routing now:
- CORE Orchestrator/Product Manager,
- Cartography Designer only for map presentation work,
- Test Automation Engineer for geometry/solution regression,
- Book/Narrative specialists only where editorial copy is not already locked,
- PDF/print QA at export stage.
No mass spatial conversion until visual standard passes.

### 4. Happy Me App / Happy Me Adventures

Product: 31-day wellbeing Android app for children.
Authoritative remote codebase: `riseshineevolve-source/riseshineevolve`.
Active branch: `mobile/mobile-first-rebuild`.
Local project source: `C:\Users\danie\GitHub\happy-me-app` with `PROJECT_BRIEF.md` as handoff context.
State: active rebuild, requires fresh custody/audit before further feature work.
Known product identity: `Happy Me Adventures`, Android package `com.riseshineevolve.happyme`.
Known unresolved area: release/payment path and fresh end-to-end verification have historically been incomplete.
Agent routing now:
- Minimal Change Engineer for implementation,
- Mobile/Android specialist only for native release issues,
- Test Automation Engineer for build/navigation/state regression,
- Reality Checker as independent final gate,
- security/privacy specialist only when auth/data changes are in scope.
Do not revive obsolete web/PWA commercial assumptions.

### 5. Optical Animals

Product: premium 8.5 x 11 in portrait KDP optical-animal coloring book, target exactly 20 final illustrations.
Local production source: `C:\Users\danie\GitHub\optical-animals-book-creator`, branch `feat/optical-animals-book-creator`, with `PROJECT_BRIEF.md` as source-of-context.
State: active visual curation/production; final image set not yet locked.
Non-negotiable production style remains governed by the project's latest brief and user-approved image decisions.
Current gate:
- finish image-by-image pass,
- preserve strongest existing versions,
- fix only weak assets,
- lock final 20 before full assembly/preflight.
Agent routing now:
- Visual Art Director / Illustration QA for comparative curation,
- Anatomy/consistency review where needed,
- KDP/print preflight specialist after roster lock,
- Book Creator automation for assembly, replacement and export.
Do not mass-regenerate approved images or change species/roster automatically. Final visual roster is owner-gated.

### 6. Senior / Hello Today

Product: senior-focused app.
Execution remains in its dedicated project/chat.
Portfolio role: centrally supervised dependency/status only.
Known repositories include `riseshineevolve-source/Happy-Senior` and the active Android work historically associated with `hello-today-android`.
State: active separate execution.
Rule: do not merge its detailed implementation conversation into the central RSE chat; only synchronize milestones, blockers, shared brand/localization/store dependencies and release gates.

### 7. Mind Bloom Assistant

Product: assistant / Personal Chief of Staff application.
Execution remains in its dedicated project/chat.
Repository: `riseshineevolve-source/mind-bloom-assistant`.
State: active separate execution.
Rule: synchronize milestones, blockers and shared infrastructure only. Do not collapse its execution context into the central RSE workstream.

### 8. Opinie

Product/workbench: local AI-assisted expert accident-reconstruction opinion workbench. This is not an autonomous final-opinion generator.
Local-only root: `C:\Users\danie\AI_LOCAL\opinie`.
State: active preparation.
Privacy boundary: confidential case files, historical archive, indexes, embeddings and analysis remain local/offline on Windows. Online tools and GitHub must not receive case data or archive content.
Source of truth: local `PROJECT_BRIEF.md`, original case files and original archive.
Agentization target:
- local Orchestrator,
- evidence/provenance extractor,
- timeline/scene builder,
- calculation checker,
- variant/reconstruction reviewer,
- citation/provenance QA,
- final human expert review queue.
First operational gate remains local validation of the privacy/path separation and then a minimal end-to-end case pipeline. Remote orchestration may track only non-confidential status metadata.

## INVENTORY / HOLD

These are real repositories/products found in the RSE ecosystem but are not automatically reactivated by the portfolio Orchestrator. They require explicit portfolio confirmation or a current `PROJECT_BRIEF.md` before consuming development budget:

- `happy-makers-quest`
- `family-mission-control`
- `unstoppable-me`
- `night-command`
- `family-hearth-stories`
- `spark-joy-fam`
- `neon-wonder-world`
- `word-search-puzzle`
- `Happy-Makers-Calm-Wheel`
- `1-minute-challange`

The small RSE GIFTS tools historically include experiences such as 1-Minute Challenge, Calm/Energy Wheel and word-search/word-hunt tools. They may remain useful site products, but they are not priorities unless promoted out of HOLD.

## OUTSIDE CURRENT BUSINESS BUILD QUEUE

Track only when explicitly requested:
- Kuratoryjny/MKJA educational study app,
- CV Tailor,
- job-search tooling,
- family finance spreadsheet/tooling.

These may use the agent library but should not compete with active commercial book/app production capacity.

## Standard agentization package for every ACTIVE build project

Each active build project should converge toward:

- `PROJECT_BRIEF.md` — current source-of-context and locked decisions,
- `AGENTS.md` — safe agent rules / boundaries,
- machine-verifiable build or preflight command,
- regression tests for locked behavior/content,
- a short checkpoint/status file or issue,
- one active implementation branch at a time for the current milestone,
- automated artifact generation where practical,
- independent QA/reality-check pass before promotion.

The Orchestrator should not create heavyweight agent swarms by default. Typical execution uses 2-4 roles, expanding only for a demonstrated specialist need.

## Portfolio sequencing

Parallel lane A — RSE commercial foundation:
RSE strategy -> approved English changes -> AI Discovery reconciliation -> English freeze -> Polish rollout.

Parallel lane B — published/frozen localization calibration:
Published Happy Makers book -> Polish Engine regression corpus -> engine refinement -> full Polish edition when quality gate passes.

Parallel lane C — books in production:
Detective Academy visual/map gate -> complete Book 1 -> English print master -> Polish edition.
Optical Animals curation -> final 20 lock -> automated assembly/preflight -> KDP master.

Parallel lane D — apps:
Happy Me branch custody/audit -> minimal rebuild completion -> automated verification -> Android release path.
Senior and Mind Bloom continue in dedicated execution chats with portfolio-level synchronization.

Parallel lane E — confidential local system:
Opinie privacy validation -> minimal local end-to-end workflow -> local agent loop -> human expert review.

## Definition of portfolio health

A project is healthy when:
- one source of truth is identifiable,
- current branch/repo/local root is known,
- next milestone is explicit,
- automated verification exists or is being built,
- no duplicate agents are changing the same surface,
- blockers are visible,
- owner input is requested only at meaningful gates,
- completed decisions are not reopened without evidence.
