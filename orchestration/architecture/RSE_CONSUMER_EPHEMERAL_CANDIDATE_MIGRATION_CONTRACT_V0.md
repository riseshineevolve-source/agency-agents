# RSE Consumer Platform — Ephemeral Candidate Migration Contract v0

Status: **SYNTHETIC / PRE-DEPLOYMENT ONLY**  
Scope: shared RSE Consumer Platform account/profile/product-entitlement/progress surface.  
Not authorized for: live Supabase deployment, paid project creation, real customer data, Happy Me, Senior/Hello Today, Mind Bloom, Opinie, Smart CV Tailor, or Domowe Finanse.

## Purpose

This contract turns the already-verified base RLS fixture plus advanced sync-boundary overlay into one reviewable candidate without duplicating SQL or creating a second source of truth. It is a composition contract, not a production migration.

The candidate is defined by the ordered pair:

1. `orchestration/architecture/fixtures/consumer-platform-v0/supabase_rls_ephemeral.sql`
2. `orchestration/architecture/fixtures/consumer-platform-v0/supabase_sync_boundary_ephemeral.sql`

Apply the base first and the advanced overlay second in disposable PostgreSQL/Supabase-style test environments only.

## Locked schema inventory

The base candidate owns exactly these shared tables:

- `accounts`
- `profiles`
- `products`
- `content_metadata`
- `entitlements`
- `progress`
- `sync_state`
- `privacy_requests`

Every table above must keep RLS enabled. No separate-security-domain table may be introduced through this candidate.

## Locked client policy inventory

The base fixture keeps these reviewed client policies and no silent additions:

- account: own-row select and locale-only update path;
- profile: same-account select/insert/update;
- entitlement: same-account read only, server-authoritative mutation;
- progress: exact account/profile/product select/insert/update with exact-product entitlement proof;
- sync state: exact account/profile/product select/insert/update with exact-product entitlement proof;
- privacy request: own select plus pending-only insert; lifecycle completion remains server-authoritative;
- products/content metadata: explicit public-release read only.

The advanced overlay does **not** redefine schema or RLS policies. It removes direct `authenticated` insert/update privileges from `progress` and `sync_state` and introduces exactly one reviewed server-mediated primitive: `public.sync_progress_ephemeral(...)`.

## Locked authority boundary

The composed candidate must preserve all of the following:

- authentication is never equivalent to product entitlement;
- entitlement proof is exact-account + exact-product;
- entitlement authority is `server_verified`;
- revoked or expired entitlement fails closed;
- the browser/mobile client cannot mutate entitlement state;
- the advanced sync primitive is `SECURITY INVOKER`, never `SECURITY DEFINER`;
- the sync primitive is executable by `trusted_server` only and explicitly unavailable to `public`, `anon`, and `authenticated`;
- direct client progress/sync mutation is revoked in the advanced model;
- stale progress may merge monotonically, while future revisions fail closed;
- no client-supplied premium/entitlement claim becomes authority;
- Happy Me, Senior/Hello Today, Mind Bloom, Opinie, Smart CV Tailor, and Domowe Finanse remain separate security domains.

## Deterministic drift gate

Run:

```bash
python scripts/test-rse-consumer-schema-policy-drift.py
```

The gate fails if the reviewed table inventory, RLS inventory, policy inventory, advanced-overlay role boundary, sync-function scope, entitlement invariants, or security-domain separation drifts.

This gate complements rather than replaces:

- `scripts/test-rse-consumer-supabase-sql-fixture.py`
- `scripts/test-rse-consumer-supabase-advanced-static.py`
- disposable PostgreSQL runtime tests.

## Promotion rule

A green synthetic candidate is **not** authorization to deploy. Promotion to a real Supabase project remains owner-gated and requires an explicit deployment decision plus a fresh review of secrets, environment isolation, retention, backup/export, observability, and rollback.

Until that approval exists, this candidate remains a deterministic pre-deployment artifact only.
