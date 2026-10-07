# RSE Universe Factory v1.0 — Implementation Plan

Status: ACTIVE IMPLEMENTATION
Date: 2026-10-07
Architecture: FROZEN in RSE_UNIVERSE_FACTORY_V1_0_FREEZE.md

## Definition of "100% implemented"

Factory v1.0 is 100% implemented when all of the following are true:

1. Control Plane registry/mailboxes validate automatically.
2. Hourly deterministic portfolio snapshot runs without chat/Desktop Commander.
3. Every active lane has a durable bootstrap + checkpoint + mailbox.
4. Desktop Commander is exception-only and Codex launcher is standardized.
5. Detective Graphic Gold Library has at least one genuinely owner-approved frozen family and can rebuild a changed page without visual drift.
6. Asset Vault ingestion + manifest is proven end-to-end.
7. Second ChatGPT Pro is assigned a non-overlapping Build Desk lane and uses GitHub durable handoffs.
8. n8n routes at least:
   - Control Tower events,
   - lane checkpoint events,
   - release-candidate events,
   - asset-ingest events.
9. One Agents API pilot handles only ambiguous exception triage with tracing.
10. At least one book lane and one app lane complete an end-to-end release-candidate run through the frozen architecture.

Temporal is NOT required for v1.0 completion.

## Implementation waves

### W0 — Architecture freeze and control truth
Status: PASS
- Universe map
- autonomy protocol
- chat registry
- lane mailboxes
- Asset Vault protocol
- resource/cost routing
- v1.0 freeze + ADR policy

### W1 — Deterministic Control Tower
Status: PASS
- registry/mailbox validator
- hourly GitHub Actions snapshot
- machine-readable status artifact
- condition-watch owner notification

Exit: hourly snapshot green. PASS on GitHub Actions at head `3d033679177ea21a70500f52136fa4654139fef2`.

### W2 — Lane activation
Status: PARTIAL
- each existing chat receives canonical opening message once
- each lane refreshes its mailbox from live repo state
- stale owner gates are reconciled
- bare Codex use replaced by stable RSE launcher where local CLI is used

Exit: every active lane has current mailbox/checkpoint.

### W3 — Graphic Gold Library
Status: IN PROGRESS / RELEASE-CRITICAL
- recover strongest manual Detective first ~18 pages
- official Happy Makers replacements
- Visual Storyteller + Brand Guardian extraction
- first real Gold Family implementation
- one owner family gate
- freeze reusable families

Exit: changed Detective page uses a frozen Gold Family and preserves visual parity.

### W4 — n8n orchestration MVP
Status: PENDING OWNER ACCOUNT CONNECTION
- n8n Cloud trial first
- CONTROL-TOWER-HOURLY
- LANE-CHECKPOINT
- RELEASE-CANDIDATE
- ASSET-INGEST

Exit: event routing works without owner relay.

### W5 — Second Pro Build Desk
Status: PENDING OWNER LOGIN/CHAT SETUP
- account assigned non-overlapping lane(s)
- Detective heavy Codex first when useful
- Gentle Steps / World App Factory when Detective is at gate
- GitHub/mailboxes are the only handoff

Exit: two accounts work in parallel without branch/worktree collision.

### W6 — Agents API exception pilot
Status: PENDING W4
- one traced Control Tower triage agent
- deterministic routing first
- agent only on ambiguous exceptions
- hard cost cap and retry cap

Exit: one real ambiguous event handled successfully without broad agent swarm.

### W7 — End-to-end proof
Status: PENDING PRODUCT LANES
- one book release candidate
- one app release candidate
- measure cycle time, owner touches, reuse rate, tool cost
- no architecture redesign during proof

Exit: Factory v1.0 = IMPLEMENTED.

## Non-goal

"100% implemented" does not mean every RSE product is published.
It means the factory itself is operational and proven across one book + one app.
