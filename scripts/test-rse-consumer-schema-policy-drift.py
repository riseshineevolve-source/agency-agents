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

base_tables = set(re.findall(r"create table public\.([a-z_]+)\s*\(", base))
assert base_tables == expected_tables, (
    "base schema drift: expected tables "
    f"{sorted(expected_tables)}, got {sorted(base_tables)}"
)

enabled_rls = set(
    re.findall(r"alter table public\.([a-z_]+) enable row level security;", base)
)
assert enabled_rls == expected_tables, (
    "RLS drift: every candidate table must have row level security enabled"
)

expected_policies = {
    ("accounts_select_own", "accounts", "select"),
    ("accounts_update_own", "accounts", "update"),
    ("profiles_select_own", "profiles", "select"),
    ("profiles_insert_own", "profiles", "insert"),
    ("profiles_update_own", "profiles", "update"),
    ("entitlements_select_own", "entitlements", "select"),
    ("progress_select_own_product", "progress", "select"),
    ("progress_insert_own_product", "progress", "insert"),
    ("progress_update_own_product", "progress", "update"),
    ("sync_state_select_own_product", "sync_state", "select"),
    ("sync_state_insert_own_product", "sync_state", "insert"),
    ("sync_state_update_own_product", "sync_state", "update"),
    ("privacy_requests_select_own", "privacy_requests", "select"),
    ("privacy_requests_insert_own", "privacy_requests", "insert"),
    ("products_public_read", "products", "select"),
    ("content_metadata_public_read", "content_metadata", "select"),
}

base_policies = set(
    re.findall(
        r"create policy ([a-z0-9_]+) on public\.([a-z_]+) for (select|insert|update|delete)",
        base,
    )
)
assert base_policies == expected_policies, (
    "policy inventory drift: base fixture no longer matches the reviewed v0 set"
)

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
