# CODEX START HERE — Polish Localization Engine main reconciliation

Status: OWNER-AUTHORIZED BOUNDED EXECUTION
Authority: Central RSE Technical Orchestrator
Date: 2026-09-26

## Goal

Reconcile the proven Polish Localization Engine from branch
`rse/polish-localization-engine-v1`
onto the CURRENT main-based branch
`codex/polish-engine-main-reconcile`
without losing either current-main changes or proven localization functionality.

This is infrastructure/reconciliation work. It is NOT authorization to translate the full Detective Academy before explicit EN freeze.

## Source of truth

Read first:
- `orchestration/brain/RSE_BRAIN_MASTER.md`
- `orchestration/brain/COMMERCIAL_PRIORITY_STACK.md`
- `orchestration/brain/checkpoints/2026-09-26-codex-capacity-restored-parallel-wave.md`
- branch `rse/polish-localization-engine-v1`
- all files under `localization/pl-PL/`
- localization scripts/workflows/tests referenced by PR #6

Current proven localization branch head:
`f9d938611661f74108bdafa1df6ac8de1aaa27f1`

Current branch base:
main at the branch creation point.

## Required work

1. Inspect exact diff between current main and `rse/polish-localization-engine-v1`.
2. Identify the smallest safe set of localization-engine files, tests, workflows and docs that must exist on current main.
3. Bring them onto this branch intentionally.
4. Resolve conflicts by preserving:
   - current main orchestration truth,
   - canonical terminology,
   - Polish style guide,
   - forbidden AI-isms,
   - Detective profile/segmentation/freeze contracts,
   - Gentle Steps fit contracts,
   - all golden tests,
   - existing deterministic regression behavior.
5. Do not rewrite working engine architecture merely because a cleaner refactor is possible.
6. Add/fix tests only for concrete reconciliation risks.
7. Run all localization regression/test commands and the relevant repository validation workflows locally where possible.
8. Produce a concise reconciliation checkpoint documenting:
   - files ported,
   - conflicts resolved,
   - test evidence,
   - remaining owner/external gates.

## Hard boundaries

Do NOT:
- start full Detective PL translation;
- invent a frozen Detective source;
- alter English product content;
- merge to main;
- publish;
- change shared portfolio priorities;
- touch Gentle Steps translation candidate files being written by the separate Gentle Steps Codex lane unless required to preserve compatibility.

## Completion target

Return a clean current-main-compatible Localization Engine branch with green deterministic tests.

Final response must state:
- HEAD before/after
- files changed
- exact test commands/results
- whether branch is ready for review/PR
- any remaining conflicts/gates
- confirmation: NO full Detective translation, NO merge, NO publication.
