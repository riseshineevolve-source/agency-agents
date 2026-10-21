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


## Live authenticated inspection — 2026-10-21

Supersedes the assumption that only a one-time October 7 test exists.

- Workspace origin recovered from prior configuration: https://riseshineevolve.app.n8n.cloud
- Secure owner-assisted login completed; authenticated Overview and execution pages were observed.
- Banner: "Your trial is over. Upgrade now to keep automating."
- Overview contains exactly two workflows: RSE CONTROL TOWER — HEALTH CHECK (Published) and RSE LANE CHECKPOINT. Lane Checkpoint was last updated approximately one week ago; its publication/execution status was not verified.
- Overview displayed 163 production executions, zero failed production executions, and average runtime 0.56 seconds in the dashboard's current reporting window. Do not treat these as lifetime totals.
- Health Check has real hourly execution history through October 21. Most recent displayed execution: #352, October 21 07:00:15, Succeeded in 588 ms. The panel timezone was not verified, so do not translate that timestamp to Warsaw time.
- Observed Health Check nodes: Every Hour, Fetch latest run, Classify run health, Completed and Success?, No Final Conclusion Yet?, PASS, PENDING, ATTENTION.
- The classification group explicitly states: "Ends every run in exactly one state: PASS, PENDING or ATTENTION. No notifications are sent."
- Workflow execution success is not proof that current RSE product health is PASS. Exact node output/current GitHub-run freshness was not extracted.
- GitHub Control Plane main configuration was freshly read: workflow_dispatch only, 10-minute job timeout, artifact retention one day. Hourly n8n polling must not be mistaken for fresh hourly GitHub Control Plane generation.
- No paid plan, subscription, credentials, permissions, workflow publication or schedule change was made.

### Concrete remaining blocker

Export JSON was found in the workflow menu. The browser's native credential protection then rejected further interaction/download before any export file was returned. A fresh-tab attempt and browser runtime reset did not clear the restriction. No workflow export is claimed saved. Do not reconstruct workflow JSON from screenshots.

### Continuation

1. Recover an authenticated browser context that permits normal post-login workflow downloads.
2. Export both actual workflow definitions without credentials and preserve them in a private durable destination.
3. Read Lane Checkpoint state, billing/trial details and latest Health Check classified output.
4. Keep paid n8n upgrade closed. Decide a zero-subscription execution route only after inspecting actual definitions and costs; do not reactivate billable GitHub Actions as a substitute.
