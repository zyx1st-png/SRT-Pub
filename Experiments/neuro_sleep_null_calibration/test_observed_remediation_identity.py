"""Synthetic metadata-only identity tests; no RIKEN signal or Q computation.

Fixtures are deliberately retained under a new temporary directory on every
case, including failures; they contain only virtual results and audit records.
"""
from __future__ import annotations

import copy
import json
import os
import sys
import tempfile
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import h3_supervised_pilot as pilot
import observed_calibration_runner as runner
import observed_remediation_identity as subject
from nc0a_watchdog import HashChainLog
from observed_calibration_sample import canonical, validate_sample
from riken_source_identity import sha256_file


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical(value) + b"\n")


def synthetic_old_fixture(root):
    packet = copy.deepcopy(subject.load_packet())
    rows = [{"sample_order": i, "graph_id": f"synthetic-original-{i}"} for i in range(1, 48)]
    packet.update(prefix_rows=rows[:6], suffix_rows=rows[6:],
                  suffix_sha256=subject._digest(rows[6:]), full_sample_sha256="b" * 64)
    prior = packet["prior_run"]
    prior.update(uuid=str(uuid.uuid4()), head_sha="a" * 40,
                 reported_wall_seconds=9.0, reported_cpu_seconds=7.0,
                 preflight_wall_seconds=1.0, preflight_cpu_seconds=0.2,
                 elapsed_controller_seconds=9.2,
                 host_started_utc="2026-10-26T01:00:00+00:00",
                 host_finished_utc="2026-10-26T01:00:10+00:00",
                 accounting_cpu_count_upper_bound=8)
    run = root / "old-runs" / prior["uuid"]
    state = root / "state"
    run.mkdir(parents=True)
    for i, row in enumerate(rows[:6], 1):
        write(run / f"observed-cost-rows/{i:03d}.json", {
            "input_identity": row, "graph_id": row["graph_id"],
            "louvain_seeds": list(range(200)), "canonical": {"q_values": [0.0] * 200}})
    tips = {}
    for name in ("h3-control.jsonl", "h3-evidence.jsonl", "watchdog.jsonl"):
        with HashChainLog(run / name) as log:
            tips[name] = log.append({"kind": "synthetic-audit"})
    prior["hash_chain_tips"] = tips
    manifest = {"candidate_limits_not_authorized_in_packet": {"preflight": {
        "preflight_wall_seconds": 1.0, "preflight_process_cpu_seconds": 0.2}}}
    write(run / "run-manifest.json", manifest)
    summary = {"run_id": prior["uuid"], "head_sha": prior["head_sha"],
               "pilot_sha256": packet["full_sample_sha256"],
               "status": prior["terminal_status"], "failure_category": prior["failure_category"],
               "resume_allowed": False, "runner": None, "runner_terminal_sha256": None,
               "elapsed_controller_seconds": 9.2,
               "watchdog": {"reason": prior["watchdog_reason"], "usage": {
                   "wall_seconds": 9.0, "cpu_seconds": 7.0,
                   "cpu_accounting": "max_process_group_ps_and_waited_child_rusage_plus_watchdog"}}}
    write(run / "h3-summary.json", summary)
    prior["file_sha256"] = {str(f.relative_to(run)): sha256_file(f)
                            for f in run.rglob("*") if f.is_file()}
    prior["prefix_artifacts"] = [
        {"relative_path": f"observed-cost-rows/{i:03d}.json", "sample_order": i,
         "graph_id": row["graph_id"], "sha256": prior["file_sha256"][f"observed-cost-rows/{i:03d}.json"]}
        for i, row in enumerate(rows[:6], 1)]
    start = {"kind": "activity_started", "run_id": prior["uuid"],
             "head_sha": prior["head_sha"], "pilot_sha256": packet["full_sample_sha256"],
             "run_directory": str(run), "started_utc": prior["host_started_utc"]}
    finish = {"kind": "activity_finished", "run_id": prior["uuid"],
              "pilot_sha256": packet["full_sample_sha256"], "run_directory": str(run),
              "finished_utc": prior["host_finished_utc"], "status": prior["terminal_status"],
              "failure_category": prior["failure_category"],
              "summary_sha256": prior["file_sha256"]["h3-summary.json"],
              "run_manifest_sha256": prior["file_sha256"]["run-manifest.json"],
              "runner_terminal_sha256": None, "wall_seconds": 9.0, "cpu_seconds": 7.0,
              "watchdog_audit_tip_sha256": tips["watchdog.jsonl"],
              "evidence_tip_sha256": tips["h3-evidence.jsonl"]}
    prep = (root / "canonical_observed_authorization_preparation_2026-10-26" /
            prior["uuid"] / "preflight-evidence.json")
    write(prep, {"component_checks": {"cpu_count": 8},
                 "head_sha": prior["head_sha"], "run_uuid": prior["uuid"]})
    prior["preparation_evidence_sha256"] = sha256_file(prep)
    approved = {"status": "APPROVED_FOR_SINGLE_RUN",
                "confirmed_at_utc": "2026-10-26T00:59:59+00:00",
                "preparation_evidence_sha256": prior["preparation_evidence_sha256"],
                "binding": {"head_sha": prior["head_sha"], "run_uuid": prior["uuid"],
                            "sample_sha256": packet["full_sample_sha256"],
                            "output_directory": str(run)}}
    write(prep.parent / "approved-single-run-authorization.json", approved)
    write(prep.parent / "pending-researcher-authorization.json", {"status": "SYNTHETIC_PENDING"})
    write(prep.parent / "frozen-sample.json", {"synthetic_primary_rows": rows})
    prior["preparation_file_sha256"] = {f.name: sha256_file(f) for f in prep.parent.iterdir()}
    manifest["candidate_limits_not_authorized_in_packet"]["researcher_authorization"] = {
        "authorization_sha256": sha256_file(prep.parent / "approved-single-run-authorization.json")}
    write(run / "run-manifest.json", manifest)
    prior["file_sha256"]["run-manifest.json"] = sha256_file(run / "run-manifest.json")
    finish["run_manifest_sha256"] = prior["file_sha256"]["run-manifest.json"]
    with HashChainLog(state / pilot._HOST_LEDGER) as log:
        log.append(start)
        prefix_tip = log.append(finish)
    prior.update(host_ledger_prefix_event_count=2, host_ledger_prefix_tip=prefix_tip,
                 host_ledger_prefix_sha256=sha256_file(state / pilot._HOST_LEDGER))
    verified = {"status": "VERIFIED_TERMINAL", "completed": False, "resume_allowed": False,
                "rows_verified": 6, "hash_chain_tips": tips}
    return packet, run, state, verified, prep


