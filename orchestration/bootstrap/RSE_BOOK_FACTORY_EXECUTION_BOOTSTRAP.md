# RSE Book Factory v1 — Execution Bootstrap

Take over implementation of the RSE Book Factory.

GitHub is source of truth.

Read in order:
1. `orchestration/brain/RSE_BRAIN_MASTER.md`
2. `orchestration/RESUME_FROM_ZERO.md`
3. `orchestration/architecture/RSE_BOOK_FACTORY_V1.md`
4. `orchestration/bootstrap/DETECTIVE_FIRST18_EXECUTION_BOOTSTRAP.md`
5. `orchestration/detective/DETECTIVE_CASES_02_30_PRODUCTION_MAP.md`
6. `orchestration/detective/DETECTIVE_KDP_REGRESSION_GATE.md`
7. `orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`
8. newest Detective owner locks/checkpoints.

## Editorial content gate

For a new book or edition, do not begin page production from a draft. If content is not already owner-approved and hash-locked as `FROZEN_CONTENT`, first use `orchestration/bootstrap/PREMIUM_BOOK_CONTENT_UPGRADE_BOOTSTRAP.md` and require its `CONTENT_FREEZE_MANIFEST` before rendering.

## Mission

Create a new dedicated repository:
`riseshineevolve-source/rse-book-factory`

Implement a deterministic fixed-layout publishing engine for RSE books.

Do not redesign current Detective pages.
Do not mutate active FIRST18 execution work.

First usable milestone:
1. repository skeleton + AGENTS/PROJECT_BRIEF/CHECKPOINT;
2. fixed-size page renderer;
3. frozen-PNG page support;
4. page manifest with checksums;
5. PDF export;
6. per-page PNG proof export;
7. contact sheet;
8. Case Intro component;
9. HM Comms component;
10. Witness Board component;
11. Live Map + Verdict component;
12. structured Case YAML schema;
13. render Case 02 from data using the Case 01 design system;
14. deterministic QA + preflight report.

## Critical rules

- renderer is deterministic;
- AI does not invent page copy at render time;
- exact assets use stable IDs;
- no character substitutions;
- no logo substitutions;
- no hardcoded stale page references;
- no font shrinking below readability floor;
- Polish uses same templates with separate canonical text data;
- maps are SVG/data-driven;
- witness boards are data-driven;
- same source data drives live/solution maps.

## Execution lanes

Use max four active implementation roles:
A. engine/build
B. content/schema
C. templates/maps
D. QA/preflight

Coordinate through one branch owner and checkpoint frequently.

## First demonstration

Do NOT batch 29 cases before proof.

Produce:
- one build containing frozen approved opening pages;
- generated Case 02 intro;
- generated Case 02 Witness Board;
- generated Case 02 Live Map + Verdict;
- contact sheet;
- QA report.

If Case 02 passes owner visual review, freeze the template and batch the remaining spatial cases.

## Stop condition

Stop at the first real owner gate:
- Case 02 generated proof is ready for owner visual approval,
or
- a real source/asset ambiguity prevents deterministic implementation.

Do not continue into a mass rollout before that gate.
