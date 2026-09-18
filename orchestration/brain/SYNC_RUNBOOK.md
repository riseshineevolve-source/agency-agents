# RSE Brain Sync Runbook

Purpose: recurring continuity checks without re-auditing the entire portfolio.

## Three-times-daily sync philosophy

A sync is not a giant status report. It is a delta reconciliation.

At each sync:
1. Read central Brain + registries.
2. Inspect active Wave 1 project heads/PRs/issues only.
3. Inspect current dedicated-project handoffs for Senior and Mind Bloom.
4. Check AI Discovery measurement only when fresh external evidence exists.
5. Detect changed branches, PRs, CI, blockers, merged milestones and newly crossed owner gates.
6. Update RSE Brain files only when something changed.
7. Add concise checkpoint evidence in the relevant project surface.
8. Never spend Codex just to produce the sync.
9. Never wake Wave 2 automatically.
10. Never copy confidential Opinie data.

## Suggested cadence

Europe/Warsaw:
- morning sync around 08:00,
- afternoon sync around 15:00,
- evening sync around 22:00.

These are portfolio continuity checks, not permission to make owner-gated changes.

## Delta output

If nothing meaningful changed:
- do not churn files,
- record no fake milestone,
- no notification needed unless requested.

If something changed:
- update program state,
- update blockers/owner gates,
- update source registry if a new canonical artifact appeared,
- append Brain changelog,
- flag only decisions requiring owner input.

## Escalation

Notify owner when:
- an owner gate is reached,
- a previously safe assumption becomes false,
- canonical sources conflict,
- CI/source evidence shows a real blocker,
- a dedicated project risks losing uncommitted/local-only work,
- privacy or publication risk appears.
