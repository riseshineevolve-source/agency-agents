-- RSE Consumer Platform — advanced ephemeral sync boundary
-- SYNTHETIC ONLY. DO NOT APPLY TO A LIVE PROJECT.
--
-- This overlay is applied only after the base RLS prototype in disposable CI.
-- It models the approved v0 direction that ordinary clients do not directly
-- mutate progress/sync rows; a future reviewed server boundary owns atomic sync.

begin;

-- Direct browser/mobile writes are removed for the advanced Gate E harness.
revoke insert, update on public.progress from authenticated;
revoke insert, update on public.sync_state from authenticated;

-- Test-only server-mediated atomic progress sync. This function is deliberately
-- SECURITY INVOKER and executable only by the synthetic trusted_server role.
-- It is not a production API and accepts no entitlement/premium claims.
create or replace function public.sync_progress_ephemeral(
  p_account_id uuid,
  p_profile_id uuid,
  p_product_id text,
  p_item_id text,
  p_client_base_revision bigint,
  p_client_progress_state text
)
returns table (
  outcome text,
  server_revision bigint,
  merged_progress_state text
)
language plpgsql
security invoker
set search_path = public, pg_temp
as $$
declare
  v_server_revision bigint;
  v_current_state text;
  v_merged_state text;
  v_next_revision bigint;
begin
  if p_client_base_revision is null or p_client_base_revision < 0 then
    return query select 'invalid_revision'::text, null::bigint, null::text;
    return;
  end if;

  if p_client_progress_state not in ('not_started', 'in_progress', 'completed') then
    return query select 'invalid_progress_state'::text, null::bigint, null::text;
    return;
  end if;

  if not exists (
    select 1
    from public.profiles p
    where p.id = p_profile_id
      and p.account_id = p_account_id
  ) then
    return query select 'invalid_scope'::text, null::bigint, null::text;
    return;
  end if;

  if not exists (
    select 1
    from public.products pr
    where pr.product_id = p_product_id
      and (
        pr.requires_entitlement = false
        or exists (
          select 1
          from public.entitlements e
          where e.account_id = p_account_id
            and e.product_id = p_product_id
            and e.authority = 'server_verified'
            and e.status = 'active'
            and e.revoked_at is null
            and (e.valid_until is null or e.valid_until > now())
        )
      )
  ) then
    return query select 'not_entitled'::text, null::bigint, null::text;
    return;
  end if;

  select s.revision
    into v_server_revision
  from public.sync_state s
  where s.account_id = p_account_id
    and s.profile_id = p_profile_id
    and s.product_id = p_product_id
  for update;

  if not found then
    return query select 'missing_stream'::text, null::bigint, null::text;
    return;
  end if;

  if p_client_base_revision > v_server_revision then
    return query select 'invalid_future_revision'::text, v_server_revision, null::text;
    return;
  end if;

  select p.progress_state
    into v_current_state
  from public.progress p
  where p.account_id = p_account_id
    and p.profile_id = p_profile_id
    and p.product_id = p_product_id
    and p.item_id = p_item_id
  for update;

  if found then
    v_merged_state := case
      when v_current_state = 'completed' or p_client_progress_state = 'completed' then 'completed'
      when v_current_state = 'in_progress' or p_client_progress_state = 'in_progress' then 'in_progress'
      else 'not_started'
    end;
  else
    v_merged_state := p_client_progress_state;
  end if;

  v_next_revision := v_server_revision + 1;

  if v_current_state is null then
    insert into public.progress(
      id, account_id, profile_id, product_id, item_id, progress_state, revision
    ) values (
      gen_random_uuid(), p_account_id, p_profile_id, p_product_id, p_item_id,
      v_merged_state, v_next_revision
    );
  else
    update public.progress
    set progress_state = v_merged_state,
        revision = v_next_revision,
        updated_at = now()
    where account_id = p_account_id
      and profile_id = p_profile_id
      and product_id = p_product_id
      and item_id = p_item_id;
  end if;

  update public.sync_state
  set revision = v_next_revision,
      updated_at = now()
  where account_id = p_account_id
    and profile_id = p_profile_id
    and product_id = p_product_id;

  return query
  select
    case
      when p_client_base_revision < v_server_revision then 'merged_stale'
      else 'applied'
    end,
    v_next_revision,
    v_merged_state;
end;
$$;

revoke all on function public.sync_progress_ephemeral(uuid, uuid, text, text, bigint, text)
  from public, anon, authenticated;
grant execute on function public.sync_progress_ephemeral(uuid, uuid, text, text, bigint, text)
  to trusted_server;

commit;
