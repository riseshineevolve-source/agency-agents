# RSE Consumer Platform — Supabase SQL Security Test Plan v0

Status: SYNTHETIC TEST PLAN / NO REMOTE EXECUTION AUTHORIZED
Updated: 2026-09-20

## Purpose

Define the executable security test matrix that a future Supabase implementation must pass before any shared RSE Consumer backend is activated for real users or real products.

This plan intentionally uses synthetic identities and product IDs only. It does not authorize project creation, migrations, remote SQL execution, paid resources, real auth users, Play Billing, or migration of any existing product data.

Authoritative companion:
- `RSE_CONSUMER_SUPABASE_RLS_POLICY_MAP_V0.md`

## Synthetic actors

- Account A: `00000000-0000-4000-8000-000000000001`
- Account B: `00000000-0000-4000-8000-000000000002`
- Profile A1: synthetic profile owned by Account A
- Profile B1: synthetic profile owned by Account B
- anon actor
- trusted server/service role used only in explicitly server-authoritative tests

Products:
- `world_01`
- `world_02`
- `gentle_steps_christmas`

Entitlement baseline:
- Account A: valid `world_01` only
- Account B: valid `world_02` only

No fixture may contain a real email, person, transaction, child data, CV data, finance data, private Mind Bloom data, or real purchase token.

## Test harness direction

Preferred future implementation:
- run against an ephemeral/local Postgres/Supabase test database;
- apply the candidate migration from a clean schema;
- seed synthetic fixtures;
- execute each case in a transaction that is rolled back;
- switch actor/JWT claims explicitly between Account A, Account B, anon, and trusted server;
- never use production data or a production project for policy tests.

The harness may use pgTAP, SQL assertions, or a repository-native equivalent. The pass/fail semantics below are mandatory even if the syntax changes.

## Gate A — RLS enabled and grants narrow

For every private table (`accounts`, `profiles`, `progress`, `sync_state`, `entitlements`, `privacy_requests` or their approved replacements):

1. RLS is enabled.
2. anon has no SELECT/INSERT/UPDATE/DELETE.
3. authenticated has only the explicitly required operations.
4. authenticated has no entitlement INSERT/UPDATE/DELETE.
5. PUBLIC has no write grants.
6. no migration creates broad authenticated `USING (true)` / `WITH CHECK (true)` policies on private rows.
7. any privileged function is absent by default; if later introduced, it has a separately reviewed threat model and narrow EXECUTE grants.

Expected: all pass before any row-level behavior tests are meaningful.

## Gate B — account/profile isolation

### B1 own account read
Actor: Account A
Action: SELECT Account A account row
Expected: 1 own row visible.

### B2 cross-account read
Actor: Account A
Action: SELECT Account B account row
Expected: 0 rows.

### B3 own safe preference update
Actor: Account A
Action: update an approved safe field such as locale on Account A
Expected: allowed if the final schema exposes that field directly.

### B4 ownership reassignment blocked
Actor: Account A
Action: attempt to change immutable ownership/account ID
Expected: denied / zero affected / constraint failure.

### B5 own profile CRUD
Actor: Account A
Action: read/create/update Profile A1 within the approved profile lifecycle
Expected: allowed only for Account A.

### B6 cross-profile access
Actor: Account A
Action: read/update/delete Profile B1
Expected: denied.

### B7 guessed profile ID
Actor: Account A
Action: use a known Profile B1 UUID directly in a mutation
Expected: denied even when the identifier is valid.

## Gate C — product-scoped progress isolation

### C1 own World 01 progress
Actor: Account A
Target: Profile A1 + `world_01`
Expected: allowed when the final product state is eligible for cloud sync.

### C2 cross-user progress
Actor: Account A
Target: Profile B1 + `world_02`
Expected: denied.

### C3 same user, wrong product
Actor: Account A
Target: Profile A1 + `world_02`
Baseline entitlement: Account A owns only `world_01`
Expected: protected World 02 cloud state denied.

### C4 product substitution on insert
Actor: Account A
Action: submit a row whose profile belongs to A but whose protected product is `world_02`
Expected: denied if World 02 requires entitlement.

### C5 product substitution on update
Actor: Account A
Action: mutate a valid World 01 progress row and change `product_id` to `world_02`
Expected: denied by policy and/or immutable constraint.

### C6 locale does not widen access
Actor: Account A
Action: switch locale to `pl-PL` and retry World 02 access
Expected: still denied.

### C7 email change does not widen access
Actor: Account A
Action: change auth email in the test identity while keeping immutable account UUID
Expected: ownership and product access unchanged.

## Gate D — entitlement authority

### D1 own entitlement status read
Actor: Account A
Action: SELECT own `world_01` entitlement status
Expected: allowed only if the final UI needs direct status read.

### D2 cross-user entitlement read
Actor: Account A
Action: SELECT Account B `world_02` entitlement
Expected: denied.

### D3 client self-grant
Actor: Account A
Action: INSERT `(A, world_02, authority=server_verified)`
Expected: denied.

### D4 client extension
Actor: Account A
Action: UPDATE own entitlement validity/expiry/revocation/authority
Expected: denied.

### D5 client revoke/delete
Actor: Account A
Action: DELETE own entitlement
Expected: denied.

### D6 trusted server exact grant
Actor: trusted server
Action: create a valid synthetic entitlement for exact `(A, world_02)`
Expected: allowed only through the approved server-authoritative path.

