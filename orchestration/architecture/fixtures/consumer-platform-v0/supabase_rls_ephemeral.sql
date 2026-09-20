-- RSE Consumer Platform — ephemeral Supabase/Postgres RLS prototype
-- SYNTHETIC ONLY. DO NOT APPLY TO A LIVE PROJECT.
--
-- This file exists solely to exercise the locked authorization contract against
-- a disposable PostgreSQL database. It assumes Supabase-style roles `anon` and
-- `authenticated` plus auth.uid(). The CI harness creates those test-only roles
-- and a synthetic auth.uid() shim before applying this file.

begin;

-- Harden the public schema surface for this synthetic prototype.
revoke create on schema public from public;
grant usage on schema public to anon, authenticated, trusted_server;

create table public.products (
  product_id text primary key,
  is_public boolean not null default false,
  requires_entitlement boolean not null default true
);

create table public.content_metadata (
  content_id text primary key,
  product_id text not null references public.products(product_id),
  locale text not null check (locale in ('en', 'pl-PL')),
  is_public boolean not null default false
);

create table public.accounts (
  id uuid primary key,
  locale text not null default 'en' check (locale in ('en', 'pl-PL')),
  created_at timestamptz not null default now()
);

create table public.profiles (
  id uuid primary key,
  account_id uuid not null references public.accounts(id) on delete cascade,
  display_name text not null,
  created_at timestamptz not null default now(),
  unique (id, account_id)
);

create table public.entitlements (
  id uuid primary key,
  account_id uuid not null references public.accounts(id) on delete cascade,
  product_id text not null references public.products(product_id),
  authority text not null check (authority in ('server_verified')),
  status text not null check (status in ('active', 'revoked', 'expired')),
  valid_until timestamptz,
  revoked_at timestamptz,
  created_at timestamptz not null default now(),
  unique (account_id, product_id)
);

create table public.progress (
  id uuid primary key,
  account_id uuid not null references public.accounts(id) on delete cascade,
  profile_id uuid not null,
  product_id text not null references public.products(product_id),
  item_id text not null,
  progress_state text not null check (progress_state in ('not_started', 'in_progress', 'completed')),
  revision bigint not null default 0 check (revision >= 0),
  updated_at timestamptz not null default now(),
  foreign key (profile_id, account_id)
    references public.profiles(id, account_id) on delete cascade,
  unique (profile_id, product_id, item_id)
);

create table public.sync_state (
  id uuid primary key,
  account_id uuid not null references public.accounts(id) on delete cascade,
  profile_id uuid not null,
  product_id text not null references public.products(product_id),
  revision bigint not null default 0 check (revision >= 0),
  updated_at timestamptz not null default now(),
  foreign key (profile_id, account_id)
    references public.profiles(id, account_id) on delete cascade,
  unique (profile_id, product_id)
);

create table public.privacy_requests (
  id uuid primary key,
  account_id uuid not null references public.accounts(id) on delete cascade,
  request_type text not null check (request_type in ('export', 'delete')),
  status text not null default 'pending' check (status in ('pending', 'processing', 'completed', 'failed')),
  created_at timestamptz not null default now()
);

-- Policy-critical indexes. These are deliberately explicit even where a unique
-- constraint also creates an index so the intended access paths are reviewable.
create index idx_profiles_account_id on public.profiles(account_id);
create index idx_entitlements_account_product on public.entitlements(account_id, product_id);
create index idx_progress_account_product_profile on public.progress(account_id, product_id, profile_id);
create index idx_sync_state_account_product_profile on public.sync_state(account_id, product_id, profile_id);
create index idx_privacy_requests_account_id on public.privacy_requests(account_id);

alter table public.accounts enable row level security;
alter table public.profiles enable row level security;
alter table public.entitlements enable row level security;
alter table public.progress enable row level security;
alter table public.sync_state enable row level security;
alter table public.privacy_requests enable row level security;
alter table public.products enable row level security;
alter table public.content_metadata enable row level security;

-- Accounts: client can read its own row and update locale only. Column grants
-- below prevent changing identity/ownership columns through the client role.
create policy accounts_select_own
  on public.accounts for select to authenticated
  using (id = auth.uid());

