# RSE Consumer Platform — Advanced Supabase Gate A-H Checkpoint

Status: **VERIFIED GREEN / SYNTHETIC ONLY / NO LIVE BACKEND**

Verified: 2026-09-21

## Durable result

The disposable PostgreSQL 16 harness now exercises the remaining high-risk parts of the Supabase security plan without creating or contacting a live Supabase project.

New synthetic artifacts:

- `orchestration/architecture/fixtures/consumer-platform-v0/supabase_sync_boundary_ephemeral.sql`
- `scripts/test-rse-consumer-supabase-advanced-static.py`
- `scripts/test-rse-consumer-supabase-ephemeral-advanced.sql`
- `.github/workflows/rse-consumer-advanced-gates.yml`

The advanced overlay deliberately removes direct `authenticated` INSERT/UPDATE privileges from `progress` and `sync_state` and models an atomic sync boundary through a **SECURITY INVOKER** function that is executable only by the synthetic `trusted_server` role. It accepts no entitlement/premium claim from the client.

This overlay is test-only. It is not a production migration or an authorization to deploy a backend.

## Gate coverage added

The advanced runtime/static matrix now verifies, in combination with the existing contract suite:

- private-table RLS is enabled;
- browser/mobile roles cannot directly mutate protected progress/sync state in the advanced model;
- the server sync primitive is not executable by `authenticated`;
- own-profile lifecycle remains allowed while cross-owner/guessed-profile mutations fail closed;
- profile ownership reassignment is denied;
- client entitlement extension and deletion are denied;
- trusted-server exact-product activation does not widen unrelated product access;
- revoked and expired entitlements immediately fail closed;
- unsupported entitlement authority is rejected;
- future client sync revisions fail closed without mutation;
- stale weaker progress merges monotonically and cannot downgrade `completed`;
- cross-owner and non-entitled product sync attempts fail closed;
- server privacy/export enumeration remains explicitly account-scoped inside the shared Consumer domain;
- public catalog metadata is read-only and never implies entitlement;
- composite owner/profile provenance rejects cross-owner rows even for the synthetic server role;
- static guards continue to reject `SECURITY DEFINER`, wildcard `is_premium`, token/secret fields, broad browser execution, and dependencies on separate Happy Me / Senior / Mind Bloom / Opinie / CV / finance domains.

## Verification

Workflow: `RSE Consumer Advanced Gates`

Run: **#1 / 35541200417**

Head: `9baf778da210b4c354dcb10e19d452f9524df8e6`

Result: **PASS**

Both jobs passed:

- `static-guard`
- `exercise-advanced-ephemeral-postgres`

The PostgreSQL job successfully completed the baseline fixture, applied the advanced server-mediated sync overlay, and passed the full advanced Gate A-H script.

## Boundaries preserved

- no live Supabase project created or modified;
- no paid/billable resource restored;
- no real user, child, purchase, CV, finance, Mind Bloom, Opinie, or production product data used;
- no real World 01 / World 02 / Gentle Steps content converted;
- Happy Me remains a separate child/family-sensitive backend domain;
- authentication remains identity only and does not grant product access;
- product entitlement remains exact `(account_id, product_id)` server authority.

## Known non-goals

This checkpoint does not choose the final production sync transport, token/payment verification mechanism, server runtime, privacy deletion executor, or live Supabase project. Those remain future implementation/owner-gated decisions.

The base RLS fixture plus advanced overlay are still a test architecture, not a final production migration bundle.

## Next safe slice

A safe next synthetic slice is to consolidate the verified base + advanced overlay semantics into a single **candidate migration contract** that can be applied from a clean ephemeral database, then verify schema/policy drift deterministically. This must remain local/CI-only and must not be deployed to a real Supabase project without explicit owner approval.
