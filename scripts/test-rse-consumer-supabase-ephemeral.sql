\set ON_ERROR_STOP on

-- Real row-level behavior checks against a disposable PostgreSQL database.
-- All identities, product IDs and records below are synthetic.

insert into public.products(product_id, is_public, requires_entitlement) values
  ('world_01', true, true),
  ('world_02', true, true),
  ('gentle_steps_christmas', true, true),
  ('free_demo', true, false);

insert into public.content_metadata(content_id, product_id, locale, is_public) values
  ('world_01.en.public', 'world_01', 'en', true),
  ('world_01.pl.public', 'world_01', 'pl-PL', true),
  ('world_02.en.private-draft', 'world_02', 'en', false);

insert into public.accounts(id, locale) values
  ('00000000-0000-4000-8000-000000000001', 'en'),
  ('00000000-0000-4000-8000-000000000002', 'pl-PL');

insert into public.profiles(id, account_id, display_name) values
  ('00000000-0000-4000-8000-000000000101', '00000000-0000-4000-8000-000000000001', 'Synthetic A1'),
  ('00000000-0000-4000-8000-000000000201', '00000000-0000-4000-8000-000000000002', 'Synthetic B1');

insert into public.entitlements(id, account_id, product_id, authority, status, valid_until, revoked_at) values
  ('00000000-0000-4000-8000-000000001001', '00000000-0000-4000-8000-000000000001', 'world_01', 'server_verified', 'active', now() + interval '30 days', null),
  ('00000000-0000-4000-8000-000000001002', '00000000-0000-4000-8000-000000000001', 'world_02', 'server_verified', 'revoked', now() + interval '30 days', now()),
  ('00000000-0000-4000-8000-000000001003', '00000000-0000-4000-8000-000000000002', 'world_02', 'server_verified', 'active', now() + interval '30 days', null);

insert into public.progress(id, account_id, profile_id, product_id, item_id, progress_state, revision) values
  ('00000000-0000-4000-8000-000000002001', '00000000-0000-4000-8000-000000000001', '00000000-0000-4000-8000-000000000101', 'world_01', 'mission_01', 'in_progress', 2),
  ('00000000-0000-4000-8000-000000002002', '00000000-0000-4000-8000-000000000001', '00000000-0000-4000-8000-000000000101', 'world_02', 'mission_01', 'completed', 5),
  ('00000000-0000-4000-8000-000000002003', '00000000-0000-4000-8000-000000000001', '00000000-0000-4000-8000-000000000101', 'free_demo', 'demo_01', 'completed', 1),
  ('00000000-0000-4000-8000-000000002004', '00000000-0000-4000-8000-000000000002', '00000000-0000-4000-8000-000000000201', 'world_02', 'mission_01', 'in_progress', 3);

insert into public.sync_state(id, account_id, profile_id, product_id, revision) values
  ('00000000-0000-4000-8000-000000003001', '00000000-0000-4000-8000-000000000001', '00000000-0000-4000-8000-000000000101', 'world_01', 2),
  ('00000000-0000-4000-8000-000000003002', '00000000-0000-4000-8000-000000000001', '00000000-0000-4000-8000-000000000101', 'world_02', 5),
  ('00000000-0000-4000-8000-000000003003', '00000000-0000-4000-8000-000000000002', '00000000-0000-4000-8000-000000000201', 'world_02', 3);

insert into public.privacy_requests(id, account_id, request_type, status) values
  ('00000000-0000-4000-8000-000000004001', '00000000-0000-4000-8000-000000000001', 'export', 'pending'),
  ('00000000-0000-4000-8000-000000004002', '00000000-0000-4000-8000-000000000002', 'delete', 'pending');

-- Gate A: grants stay narrow before row-level behavior is exercised.
select not has_table_privilege('anon', 'public.accounts', 'SELECT') as ok \gset
\if :ok
\else
  \echo 'FAIL: anon can SELECT private accounts'
  \quit 1
\endif

select not has_table_privilege('authenticated', 'public.entitlements', 'INSERT') as ok \gset
\if :ok
\else
  \echo 'FAIL: authenticated can INSERT entitlements'
  \quit 1
\endif

select not has_table_privilege('authenticated', 'public.entitlements', 'UPDATE') as ok \gset
\if :ok
\else
  \echo 'FAIL: authenticated can UPDATE entitlements'
  \quit 1
\endif

select not has_table_privilege('authenticated', 'public.entitlements', 'DELETE') as ok \gset
\if :ok
\else
  \echo 'FAIL: authenticated can DELETE entitlements'
  \quit 1
\endif

select not has_table_privilege('authenticated', 'public.privacy_requests', 'UPDATE') as ok \gset
\if :ok
\else
  \echo 'FAIL: authenticated can forge privacy request lifecycle status'
  \quit 1
\endif

-- Gate G: anon sees explicitly public catalog/content metadata only.
set role anon;
select count(*) = 4 as ok from public.products \gset
\if :ok
\else
  \echo 'FAIL: anon public product read mismatch'
  \quit 1
\endif

