# RSE Consumer Platform — Ephemeral Candidate Drift-Gate Checkpoint

Status: **GREEN STRUCTURAL / SYNTHETIC ONLY / NO LIVE BACKEND**

Verified: 2026-09-21  
Candidate contract head: `deaff301895f0d23942078e698af59cceece3301`

## Candidate boundary

The candidate is the ordered, clean-database composition of:

1. `orchestration/architecture/fixtures/consumer-platform-v0/supabase_rls_ephemeral.sql`
2. `orchestration/architecture/fixtures/consumer-platform-v0/supabase_sync_boundary_ephemeral.sql`

It remains a disposable PostgreSQL/Supabase-style test artifact. It is not a
production migration and must not be applied to a live Supabase project.

## Deterministic result

The local synthetic gate passed these exact checks:

- `validate-rse-consumer-contract.py` against `synthetic_consumer.valid.json`;
- `test-rse-consumer-contract.py`;
- `test-rse-consumer-security-boundaries.py`;
- `test-rse-consumer-privacy-lifecycle.py`;
- `test-rse-consumer-supabase-policy-contract.py`;
- `test-rse-consumer-supabase-sql-fixture.py`;
- `test-rse-consumer-supabase-advanced-static.py`;
- `test-rse-consumer-schema-policy-drift.py`.

The drift guard now fails closed on changes to the complete candidate table
inventory, columns, types, defaults, constraints, indexes, RLS enablement,
policy names/operations/roles, trigger surface, function inventory/signature,
client grants, advanced sync authority boundary, exact entitlement predicates,
and separate-domain exclusion.

## Ephemeral runtime and security result

The existing disposable PostgreSQL 16 baseline remains the runtime evidence for
the unchanged SQL composition: `RSE Consumer Advanced Gates` run
`35541200417` at `9baf778da210b4c354dcb10e19d452f9524df8e6` passed both the
static guard and the base-plus-overlay runtime suite. It exercised clean apply,
RLS role behavior, cross-user and cross-product denial, revoked/expired
entitlement denial, client entitlement mutation denial, trusted-server-only
monotonic sync, future revision rejection, privacy/export isolation, public
metadata boundaries, and owner/profile provenance.

This local workstation has no PostgreSQL client, server, Docker, or WSL runtime,
so it did not contact any database. The hardened drift guard is included in the
same `RSE Consumer Advanced Gates` CI boundary for a fresh disposable PostgreSQL
execution after this checkpoint is pushed.

## External gates and next safe slice

Still external/owner-gated:

- live Supabase project creation or SQL deployment;
- production purchase verification, secrets, retention/deletion executor and
  privacy/legal review;
- real World 01 source approval and product conversion;
- any consolidation of Happy Me, Senior, Mind Bloom, Opinie, Smart CV Tailor or
  Domowe Finanse into the shared consumer domain.

No further Consumer Platform repository-side slice is selected. The current
architecture's next listed safe slice was this candidate drift gate; real
product/app work remains gated by source approval and the listed owner decisions.
