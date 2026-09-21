#!/usr/bin/env python3
"""Deterministic drift checks for the synthetic Consumer Platform SQL contract.

This test is static and synthetic-only. It does not connect to Supabase/Postgres.
It verifies that the base RLS fixture and the advanced sync overlay still compose
into the reviewed v0 candidate without silently changing schema or client policy
surface.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "orchestration/architecture/fixtures/consumer-platform-v0"
BASE_PATH = FIXTURE_DIR / "supabase_rls_ephemeral.sql"
OVERLAY_PATH = FIXTURE_DIR / "supabase_sync_boundary_ephemeral.sql"


def normalize(raw: str) -> str:
    raw = re.sub(r"/\*.*?\*/", "", raw, flags=re.S)
    raw = re.sub(r"--[^\n]*", "", raw)
    return re.sub(r"\s+", " ", raw).strip().lower()


base = normalize(BASE_PATH.read_text(encoding="utf-8"))
overlay = normalize(OVERLAY_PATH.read_text(encoding="utf-8"))
combined = f"{base} {overlay}"


def extract_create_table_bodies(sql: str) -> dict[str, str]:
    """Return each CREATE TABLE body without relying on formatting.

    The candidate is intentionally small and locked. Comparing the normalized
    table bodies makes a column, type, default, foreign-key, UNIQUE or CHECK
    change a deliberate contract-review event rather than silent drift.
    """
    pattern = re.compile(r"create table public\.([a-z_]+)\s*\(")
    tables: dict[str, str] = {}
    for match in pattern.finditer(sql):
        depth = 1
        cursor = match.end()
        start = cursor
        while cursor < len(sql) and depth:
            if sql[cursor] == "(":
                depth += 1
            elif sql[cursor] == ")":
                depth -= 1
            cursor += 1
        assert depth == 0, f"unterminated CREATE TABLE for {match.group(1)}"
        assert sql[cursor:cursor + 1] == ";", (
            f"CREATE TABLE for {match.group(1)} must end at its closing semicolon"
        )
        tables[match.group(1)] = sql[start:cursor - 1].strip()
    return tables


expected_table_bodies = {
    "products": """
        product_id text primary key,
        is_public boolean not null default false,
        requires_entitlement boolean not null default true
    """,
    "content_metadata": """
        content_id text primary key,
        product_id text not null references public.products(product_id),
        locale text not null check (locale in ('en', 'pl-PL')),
        is_public boolean not null default false
    """,
    "accounts": """
        id uuid primary key,
        locale text not null default 'en' check (locale in ('en', 'pl-PL')),
        created_at timestamptz not null default now()
    """,
    "profiles": """
        id uuid primary key,
        account_id uuid not null references public.accounts(id) on delete cascade,
        display_name text not null,
        created_at timestamptz not null default now(),
        unique (id, account_id)
    """,
    "entitlements": """
        id uuid primary key,
        account_id uuid not null references public.accounts(id) on delete cascade,
        product_id text not null references public.products(product_id),
        authority text not null check (authority in ('server_verified')),
        status text not null check (status in ('active', 'revoked', 'expired')),
        valid_until timestamptz,
        revoked_at timestamptz,
        created_at timestamptz not null default now(),
        unique (account_id, product_id)
    """,
    "progress": """
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
    """,
    "sync_state": """
        id uuid primary key,
        account_id uuid not null references public.accounts(id) on delete cascade,
        profile_id uuid not null,
        product_id text not null references public.products(product_id),
        revision bigint not null default 0 check (revision >= 0),
        updated_at timestamptz not null default now(),
        foreign key (profile_id, account_id)
          references public.profiles(id, account_id) on delete cascade,
        unique (profile_id, product_id)
    """,
    "privacy_requests": """
        id uuid primary key,
        account_id uuid not null references public.accounts(id) on delete cascade,
        request_type text not null check (request_type in ('export', 'delete')),
        status text not null default 'pending' check (status in ('pending', 'processing', 'completed', 'failed')),
        created_at timestamptz not null default now()
    """,
}

expected_tables = {
    "accounts",
    "content_metadata",
    "entitlements",
    "privacy_requests",
    "products",
    "profiles",
    "progress",
    "sync_state",
}

base_table_bodies = extract_create_table_bodies(base)
assert set(base_table_bodies) == expected_tables, (
    "base schema drift: expected tables "
    f"{sorted(expected_tables)}, got {sorted(base_table_bodies)}"
)
assert base_table_bodies == {
    table: normalize(body) for table, body in expected_table_bodies.items()
}, (
    "base schema drift: candidate column, type, default or constraint inventory "
    "no longer matches the reviewed v0 definition"
)

enabled_rls = set(
    re.findall(r"alter table public\.([a-z_]+) enable row level security;", base)
)
assert enabled_rls == expected_tables, (
    "RLS drift: every candidate table must have row level security enabled"
)

expected_policies = {
    ("accounts_select_own", "accounts", "select", "authenticated"),
    ("accounts_update_own", "accounts", "update", "authenticated"),
    ("profiles_select_own", "profiles", "select", "authenticated"),
    ("profiles_insert_own", "profiles", "insert", "authenticated"),
    ("profiles_update_own", "profiles", "update", "authenticated"),
    ("entitlements_select_own", "entitlements", "select", "authenticated"),
    ("progress_select_own_product", "progress", "select", "authenticated"),
    ("progress_insert_own_product", "progress", "insert", "authenticated"),
    ("progress_update_own_product", "progress", "update", "authenticated"),
    ("sync_state_select_own_product", "sync_state", "select", "authenticated"),
    ("sync_state_insert_own_product", "sync_state", "insert", "authenticated"),
    ("sync_state_update_own_product", "sync_state", "update", "authenticated"),
    ("privacy_requests_select_own", "privacy_requests", "select", "authenticated"),
    ("privacy_requests_insert_own", "privacy_requests", "insert", "authenticated"),
    ("products_public_read", "products", "select", "anon,authenticated"),
    ("content_metadata_public_read", "content_metadata", "select", "anon,authenticated"),
}

base_policies = set(
    re.findall(
        r"create policy ([a-z0-9_]+) on public\.([a-z_]+) for (select|insert|update|delete) to ([a-z, ]+?) (?:using|with check)",
        base,
    )
)
base_policies = {
    (name, table, operation, roles.replace(" ", ""))
    for name, table, operation, roles in base_policies
}
assert base_policies == expected_policies, (
    "policy identity drift: base fixture no longer matches the reviewed v0 set"
)

assert not re.search(r"\b(create|alter)\s+trigger\b", combined), (
    "trigger drift: the reviewed candidate contains no trigger-based authority path"
)
assert not re.search(r"\bcreate\s+(or\s+replace\s+)?function\b", base), (
    "base fixture drift: functions belong only to the reviewed advanced overlay"
)

expected_indexes = {
    "idx_profiles_account_id",
    "idx_entitlements_account_product",
    "idx_progress_account_product_profile",
    "idx_sync_state_account_product_profile",
    "idx_privacy_requests_account_id",
}
base_indexes = set(re.findall(r"create index ([a-z0-9_]+) on public\.", base))
assert base_indexes == expected_indexes, "index inventory drift in candidate schema"

for required_grant in (
    "grant select on public.accounts to authenticated;",
    "grant update (locale) on public.accounts to authenticated;",
    "grant select, insert, update on public.profiles to authenticated;",
    "grant select on public.entitlements to authenticated;",
    "grant select, insert, update on public.progress to authenticated;",
    "grant select, insert, update on public.sync_state to authenticated;",
    "grant select, insert on public.privacy_requests to authenticated;",
    "grant select on public.products, public.content_metadata to anon, authenticated;",
):
    assert required_grant in base, f"client grant drift: missing {required_grant}"

# The overlay is an authorization-boundary overlay, not a schema migration.
for forbidden in (
    r"\bcreate\s+table\b",
    r"\balter\s+table\b",
    r"\bdrop\s+table\b",
    r"\bcreate\s+policy\b",
    r"\bdrop\s+policy\b",
    r"\bsecurity\s+definer\b",
):
    assert not re.search(forbidden, overlay), f"advanced overlay schema/policy drift: {forbidden}"

# The only client capability removed by the overlay is direct progress/sync write.
for table in ("progress", "sync_state"):
    assert (
        f"revoke insert, update on public.{table} from authenticated;" in overlay
    ), f"advanced overlay must revoke direct authenticated writes on {table}"

assert not re.search(
    r"grant\s+[^;]*(insert|update|delete|execute)[^;]*\s+to\s+(anon|authenticated)\b",
    overlay,
), "advanced overlay must not add client write/execute capability"

functions = re.findall(
    r"create or replace function public\.([a-z_]+)\s*\(", overlay
)
assert functions == ["sync_progress_ephemeral"], (
    "advanced overlay may define only the reviewed sync_progress_ephemeral function"
)

sig = "public.sync_progress_ephemeral(uuid, uuid, text, text, bigint, text)"
assert re.search(
    r"create or replace function public\.sync_progress_ephemeral\(\s*"
    r"p_account_id uuid, p_profile_id uuid, p_product_id text, p_item_id text, "
    r"p_client_base_revision bigint, p_client_progress_state text\s*\)",
    overlay,
), (
    "sync function signature drift: no overloads or caller-controlled authority inputs"
)
assert f"grant execute on function {sig} to trusted_server;" in overlay
assert re.search(
    rf"revoke all on function {re.escape(sig)} from public, anon, authenticated;",
    overlay,
), "sync function must remain unavailable to client roles"

# Candidate composition must preserve the locked product/account entitlement model.
for required in (
    "e.account_id = auth.uid()",
    "e.authority = 'server_verified'",
    "e.status = 'active'",
    "e.revoked_at is null",
    "e.valid_until is null or e.valid_until > now()",
    "security invoker",
):
    assert required in combined, f"candidate invariant missing after composition: {required}"

for separate_domain in (
    "happy_me",
    "mind_bloom",
    "hello_today",
    "opinie",
    "smart_cv",
    "domowe_finanse",
):
    assert separate_domain not in combined, (
        f"separate security domain leaked into shared Consumer candidate: {separate_domain}"
    )

print("PASS: Consumer base + advanced overlay match the reviewed schema/policy candidate")
