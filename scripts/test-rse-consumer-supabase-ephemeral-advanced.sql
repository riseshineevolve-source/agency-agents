\set ON_ERROR_STOP on

-- Advanced Gate A-H checks for the synthetic Consumer Platform prototype.
-- Requires the base fixture + supabase_sync_boundary_ephemeral.sql overlay.
-- All identities and records are synthetic.

-- Gate A: RLS is active on every private table and direct client sync writes are closed.
select count(*) = 6 as ok
from pg_class c
join pg_namespace n on n.oid = c.relnamespace
where n.nspname = 'public'
  and c.relname in ('accounts','profiles','entitlements','progress','sync_state','privacy_requests')
  and c.relrowsecurity \gset
\if :ok
\else
  \echo 'FAIL: one or more private tables do not have RLS enabled'
  \quit 1
\endif

select not has_table_privilege('authenticated', 'public.progress', 'INSERT')
   and not has_table_privilege('authenticated', 'public.progress', 'UPDATE')
   and not has_table_privilege('authenticated', 'public.sync_state', 'INSERT')
   and not has_table_privilege('authenticated', 'public.sync_state', 'UPDATE') as ok \gset
\if :ok
\else
  \echo 'FAIL: authenticated retains direct progress/sync mutation privileges'
  \quit 1
\endif

select not has_function_privilege(
  'authenticated',
  'public.sync_progress_ephemeral(uuid,uuid,text,text,bigint,text)',
  'EXECUTE'
) as ok \gset
\if :ok
\else
  \echo 'FAIL: authenticated can execute server-only sync function'
  \quit 1
\endif

select has_function_privilege(
  'trusted_server',
  'public.sync_progress_ephemeral(uuid,uuid,text,text,bigint,text)',
  'EXECUTE'
) as ok \gset
\if :ok
\else
  \echo 'FAIL: trusted server cannot execute sync function'
  \quit 1
\endif

-- Account A client context.
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-4000-8000-000000000001', false);

-- Gate B5: own profile create/update remains allowed.
begin;
insert into public.profiles(id, account_id, display_name)
values (
  '00000000-0000-4000-8000-000000000102',
  auth.uid(),
  'Synthetic A2'
);
update public.profiles
set display_name = 'Synthetic A2 updated'
where id = '00000000-0000-4000-8000-000000000102';
select count(*) = 1 as ok
from public.profiles
where id = '00000000-0000-4000-8000-000000000102'
  and display_name = 'Synthetic A2 updated' \gset
\if :ok
\else
  \echo 'FAIL: own profile lifecycle path failed'
  \quit 1
\endif
rollback;

-- Gate B6: cross-profile update affects no rows.
with changed as (
  update public.profiles
  set display_name = 'forbidden'
  where id = '00000000-0000-4000-8000-000000000201'
  returning 1
)
select count(*) = 0 as ok from changed \gset
\if :ok
\else
  \echo 'FAIL: cross-profile update escaped owner isolation'
  \quit 1
\endif

-- Gate B7: guessed foreign profile owner cannot be inserted by Account A.
begin;
\set ON_ERROR_STOP off
insert into public.profiles(id, account_id, display_name)
values (
  '00000000-0000-4000-8000-000000000199',
  '00000000-0000-4000-8000-000000000002',
  'forbidden'
);
\if :ERROR
  \echo 'PASS: guessed foreign profile owner denied'
\else
  \echo 'FAIL: guessed foreign profile owner unexpectedly inserted'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

-- Gate B4: profile ownership reassignment fails closed.
begin;
\set ON_ERROR_STOP off
update public.profiles
set account_id = '00000000-0000-4000-8000-000000000002'
where id = '00000000-0000-4000-8000-000000000101';
\if :ERROR
  \echo 'PASS: profile ownership reassignment denied'
\else
  \echo 'FAIL: profile ownership reassignment unexpectedly succeeded'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

-- Gate C5/E1: direct client progress/sync mutation is closed in the advanced model.
begin;
\set ON_ERROR_STOP off
update public.progress
set product_id = 'world_02'
where id = '00000000-0000-4000-8000-000000002001';
\if :ERROR
  \echo 'PASS: direct cross-product progress update denied'
\else
  \echo 'FAIL: direct progress update unexpectedly succeeded'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

begin;
\set ON_ERROR_STOP off
update public.sync_state
set revision = 999
where id = '00000000-0000-4000-8000-000000003001';
\if :ERROR
  \echo 'PASS: client cannot forge sync revision'
\else
  \echo 'FAIL: client forged sync revision directly'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

