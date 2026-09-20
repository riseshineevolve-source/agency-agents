#!/usr/bin/env python3
"""Deterministic synthetic policy tests for the future RSE Consumer Supabase RLS layer.

No database connection is used. This is the executable reference matrix that a later
SQL/pgTAP harness must reproduce before any remote backend activation.
"""

from dataclasses import dataclass
from pathlib import Path

A = "00000000-0000-4000-8000-000000000001"
B = "00000000-0000-4000-8000-000000000002"

SELECT = "select"
INSERT = "insert"
UPDATE = "update"
DELETE = "delete"

PRIVATE_TABLES = {
    "accounts",
    "profiles",
    "progress",
    "sync_state",
    "entitlements",
    "privacy_requests",
}


@dataclass(frozen=True)
class Entitlement:
    account_id: str
    product_id: str
    authority: str = "server_verified"
    revoked: bool = False
    expired: bool = False


@dataclass(frozen=True)
class Row:
    table: str
    owner_account_id: str | None = None
    product_id: str | None = None
    public: bool = False
    protected: bool = False


def valid_entitlement(actor: str, product_id: str | None, entitlements: list[Entitlement]) -> bool:
    if product_id is None:
        return False
    return any(
        e.account_id == actor
        and e.product_id == product_id
        and e.authority == "server_verified"
        and not e.revoked
        and not e.expired
        for e in entitlements
    )


def allowed(actor_role: str, actor_account_id: str | None, action: str, row: Row,
            entitlements: list[Entitlement], *, profile_delete_supported: bool = False) -> bool:
    """Reference authorization matrix. Missing/unknown state fails closed."""
    if actor_role == "trusted_server":
        return True

    if actor_role == "anon":
        return row.table in {"products", "content_metadata"} and row.public and action == SELECT

    if actor_role != "authenticated" or actor_account_id is None:
        return False

    own = row.owner_account_id == actor_account_id

    if row.table == "accounts":
        if not own:
            return False
        return action in {SELECT, UPDATE}

    if row.table == "profiles":
        if not own:
            return False
        if action in {SELECT, INSERT, UPDATE}:
            return True
        if action == DELETE:
            return profile_delete_supported
        return False

    if row.table == "progress":
        if not own or row.product_id is None:
            return False
        if row.protected and not valid_entitlement(actor_account_id, row.product_id, entitlements):
            return False
        return action in {SELECT, INSERT, UPDATE}

    if row.table == "sync_state":
        if not own or row.product_id is None:
            return False
        if row.protected and not valid_entitlement(actor_account_id, row.product_id, entitlements):
            return False
        return action in {SELECT, INSERT, UPDATE}

    if row.table == "entitlements":
        return own and action == SELECT

    if row.table == "privacy_requests":
        if not own:
            return False
        return action in {SELECT, INSERT}

    if row.table in {"products", "content_metadata"}:
        return row.public and action == SELECT

    return False


ents = [
    Entitlement(A, "world_01"),
    Entitlement(B, "world_02"),
]

# Gate A: anon/private fail closed and public metadata is read-only.
for table in PRIVATE_TABLES:
    for action in (SELECT, INSERT, UPDATE, DELETE):
        assert not allowed("anon", None, action, Row(table, owner_account_id=A), ents), (table, action)

for table in ("products", "content_metadata"):
    assert allowed("anon", None, SELECT, Row(table, public=True), ents)
    for action in (INSERT, UPDATE, DELETE):
        assert not allowed("anon", None, action, Row(table, public=True), ents)
        assert not allowed("authenticated", A, action, Row(table, public=True), ents)

# Gate B: account/profile ownership isolation.
assert allowed("authenticated", A, SELECT, Row("accounts", A), ents)
assert allowed("authenticated", A, UPDATE, Row("accounts", A), ents)
assert not allowed("authenticated", A, SELECT, Row("accounts", B), ents)
assert not allowed("authenticated", A, INSERT, Row("accounts", A), ents)
assert not allowed("authenticated", A, DELETE, Row("accounts", A), ents)

for action in (SELECT, INSERT, UPDATE):
    assert allowed("authenticated", A, action, Row("profiles", A), ents)
    assert not allowed("authenticated", A, action, Row("profiles", B), ents)
assert not allowed("authenticated", A, DELETE, Row("profiles", A), ents)
assert allowed("authenticated", A, DELETE, Row("profiles", A), ents, profile_delete_supported=True)
assert not allowed("authenticated", A, DELETE, Row("profiles", B), ents, profile_delete_supported=True)

