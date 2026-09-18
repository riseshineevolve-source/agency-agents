# RSE Brain

Status: CANONICAL CONTINUITY LAYER
Owner: Rise.Shine.Evolve.
Last rebuilt from recovered chat history: 2026-09-18

RSE Brain exists because chat history is not a reliable durable memory layer.

It is the durable, GitHub-backed map of:
- strategic decisions,
- project state,
- brand and business rules,
- technical checkpoints,
- current vs superseded assumptions,
- source provenance,
- owner gates,
- recovery pointers,
- integration status,
- cross-project dependencies,
- autonomous next actions.

## Truth hierarchy

When sources disagree, use this order:

1. Current repository code/config + current merged/active branch evidence.
2. Explicit owner-approved current manifest / checkpoint / decision lock.
3. RSE Brain decision ledger and current project registry.
4. Current Project/Library artifacts.
5. Recovered chat exports.
6. Model recollection.

A newer, explicit source beats an older summary.

## Read order for any new RSE session

1. `orchestration/brain/RSE_BRAIN_MASTER.md`
2. `orchestration/brain/DECISION_LEDGER.md`
3. `orchestration/brain/PROGRAM_REGISTRY.yml`
4. `orchestration/brain/SOURCE_REGISTRY.yml`
5. `orchestration/brain/OWNER_GATES.md`
6. `orchestration/brain/CONFLICT_LOG.md`
7. `orchestration/rse-business-projects.yml`
8. `orchestration/RESUME_FROM_ZERO.md`
9. project-specific repo handoff/checkpoint

## Brain rules

- CHAT IS NOT SOURCE OF TRUTH.
- Do not silently overwrite settled decisions.
- Do not silently promote a historical candidate into current truth.
- Every meaningful milestone ends in a GitHub checkpoint.
- Every recovered external/chat artifact gets provenance and status.
- Every contradiction is logged and resolved explicitly.
- Every owner-gated decision remains owner-gated until explicit approval.
- Dedicated execution projects may work separately, but their milestone/blocker/dependency state must sync back into RSE Brain.
- Real confidential Opinie data never enters this repository.
- Heavy proprietary publication binaries remain in private durable storage; GitHub stores manifests, hashes, provenance and structured source pointers.

## Core continuity files

- `RSE_BRAIN_MASTER.md` — human-readable master state.
- `DECISION_LEDGER.md` — decisions that must not vanish.
- `PROGRAM_REGISTRY.yml` — machine-readable portfolio/program map.
- `SOURCE_REGISTRY.yml` — provenance and source authority.
- `CHAT_RECOVERY_INDEX.md` — what was recovered from inaccessible/large chats.
- `CONFLICT_LOG.md` — stale-vs-current contradictions.
- `OWNER_GATES.md` — decisions agents may not take.
- `CHECKPOINT_PROTOCOL.md` — mandatory durable handoff format.
- `SYNC_RUNBOOK.md` — how recurring sync works.
- `CHANGELOG.md` — meaningful Brain updates.
