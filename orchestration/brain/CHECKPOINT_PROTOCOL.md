# RSE Checkpoint Protocol

Every meaningful RSE milestone must end in a durable checkpoint.

## Mandatory checkpoint payload

1. Timestamp
2. Program/project
3. Repository
4. Branch / PR / issue
5. What changed
6. Why it changed
7. Source authority used
8. Files changed/created
9. Tests/evidence
10. PASS / NEEDS WORK / BLOCKED
11. New decisions or conflicts
12. Owner gates
13. Next safe autonomous task
14. Rollback/recovery pointer if relevant

## Checkpoint location

Prefer:
- project `CHECKPOINT.yml`,
- project handoff doc,
- current PR/issue comment,
- then sync compact state into central RSE Brain / registry.

## Brain sync requirement

After a project checkpoint changes any of:
- phase,
- branch/PR,
- blocker,
- owner gate,
- source-of-truth file,
- canonical asset,
- product/business decision,
- external integration dependency,

update central Brain on the same workday.

## No "chat-only done"

A milestone is NOT durable if the only evidence is a chat message.

## Recovery-safe status words

Use:
- PASS
- ACTIVE
- NEEDS_WORK
- BLOCKED
- OWNER_GATE
- SUPERSEDED
- ARCHIVAL
- LOCAL_ONLY
- VERIFY_ON_USE

Avoid ambiguous "done" when external/account/device verification is still pending.
