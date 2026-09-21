#!/usr/bin/env python3
"""Synthetic tests for RSE Consumer privacy/account lifecycle boundaries."""

A = "00000000-0000-4000-8000-000000000001"
B = "00000000-0000-4000-8000-000000000002"

records = [
    {"kind": "profile", "account_id": A, "product_id": None, "value": "A-profile"},
    {"kind": "progress", "account_id": A, "product_id": "world_01", "value": "completed"},
    {"kind": "progress", "account_id": A, "product_id": "world_02", "value": "not_started"},
    {"kind": "profile", "account_id": B, "product_id": None, "value": "B-profile"},
    {"kind": "progress", "account_id": B, "product_id": "world_02", "value": "in_progress"},
]


def enumerate_owner_records(account_id):
    return [r for r in records if r["account_id"] == account_id]


def change_email(account_row, new_email):
    out = dict(account_row)
    out["email"] = new_email
    return out


def deletion_state_after_offline_sync(server_state, offline_claim):
    authoritative = {"requested", "in_progress", "completed"}
    if server_state in authoritative:
        return server_state
    return offline_claim


def link_guest(existing, guest, link_key, applied):
    if link_key in applied:
        return existing, applied, False
    merged = max(existing or "not_started", guest, key={"not_started": 0, "in_progress": 1, "completed": 2}.get)
    return merged, applied | {link_key}, True


def link_purchase(entitlements, account_id, product_id, provider_ref_hash):
    if not account_id or product_id not in {"world_01", "world_02", "gentle_steps_christmas"}:
        raise ValueError("unknown account/product")
    key = (account_id, product_id, provider_ref_hash)
    if any(e["key"] == key for e in entitlements):
        return entitlements, False
    return entitlements + [{"key": key, "account_id": account_id, "product_id": product_id}], True


# Export/deletion enumeration never crosses account boundary.
a_rows = enumerate_owner_records(A)
assert len(a_rows) == 3
assert all(r["account_id"] == A for r in a_rows)
assert not any(r["account_id"] == B for r in a_rows)

# Stable account ID survives email changes and remains ownership key.
account = {"account_id": A, "email": "synthetic-a@example.invalid"}
changed = change_email(account, "synthetic-a-new@example.invalid")
assert changed["account_id"] == A
assert enumerate_owner_records(changed["account_id"]) == a_rows

# Offline client cannot cancel authoritative deletion lifecycle.
assert deletion_state_after_offline_sync("requested", "active") == "requested"
assert deletion_state_after_offline_sync("in_progress", "active") == "in_progress"
assert deletion_state_after_offline_sync("completed", "active") == "completed"

# Explicit guest link is idempotent and only moves progress, not ownership.
applied = set()
state, applied, changed_link = link_guest("in_progress", "completed", "guest-link-1", applied)
assert state == "completed" and changed_link is True
state2, applied2, changed_link2 = link_guest(state, "completed", "guest-link-1", applied)
assert state2 == "completed" and applied2 == applied and changed_link2 is False

# Verified purchase linking is exact-product and idempotent.
ents = []
ents, created = link_purchase(ents, A, "world_01", "synthetic-hash-01")
assert created is True and len(ents) == 1
ents2, created2 = link_purchase(ents, A, "world_01", "synthetic-hash-01")
assert created2 is False and ents2 == ents
assert not any(e["product_id"] == "world_02" for e in ents)

try:
    link_purchase(ents, A, "ghost_product", "synthetic-hash-x")
except ValueError as exc:
    assert "unknown account/product" in str(exc)
else:
    raise AssertionError("unknown product purchase link was accepted")

# Shared-consumer lifecycle deliberately excludes separate security domains.
separate_domains = {"happy_me", "senior", "mind_bloom", "opinie", "smart_cv_tailor", "domowe_finanse"}
shared_products = {r["product_id"] for r in a_rows if r["product_id"]}
assert shared_products.isdisjoint(separate_domains)

print("PASS: privacy lifecycle, stable ownership, idempotent linking, separate-domain boundary")
