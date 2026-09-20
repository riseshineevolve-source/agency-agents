#!/usr/bin/env python3
"""Backend-neutral synthetic tests for RSE Consumer authorization and offline sync rules."""

from dataclasses import dataclass

STATE_RANK = {"not_started": 0, "in_progress": 1, "completed": 2}
SUPPORTED_LOCALES = {"en", "pl-PL"}


@dataclass(frozen=True)
class Entitlement:
    account_id: str
    product_id: str
    authority: str = "server_verified"
    revoked: bool = False
    expired: bool = False


def can_access_paid(account_id: str, product_id: str, entitlements: list[Entitlement]) -> bool:
    """Exact-product access only; authentication is intentionally not ownership."""
    return any(
        e.account_id == account_id
        and e.product_id == product_id
        and e.authority == "server_verified"
        and not e.revoked
        and not e.expired
        for e in entitlements
    )


def can_mutate_profile(actor_account_id: str, owner_account_id: str) -> bool:
    return actor_account_id == owner_account_id


def can_client_mutate_entitlement(_actor_account_id: str, _product_id: str) -> bool:
    return False


def merge_progress(server_state: str, client_state: str) -> str:
    if server_state not in STATE_RANK or client_state not in STATE_RANK:
        raise ValueError("invalid progress state")
    return max((server_state, client_state), key=STATE_RANK.__getitem__)


def merge_preference(server_value: str, server_rev: int, client_value: str, client_base_rev: int, client_new_rev: int):
    if server_value not in SUPPORTED_LOCALES or client_value not in SUPPORTED_LOCALES:
        raise ValueError("unsupported locale")
    if client_base_rev > server_rev:
        raise ValueError("future client base revision")
    if client_base_rev < server_rev:
        return {"status": "conflict", "value": server_value, "revision": server_rev}
    if client_new_rev <= server_rev:
        raise ValueError("non-monotonic preference revision")
    return {"status": "merged", "value": client_value, "revision": client_new_rev}


def validate_sync_scope(packet_product_id: str, row_product_ids: list[str]) -> None:
    if any(p != packet_product_id for p in row_product_ids):
        raise ValueError("cross-product sync packet")


def link_guest_progress(existing_state: str | None, guest_state: str, link_key: str, applied_link_keys: set[str]):
    """Idempotent synthetic guest-link model. Linking never grants entitlement."""
    if link_key in applied_link_keys:
        return existing_state, applied_link_keys, False
    merged = guest_state if existing_state is None else merge_progress(existing_state, guest_state)
    return merged, applied_link_keys | {link_key}, True


def require_compatible_content_version(server_version: str, client_version: str, migration_allowed: bool) -> None:
    if server_version != client_version and not migration_allowed:
        raise ValueError("incompatible content version without migration rule")


A = "00000000-0000-4000-8000-000000000001"
B = "00000000-0000-4000-8000-000000000002"
ENTS = [
    Entitlement(A, "world_01"),
    Entitlement(B, "world_02"),
]

# Authorization: identity != entitlement.
assert can_access_paid(A, "world_01", ENTS) is True
assert can_access_paid(A, "world_02", ENTS) is False
assert can_access_paid(B, "world_02", ENTS) is True
assert can_access_paid(B, "world_01", ENTS) is False
assert can_mutate_profile(A, A) is True
assert can_mutate_profile(A, B) is False
assert can_client_mutate_entitlement(A, "world_01") is False

revoked = ENTS + [Entitlement(A, "gentle_steps_christmas", revoked=True)]
assert can_access_paid(A, "gentle_steps_christmas", revoked) is False
expired = ENTS + [Entitlement(A, "gentle_steps_christmas", expired=True)]
assert can_access_paid(A, "gentle_steps_christmas", expired) is False
client_claim = ENTS + [Entitlement(A, "world_02", authority="client_claimed")]
assert can_access_paid(A, "world_02", client_claim) is False

# Offline progress is monotonic.
assert merge_progress("not_started", "in_progress") == "in_progress"
assert merge_progress("in_progress", "completed") == "completed"
assert merge_progress("completed", "in_progress") == "completed"
assert merge_progress("completed", "not_started") == "completed"

# Preferences use explicit revisions and surface stale conflicts.
merged = merge_preference("en", 4, "pl-PL", 4, 5)
assert merged == {"status": "merged", "value": "pl-PL", "revision": 5}
conflict = merge_preference("pl-PL", 5, "en", 4, 5)
assert conflict == {"status": "conflict", "value": "pl-PL", "revision": 5}

try:
    merge_preference("en", 4, "pl-PL", 5, 6)
except ValueError as exc:
    assert "future client base revision" in str(exc)
else:
    raise AssertionError("future client revision was accepted")

# Product-scoped sync packets fail closed.
validate_sync_scope("world_01", ["world_01", "world_01"])
try:
    validate_sync_scope("world_01", ["world_01", "world_02"])
except ValueError as exc:
    assert "cross-product" in str(exc)
else:
    raise AssertionError("mixed-product sync packet was accepted")

# Guest linking is explicit/idempotent and does not imply any entitlement grant.
applied = set()
state, applied, changed = link_guest_progress("in_progress", "completed", "link-001", applied)
assert state == "completed" and changed is True
state2, applied2, changed2 = link_guest_progress(state, "completed", "link-001", applied)
assert state2 == "completed" and applied2 == applied and changed2 is False
assert can_access_paid(A, "world_02", ENTS) is False

# Content version mismatch requires an explicit migration rule.
require_compatible_content_version("1.0.0", "1.0.0", False)
try:
    require_compatible_content_version("1.1.0", "1.0.0", False)
except ValueError as exc:
    assert "incompatible content version" in str(exc)
else:
    raise AssertionError("incompatible content version was silently accepted")

print("PASS: authorization isolation + product entitlements + offline conflict rules")
