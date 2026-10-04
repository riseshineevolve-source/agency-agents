# 2026-10-04 — RSE Book Agent v3 architecture reset

Status: CANONICAL DIRECTION / IMPLEMENTATION AUTHORIZED
Owner: Central RSE Technical Orchestrator

## Decision

After two weeks of Detective Book Factory iteration, the renderer is not the primary
problem. RSE already has strong source normalization, puzzle validation, fixed-page
rendering and preflight. The missing layer is a stateful production orchestrator with
content-addressed page dependencies, atomic image assets and exception-only review.

Canonical architecture:
`orchestration/architecture/RSE_BOOK_AGENT_V3.md`

Operational agent:
`specialized/rse-book-production-agent.md`

## Immediate consequences

- Do not restart the renderer.
- Keep React/TypeScript/CSS/SVG + Vivliostyle + Playwright + Python validators.
- Codex becomes deterministic implementation/validation worker only.
- Whole AI-generated spatial maps are STYLE_REFERENCE_ONLY.
- Final maps use locked runtime geometry + code-rendered SVG + hash-locked isolated prop sprites.
- All books get a BOOK_MAP with content/template/asset/page locks and dependency hashes.
- Builds are incremental; unchanged page outputs are reused and not sent for owner review.
- Owner review is limited to new look/template/asset families, exceptions and release gate.

## External patterns adopted

- agent judgment separated from deterministic processing;
- style bible + visual anchor + reference-guided edits;
- checkpointed workflow state;
- code-rendered figures for text/data;
- contact-sheet review.

No external repository becomes source of truth.

## Detective current boundary

Current Case01 v2 reconstruction remains at owner visual gate.
Do not batch Cases03–30.
Do not treat current whole-map AI candidates as canonical puzzle assets.
No EN freeze or KDP publication is authorized.

Next engineering slice:
Book Map schema + dependency hashing + incremental page cache + changed-page review packet,
implemented around existing v2 without redesigning current pages.