# Gate C: own/product-scoped progress; login is not entitlement.
a_world1 = Row("progress", A, "world_01", protected=True)
a_world2 = Row("progress", A, "world_02", protected=True)
b_world2 = Row("progress", B, "world_02", protected=True)
for action in (SELECT, INSERT, UPDATE):
    assert allowed("authenticated", A, action, a_world1, ents)
    assert not allowed("authenticated", A, action, a_world2, ents)
    assert not allowed("authenticated", A, action, b_world2, ents)
assert not allowed("authenticated", A, DELETE, a_world1, ents)

# Free/non-protected product state still remains owner/product scoped.
a_free = Row("progress", A, "free_demo", protected=False)
assert allowed("authenticated", A, SELECT, a_free, ents)
assert not allowed("authenticated", B, SELECT, a_free, ents)

# Gate D: entitlements are readable-own, never client-mutable.
assert allowed("authenticated", A, SELECT, Row("entitlements", A, "world_01"), ents)
assert not allowed("authenticated", A, SELECT, Row("entitlements", B, "world_02"), ents)
for action in (INSERT, UPDATE, DELETE):
    assert not allowed("authenticated", A, action, Row("entitlements", A, "world_01"), ents)
    assert allowed("trusted_server", None, action, Row("entitlements", A, "world_01"), ents)

# Revoked/expired/client-claimed rows do not authorize protected cloud state.
assert not allowed(
    "authenticated", A, SELECT, a_world2,
    ents + [Entitlement(A, "world_02", revoked=True)],
)
assert not allowed(
    "authenticated", A, SELECT, a_world2,
    ents + [Entitlement(A, "world_02", expired=True)],
)
assert not allowed(
    "authenticated", A, SELECT, a_world2,
    ents + [Entitlement(A, "world_02", authority="client_claimed")],
)
assert allowed(
    "authenticated", A, SELECT, a_world2,
    ents + [Entitlement(A, "world_02")],
)

# Gate E: sync state is owner + exact product scoped and client cannot delete it by default.
a_sync = Row("sync_state", A, "world_01", protected=True)
b_sync = Row("sync_state", B, "world_02", protected=True)
for action in (SELECT, INSERT, UPDATE):
    assert allowed("authenticated", A, action, a_sync, ents)
    assert not allowed("authenticated", A, action, b_sync, ents)
assert not allowed("authenticated", A, DELETE, a_sync, ents)

# Gate F: privacy requests are own create/read only; server owns lifecycle completion.
assert allowed("authenticated", A, INSERT, Row("privacy_requests", A), ents)
assert allowed("authenticated", A, SELECT, Row("privacy_requests", A), ents)
assert not allowed("authenticated", A, INSERT, Row("privacy_requests", B), ents)
assert not allowed("authenticated", A, SELECT, Row("privacy_requests", B), ents)
assert not allowed("authenticated", A, UPDATE, Row("privacy_requests", A), ents)
assert not allowed("authenticated", A, DELETE, Row("privacy_requests", A), ents)
assert allowed("trusted_server", None, UPDATE, Row("privacy_requests", A), ents)

# Missing actor/product/unknown resources fail closed.
assert not allowed("authenticated", None, SELECT, Row("accounts", A), ents)
assert not allowed("authenticated", A, SELECT, Row("progress", A, None, protected=True), ents)
assert not allowed("authenticated", A, SELECT, Row("unknown", A), ents)

# Durable docs must retain the locked invariants this executable matrix represents.
root = Path(__file__).resolve().parents[1]
policy_doc = (root / "orchestration/architecture/RSE_CONSUMER_SUPABASE_RLS_POLICY_MAP_V0.md").read_text(encoding="utf-8")
test_plan = (root / "orchestration/architecture/RSE_CONSUMER_SUPABASE_SQL_TEST_PLAN_V0.md").read_text(encoding="utf-8")
for needle in (
    "Authentication identifies the account. It does not grant product ownership.",
    "client entitlement mutation denial",
    "no wildcard premium authorization",
    "NO DEPLOYMENT AUTHORIZATION",
):
    assert needle in policy_doc, f"missing policy invariant: {needle}"

for needle in (
    "client self-grant",
    "same user, wrong product",
    "separate-domain exclusion",
    "authenticated `USING (true)` / `WITH CHECK (true)`",
):
    assert needle.lower() in test_plan.lower(), f"missing SQL test-plan gate: {needle}"

print("PASS: synthetic Supabase RLS policy matrix + SQL test-plan invariants")
