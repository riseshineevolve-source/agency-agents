import importlib.util
import json
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import patch

import yaml

MODULE_PATH = Path(__file__).with_name("rse-control-plane-status.py")
spec = importlib.util.spec_from_file_location("rse_control_plane_status", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class ControlPlaneTests(unittest.TestCase):
    def test_nullish_attention(self):
        for value in (None, "", "null", "none", "NONE"):
            self.assertFalse(mod.normalize_attention(value))
        self.assertTrue(mod.normalize_attention("OWNER_REVIEW"))

    def test_collect_current_repo(self):
        snapshot = mod.collect()
        self.assertEqual(snapshot["schema"], "rse-control-plane-snapshot-v1")
        self.assertGreaterEqual(snapshot["lane_count"], 10)
        self.assertEqual(snapshot["validation_errors"], [])
        lane_ids = {x["lane"] for x in snapshot["lanes"]}
        self.assertIn("detective_book_factory", lane_ids)
        self.assertIn("marketing_autopilot", lane_ids)

    def test_markdown_has_table(self):
        text = mod.markdown(mod.collect())
        self.assertIn("# RSE Control Plane Snapshot", text)
        self.assertIn("| Lane | Status |", text)

    def test_snapshot_json_serializable(self):
        payload = json.dumps(mod.collect(), default=str)
        self.assertIn("rse-control-plane-snapshot-v1", payload)

    def test_supplemental_coverage_and_mailbox_freshness(self):
        """References do not change writer count; old metadata does not fail CI."""
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            control = root / "orchestration" / "control-plane"
            mailboxes = control / "mailboxes"
            mailboxes.mkdir(parents=True)
            dates = {
                "old_bootstrap": date(2026, 10, 7),
                "recent": datetime(2026, 10, 20, 12, tzinfo=timezone.utc),
                "missing": None,
                "invalid": "not-a-date",
                "future": date(2026, 10, 22),
            }
            registry = {"chats": {}, "supplemental_streams": {}}
            for lane, updated in dates.items():
                mailbox = mailboxes / f"{lane}.yml"
                registry["chats"][lane] = {
                    "title": lane,
                    "mailbox": str(mailbox.relative_to(root)),
                }
                content = {
                    "lane": lane,
                    "status": "BOOTSTRAP_READY" if lane == "old_bootstrap" else "RECORDED",
                    "owner_gate": "null",
                    "blocker": None,
                    "dependencies_needed": [],
                }
                if updated is not None:
                    content["updated"] = updated
                mailbox.write_text(yaml.safe_dump(content), encoding="utf-8")
            streams = ("optical_halloween", "website_factory", "ai_discovery", "build_desk", "quick_desk")
            for stream in streams:
                registry["supplemental_streams"][stream] = {
                    "title": stream,
                    "mode": "reference_only",
                    "owner_lane": "central_control_tower",
                    "current_reference": "example/reference.md",
                }
            registry_path = control / "RSE_CHAT_REGISTRY_V1.yml"
            registry_path.write_text(yaml.safe_dump(registry), encoding="utf-8")
            with patch.multiple(
                mod,
                ROOT=root,
                REGISTRY=registry_path,
                FREEZE=control / "RSE_UNIVERSE_FACTORY_V1_0_FREEZE.md",
            ):
                snapshot = mod.collect(as_of=date(2026, 10, 21))
                self.assertEqual(snapshot, mod.collect(as_of=date(2026, 10, 21)))
            self.assertEqual(snapshot["lane_count"], 5)
            self.assertEqual(snapshot["supplemental_stream_count"], 5)
            self.assertEqual({x["stream"] for x in snapshot["supplemental_streams"]}, set(streams))
            self.assertEqual(snapshot["as_of"], "2026-10-21")
            self.assertEqual(snapshot["validation_errors"], [])
            self.assertEqual(snapshot["owner_attention_lanes"], [])
            self.assertEqual(len(snapshot["freshness_warnings"]), 4)
            by_lane = {x["lane"]: x for x in snapshot["lanes"]}
            for lane, expected in (
                ("old_bootstrap", (14, "STALE")),
                ("recent", (1, "RECENT")),
                ("missing", (None, "MISSING")),
                ("invalid", (None, "INVALID")),
                ("future", (-1, "UNKNOWN")),
            ):
                self.assertEqual(
                    (by_lane[lane]["mailbox_age_days"], by_lane[lane]["mailbox_freshness"]),
                    expected,
                )
            payload = json.dumps(snapshot, default=str)
            self.assertIn("2026-10-20", payload)
            report = mod.markdown(snapshot)
            self.assertIn("not independent core writers", report)
            self.assertIn("Mailbox freshness warnings", report)
            self.assertIn("mailbox updated date is in the future", report)
            self.assertIn("example/reference.md", report)

    def test_freshness_boundary_and_date_inputs(self):
        as_of = date(2026, 10, 21)
        for updated in ("2026-10-14", date(2026, 10, 14), "2026-10-14T23:00:00Z"):
            self.assertEqual(mod.mailbox_freshness(updated, as_of), {
                "mailbox_age_days": 7, "mailbox_freshness": "RECENT",
            })
        for updated in (42, {}, "2026-99-99"):
            self.assertEqual(mod.mailbox_freshness(updated, as_of)["mailbox_freshness"], "INVALID")
        self.assertEqual(
            mod.mailbox_freshness("2026-10-20T23:30:00-02:00", as_of)["mailbox_age_days"], 0,
        )

    def test_supplemental_registry_is_optional(self):
        with patch.object(mod, "load_yaml", side_effect=[
            {"chats": {"test": {"mailbox": __file__}}},
            {"lane": "test", "updated": "2026-10-21"},
        ]):
            snapshot = mod.collect(as_of=date(2026, 10, 21))
        self.assertEqual(snapshot["lane_count"], 1)
        self.assertEqual(snapshot["supplemental_streams"], [])
        self.assertEqual(snapshot["validation_errors"], [])


if __name__ == "__main__":
    unittest.main()