create policy accounts_update_own
  on public.accounts for update to authenticated
  using (id = auth.uid())
  with check (id = auth.uid());

-- Profiles: same-account only. No client DELETE policy in v0.
create policy profiles_select_own
  on public.profiles for select to authenticated
  using (account_id = auth.uid());

create policy profiles_insert_own
  on public.profiles for insert to authenticated
  with check (account_id = auth.uid());

create policy profiles_update_own
  on public.profiles for update to authenticated
  using (account_id = auth.uid())
  with check (account_id = auth.uid());

-- Entitlements are server authoritative. Clients may read their own status only.
create policy entitlements_select_own
  on public.entitlements for select to authenticated
  using (account_id = auth.uid());

-- Exact-product authorization predicate for protected cloud state is intentionally
-- inlined in progress/sync policies so the prototype does not introduce a
-- privileged helper function or SECURITY DEFINER escape hatch.
create policy progress_select_own_product
  on public.progress for select to authenticated
  using (
    account_id = auth.uid()
    and exists (
      select 1 from public.profiles p
      where p.id = progress.profile_id
        and p.account_id = progress.account_id
        and p.account_id = auth.uid()
    )
    and exists (
      select 1 from public.products pr
      where pr.product_id = progress.product_id
        and (
          pr.requires_entitlement = false
          or exists (
            select 1 from public.entitlements e
            where e.account_id = auth.uid()
              and e.product_id = progress.product_id
              and e.authority = 'server_verified'
              and e.status = 'active'
              and e.revoked_at is null
              and (e.valid_until is null or e.valid_until > now())
          )
        )
    )
  );

create policy progress_insert_own_product
  on public.progress for insert to authenticated
  with check (
    account_id = auth.uid()
    and exists (
      select 1 from public.profiles p
      where p.id = progress.profile_id
        and p.account_id = progress.account_id
        and p.account_id = auth.uid()
    )
    and exists (
      select 1 from public.products pr
      where pr.product_id = progress.product_id
        and (
          pr.requires_entitlement = false
          or exists (
            select 1 from public.entitlements e
            where e.account_id = auth.uid()
              and e.product_id = progress.product_id
              and e.authority = 'server_verified'
              and e.status = 'active'
              and e.revoked_at is null
              and (e.valid_until is null or e.valid_until > now())
          )
        )
    )
  );

create policy progress_update_own_product
  on public.progress for update to authenticated
  using (
    account_id = auth.uid()
    and exists (
      select 1 from public.profiles p
      where p.id = progress.profile_id
        and p.account_id = progress.account_id
        and p.account_id = auth.uid()
    )
    and exists (
      select 1 from public.products pr
      where pr.product_id = progress.product_id
        and (
          pr.requires_entitlement = false
          or exists (
            select 1 from public.entitlements e
            where e.account_id = auth.uid()
              and e.product_id = progress.product_id
              and e.authority = 'server_verified'
              and e.status = 'active'
              and e.revoked_at is null
              and (e.valid_until is null or e.valid_until > now())
          )
        )
    )
  )
  with check (
    account_id = auth.uid()
    and exists (
      select 1 from public.profiles p
      where p.id = progress.profile_id
        and p.account_id = progress.account_id
        and p.account_id = auth.uid()
    )
    and exists (
      select 1 from public.products pr
      where pr.product_id = progress.product_id
        and (
          pr.requires_entitlement = false
          or exists (
            select 1 from public.entitlements e
            where e.account_id = auth.uid()
              and e.product_id = progress.product_id
              and e.authority = 'server_verified'
              and e.status = 'active'
              and e.revoked_at is null
              and (e.valid_until is null or e.valid_until > now())
          )
        )
    )
  );

create policy sync_state_select_own_product
  on public.sync_state for select to authenticated
  using (
    account_id = auth.uid()
    and exists (
      select 1 from public.profiles p
      where p.id = sync_state.profile_id
        and p.account_id = sync_state.account_id
        and p.account_id = auth.uid()
    )
    and exists (
      select 1 from public.products pr
      where pr.product_id = sync_state.product_id
        and (
          pr.requires_entitlement = false
          or exists (
            select 1 from public.entitlements e
            where e.account_id = auth.uid()
              and e.product_id = sync_state.product_id
              and e.authority = 'server_verified'
              and e.status = 'active'
              and e.revoked_at is null
              and (e.valid_until is null or e.valid_until > now())
          )
        )
    )
  );

