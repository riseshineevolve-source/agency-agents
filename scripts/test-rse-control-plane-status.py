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
