# Optical Animals — Codex Overnight Finish Handoff

Date: 2026-09-29
Authority: Central RSE Technical Orchestrator
Status: CODEX DELEGATED / CENTRAL READ-ONLY / OWNER ART GATES PRESERVED

## Live durable baseline

Repository:
`riseshineevolve-source/riseshineevolve`

Branch:
`feat/optical-animals-book-creator`

PR:
#14 — Optical Animals: reusable book + seek-and-find creator

Head at handoff:
`99ef2924ab4037648069d4634473be36c51bbb39`

Current-head quality:
**Optical Book Creator quality #98 — SUCCESS**

## Current product truth

The seek-and-find engineering is not a blank slate.

Implemented:
- manifest-driven 8.5x11 book assembly;
- 20 hero slots;
- five group seek-and-find pages after groups of four;
- all-20 grand challenge;
- deterministic optical compositor;
- answer maps/previews;
- exact hero -> reviewed mask -> exact source-pixel token contract;
- exact placement proof;
- current-source integrity verification;
- owner-proof packet tooling;
- hero ZERO TEXT / ZERO LABELS;
- white hero versos;
- butterfly A/B production comparison gate.

Current exact compositor files include:
- exact_identity.py
- exact_seek_find.py
- seek_find.py
- exact_book.py
- exact_volume_proof.py
- exact_volume_integrity.py

## Important mismatch to reconcile

Owner reports local working art is approximately 19/20 ready.

Canonical `FINAL20_MANIFEST.json` remains:
- state DRAFT;
- 12 APPROVED;
- 8 owner-gated.

Do not interpret the owner's current working-art report as permission to auto-promote those eight slots.

Local asset root recorded by the manifest:
`C:\Users\danie\Desktop\Asia\KDP\coloring\optical animals`

Canonical folders:
- 01_FINAL_20_SOURCE
- 00_NEW_RENDERS_INBOX
- 02_WORKING_CANDIDATES_20
- 99_ARCHIVE_REPLACED

## Known code gap

The strong exact owner-proof path is fail-closed.
The ordinary non-preview release command historically routes through a weaker generic builder.

Latest checkpoint:
`tools/optical-book-creator/checkpoints/2026-09-29-generic-release-fail-close-ready.md`

The overnight Codex sprint should at minimum fail closed on a weak generic RELEASE path and preferably wire a true exact release package using the same exact-identity proof semantics.

## Overnight owner intent

Move everything possible toward KDP ASAP while the final visual art/butterfly decisions remain owner-gated.

Highest-value overnight work:
1. reconcile local working art to canonical slots without automatic approval;
2. prepare owner-review contact sheets and exact hashes;
3. close exact release-path gap;
4. create/review subject-mask proposals from real owner art without generating target pixels;
5. derive exact hero-pixel tokens where trustworthy;
6. generate real exact search pages where inputs are fully verified;
7. generate explicitly watermarked provisional search layouts where only mask review is missing;
8. prepare all-20/grand challenge evidence where possible;
9. render butterfly single-page vs gutter-safe spread comparison without selecting A/B;
10. assemble the most complete owner-review packet possible.

## Hard gates

No:
- automatic art selection/promotion;
- mutation of approved hero bytes;
- generated/redrawn/reposed lookalike target animals;
- fabricated mask-review/owner-approval records;
- butterfly selection;
- final manifest lock without owner review;
- KDP publication;
- main merge.

Codex prompt:
`OPTICAL_ANIMALS_CODEX_OVERNIGHT_FINISH_SPRINT_2026-09-29.md`

Central and Daily Autopilot are read-only for Optical while this handoff is active.
