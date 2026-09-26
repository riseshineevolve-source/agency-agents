# CODEX START HERE — Interactive Book App Factory / World 01 bounded real pilot

Status: OWNER-PROMOTED BOUNDED REAL-PILOT READINESS
Authority: Central RSE Technical Orchestrator
Date: 2026-09-26

## Goal

Move the RSE Interactive Book App Factory from synthetic-contract-only toward the first real World 01 pilot WITHOUT silently treating divergent app copy as canonical and WITHOUT deploying a production backend/app.

## Read first

- `orchestration/architecture/RSE_INTERACTIVE_BOOK_CONTENT_CONTRACT_V0.md`
- `orchestration/checkpoints/INTERACTIVE_BOOK_FACTORY_V0_2026-09-20.md`
- `orchestration/content-sources/level-up-your-brain-world-01.yml`
- `orchestration/content-sources/level-up-your-brain-interactive.yml`
- current interactive-book validators/tests/workflow
- current RSE Brain / Program Registry

Read-only comparison repository:
`riseshineevolve-source/spark-joy-fam`
especially:
`src/data/storyContent.ts`

Do NOT write to spark-joy-fam in this task.

## Source custody

Canonical published World 01 overrides app copy when they conflict.

Owner Library currently contains a more text-readable 108-page World 01 paperback:
`10 STORIES WORLD 01 FINAL paperback(2).pdf`

If attached/available to the Codex task, use it as exact published-source evidence and record provenance/hash if possible.

If unavailable:
- do not claim full source parity;
- use only repository-verifiable canonical facts plus the existing source manifest;
- identify exact source gaps;
- still complete architecture/content-model work that does not depend on unverified prose.

## Required work

1. Audit existing synthetic v0 contract/validator.
2. Perform custody/reproducibility review for World 01.
3. Read the structured interactive derivative in `spark-joy-fam`.
4. Produce a deterministic diff model:
   - canonical/published-supported content;
   - structured app content that matches;
   - app-only/divergent content requiring review;
   - reusable interaction/runtime concepts independent of product copy.
5. Define stable language-neutral IDs for the first bounded World 01 pilot slice.
6. Build the first REAL content-pack candidate only for source-supported material.
7. Prefer a small complete slice (e.g. first 1–3 missions/stories) over speculative full conversion.
8. Validate against `RSE_INTERACTIVE_BOOK_CONTENT_CONTRACT_V0.md`.
9. Preserve future EN + pl-PL architecture but DO NOT translate product prose in this task unless an already-approved translation exists.
10. Add deterministic tests for real-pack provenance/parity boundaries.

## Architecture principles

- published book source wins over derivative app copy;
- IDs language-neutral;
- behavior/config separate from localized copy;
- offline-first core content where feasible;
- no client-authoritative premium/entitlement;
- no new backend merely because a real pilot exists;
- Happy Me remains a separate sensitive backend domain;
- no private user data.

## Hard boundaries

Do NOT:
- deploy;
- create/activate Supabase/Firebase;
- choose pricing;
- publish to Google Play;
- migrate users;
- rewrite published World 01 prose;
- silently promote app-only copy;
- touch Wave 2 product implementation beyond read-only evidence gathering.

## Deliverables

- World 01 source-custody report
- structured app-vs-canonical comparison
- bounded real content-pack candidate if evidence supports it
- validator/test updates needed for provenance
- checkpoint stating exactly what is proven vs still source-gated

Final response:
HEAD, files changed, tests, source coverage %, exact unresolved source gaps, candidate-pack path, and recommendation for next pilot slice.