### D7 exact-product proof
After D6, Actor A may access protected World 02 state.
Expected: World 01 and World 02 decisions remain independent.

### D8 revoked entitlement
Actor: trusted server marks Account A World 01 entitlement revoked.
Actor: Account A retries protected World 01 cloud access.
Expected: denied.

### D9 expired entitlement
Seed an expired synthetic entitlement.
Expected: protected access denied.

### D10 client-claimed authority
Seed/attempt authority other than approved server verification.
Expected: does not satisfy protected access.

## Gate E — sync state and offline conflict boundary

RLS covers ownership/product scope. Revision/conflict logic must be tested at the atomic sync boundary.

### E1 own sync state
Actor: Account A
Target: Profile A1 + World 01
Expected: permitted only through the approved sync contract.

### E2 cross-user sync
Actor: Account A
Target: Profile B1
Expected: denied.

### E3 mixed-product packet
Actor: Account A
Packet scope: World 01
Rows include World 02
Expected: whole incompatible mutation fails closed; no World 02 row is changed.

### E4 stale revision
Server revision newer than client base revision.
Expected: explicit conflict/retry result; no silent overwrite.

### E5 monotonic completion
Server progress `completed`, client stale state `in_progress` or `not_started`.
Expected: remains `completed`.

### E6 entitlement never merges from client
Client packet includes an ownership/premium/entitlement claim.
Expected: ignored/rejected; no authoritative entitlement row changes.

## Gate F — privacy lifecycle

### F1 own privacy request
Actor: Account A
Action: INSERT export/delete request for Account A
Expected: allowed.

### F2 forged owner privacy request
Actor: Account A
Action: INSERT request with Account B owner ID
Expected: denied.

### F3 cross-account privacy read
Actor: Account A
Action: SELECT Account B privacy request
Expected: denied.

### F4 client completion forgery
Actor: Account A
Action: UPDATE request to completed / alter server lifecycle state
Expected: denied.

### F5 server enumeration isolation
Actor: trusted server running approved export/delete workflow for Account A
Expected: only shared-consumer records owned by Account A are enumerated.

### F6 separate-domain exclusion
Account A deletion workflow must not implicitly delete or enumerate data from:
- Happy Me;
- Senior / Hello Today;
- Mind Bloom;
- Opinie;
- Smart CV Tailor;
- Domowe Finanse.

Expected: separate security domains remain untouched unless a separate explicit product-specific workflow exists.

## Gate G — public product/content metadata

### G1 anon public metadata read
Actor: anon
Action: SELECT explicitly released non-sensitive product/content metadata
Expected: allowed only through approved public table/view/policy.

### G2 anon private-row probe
Actor: anon
Action: query profiles/progress/sync/entitlements/privacy requests
Expected: 0 rows / permission denied.

### G3 public metadata mutation
Actor: anon or authenticated client
Action: INSERT/UPDATE/DELETE catalog/content release metadata
Expected: denied.

### G4 public catalog is not entitlement
Actor: Account A or anon can read World 02 catalog metadata.
Expected: this does not grant protected World 02 progress/content access.

## Gate H — wildcard/policy escape regression

Static migration review plus executable tests must reject:

1. a global `is_premium` flag used as product authorization;
2. email-based owner policies;
3. policies that trust client locale/device/app route as ownership evidence;
4. authenticated `USING (true)` / `WITH CHECK (true)` on private tables;
5. client write grants on entitlements;
6. cross-product UPDATE of product-scoped rows;
7. foreign-key/provenance paths that permit a Profile A row to point at Account B state;
8. SECURITY DEFINER helper functions with broad EXECUTE, caller-controlled owner IDs, or unsafe search path;
9. public exposure of purchase references beyond safe hashes/status required by UX;
10. any dependency on data from the separate Happy Me, Senior, Mind Bloom, Opinie, CV, or finance domains.

## Suggested SQL assertion shape

Exact syntax is intentionally deferred until the candidate schema exists. A future harness should make each assertion explicit, for example:

```sql
-- Pseudocode only; do not run remotely from this document.
begin;
-- set authenticated JWT/sub claim to synthetic Account A
-- assert Account A can see profile A1
-- assert Account A cannot see profile B1
-- assert Account A cannot insert/update/delete entitlement rows
-- assert World 01 entitlement does not authorize World 02
rollback;
```

Tests should fail if they cannot establish the intended actor context. Do not treat a harness running accidentally as database owner/service role as a PASS.

## Performance/advisor verification before activation

After functional RLS tests pass in a local/ephemeral environment, verify:
- policy predicates have supporting indexes;
- no unindexed foreign keys on policy-critical ownership/product relationships;
- no accidental duplicate permissive policies widen access;
- Security Advisor / equivalent shows no policy-critical finding;
- query plans for own progress/entitlement lookup do not require unbounded scans at expected scale.

This remains AUTO_VERIFY work. Applying SQL to a real project remains separately gated.

## Exit criteria

A candidate Supabase migration is eligible for reviewed remote activation only when:
- every Gate A-H mandatory case is executable and green locally/ephemerally;
- the migration contains no secrets or real user data;
- the final table/policy names are checkpointed;
- entitlement mutation is server-only;
- exact product isolation is proven;
- privacy export/delete isolation is proven;
- no separate security domain is pulled into the shared consumer backend;
- cost/backend creation gate has been explicitly passed by the owner.
