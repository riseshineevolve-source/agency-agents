#!/usr/bin/env python3
"""Deterministic synthetic validator for the RSE Consumer identity/entitlement contract."""
from __future__ import annotations
import json, sys
from pathlib import Path

ALLOWED_LOCALES={"en","pl-PL"}
ALLOWED_STATES={"not_started","in_progress","completed"}
ALLOWED_AUTHORITY={"server_verified"}

def validate(data):
    errors=[]
    if data.get("schema_version")!="0.1.0":
        errors.append("unsupported schema_version")
    accounts={a.get("account_id") for a in data.get("accounts",[])}
    if None in accounts or len(accounts)!=len(data.get("accounts",[])):
        errors.append("invalid or duplicate account_id")
    for a in data.get("accounts",[]):
        if a.get("locale") not in ALLOWED_LOCALES:
            errors.append("unsupported account locale")
    products={p.get("product_id") for p in data.get("products",[])}
    if None in products or len(products)!=len(data.get("products",[])):
        errors.append("invalid or duplicate product_id")

    profiles={}
    for p in data.get("profiles",[]):
        pid=p.get("profile_id")
        if not pid or pid in profiles:
            errors.append("invalid or duplicate profile_id"); continue
        if p.get("account_id") not in accounts:
            errors.append("profile references unknown account")
        if p.get("locale") not in ALLOWED_LOCALES:
            errors.append("unsupported profile locale")
        profiles[pid]=p.get("account_id")

    progress_keys=set()
    for row in data.get("progress",[]):
        pid=row.get("profile_id"); product=row.get("product_id"); item=row.get("content_item_id")
        if pid not in profiles:
            errors.append("progress references unknown profile")
        if product not in products:
            errors.append("progress references unknown product")
        if row.get("state") not in ALLOWED_STATES:
            errors.append("invalid progress state")
        if not isinstance(row.get("sync_revision"),int) or row.get("sync_revision")<0:
            errors.append("invalid sync_revision")
        key=(pid,product,item)
        if None in key or key in progress_keys:
            errors.append("invalid or duplicate progress key")
        progress_keys.add(key)

    ent_keys=set()
    for e in data.get("entitlements",[]):
        aid=e.get("account_id"); product=e.get("product_id"); et=e.get("entitlement_type")
        if aid not in accounts:
            errors.append("entitlement references unknown account")
        if product not in products:
            errors.append("entitlement references unknown product")
        if e.get("authority") not in ALLOWED_AUTHORITY:
            errors.append("entitlement is not server-authoritative")
        if not e.get("external_purchase_ref_hash"):
            errors.append("missing purchase reference hash")
        key=(aid,product,et)
        if None in key or key in ent_keys:
            errors.append("invalid or duplicate entitlement key")
        ent_keys.add(key)

    # Contract invariant: identity does not imply product ownership.
    # A valid fixture must demonstrate at least one authenticated account lacking
    # an entitlement for at least one known product.
    if accounts and products:
        has_missing_scope=any(
            not any(e.get("account_id")==aid and e.get("product_id")==product and e.get("revoked_at") is None
                    for e in data.get("entitlements",[]))
            for aid in accounts for product in products
        )
        if not has_missing_scope:
            errors.append("fixture does not prove product-scoped entitlement separation")
    return errors

def main():
    if len(sys.argv)!=2:
        raise SystemExit("usage: validate-rse-consumer-contract.py FIXTURE.json")
    data=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors=validate(data)
    if errors:
        for e in errors: print("ERROR:",e)
        raise SystemExit(1)
    print("PASS: RSE consumer synthetic identity/entitlement contract")

if __name__=="__main__":
    main()
