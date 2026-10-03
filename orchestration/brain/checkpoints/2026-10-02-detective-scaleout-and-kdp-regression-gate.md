# Detective Academy — scaleout plan + KDP regression gate
Date: 2026-10-02
Status: CENTRAL PREPARATION COMPLETE / FIRST18 WORKER ACTIVE

## Why this exists

The dedicated First18 worker now owns Pages 1–18 through complete Case 01.

Central RSE Technical Orchestrator prepared the rollout system for the rest of the book without writing to the active First18 surface.

## New canonical production surfaces

1. `orchestration/detective/DETECTIVE_CASES_02_30_PRODUCTION_MAP.md`
   - maps every remaining case to its production family;
   - locks the 15 spatial cases;
   - defines when Witness Board + Live Map facing spreads are required;
   - removes generic duplicate intro/evidence-grid filler;
   - protects all special-case locks and meta payoffs.

2. `orchestration/detective/DETECTIVE_KDP_REGRESSION_GATE.md`
   - defines source, identity, logo, typography, duplication, case-structure, spatial, map, witness-board, special-case, page-reference, back-matter, PDF/preflight and visual-inspection gates;
   - prevents repeated Dilo/Alio, wrong-logo, tiny-type, stale-page-ref, duplicate-intro, map-key and frozen-page regressions.

## Rollout rule

Do not start Case 02 production until the owner accepts the First18 / Case 01 block.

After Case 01 approval:
- freeze Intro template;
- freeze HM Comms visual grammar;
- freeze Witness Board grammar;
- freeze Map grammar;
- freeze Verdict grammar;
- rollout Cases 02–30 by the production map, not by ad-hoc page generation.

## Optical note

Central attempted live verification of the historical Optical repository/branch names from older state, but the current GitHub connector returned NOT_FOUND for those old paths. Do not infer current Optical state from stale branch names. Optical should continue only in its dedicated execution stream/bootstrap using live accessible source truth.