select count(*) = 2 as ok from public.content_metadata \gset
\if :ok
\else
  \echo 'FAIL: anon saw private content metadata or missed public metadata'
  \quit 1
\endif
reset role;

-- Account A actor context.
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-4000-8000-000000000001', false);

-- Gate B: own/cross-account and profile isolation.
select count(*) = 1 as ok from public.accounts \gset
\if :ok
\else
  \echo 'FAIL: Account A account-row isolation'
  \quit 1
\endif

select count(*) = 1 as ok from public.profiles \gset
\if :ok
\else
  \echo 'FAIL: Account A profile isolation'
  \quit 1
\endif

-- Gate C/D: login is not entitlement. A owns World 01, has revoked World 02,
-- and may also see its free-demo row. B state remains invisible.
select count(*) = 2 as ok from public.progress \gset
\if :ok
\else
  \echo 'FAIL: Account A progress product/owner scope mismatch'
  \quit 1
\endif

select count(*) = 0 as ok from public.progress where product_id = 'world_02' \gset
\if :ok
\else
  \echo 'FAIL: revoked World 02 entitlement widened progress access'
  \quit 1
\endif

select count(*) = 1 as ok from public.entitlements \gset
\if :ok
\else
  \echo 'FAIL: Account A entitlement visibility is not own-row isolated'
  \quit 1
\endif

select count(*) = 1 as ok from public.sync_state \gset
\if :ok
\else
  \echo 'FAIL: Account A sync state product/owner scope mismatch'
  \quit 1
\endif

select count(*) = 1 as ok from public.privacy_requests \gset
\if :ok
\else
  \echo 'FAIL: Account A privacy request isolation'
  \quit 1
\endif

-- Allowed path: safe preference update and exact-entitled progress insert.
begin;
update public.accounts set locale = 'pl-PL' where id = auth.uid();
insert into public.progress(id, account_id, profile_id, product_id, item_id, progress_state, revision)
values (
  '00000000-0000-4000-8000-000000002099',
  auth.uid(),
  '00000000-0000-4000-8000-000000000101',
  'world_01',
  'mission_ephemeral',
  'in_progress',
  1
);
rollback;

-- Denied path: product substitution must fail because A has no valid World 02 entitlement.
begin;
\set ON_ERROR_STOP off
insert into public.progress(id, account_id, profile_id, product_id, item_id, progress_state, revision)
values (
  '00000000-0000-4000-8000-000000002098',
  auth.uid(),
  '00000000-0000-4000-8000-000000000101',
  'world_02',
  'mission_forbidden',
  'in_progress',
  1
);
\if :ERROR
  \echo 'PASS: cross-product progress insert denied'
\else
  \echo 'FAIL: cross-product progress insert unexpectedly succeeded'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

-- Denied path: client cannot self-grant an entitlement.
begin;
\set ON_ERROR_STOP off
insert into public.entitlements(id, account_id, product_id, authority, status)
values (
  '00000000-0000-4000-8000-000000001099',
  auth.uid(),
  'gentle_steps_christmas',
  'server_verified',
  'active'
);
\if :ERROR
  \echo 'PASS: client entitlement self-grant denied'
\else
  \echo 'FAIL: client entitlement self-grant unexpectedly succeeded'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

-- Denied path: forged privacy request for another owner fails closed.
begin;
\set ON_ERROR_STOP off
insert into public.privacy_requests(id, account_id, request_type, status)
values (
  '00000000-0000-4000-8000-000000004099',
  '00000000-0000-4000-8000-000000000002',
  'export',
  'pending'
);
\if :ERROR
  \echo 'PASS: forged privacy owner denied'
\else
  \echo 'FAIL: forged privacy owner unexpectedly succeeded'
  \quit 1
\endif
rollback;
\set ON_ERROR_STOP on

-- Locale is a preference, never an authorization key. Even after the allowed
-- locale change attempt above, World 02 remains inaccessible.
select count(*) = 0 as ok from public.progress where product_id = 'world_02' \gset
\if :ok
\else
  \echo 'FAIL: locale widened product authorization'
  \quit 1
\endif

reset role;

-- Account B proves the same physical World 02 rows are visible to the correct
-- owner with the exact valid entitlement while Account A cannot see them.
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-4000-8000-000000000002', false);
select count(*) = 1 as ok from public.progress where product_id = 'world_02' \gset
\if :ok
\else
  \echo 'FAIL: Account B cannot see own entitled World 02 progress'
  \quit 1
\endif

select count(*) = 1 as ok from public.sync_state where product_id = 'world_02' \gset
\if :ok
\else
  \echo 'FAIL: Account B cannot see own entitled World 02 sync state'
  \quit 1
\endif

select count(*) = 1 as ok from public.entitlements where product_id = 'world_02' \gset
\if :ok
\else
  \echo 'FAIL: Account B entitlement visibility mismatch'
  \quit 1
\endif
reset role;

\echo 'PASS: ephemeral PostgreSQL exercised owner isolation, exact-product entitlement, public metadata and privacy boundaries'
