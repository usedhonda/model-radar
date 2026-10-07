"""Offline distribution-contract checks; these do not execute an LLM or GitHub writes."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bootstrap(path):
    return re.search(r"```text\n(Run Model Radar.*?)(?:\n```)",
                     (ROOT / path).read_text(), re.S).group(1)


class BootstrapContract(unittest.TestCase):
    def test_readme_distributes_canonical_bootstrap(self):
        self.assertEqual(bootstrap("README.md"), bootstrap("examples/chatgpt-schedule.md"))

    def test_policy_fetch_is_one_snapshot_before_execution(self):
        text = bootstrap("examples/chatgpt-schedule.md")
        self.assertIn("resolve its default branch to a full commit SHA", text)
        self.assertIn("both `manifest.json` and the exact prompt file named by `manifest.prompt` from that same commit SHA", text)
        self.assertIn("Do not fetch either file through a moving branch reference", text)
        self.assertIn("Before executing the resolved prompt", text)
        self.assertIn("minimum_bootstrap_version", text)
        self.assertIn("prompt's declared policy version matches `manifest.version`", text)

    def test_stable_manifest_resolves_existing_matching_policy(self):
        manifest = json.loads((ROOT / "manifest.json").read_text())
        policy = (ROOT / manifest["prompt"]).read_text()
        declared = re.search(r"^# Model Radar Scheduled Audit Policy — v(\S+)", policy).group(1)
        self.assertEqual(declared, manifest["version"])
        self.assertLessEqual(manifest["minimum_bootstrap_version"], 1)
        self.assertEqual(manifest["write_policy_major"], 1)

    def test_branch_movement_fixture_requires_snapshot_consistency(self):
        # No real provider claims: two synthetic policy snapshots.
        snapshots = {
            "a" * 40: {"manifest": {"version": "1.1.0", "write_policy_major": 1},
                       "prompt_version": "1.1.0"},
            "b" * 40: {"manifest": {"version": "2.0.0", "write_policy_major": 2},
                       "prompt_version": "2.0.0"},
        }
        first, second = snapshots.values()
        # Manifest read before branch movement, prompt read after it.
        self.assertNotEqual(first["manifest"]["version"], second["prompt_version"])
        # Pinning both reads to the first SHA keeps the accepted policy coherent.
        pinned = snapshots["a" * 40]
        self.assertEqual(pinned["manifest"]["version"], pinned["prompt_version"])
        self.assertEqual(pinned["manifest"]["write_policy_major"], 1)

    def test_trial_uses_one_snapshot(self):
        text = (ROOT / "prompts/read-only-trial.md").read_text()
        self.assertIn("same commit SHA", text)
        self.assertIn("do not create, edit, close, reopen, or merge", text)


if __name__ == "__main__":
    unittest.main()
