import importlib.util
import tempfile
import unittest
from pathlib import Path

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


    def test_wf02_four_classification_samples(self):
        samples = [
            ("blocked overrides all", "hard failure", "owner review", ["other"], "BLOCKED"),
            ("owner gate overrides dependency", None, "visual review", ["other"], "OWNER_GATE"),
            ("dependency only", None, None, [{"lane": "other", "need": "proof"}], "DEPENDENCY"),
            ("normal / empty structures", None, {}, [], "NORMAL"),
        ]
        for label, blocker, gate, deps, expected in samples:
            with self.subTest(label=label):
                self.assertEqual(mod.classify_lane_attention(blocker, gate, deps), expected)

    def test_wf02_dedupe_stable_and_changes_on_material_update(self):
        one = [{"lane": "optical", "need": "sha proof"}]
        first = mod.attention_dedupe_key("central", "DEPENDENCY", None, None, one)
        same = mod.attention_dedupe_key("central", "DEPENDENCY", None, None, [{"need": "sha proof", "lane": "optical"}])
        changed = mod.attention_dedupe_key("central", "DEPENDENCY", None, None, [{"lane": "optical", "need": "final print proof"}])
        self.assertEqual(first, same)
        self.assertNotEqual(first, changed)
        self.assertIsNone(mod.attention_dedupe_key("central", "NORMAL", None, None, []))

    def test_wf02_live_registry_and_events(self):
        snapshot = mod.collect()
        self.assertEqual(snapshot["lane_count"], 11)
        self.assertEqual(snapshot["validation_errors"], [])
        self.assertEqual(len({x["lane"] for x in snapshot["lanes"]}), 11)
        self.assertTrue(all(e["dedupe_key"].startswith("rse-wf02-v1:") for e in snapshot["attention_events"]))
        self.assertTrue(all(e["classification"] in {"BLOCKED", "OWNER_GATE", "DEPENDENCY"} for e in snapshot["attention_events"]))

    def test_wf02_registry_rejects_wrong_lane_count(self):
        def registered(n):
            return {
                f"lane_{i:02d}": {
                    "mailbox": f"orchestration/control-plane/mailboxes/lane_{i:02d}.yml"
                }
                for i in range(n)
            }

        self.assertEqual(len(mod.validated_mailbox_paths(registered(11))), 11)
        for invalid_count in (0, 10, 12):
            with self.subTest(count=invalid_count):
                with self.assertRaisesRegex(ValueError, "exactly 11"):
                    mod.validated_mailbox_paths(registered(invalid_count))

    def test_wf02_registry_rejects_unsafe_or_noncanonical_paths(self):
        chats = {
            f"lane_{i:02d}": {
                "mailbox": f"orchestration/control-plane/mailboxes/lane_{i:02d}.yml"
            }
            for i in range(11)
        }
        unsafe = (
            "../secrets.yml",
            "orchestration/control-plane/mailboxes/../secrets.yml",
            "orchestration/control-plane/mailboxes/lane_01.yml",
            "/tmp/lane_00.yml",
        )
        for replacement in unsafe:
            with self.subTest(path=replacement):
                mutated = {k: dict(v) for k, v in chats.items()}
                mutated["lane_00"]["mailbox"] = replacement
                with self.assertRaisesRegex(ValueError, "noncanonical"):
                    mod.validated_mailbox_paths(mutated)

    def test_wf02_registry_rejects_path_traversal_lane_id(self):
        chats = {
            f"lane_{i:02d}": {
                "mailbox": f"orchestration/control-plane/mailboxes/lane_{i:02d}.yml"
            }
            for i in range(10)
        }
        chats["../../../outside"] = {
            "mailbox": "orchestration/control-plane/mailboxes/../../../outside.yml"
        }
        with self.assertRaisesRegex(ValueError, "escapes root"):
            mod.validated_mailbox_paths(chats)

    def test_wf02_registry_rejects_nonmapping_spec(self):
        chats = {
            f"lane_{i:02d}": {
                "mailbox": f"orchestration/control-plane/mailboxes/lane_{i:02d}.yml"
            }
            for i in range(11)
        }
        chats["lane_00"] = None
        with self.assertRaisesRegex(ValueError, "not a mapping"):
            mod.validated_mailbox_paths(chats)

    def test_markdown_has_table(self):
        text = mod.markdown(mod.collect())
        self.assertIn("# RSE Control Plane Snapshot", text)
        self.assertIn("| Lane | Status |", text)

    def test_snapshot_json_serializable(self):
        import json
        payload = json.dumps(mod.collect(), default=str)
        self.assertIn("rse-control-plane-snapshot-v1", payload)


if __name__ == "__main__":
    unittest.main()
