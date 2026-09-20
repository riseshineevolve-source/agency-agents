# RSE Consumer Platform — Ephemeral Supabase/Postgres RLS Checkpoint

Status: VERIFIED GREEN / SYNTHETIC ONLY / NO LIVE BACKEND
Updated: 2026-09-20

## What is now durable

A concrete Supabase/Postgres-oriented RLS prototype now exists at:

`orchestration/architecture/fixtures/consumer-platform-v0/supabase_rls_ephemeral.sql`

It is deliberately synthetic and must not be applied to any live project. It translates the backend-neutral authorization contract into executable PostgreSQL tables, grants and RLS policies for:

- accounts
- profiles
- entitlements
- progress
- sync state
- privacy requests
- public product/content metadata

The prototype preserves the locked rule that authentication identity is not product ownership. Protected progress/sync access requires the exact authenticated account + exact product entitlement; a valid World 01 entitlement cannot authorize World 02.

## Security properties exercised

The disposable PostgreSQL harness verifies:

- private-table RLS is enabled;
- anon cannot read private account state;
- authenticated cannot INSERT/UPDATE/DELETE entitlements;
- public catalog/content metadata is read-only and explicitly public;
- Account A sees only Account A account/profile/privacy rows;
- cross-user profile/progress/sync/entitlement rows remain hidden;
- Account A valid World 01 entitlement allows World 01 protected state;
- Account A revoked World 02 entitlement does not allow World 02 protected state;
- free-demo product state can remain accessible without a paid entitlement while staying owner-scoped;
- Account B can access its own exact World 02 state with a valid World 02 entitlement;
- cross-product progress insertion fails closed;
- client entitlement self-grant fails closed;
- forged privacy request ownership fails closed;
- locale changes do not widen product access;
- no SECURITY DEFINER helper is introduced;
- no global `is_premium`, email-based ownership key, token field or separate security-domain dependency is present in the SQL fixture.

Static SQL contract verification additionally checks policy-supporting indexes, exact entitlement predicates, client entitlement immutability and privacy-request lifecycle grants.

## Test harness

Test-only files:

- `scripts/test-rse-consumer-supabase-sql-fixture.py`
- `scripts/rse-consumer-supabase-ephemeral-bootstrap.sql`
- `scripts/test-rse-consumer-supabase-ephemeral.sql`

The CI bootstrap creates disposable `anon`, `authenticated`, `trusted_server` roles and a synthetic `auth.uid()` shim inside a temporary PostgreSQL 16 service container. No Supabase project, remote database, real auth user, purchase token or product data is contacted.

## Verification

GitHub Actions workflow: `RSE Consumer Contract`

- run: **#7**
- run id: **35538201529**
- head: `6c5cd653c987ce6095c49896a1db968d75b0474a`
- conclusion: **SUCCESS**

Both jobs passed:

1. deterministic synthetic consumer contract + static SQL fixture checks;
2. executable RLS behavior in disposable PostgreSQL 16.

## Boundary / not authorized

This checkpoint does **not** authorize:

- creation/restoration of a Supabase project;
- applying this SQL to a live backend;
- real users or real product migration;
- Play Billing / purchase verification;
- real OAuth/provider integration;
- combining Happy Me with the shared Consumer Platform;
- World 01/World 02/Gentle Steps real-content conversion.

Happy Me, Senior, Mind Bloom, Opinie, Smart CV Tailor and Domowe Finanse remain outside this shared consumer SQL prototype according to their existing security-domain rules.

## Remaining gap before any future remote activation

The SQL harness is now real rather than purely conceptual, but the broader SQL test plan is not yet fully exhausted. Before a candidate remote migration can ever become eligible, keep extending the disposable harness until every mandatory Gate A-H case in `RSE_CONSUMER_SUPABASE_SQL_TEST_PLAN_V0.md` is executable and green, including the remaining revision/conflict and server-side privacy lifecycle cases.

No live-backend work is currently authorized.
