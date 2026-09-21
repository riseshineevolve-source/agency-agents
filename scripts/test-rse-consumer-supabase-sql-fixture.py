#!/usr/bin/env python3
"""Static fail-closed checks for the synthetic RSE Consumer Supabase SQL fixture.

This test never opens a database connection. It guards the candidate SQL before the
separate ephemeral PostgreSQL job attempts to execute it.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SQL_PATH = ROOT / "orchestration/architecture/fixtures/consumer-platform-v0/supabase_rls_ephemeral.sql"
raw = SQL_PATH.read_text(encoding="utf-8")

# Remove comments so safety words in explanatory prose do not cause false positives.
sql = re.sub(r"/\*.*?\*/", "", raw, flags=re.S)
sql = re.sub(r"--[^\n]*", "", sql)
normalized = re.sub(r"\s+", " ", sql).strip().lower()

private_tables = (
    "accounts",
    "profiles",
    "entitlements",
    "progress",
    "sync_state",
    "privacy_requests",
)

for table in private_tables:
    needle = f"alter table public.{table} enable row level security;"
    assert needle in normalized, f"RLS not enabled for private table {table}"

for forbidden in (
    r"\bsecurity\s+definer\b",
    r"\busing\s*\(\s*true\s*\)",
    r"\bwith\s+check\s*\(\s*true\s*\)",
    r"\bis_premium\b",
    r"\baccess_token\b",
    r"\brefresh_token\b",
    r"\bauthorization_code\b",
    r"\bpkce\b",
    r"\bclient_secret\b",
    r"\bservice_role\b",
):
    assert not re.search(forbidden, normalized), f"forbidden SQL pattern present: {forbidden}"

# Separate security domains must not become schema dependencies of the shared consumer fixture.
for separate_domain in (
    "happy_me",
    "mind_bloom",
    "hello_today",
    "opinie",
    "smart_cv",
    "domowe_finanse",
):
    assert separate_domain not in normalized, f"separate security domain leaked into SQL: {separate_domain}"

# Authentication is necessary but never sufficient for paid product state.
for table in ("progress", "sync_state"):
    assert f"e.product_id = {table}.product_id" in normalized, f"missing exact-product entitlement check for {table}"
    assert "e.account_id = auth.uid()" in normalized, "missing exact-account entitlement check"
    assert "e.authority = 'server_verified'" in normalized, "missing server authority requirement"
    assert "e.status = 'active'" in normalized, "missing active entitlement requirement"
    assert "e.revoked_at is null" in normalized, "missing revocation fail-closed rule"
    assert "e.valid_until is null or e.valid_until > now()" in normalized, "missing expiry fail-closed rule"
    assert "pr.requires_entitlement = false" in normalized, "free/public product exception must be explicit"

# Composite ownership provenance must exist in schema, not only in application code.
assert "foreign key (profile_id, account_id) references public.profiles(id, account_id)" in normalized

# Client entitlement mutation is structurally denied: read-only grant and no write policy.
assert "grant select on public.entitlements to authenticated;" in normalized
assert not re.search(r"grant\s+[^;]*(insert|update|delete)[^;]*on\s+public\.entitlements\s+to\s+authenticated", normalized)
assert not re.search(r"create\s+policy\s+\w+\s+on\s+public\.entitlements\s+for\s+(insert|update|delete)", normalized)

# Privacy lifecycle remains client create/read only; completion is server authoritative.
assert "privacy_requests_insert_own" in normalized
assert "account_id = auth.uid() and status = 'pending'" in normalized
assert "grant select, insert on public.privacy_requests to authenticated;" in normalized
assert not re.search(r"grant\s+[^;]*(update|delete)[^;]*on\s+public\.privacy_requests\s+to\s+authenticated", normalized)

# Public release metadata is read-only to anon/authenticated and cannot imply ownership.
for table in ("products", "content_metadata"):
    assert f"create policy {table}_public_read" in normalized
    assert f"grant select on public.{table}" in normalized or "grant select on public.products, public.content_metadata" in normalized

# Product/ownership critical indexes are part of the prototype contract.
for index_name in (
    "idx_profiles_account_id",
    "idx_entitlements_account_product",
    "idx_progress_account_product_profile",
    "idx_sync_state_account_product_profile",
    "idx_privacy_requests_account_id",
):
    assert index_name in normalized, f"missing policy-supporting index {index_name}"

print("PASS: ephemeral consumer Supabase SQL fixture is fail-closed by static contract")