create policy sync_state_insert_own_product
  on public.sync_state for insert to authenticated
  with check (
    account_id = auth.uid()
    and exists (
      select 1 from public.profiles p
      where p.id = sync_state.profile_id
        and p.account_id = sync_state.account_id
        and p.account_id = auth.uid()
    )
    and exists (
      select 1 from public.products pr
      where pr.product_id = sync_state.product_id
        and (
          pr.requires_entitlement = false
          or exists (
            select 1 from public.entitlements e
            where e.account_id = auth.uid()
              and e.product_id = sync_state.product_id
              and e.authority = 'server_verified'
              and e.status = 'active'
              and e.revoked_at is null
              and (e.valid_until is null or e.valid_until > now())
          )
        )
    )
  );

create policy sync_state_update_own_product
  on public.sync_state for update to authenticated
  using (
    account_id = auth.uid()
    and exists (
      select 1 from public.profiles p
      where p.id = sync_state.profile_id
        and p.account_id = sync_state.account_id
        and p.account_id = auth.uid()
    )
    and exists (
      select 1 from public.products pr
      where pr.product_id = sync_state.product_id
        and (
          pr.requires_entitlement = false
          or exists (
            select 1 from public.entitlements e
            where e.account_id = auth.uid()
              and e.product_id = sync_state.product_id
              and e.authority = 'server_verified'
              and e.status = 'active'
              and e.revoked_at is null
              and (e.valid_until is null or e.valid_until > now())
          )
        )
    )
  )
  with check (
    account_id = auth.uid()
    and exists (
      select 1 from public.profiles p
      where p.id = sync_state.profile_id
        and p.account_id = sync_state.account_id
        and p.account_id = auth.uid()
    )
    and exists (
      select 1 from public.products pr
      where pr.product_id = sync_state.product_id
        and (
          pr.requires_entitlement = false
          or exists (
            select 1 from public.entitlements e
            where e.account_id = auth.uid()
              and e.product_id = sync_state.product_id
              and e.authority = 'server_verified'
              and e.status = 'active'
              and e.revoked_at is null
              and (e.valid_until is null or e.valid_until > now())
          )
        )
    )
  );

-- Privacy workflow: client may create/read only its own request. Server owns all
-- lifecycle status mutations and the authoritative export/delete enumeration.
create policy privacy_requests_select_own
  on public.privacy_requests for select to authenticated
  using (account_id = auth.uid());

create policy privacy_requests_insert_own
  on public.privacy_requests for insert to authenticated
  with check (account_id = auth.uid() and status = 'pending');

-- Public release metadata is readable only when explicitly marked public.
create policy products_public_read
  on public.products for select to anon, authenticated
  using (is_public = true);

create policy content_metadata_public_read
  on public.content_metadata for select to anon, authenticated
  using (is_public = true);

-- Start from deny-all table privileges, then grant only the client operations the
-- product contract permits. Trusted server is test-only here; a future Supabase
-- implementation must use its reviewed server-authoritative boundary instead.
revoke all on public.accounts, public.profiles, public.entitlements,
  public.progress, public.sync_state, public.privacy_requests,
  public.products, public.content_metadata
  from public, anon, authenticated;

grant select on public.accounts to authenticated;
grant update (locale) on public.accounts to authenticated;

grant select, insert, update on public.profiles to authenticated;
grant select on public.entitlements to authenticated;
grant select, insert, update on public.progress to authenticated;
grant select, insert, update on public.sync_state to authenticated;
grant select, insert on public.privacy_requests to authenticated;
grant select on public.products, public.content_metadata to anon, authenticated;

grant select, insert, update, delete on public.accounts, public.profiles,
  public.entitlements, public.progress, public.sync_state, public.privacy_requests,
  public.products, public.content_metadata
  to trusted_server;

commit;
