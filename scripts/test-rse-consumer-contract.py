#!/usr/bin/env python3
"""Fail-closed regression tests for shared RSE account + product entitlement boundaries."""
import copy, importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VALIDATOR=ROOT/"scripts"/"validate-rse-consumer-contract.py"
FIXTURE=ROOT/"orchestration"/"architecture"/"fixtures"/"consumer-platform-v0"/"synthetic_consumer.valid.json"
spec=importlib.util.spec_from_file_location("consumer_contract",VALIDATOR)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
base=json.loads(FIXTURE.read_text(encoding="utf-8"))

assert not mod.validate(base), mod.validate(base)

# Explicit business-security assertion answering the shared-account question:
A="00000000-0000-4000-8000-000000000001"
def active_entitlement(data, account_id, product_id):
    return any(e["account_id"]==account_id and e["product_id"]==product_id
               and e.get("authority")=="server_verified" and e.get("revoked_at") is None
               for e in data["entitlements"])

assert active_entitlement(base,A,"world_01") is True
assert active_entitlement(base,A,"world_02") is False

cases={}
def case(name, mutate):
    x=copy.deepcopy(base); mutate(x); cases[name]=x

case("client_self_grant",lambda d:d["entitlements"][0].update(authority="client_claimed"))
case("unknown_product",lambda d:d["entitlements"][0].update(product_id="ghost_product"))
case("unknown_account",lambda d:d["entitlements"][0].update(account_id="ghost"))
case("missing_purchase_hash",lambda d:d["entitlements"][0].update(external_purchase_ref_hash=""))
case("duplicate_entitlement_scope",lambda d:d["entitlements"].append(copy.deepcopy(d["entitlements"][0])))
case("cross_user_profile_reference",lambda d:d["profiles"][0].update(account_id="ghost"))
case("progress_unknown_product",lambda d:d["progress"][0].update(product_id="ghost_product"))
case("invalid_progress_revision",lambda d:d["progress"][0].update(sync_revision=-1))

failed=[]
for name,data in cases.items():
    errors=mod.validate(data)
    if not errors: failed.append(name)
    else: print(f"PASS fail-closed: {name} -> {errors[0]}")
if failed:
    raise SystemExit(f"Validator accepted invalid cases: {failed}")
print(f"PASS: shared account does not imply shared entitlement; {len(cases)} invalid classes rejected")