-- Gate D4/D5: client cannot extend, revoke, or delete its entitlement.
begin;
\set ON_ERROR_STOP off
update public.entitlements
set valid_until = now() + interval '365 days'
where account_id = auth.uid() and product_id = 'world_01';
\if :ERROR
  \echo 'PASS: client entitlement extension denied'
\else
  \echo 'FAIL: client entitlement extension unexpectedly succeeded'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

begin;
\set ON_ERROR_STOP off
delete from public.entitlements
where account_id = auth.uid() and product_id = 'world_01';
\if :ERROR
  \echo 'PASS: client entitlement delete denied'
\else
  \echo 'FAIL: client entitlement delete unexpectedly succeeded'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

reset role;

-- Gate D6/D7: trusted server may activate the exact synthetic product only.
begin;
set role trusted_server;
update public.entitlements
set status = 'active', revoked_at = null, valid_until = now() + interval '30 days'
where account_id = '00000000-0000-4000-8000-000000000001'
  and product_id = 'world_02';
reset role;
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-4000-8000-000000000001', false);
select count(*) = 1 as ok
from public.progress
where product_id = 'world_02' \gset
\if :ok
\else
  \echo 'FAIL: exact trusted-server World 02 activation did not authorize World 02'
  \quit 1
\endif
select count(*) = 1 as ok
from public.progress
where product_id = 'world_01' \gset
\if :ok
\else
  \echo 'FAIL: exact World 02 activation disturbed World 01 authorization'
  \quit 1
\endif
reset role;
rollback;

-- Gate D8: trusted-server revocation immediately fails closed for protected state.
begin;
set role trusted_server;
update public.entitlements
set status = 'revoked', revoked_at = now()
where account_id = '00000000-0000-4000-8000-000000000001'
  and product_id = 'world_01';
reset role;
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-4000-8000-000000000001', false);
select count(*) = 0 as ok
from public.progress
where product_id = 'world_01' \gset
\if :ok
\else
  \echo 'FAIL: revoked entitlement still authorized protected state'
  \quit 1
\endif
reset role;
rollback;

-- Gate D9: expired entitlement fails closed.
begin;
set role trusted_server;
update public.entitlements
set status = 'active', revoked_at = null, valid_until = now() - interval '1 second'
where account_id = '00000000-0000-4000-8000-000000000001'
  and product_id = 'world_01';
reset role;
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-4000-8000-000000000001', false);
select count(*) = 0 as ok
from public.progress
where product_id = 'world_01' \gset
\if :ok
\else
  \echo 'FAIL: expired entitlement still authorized protected state'
  \quit 1
\endif
reset role;
rollback;

-- Gate D10: unsupported authority cannot become authoritative even server-side.
begin;
set role trusted_server;
\set ON_ERROR_STOP off
update public.entitlements
set authority = 'client_claimed'
where account_id = '00000000-0000-4000-8000-000000000001'
  and product_id = 'world_01';
\if :ERROR
  \echo 'PASS: unsupported entitlement authority rejected'
\else
  \echo 'FAIL: unsupported entitlement authority unexpectedly accepted'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on
reset role;

-- Gate E4/E5: atomic trusted-server sync rejects future revisions and performs
-- monotonic stale merge without downgrading completed progress.
begin;
set role trusted_server;
select outcome = 'applied'
   and server_revision = 3
   and merged_progress_state = 'completed' as ok
from public.sync_progress_ephemeral(
  '00000000-0000-4000-8000-000000000001',
  '00000000-0000-4000-8000-000000000101',
  'world_01',
  'mission_01',
  2,
  'completed'
) \gset
\if :ok
\else
  \echo 'FAIL: current-revision sync did not apply completed progress'
  \quit 1
\endif

select outcome = 'merged_stale'
   and server_revision = 4
   and merged_progress_state = 'completed' as ok
from public.sync_progress_ephemeral(
  '00000000-0000-4000-8000-000000000001',
  '00000000-0000-4000-8000-000000000101',
  'world_01',
  'mission_01',
  2,
  'in_progress'
) \gset
\if :ok
\else
  \echo 'FAIL: stale weaker progress was not merged monotonically'
  \quit 1
\endif

select progress_state = 'completed' and revision = 4 as ok
from public.progress
where account_id = '00000000-0000-4000-8000-000000000001'
  and profile_id = '00000000-0000-4000-8000-000000000101'
  and product_id = 'world_01'
  and item_id = 'mission_01' \gset
\if :ok
\else
  \echo 'FAIL: completed progress was downgraded or revision mismatch occurred'
  \quit 1
\endif
rollback;

