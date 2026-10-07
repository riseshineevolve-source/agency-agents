# RSE n8n Trial Activation — 2026-10-07

Status: WORKSPACE_CREATED / MVP CONFIGURATION NEXT
Owner: RSE Technical Orchestrator
Architecture: RSE Universe Factory v1.0 FROZEN

## Current state

n8n Cloud trial workspace has been created successfully.

Do not buy a paid plan during the proof period.
Do not make n8n the source of product truth.
Do not store canonical book/app logic in workflow nodes.

## MVP order

1. RSE_HEALTH / CONTROL-TOWER signal path
2. LANE-CHECKPOINT event path
3. ASSET-INGEST event path
4. RELEASE-CANDIDATE event path

## Credentials policy

Connect only the minimum required service credentials.
Initial expected credential:
- GitHub

OpenAI/API credentials are NOT required for the first deterministic workflows.

Do not connect Desktop Commander to n8n.
Desktop Commander remains an exception-only local bridge through lane chats.

## GitHub truth

Repository:
`riseshineevolve-source/agency-agents`

Control Plane workflow:
`.github/workflows/rse-control-plane.yml`

Control Plane implementation head verified green:
`3d033679177ea21a70500f52136fa4654139fef2`

## First n8n build principle

The first workflow must prove:
- n8n can authenticate to GitHub;
- n8n can observe/trigger the deterministic Control Plane;
- no AI call is needed for normal PASS state;
- owner notification happens only for real exception state.

Do not add LLM nodes until deterministic routing is proven.


## First live workflow proof

Date: 2026-10-07
Workflow: `RSE CONTROL TOWER — HEALTH CHECK`

Live GitHub credential connection: PASS.

Real execution against:
`riseshineevolve-source/agency-agents`
returned:
- `rse_status = PASS`
- `owner_action_required = false`
- `source = RSE Control Plane v1`

This proves the deterministic GitHub -> n8n health path on real repository data.

Before activation/publish, add an explicit `PENDING` state for latest workflow runs that are queued/in_progress or otherwise have no terminal conclusion. PASS and ATTENTION behavior remains unchanged.
