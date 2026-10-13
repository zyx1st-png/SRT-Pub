"""Fail-closed tests for authorization accounting independent of result folders."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from nc0a_authority_ledger import (
    AuthorityLedger, AuthorityLedgerError, initialize_authority_store,
)


class AuthorityLedgerTests(unittest.TestCase):
    def test_unfinished_invocation_has_unknown_cost_and_cannot_restart(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ledger_path = root / "store" / "ledger.jsonl"
            anchor_path = root / "anchor" / "tip.json"
            initialize_authority_store(ledger_path, anchor_path)
            args = dict(experiment_id="toy-id", run_dir=root / "run",
                        policy_sha256="a" * 64, approval_sha256="b" * 64,
                        wall_budget_seconds=100, cpu_budget_seconds=200,
                        max_invocations=2)
            with AuthorityLedger(ledger_path, anchor_path) as ledger:
                self.assertEqual(ledger.begin(**args)["invocation"], 1)
            with AuthorityLedger(ledger_path, anchor_path) as ledger:
                with self.assertRaisesRegex(AuthorityLedgerError, "unknown resource cost"):
                    ledger.begin(**args)

    def test_deleted_or_truncated_authority_record_cannot_be_reinitialized(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ledger_path = root / "store" / "ledger.jsonl"
            anchor_path = root / "anchor" / "tip.json"
            initialize_authority_store(ledger_path, anchor_path)
            with AuthorityLedger(ledger_path, anchor_path) as ledger:
                ledger.begin(experiment_id="toy-id", run_dir=root / "run",
                             policy_sha256="a" * 64, approval_sha256="b" * 64,
                             wall_budget_seconds=100, cpu_budget_seconds=200,
                             max_invocations=1)
            ledger_path.write_bytes(b"")
            with self.assertRaisesRegex(AuthorityLedgerError, "differs from its independent tip anchor"):
                AuthorityLedger(ledger_path, anchor_path)
            with self.assertRaisesRegex(AuthorityLedgerError, "cannot be reset"):
                initialize_authority_store(ledger_path, anchor_path)

    def test_missing_external_anchor_is_not_created_by_launcher_or_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ledger_path = root / "store" / "ledger.jsonl"
            anchor_path = root / "anchor" / "tip.json"
            initialize_authority_store(ledger_path, anchor_path)
            anchor_path.unlink()
            with self.assertRaisesRegex(AuthorityLedgerError, "is missing"):
                AuthorityLedger(ledger_path, anchor_path)

    def test_concurrent_ledger_open_is_rejected_while_an_invocation_holds_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ledger_path = root / "store" / "ledger.jsonl"
            anchor_path = root / "anchor" / "tip.json"
            initialize_authority_store(ledger_path, anchor_path)
            with AuthorityLedger(ledger_path, anchor_path):
                with self.assertRaises(BlockingIOError):
                    AuthorityLedger(ledger_path, anchor_path)


if __name__ == "__main__":
    unittest.main()
