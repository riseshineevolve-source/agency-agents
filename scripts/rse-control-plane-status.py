#!/usr/bin/env python3
"""RSE Control Plane v1 status/validation.

Deterministically validates the chat registry + lane mailboxes and emits a
portfolio snapshot for GitHub Actions / n8n / human review.

No LLM, network access or repository mutation.
"""
from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timezone
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
    return True


def dependency_text(item: Any) -> str:
    if isinstance(item, dict):
        lane = item.get("lane", "?")
        need = item.get("need", "")
        return f"{lane}: {need}".strip()
    return str(item)


def mailbox_freshness(updated: Any, as_of: date) -> dict[str, Any]:
    """Date coverage is reporting evidence, never a claim that a chat is running."""
    if updated is None or (isinstance(updated, str) and not updated.strip()):
        return {"mailbox_age_days": None, "mailbox_freshness": "MISSING"}
    try:
        if isinstance(updated, datetime):
            stamp = updated
        elif isinstance(updated, date):
            stamp = updated
        elif isinstance(updated, str):
            stamp = datetime.fromisoformat(updated.strip().replace("Z", "+00:00"))
        else:
            raise ValueError("unsupported date value")
        if isinstance(stamp, datetime):
            if stamp.tzinfo is not None:
                stamp = stamp.astimezone(timezone.utc)
            stamp = stamp.date()
    except (ValueError, TypeError, OverflowError):
        return {"mailbox_age_days": None, "mailbox_freshness": "INVALID"}
    age = (as_of - stamp).days
    if age < 0:
        return {"mailbox_age_days": age, "mailbox_freshness": "UNKNOWN"}
    return {
        "mailbox_age_days": age,
        "mailbox_freshness": "STALE" if age > 7 else "RECENT",
    }


def collect(as_of: date | None = None) -> dict[str, Any]:
    as_of = as_of or datetime.now(timezone.utc).date()
    registry = load_yaml(REGISTRY)
    chats = registry.get("chats")
    if not isinstance(chats, dict) or not chats:
        raise ValueError("chat registry has no chats")

    lanes: list[dict[str, Any]] = []
    errors: list[str] = []
    warnings: list[str] = []

    for lane_id, spec in chats.items():
        if not isinstance(spec, dict):
            errors.append(f"{lane_id}: registry entry is not a mapping")
            continue
        mailbox_rel = spec.get("mailbox")
        if not mailbox_rel:
            errors.append(f"{lane_id}: missing mailbox path")
            continue
        mailbox = ROOT / str(mailbox_rel)
        if not mailbox.exists():
            errors.append(f"{lane_id}: mailbox missing: {mailbox_rel}")
            continue
        data = load_yaml(mailbox)
        freshness = mailbox_freshness(data.get("updated"), as_of)
        if freshness["mailbox_freshness"] != "RECENT":
            label = freshness["mailbox_freshness"]
            detail = (
                "updated date is in the future"
                if label == "UNKNOWN"
                else f"updated date {label.lower()}"
            )
            warnings.append(f"{lane_id}: mailbox {detail}")
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

        lanes.append(
            {
                "lane": lane_id,
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
                **freshness,
            }
        )

    # Supplemental streams are coordination/reference surfaces, not additional
    # independent core writers. They do not require lane-owned mailboxes.
    supplemental: list[dict[str, Any]] = []
    stream_specs = registry.get("supplemental_streams", {})
    if not isinstance(stream_specs, dict):
        errors.append("supplemental_streams must be a mapping")
        stream_specs = {}
    for stream_id, spec in stream_specs.items():
        if not isinstance(spec, dict):
            errors.append(f"{stream_id}: supplemental entry is not a mapping")
            continue
        supplemental.append({**spec, "stream": stream_id})

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
        "as_of": as_of.isoformat(),
        "lane_count": len(lanes),
        "owner_attention_lanes": attention,
        "dependency_requests": dependencies,
        "validation_errors": errors,
        "freshness_warnings": warnings,
        "lanes": lanes,
        "supplemental_stream_count": len(supplemental),
        "supplemental_streams": supplemental,
    }


def markdown(snapshot: dict[str, Any]) -> str:
    def cell(v: Any) -> str:
        if v is None:
            return "—"
        if isinstance(v, str) and v in NULLISH:
            return "—"
        return str(v).replace("|", "\\|").replace("\n", " ")

    lines = [
        "# RSE Control Plane Snapshot",
        "",
        f"Factory: **v1.0 FROZEN**",
        f"Lanes: **{snapshot['lane_count']}**",
        f"As of: **{snapshot['as_of']}** (mailbox dates evaluated in UTC)",
        f"Supplemental streams: **{snapshot['supplemental_stream_count']}** (not independent core writers)",
        f"Owner attention: **{len(snapshot['owner_attention_lanes'])}**",
        f"Validation errors: **{len(snapshot['validation_errors'])}**",
        "",
        "Mailbox freshness reports date coverage only; it does not establish chat activity or release readiness.",
        "",
        "| Lane | Status | Mailbox date | Age (days) | Freshness | Owner gate | Blocker | Dependencies | Next safe task |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for lane in snapshot["lanes"]:
        deps = ", ".join(dependency_text(x) for x in lane["dependencies_needed"]) or "—"
        lines.append(
            "| {lane} | {status} | {updated} | {age} | {freshness} | {gate} | {blocker} | {deps} | {next} |".format(
                lane=cell(lane["title"]),
                status=cell(lane["status"]),
                updated=cell(lane["updated"]),
                age=cell(lane["mailbox_age_days"]),
                freshness=cell(lane["mailbox_freshness"]),
                gate=cell(lane["owner_gate"]),
                blocker=cell(lane["blocker"]),
                deps=cell(deps),
                next=cell(lane["next_safe_task"]),
            )
        )
    if snapshot["supplemental_streams"]:
        lines += [
            "", "## Supplemental coordination and reference streams", "",
            "These registry references do not add core writers or assert that a chat is running.", "",
            "| Stream | Mode | Owner lane | Writer scope | References |",
            "|---|---|---|---|---|",
        ]
        for stream in snapshot["supplemental_streams"]:
            references = "; ".join(
                str(stream[key]) for key in
                ("bootstrap", "current_reference", "checkpoint_reference")
                if stream.get(key)
            )
            lines.append(
                "| {title} | {mode} | {owner} | {scope} | {refs} |".format(
                    title=cell(stream.get("title", stream["stream"])),
                    mode=cell(stream.get("mode")),
                    owner=cell(stream.get("owner_lane")),
                    scope=cell(stream.get("writer_scope")),
                    refs=cell(references),
                )
            )
    if snapshot["freshness_warnings"]:
        lines += ["", "## Mailbox freshness warnings", ""]
        lines += [f"- {warning}" for warning in snapshot["freshness_warnings"]]
    if snapshot["validation_errors"]:
        lines += ["", "## Validation errors", ""]
        lines += [f"- {e}" for e in snapshot["validation_errors"]]
    return "\n".join(lines) + "\n"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--json", dest="json_path")
    p.add_argument("--markdown", dest="md_path")
    p.add_argument("--validate-only", action="store_true")
    p.add_argument("--as-of", type=date.fromisoformat, metavar="YYYY-MM-DD")
    args = p.parse_args()

    snapshot = collect(as_of=args.as_of)
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
        f"{len(snapshot['dependency_requests'])} dependency request(s); "
        f"{snapshot['supplemental_stream_count']} supplemental stream(s); "
        f"{len(snapshot['freshness_warnings'])} mailbox freshness warning(s) "
        f"as of {snapshot['as_of']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