begin;
set role trusted_server;
select outcome = 'invalid_future_revision' and server_revision = 2 as ok
from public.sync_progress_ephemeral(
  '00000000-0000-4000-8000-000000000001',
  '00000000-0000-4000-8000-000000000101',
  'world_01',
  'mission_01',
  99,
  'completed'
) \gset
\if :ok
\else
  \echo 'FAIL: future client revision did not fail closed'
  \quit 1
\endif
select revision = 2 as ok
from public.sync_state
where account_id = '00000000-0000-4000-8000-000000000001'
  and profile_id = '00000000-0000-4000-8000-000000000101'
  and product_id = 'world_01' \gset
\if :ok
\else
  \echo 'FAIL: future revision mutated server sync state'
  \quit 1
\endif
rollback;

-- Gate E2/E3: wrong owner/profile or non-entitled product cannot enter server sync.
begin;
set role trusted_server;
select outcome = 'invalid_scope' as ok
from public.sync_progress_ephemeral(
  '00000000-0000-4000-8000-000000000001',
  '00000000-0000-4000-8000-000000000201',
  'world_01',
  'mission_01',
  2,
  'completed'
) \gset
\if :ok
\else
  \echo 'FAIL: cross-owner profile did not fail closed at sync boundary'
  \quit 1
\endif
select outcome = 'not_entitled' as ok
from public.sync_progress_ephemeral(
  '00000000-0000-4000-8000-000000000001',
  '00000000-0000-4000-8000-000000000101',
  'world_02',
  'mission_01',
  5,
  'completed'
) \gset
\if :ok
\else
  \echo 'FAIL: wrong-product sync did not fail closed'
  \quit 1
\endif
rollback;
reset role;

-- Gate F5: server export/delete enumeration is explicitly owner-scoped across
-- shared-consumer tables; separate domains are excluded by the static contract.
set role trusted_server;
select
  (select count(*) from public.accounts where id = '00000000-0000-4000-8000-000000000001') = 1
  and (select count(*) from public.profiles where account_id = '00000000-0000-4000-8000-000000000001') = 1
  and (select count(*) from public.entitlements where account_id = '00000000-0000-4000-8000-000000000001') = 2
  and (select count(*) from public.progress where account_id = '00000000-0000-4000-8000-000000000001') = 3
  and (select count(*) from public.sync_state where account_id = '00000000-0000-4000-8000-000000000001') = 2
  and (select count(*) from public.privacy_requests where account_id = '00000000-0000-4000-8000-000000000001') = 1
  as ok \gset
\if :ok
\else
  \echo 'FAIL: server Account A enumeration is not deterministically owner-scoped'
  \quit 1
\endif
reset role;

-- Gate G2/G3/G4: public catalog visibility cannot mutate metadata or widen private state.
select not has_table_privilege('anon', 'public.products', 'INSERT')
   and not has_table_privilege('anon', 'public.products', 'UPDATE')
   and not has_table_privilege('anon', 'public.products', 'DELETE')
   and not has_table_privilege('authenticated', 'public.products', 'INSERT')
   and not has_table_privilege('authenticated', 'public.content_metadata', 'UPDATE') as ok \gset
\if :ok
\else
  \echo 'FAIL: public metadata is writable by a client role'
  \quit 1
\endif

set role anon;
select count(*) = 1 as ok from public.products where product_id = 'world_02' \gset
\if :ok
\else
  \echo 'FAIL: public World 02 catalog metadata unexpectedly hidden'
  \quit 1
\endif
reset role;
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-4000-8000-000000000001', false);
select count(*) = 0 as ok from public.progress where product_id = 'world_02' \gset
\if :ok
\else
  \echo 'FAIL: public catalog visibility widened paid product authorization'
  \quit 1
\endif
reset role;

-- Gate H7: composite ownership provenance rejects cross-owner profile/account rows
-- even from the synthetic trusted server.
begin;
set role trusted_server;
\set ON_ERROR_STOP off
insert into public.progress(
  id, account_id, profile_id, product_id, item_id, progress_state, revision
) values (
  '00000000-0000-4000-8000-000000002097',
  '00000000-0000-4000-8000-000000000001',
  '00000000-0000-4000-8000-000000000201',
  'world_01',
  'forbidden_cross_owner',
  'in_progress',
  1
);
\if :ERROR
  \echo 'PASS: composite ownership provenance rejected cross-owner row'
\else
  \echo 'FAIL: cross-owner progress provenance unexpectedly accepted'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on
reset role;

\echo 'PASS: advanced ephemeral PostgreSQL exercised remaining owner, entitlement, revision, privacy, public-metadata and provenance boundaries'
