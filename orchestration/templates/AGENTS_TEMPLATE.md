# AGENTS.md

This repository is managed by the RSE Technical Orchestrator.

## Read order
Before material work:
1. read `PROJECT_BRIEF.md`,
2. inspect only the files relevant to the current milestone,
3. check current branch/PR/issues/CI,
4. preserve locked decisions and non-negotiables.

Do not perform a fresh whole-product audit unless the brief explicitly asks for one.

## Operating mode
Default: SMART EFFICIENT.

- Class S: root only, usually no specialist.
- Class M: one implementation specialist, optional targeted reviewer.
- Class L: 2-3 distinct specialists, max 4 including verification.
- Class XL: release/security/deep audit only.

One owner per overlapping file area. Do not create competing implementations.

## Work classes
### AUTO
Read-only inspection, status/checkpoint updates, deterministic checks, documentation, derived artifacts from locked sources.

### AUTO + VERIFY
Implementation inside approved scope, targeted bug fixes, tests/CI, build/preflight automation, reversible code migration.

### OWNER GATE
Product scope, pricing/payment model, final visual/content selections, legal/compliance policy decisions, production/store/KDP publication, destructive data operations, privacy boundary changes.

## Implementation loop
1. choose smallest safe next step,
2. implement,
3. run the smallest meaningful verification,
4. self-repair bounded failures,
5. use independent review only when risk warrants it,
6. update checkpoint and next gate.

Do not report PASS/ready/fixed without evidence.

## Cost controls
Prefer scripts, tests, CI and existing repo facts before Codex-heavy reasoning. Batch related edits. Reuse fresh findings. Do not make multiple agents reread unchanged context.

## Completion states
- PASS: milestone criteria met with evidence.
- NEEDS WORK: remaining work is concrete and actionable.
- BLOCKED: requires unavailable access, owner gate, credentials, source material or unsupported tooling.
