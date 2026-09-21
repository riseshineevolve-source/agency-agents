#!/usr/bin/env python3
"""Static fail-closed checks for the advanced ephemeral sync overlay.

Synthetic-only. Never connects to a database or external service.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SQL_PATH = ROOT / "orchestration/architecture/fixtures/consumer-platform-v0/supabase_sync_boundary_ephemeral.sql"
raw = SQL_PATH.read_text(encoding="utf-8")

sql = re.sub(r"/\*.*?\*/", "", raw, flags=re.S)
sql = re.sub(r"--[^\n]*", "", sql)
normalized = re.sub(r"\s+", " ", sql).strip().lower()

# The advanced contract must never introduce a privileged browser-callable path.
assert "security definer" not in normalized
assert "security invoker" in normalized
assert "set search_path = public, pg_temp" in normalized

sig = "public.sync_progress_ephemeral(uuid, uuid, text, text, bigint, text)"
assert f"grant execute on function {sig} to trusted_server;" in normalized
assert re.search(
    rf"revoke all on function {re.escape(sig)} from public, anon, authenticated;",
    normalized,
), "sync function must be explicitly unavailable to client roles"

# Direct client progress/sync writes are intentionally removed in this overlay.
for table in ("progress", "sync_state"):
    assert f"revoke insert, update on public.{table} from authenticated;" in normalized

# The server sync primitive accepts no entitlement/premium/client-authority input.
for forbidden in (
    "is_premium",
    "entitlement_claim",
    "purchase_token",
    "access_token",
    "refresh_token",
    "service_role",
    "client_secret",
):
    assert forbidden not in normalized, f"forbidden authority/secret pattern present: {forbidden}"

# Exact account/profile/product validation and entitlement proof remain explicit.
for required in (
    "p.account_id = p_account_id",
    "pr.product_id = p_product_id",
    "e.account_id = p_account_id",
    "e.product_id = p_product_id",
    "e.authority = 'server_verified'",
    "e.status = 'active'",
    "e.revoked_at is null",
):
    assert required in normalized, f"missing sync-boundary guard: {required}"

# Stale revisions may merge monotonically; future revisions must fail closed.
assert "p_client_base_revision > v_server_revision" in normalized
assert "invalid_future_revision" in normalized
assert "merged_stale" in normalized
assert "when v_current_state = 'completed' or p_client_progress_state = 'completed' then 'completed'" in normalized

# Shared Consumer Platform stays independent of separate security domains.
for separate_domain in (
    "happy_me",
    "mind_bloom",
    "hello_today",
    "opinie",
    "smart_cv",
    "domowe_finanse",
):
    assert separate_domain not in normalized, f"separate security domain leaked into advanced SQL: {separate_domain}"

print("PASS: advanced consumer sync boundary is fail-closed by static contract")
