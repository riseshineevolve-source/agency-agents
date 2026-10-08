# RSE Lane Mailboxes

Each file in this directory has exactly ONE writer, defined in
`orchestration/control-plane/RSE_CHAT_REGISTRY_V1.yml`.

Purpose: cross-chat communication without relying on chat history or asking the owner to relay prompts.

Write only when:
- milestone changed;
- blocker changed;
- owner gate changed;
- dependency requested;
- reusable output became available;
- next safe task changed materially.

Other lanes may read every mailbox but may not edit it.

Suggested fields:
```yaml
lane:
updated:
status:
branch_or_repo_state:
milestone:
blocker:
owner_gate:
dependencies_needed: []
reusable_outputs: []
next_safe_task:
checkpoint_reference:
```
