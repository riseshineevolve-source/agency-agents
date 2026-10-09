#!/usr/bin/env python3
"""RSE Control Plane v1 status/validation.

Deterministically validates the chat registry + lane mailboxes and emits a
portfolio snapshot for GitHub Actions / n8n / human review.

No LLM, network access or repository mutation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "orchestration" / "control-plane"
REGISTRY = CONTROL / "RSE_CHAT_REGISTRY_V1.yml"
MAILBOXES = CONTROL / "mailboxes"
FREEZE = CONTROL / "RSE_UNIVERSE_FACTORY_V1_0_FREEZE.md"

NULLISH = {None, "", "null", "none", "NONE", "N/A", "n/a"}


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected YAML mapping")
    return data


def normalize_attention(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() not in {"", "null", "none", "NONE", "N/A", "n/a"}
    if isinstance(value, (list, dict, tuple, set)):
        return bool(value)
    return bool(value)


def dependency_text(item: Any) -> str:
    if isinstance(item, dict):
        lane = item.get("lane", "?")
        need = item.get("need", "")
        return f"{lane}: {need}".strip()
    return str(item)


def classify_lane_attention(blocker: Any, owner_gate: Any, dependencies: Any) -> str:
    """WF-02 deterministic precedence: BLOCKED > OWNER_GATE > DEPENDENCY > NORMAL."""
    if normalize_attention(blocker):
        return "BLOCKED"
    if normalize_attention(owner_gate):
        return "OWNER_GATE"
    if normalize_attention(dependencies):
        return "DEPENDENCY"
    return "NORMAL"


def attention_dedupe_key(
    lane_id: str, classification: str, blocker: Any, owner_gate: Any, dependencies: Any
) -> str | None:
    """Stable across unchanged hourly polls; changes on material gate/dependency drift.

    n8n keeps the last delivered key per lane in persistent workflow state.
    This function itself performs no network or state mutation.
    """
    if classification == "NORMAL":
        return None
    material = {
        "lane": lane_id,
        "classification": classification,
        "blocker": blocker,
        "owner_gate": owner_gate,
        "dependencies_needed": dependencies,
    }
    encoded = json.dumps(
        material, sort_keys=True, ensure_ascii=False, default=str, separators=(",", ":")
    ).encode("utf-8")
    return f"rse-wf02-v1:{lane_id}:{hashlib.sha256(encoded).hexdigest()[:24]}"


def validated_mailbox_paths(chats: dict[str, Any]) -> dict[str, Path]:
    """Fail closed unless all 11 registry entries have distinct, canonical mailbox paths."""
    if len(chats) != 11:
        raise ValueError(f"WF-02 requires exactly 11 registry lanes; got {len(chats)}")

    paths: dict[str, Path] = {}
    for lane_id, spec in chats.items():
        if not isinstance(lane_id, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", lane_id):
            raise ValueError(f"WF-02 invalid lane identifier: {lane_id!r}")
        if not isinstance(spec, dict):
            raise ValueError(f"WF-02 registry lane {lane_id!r} is not a mapping")
        expected = f"orchestration/control-plane/mailboxes/{lane_id}.yml"
        if spec.get("mailbox") != expected:
            raise ValueError(
                f"WF-02 unsafe or noncanonical mailbox for {lane_id}: "
                f"{spec.get('mailbox')!r}; expected {expected!r}"
            )
        mailbox = ROOT / expected
        if not mailbox.resolve().is_relative_to(MAILBOXES.resolve()):
            raise ValueError(f"WF-02 mailbox escapes root: {lane_id}")
        paths[lane_id] = mailbox

    # Physical-path uniqueness matters too: textual aliases must never double-read a mailbox.
    if len({p.resolve() for p in paths.values()}) != 11:
        raise ValueError("WF-02 mailbox paths must be unique")
    return paths


def collect() -> dict[str, Any]:
    registry = load_yaml(REGISTRY)
    chats = registry.get("chats")
    if not isinstance(chats, dict) or not chats:
        raise ValueError("chat registry has no chats")
    mailbox_paths = validated_mailbox_paths(chats)

    lanes: list[dict[str, Any]] = []
    errors: list[str] = []

    for lane_id, spec in chats.items():
        if not isinstance(spec, dict):
            errors.append(f"{lane_id}: registry entry is not a mapping")
            continue
        mailbox_rel = spec.get("mailbox")
        if not mailbox_rel:
            errors.append(f"{lane_id}: missing mailbox path")
            continue
        mailbox = mailbox_paths[lane_id]
        if not mailbox.exists():
            errors.append(f"{lane_id}: mailbox missing: {mailbox_rel}")
            continue
        data = load_yaml(mailbox)
        if data.get("lane") != lane_id:
            errors.append(
                f"{lane_id}: mailbox lane mismatch: {data.get('lane')!r}"
            )
        owner_gate = data.get("owner_gate")
        blocker = data.get("blocker")
        deps = data.get("dependencies_needed") or []
        if not isinstance(deps, list):
            errors.append(f"{lane_id}: dependencies_needed must be a list")
            deps = [str(deps)]

        classification = classify_lane_attention(blocker, owner_gate, deps)
        dedupe_key = attention_dedupe_key(
            lane_id, classification, blocker, owner_gate, deps
        )
        lanes.append(
            {
                "lane": lane_id,
                "attention_class": classification,
                "attention_dedupe_key": dedupe_key,
                "title": spec.get("title", lane_id),
                "status": data.get("status"),
                "updated": data.get("updated"),
                "milestone": data.get("milestone"),
                "blocker": blocker,
                "owner_gate": owner_gate,
                "dependencies_needed": deps,
                "next_safe_task": data.get("next_safe_task"),
                "checkpoint_reference": data.get("checkpoint_reference"),
                "owner_attention": normalize_attention(owner_gate),
                "blocked": normalize_attention(blocker),
                "has_dependencies": bool(deps),
            }
        )

    attention = [
        x["lane"]
        for x in lanes
        if x["owner_attention"] or x["blocked"]
    ]
    dependencies = [
        {"lane": x["lane"], "dependencies_needed": x["dependencies_needed"]}
        for x in lanes
        if x["has_dependencies"]
    ]

    return {
        "schema": "rse-control-plane-snapshot-v1",
        "factory_freeze": str(FREEZE.relative_to(ROOT)),
        "registry": str(REGISTRY.relative_to(ROOT)),
        "lane_count": len(lanes),
        "owner_attention_lanes": attention,
        "dependency_requests": dependencies,
        "attention_events": [
            {
                "lane": x["lane"],
                "classification": x["attention_class"],
                "dedupe_key": x["attention_dedupe_key"],
                "checkpoint_reference": x["checkpoint_reference"],
            }
            for x in lanes
            if x["attention_class"] != "NORMAL"
        ],
        "validation_errors": errors,
        "lanes": lanes,
    }


def markdown(snapshot: dict[str, Any]) -> str:
    lines = [
        "# RSE Control Plane Snapshot",
        "",
        f"Factory: **v1.0 FROZEN**",
        f"Lanes: **{snapshot['lane_count']}**",
        f"Owner attention: **{len(snapshot['owner_attention_lanes'])}**",
        f"Validation errors: **{len(snapshot['validation_errors'])}**",
        "",
        "| Lane | Status | Owner gate | Blocker | Dependencies | Next safe task |",
        "|---|---|---|---|---|---|",
    ]
    for lane in snapshot["lanes"]:
        deps = ", ".join(dependency_text(x) for x in lane["dependencies_needed"]) or "—"
        def cell(v: Any) -> str:
            if v is None:
                return "—"
            if isinstance(v, str) and v in NULLISH:
                return "—"
            return str(v).replace("|", "\\|").replace("\n", " ")
        lines.append(
            "| {lane} | {status} | {gate} | {blocker} | {deps} | {next} |".format(
                lane=cell(lane["title"]),
                status=cell(lane["status"]),
                gate=cell(lane["owner_gate"]),
                blocker=cell(lane["blocker"]),
                deps=cell(deps),
                next=cell(lane["next_safe_task"]),
            )
        )
    if snapshot["validation_errors"]:
        lines += ["", "## Validation errors", ""]
        lines += [f"- {e}" for e in snapshot["validation_errors"]]
    return "\n".join(lines) + "\n"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--json", dest="json_path")
    p.add_argument("--markdown", dest="md_path")
    p.add_argument("--validate-only", action="store_true")
    args = p.parse_args()

    snapshot = collect()
    if args.json_path and not args.validate_only:
        path = Path(args.json_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    if args.md_path and not args.validate_only:
        path = Path(args.md_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown(snapshot), encoding="utf-8")

    if snapshot["validation_errors"]:
        for err in snapshot["validation_errors"]:
            print(f"ERROR: {err}")
        return 1
    print(
        "PASS: "
        f"{snapshot['lane_count']} lanes; "
        f"{len(snapshot['owner_attention_lanes'])} owner/blocker attention lane(s); "
        f"{len(snapshot['dependency_requests'])} dependency request(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
