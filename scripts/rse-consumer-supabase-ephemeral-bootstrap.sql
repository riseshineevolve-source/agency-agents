\set ON_ERROR_STOP on

-- Test-only Supabase role/auth shim for disposable PostgreSQL CI.
-- This file is never a production migration.

create role anon nologin;
create role authenticated nologin;
create role trusted_server nologin bypassrls;

create schema auth;

create function auth.uid()
returns uuid
language sql
stable
as $$
  select nullif(current_setting('request.jwt.claim.sub', true), '')::uuid
$$;

grant usage on schema auth to anon, authenticated, trusted_server;
grant execute on function auth.uid() to anon, authenticated, trusted_server;