class TestObservedRemediationIdentity(unittest.TestCase):
    def setUp(self):
        # Keep logs even for an unexpected native/test failure. No private data
        # is copied into these synthetic artifact directories.
        self.root = Path(tempfile.mkdtemp(prefix="srt-remediation-identity-")).resolve()
        self.packet, self.run, self.state, self.verified, self.prep = synthetic_old_fixture(self.root)

    def verify(self):
        with patch.object(runner, "verify_run", return_value=self.verified) as official:
            result = subject.verify_original(self.run, self.state, packet=self.packet)
        official.assert_called_once_with(self.run, state_dir=self.state)
        return result

    def test_frozen_suffix_is_exact_7_to_47_without_reserve_or_prefix(self):
        fixed = subject.load_packet()
        sample, _ = validate_sample()
        self.assertEqual(fixed["prefix_rows"], sample["primary_rows"][:6])
        self.assertEqual(fixed["suffix_rows"], sample["primary_rows"][6:])
        self.assertEqual(fixed["suffix_sha256"], subject.SUFFIX_SHA256)
        self.assertEqual(subject.packet_sha256(fixed), subject.PACKET_SHA256)
        self.assertEqual(fixed["new_louvain_trials"], 8200)
        self.assertFalse({r["graph_id"] for r in fixed["suffix_rows"]} &
                         {r["graph_id"] for r in sample["reserve_rows_not_authorized"]})

    def test_read_only_official_verifier_and_conservative_budget_fields(self):
        before = {str(f): sha256_file(f) for f in self.root.rglob("*") if f.is_file()}
        result = self.verify()
        self.assertEqual(result["old_host_wall_seconds"], 10.0)
        self.assertEqual(result["old_wall_charge_seconds"], 11.0)
        self.assertEqual(result["old_cpu_upper_charge_seconds"], 23.0)  # max(7+.2,7+(11-9)*8)
        self.assertEqual(result["old_authorization_window_wall_seconds"], 11.0)
        self.assertEqual(result["old_authorization_confirmed_at_utc"], "2026-10-26T00:59:59+00:00")
        self.assertEqual(result["old_output_bytes"], sum(f.stat().st_size for f in self.run.rglob("*") if f.is_file()))
        self.assertEqual(result["old_auxiliary_output_bytes"],
                         sum(f.stat().st_size for f in self.prep.parent.iterdir()) +
                         (self.state / pilot._HOST_LEDGER).stat().st_size)
        self.assertEqual(before, {str(f): sha256_file(f) for f in self.root.rglob("*") if f.is_file()})

    def test_legitimate_host_suffix_append_preserves_bound_old_prefix(self):
        with HashChainLog(self.state / pilot._HOST_LEDGER) as log:
            log.append({"kind": "synthetic_later_claim", "run_id": "not-an-old-run"})
        self.assertEqual(self.verify()["old_wall_charge_seconds"], 11.0)

    def test_reordered_or_prefix_substituted_suffix_is_rejected(self):
        self.packet["suffix_rows"][0], self.packet["suffix_rows"][1] = (
            self.packet["suffix_rows"][1], self.packet["suffix_rows"][0])
        with self.assertRaises(subject.RemediationIdentityError):
            self.verify()

    def test_scientific_or_different_operational_cause_is_not_an_exception(self):
        self.packet["prior_run"]["failure_category"] = "SCIENTIFIC_INTEGRITY"
        with self.assertRaisesRegex(subject.RemediationIdentityError, "specific consumed operational"):
            self.verify()

    def test_other_uuid_cannot_be_presented_as_the_consumed_run(self):
        self.packet["prior_run"]["uuid"] = str(uuid.uuid4())
        with self.assertRaisesRegex(subject.RemediationIdentityError, "UUID/path"):
            self.verify()

    def test_modified_old_row_or_extra_file_is_rejected(self):
        row = self.run / "observed-cost-rows/001.json"
        original = row.read_bytes()
        row.write_bytes(original + b" ")
        with self.assertRaisesRegex(subject.RemediationIdentityError, "hashes"):
            self.verify()
        row.write_bytes(original)
        (self.run / "unknown.json").write_text("{}")
        with self.assertRaisesRegex(subject.RemediationIdentityError, "listing"):
            self.verify()

    def test_symlink_and_hardlink_alias_are_rejected(self):
        row = self.run / "observed-cost-rows/001.json"
        backup = self.root / "row-backup"
        row.rename(backup)
        row.symlink_to(backup)
        with self.assertRaisesRegex(subject.RemediationIdentityError, "symlink"):
            self.verify()
        row.unlink()
        os.link(backup, row)
        with self.assertRaisesRegex(subject.RemediationIdentityError, "hard-link"):
            self.verify()

    def test_truncated_old_host_chain_is_rejected(self):
        ledger = self.state / pilot._HOST_LEDGER
        ledger.write_bytes(ledger.read_bytes().splitlines(keepends=True)[0])
        with self.assertRaisesRegex(subject.RemediationIdentityError, "prefix"):
            self.verify()

    def test_official_integrity_failure_or_incomplete_prefix_is_rejected(self):
        self.verified["rows_verified"] = 5
        with self.assertRaisesRegex(subject.RemediationIdentityError, "six-row"):
            self.verify()
        self.verified["rows_verified"] = 6
        with patch.object(runner, "verify_run", side_effect=ValueError("damaged audit chain")), \
             self.assertRaisesRegex(ValueError, "damaged"):
            subject.verify_original(self.run, self.state, packet=self.packet)

    def test_accounting_reanchor_cannot_change_old_usage_or_cpu_count(self):
        summary = self.run / "h3-summary.json"
        data = json.loads(summary.read_text())
        data["watchdog"]["usage"]["cpu_seconds"] += 1
        write(summary, data)
        self.packet["prior_run"]["file_sha256"]["h3-summary.json"] = sha256_file(summary)
        with self.assertRaisesRegex(subject.RemediationIdentityError, "accounting"):
            self.verify()

    def test_cpu_bound_requires_original_preparation_evidence(self):
        data = json.loads(self.prep.read_text())
        data["component_checks"]["cpu_count"] = 1
        write(self.prep, data)
        self.packet["prior_run"]["preparation_evidence_sha256"] = sha256_file(self.prep)
        self.packet["prior_run"]["preparation_file_sha256"]["preflight-evidence.json"] = sha256_file(self.prep)
        with self.assertRaisesRegex(subject.RemediationIdentityError, "CPU-count"):
            self.verify()

    def test_approved_authentication_link_to_preparation_is_required(self):
        auth = self.prep.parent / "approved-single-run-authorization.json"
        data = json.loads(auth.read_text())
        data["preparation_evidence_sha256"] = "f" * 64
        write(auth, data)
        self.packet["prior_run"]["preparation_file_sha256"][auth.name] = sha256_file(auth)
        # Manifest still authenticates the original approved object, so a
        # reanchored auxiliary file hash cannot manufacture that approval.
        with self.assertRaisesRegex(subject.RemediationIdentityError, "approval"):
            self.verify()

    def test_unknown_or_nonregular_preparation_file_is_rejected(self):
        (self.prep.parent / "unknown.dat").write_bytes(b"not-permitted")
        with self.assertRaisesRegex(subject.RemediationIdentityError, "unknown files"):
            self.verify()

    def test_mutation_during_official_verification_is_rejected(self):
        row = self.run / "observed-cost-rows/001.json"
        def mutate(*args, **kwargs):
            row.write_bytes(row.read_bytes() + b" ")
            return self.verified
        with patch.object(runner, "verify_run", side_effect=mutate), \
             self.assertRaises(subject.RemediationIdentityError):
            subject.verify_original(self.run, self.state, packet=self.packet)


if __name__ == "__main__":
    unittest.main()
