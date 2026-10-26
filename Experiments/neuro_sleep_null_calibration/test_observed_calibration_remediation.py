"""Frozen-schedule synthetic exception admission and real Watchdog regressions.

Every fixture is retained under /tmp/srt-remediation-integration-* including
successful runs. A failure never causes a retry. No private RIKEN root or signal
is opened, and production code has no test-mode command-line authorization.
"""
from __future__ import annotations

import copy
import json
import multiprocessing
import os
import subprocess
import sys
import tempfile
import time
import unittest
import uuid
from contextlib import ExitStack
from dataclasses import asdict, replace
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import h3_supervised_pilot as pilot
import nc0a_watchdog as watchdog
import observed_calibration_remediation as remedy
import observed_calibration_runner as runner
import observed_remediation_identity as provenance
import riken_source_identity as identity
from observed_calibration_sample import canonical
from test_observed_calibration import fixture, synthetic_builder

SYNTHETIC_SCHEMA = "SRT_REMEDIATION_SYNTHETIC_FIXTURE_ONLY"


def packet_patches(stack: ExitStack, packet: dict):
    stack.enter_context(patch.object(provenance, "load_packet", return_value=packet))
    stack.enter_context(patch.object(provenance, "PACKET_SHA256", provenance.packet_sha256(packet)))
    stack.enter_context(patch.object(provenance, "SUFFIX_SHA256", packet["suffix_sha256"]))


def synthetic_child(payload_path: Path) -> int:
    payload = json.loads(payload_path.read_text())
    if payload.get("schema") != SYNTHETIC_SCHEMA:
        raise ValueError("Synthetic payload required")
    packet = payload["packet"]
    if any(not r["graph_id"].startswith("synthetic-remediation-")
           for r in packet["prefix_rows"] + packet["suffix_rows"]):
        raise ValueError("Real identity cannot enter synthetic child")
    if payload["scenario"] == "child_exit":
        os._exit(42)
    source = Path(payload["source"])
    seeds = list(range(700, 900))
    selected = list(range(18))
    saved_private = runner._private_process_row
    actual_runtime = identity.h3_runtime_manifest()
    actual_runtime["replay_environment_matches_recorded_versions_and_candidate_lock"] = True

    def private_row(row, manifest, phase2, psa, signatures, cache, phase_sink):
        if row["sample_order"] <= 6:
            raise AssertionError("Completed prefix must never be recomputed")
        if payload["scenario"] == "unknown_child":
            subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
            time.sleep(30)
        with patch.object(runner, "load_row_inputs", return_value=(source, selected, seeds)), \
             patch.object(identity, "_historical_connected_graph", return_value=(
                 synthetic_builder, identity.EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256)), \
             patch.object(subprocess, "Popen", side_effect=AssertionError(
                 "Scientific row spawned an unregistered telemetry subprocess")):
            return saved_private(row, manifest, phase2, psa,
                                 {source.name: runner._signature(source)}, cache, phase_sink)

    saved_execute = runner.execute_rows

    def execute(rows, **kwargs):
        if rows != packet["suffix_rows"]:
            raise AssertionError("Dispatch changed the frozen suffix")
        if payload["scenario"] == "synthetic_marker":
            kwargs["synthetic"] = True
        return saved_execute(rows, **kwargs)

    with ExitStack() as stack:
        packet_patches(stack, packet)
        stack.enter_context(patch.object(provenance, "verify_original", return_value=payload["prior_info"]))
        stack.enter_context(patch.object(pilot, "_git_identity"))
        stack.enter_context(patch.object(pilot, "default_host_state_dir", return_value=Path(payload["state"])))
        stack.enter_context(patch.object(remedy, "validate_sample", return_value=(
            {"primary_rows": packet["prefix_rows"] + packet["suffix_rows"]}, {})))
        stack.enter_context(patch.object(runner, "validate_private_identities", return_value=(
            source.parent, source.parent, {source.name: runner._signature(source)})))
        stack.enter_context(patch.object(identity, "h3_runtime_manifest", return_value=actual_runtime))
        stack.enter_context(patch.object(runner, "_private_process_row", side_effect=private_row))
        stack.enter_context(patch.object(runner, "execute_rows", side_effect=execute))
        if payload["scenario"] == "write_failure":
            stack.enter_context(patch.object(runner, "write_result_payload",
                                             side_effect=OSError("synthetic injected write failure")))
        return remedy._runner_child()


def claim_racer(payload_path: str, contender: int, barrier) -> None:
    payload = json.loads(Path(payload_path).read_text())
    state = Path(payload["state"])
    approved = payload["approved"][contender]
    result = {"contender": contender, "claimed": False}
    try:
        with ExitStack() as stack:
            packet_patches(stack, payload["packet"])
            stack.enter_context(patch.object(watchdog, "_default_activity_lock_path",
                                             return_value=state / "global.lock"))
            barrier.wait(timeout=10)
            with pilot._host_lock(state):
                events = pilot._verified_host_events(state / pilot._HOST_LEDGER)
                with watchdog.HashChainLog(state / pilot._HOST_LEDGER) as log:
                    result["claim_tip"] = remedy.claim_locked(log, events, approved)
                    result["claimed"] = True
                    time.sleep(0.2)
    except BaseException as exc:  # noqa: BLE001 -- preserve every contender failure as evidence
        result.update({"failure_type": type(exc).__name__, "reason": str(exc)})
    (state / f"contender-{contender}.json").write_text(json.dumps(result))


def claim_and_exit(payload_path: str) -> None:
    payload = json.loads(Path(payload_path).read_text())
    state = Path(payload["state"])
    with ExitStack() as stack:
        packet_patches(stack, payload["packet"])
        stack.enter_context(patch.object(watchdog, "_default_activity_lock_path",
                                         return_value=state / "global.lock"))
        with pilot._host_lock(state), watchdog.HashChainLog(state / pilot._HOST_LEDGER) as log:
            remedy.claim_locked(log, pilot._verified_host_events(state / pilot._HOST_LEDGER),
                                 payload["approved"])
            os._exit(19)  # fsynced claim must survive loss before activity_started


class TestObservedRemediation(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="srt-remediation-integration-")).resolve()
        print(f"RETAINED_REMEDIATION_FIXTURE={self.root}", flush=True)
        self.signal_dir = self.root / "signals"
        self.signal_dir.mkdir()
        self.source, initial, _ = fixture(self.signal_dir)
        self.psa = self.root / "psa"
        self.parent = self.psa / runner.OUTPUT_PARENT
        self.parent.mkdir(parents=True)
        self.state = self.root / "state"
        self.state.mkdir()
        self.old_id = str(uuid.uuid4())
        self.old_run = self.parent / self.old_id
        self.old_run.mkdir()
        self.head = "a" * 40
        base = initial[0]
        rows = [{**base, "sample_order": i, "graph_id": f"synthetic-remediation-{i:03d}",
                 "engineering_fixture_only": True,
                 "N": 18, "expected_edge_count": 144,
                 "selected_neuron_indices_sha256": identity.hash_int64(range(18))}
                for i in range(1, 48)]
        for i in range(1, 7):
            (self.old_run / f"old-prefix-{i}.json").write_text(json.dumps({
                "synthetic_history_only": True, "sample_order": i, "no_new_Q": True}))
        (self.old_run / "h3-summary.json").write_text('{"synthetic_old_terminal":true}')
        (self.old_run / "run-manifest.json").write_text('{"synthetic_old_manifest":true}')
        self.old_hashes = {p.name: identity.sha256_file(p) for p in self.old_run.iterdir()}
        prior = {"uuid": self.old_id, "head_sha": "0" * 40,
                 "terminal_status": "STOPPED_BY_WATCHDOG",
                 "failure_category": "OPERATIONAL_RESOURCE_STOP",
                 "file_sha256": self.old_hashes}
        self.packet = {"schema": SYNTHETIC_SCHEMA, "prior_run": prior,
                       "prefix_rows": rows[:6], "suffix_rows": rows[6:],
                       "suffix_sha256": identity.sha256_bytes(canonical(rows[6:]))}
        self.prior_info = {"verification": {"status": "VERIFIED_TERMINAL", "rows_verified": 6},
                           "old_output_bytes": sum(p.stat().st_size for p in self.old_run.iterdir()),
                           "old_auxiliary_output_bytes": 0,
                           "old_wall_charge_seconds": 190.68176041699851,
                           "old_cpu_upper_charge_seconds": 247.79796356279473}
        self._write_old_host()

    def _write_old_host(self):
        with watchdog.HashChainLog(self.state / pilot._HOST_LEDGER) as log:
            log.append({"kind": "activity_started", "run_id": self.old_id,
                        "head_sha": "0" * 40, "pilot_sha256": runner.EXPECTED_SAMPLE_SHA256,
                        "run_directory": str(self.old_run)})
            log.append({"kind": "activity_finished", "run_id": self.old_id,
                        "status": "STOPPED_BY_WATCHDOG", "failure_category": "OPERATIONAL_RESOURCE_STOP",
                        "summary_sha256": self.old_hashes["h3-summary.json"],
                        "run_manifest_sha256": self.old_hashes["run-manifest.json"]})

    def patches(self):
        stack = ExitStack()
        packet_patches(stack, self.packet)
        stack.enter_context(patch.object(watchdog, "_default_activity_lock_path",
                                         return_value=self.state / "global.lock"))
        stack.enter_context(patch.object(provenance, "verify_original", return_value=self.prior_info))
        stack.enter_context(patch.object(pilot, "default_host_state_dir", return_value=self.state))
        stack.enter_context(patch.object(runner, "validate_sample", return_value=(
            {"primary_rows": self.packet["prefix_rows"] + self.packet["suffix_rows"]}, {})))
        runtime = identity.h3_runtime_manifest()
        runtime["replay_environment_matches_recorded_versions_and_candidate_lock"] = True
        stack.enter_context(patch.object(identity, "h3_runtime_manifest", return_value=runtime))
        return stack

    def make_auth(self, *, approved=True):
        run_id = str(uuid.uuid4())
        run_dir = self.parent / run_id
        auth = remedy.authorization_draft(self.head, run_id, run_dir, self.old_run)
        line = remedy.confirmation_text(self.head, run_id)
        if approved:
            auth.update({"status": "APPROVED_FOR_SINGLE_REMEDIATION",
                         "researcher_confirmation": line, "researcher_confirmed_risks": True,
                         "researcher_identity": "SYNTHETIC_TEST_ONLY_NEVER_A_REAL_APPROVAL",
                         "confirmed_at_utc": "2026-10-26T00:00:00Z"})
        path = self.root / f"synthetic-auth-{run_id}.json"
        path.write_bytes(canonical(auth))
        args = {"head": self.head, "run_id": run_id, "run_dir": run_dir,
                "old_run_dir": self.old_run, "confirmation": line}
        return path, auth, args

    def events(self):
        return pilot._verified_host_events(self.state / pilot._HOST_LEDGER)

    def test_authorization_is_separate_positive_and_every_binding_negative(self):
        with self.patches():
            path, auth, args = self.make_auth()
            self.assertEqual(remedy.validate_authorization(path, **args)["binding"], auth["binding"])
            for key in auth["binding"]:
                broken = copy.deepcopy(auth)
                broken["binding"][key] = "tampered"
                path.write_bytes(canonical(broken))
                with self.subTest(binding=key), self.assertRaises((ValueError, TypeError)):
                    remedy.validate_authorization(path, **args)
            path.write_bytes(canonical(auth))
            for key, value in (("head", "b" * 40), ("run_id", str(uuid.uuid4())),
                               ("confirmation", args["confirmation"] + " wrong")):
                with self.subTest(argument=key), self.assertRaises(ValueError):
                    remedy.validate_authorization(path, **{**args, key: value})
            path.write_bytes(canonical({**auth, "status": "APPROVED_FOR_SINGLE_RUN"}))
            with self.assertRaises(ValueError):
                remedy.validate_authorization(path, **args)
            path, _, args = self.make_auth(approved=False)
            before = (self.state / pilot._HOST_LEDGER).read_bytes()
            with self.assertRaises(ValueError):
                remedy.launch(**args, authorization=path, phase2=self.signal_dir,
                              psa=self.psa, state_dir=self.state)
            self.assertEqual((self.state / pilot._HOST_LEDGER).read_bytes(), before)
            self.assertFalse(args["run_dir"].exists())

    def test_claim_is_consumed_once_even_after_controller_crash_and_new_UUID(self):
        with self.patches():
            path, _, args = self.make_auth()
            approved = remedy.validate_authorization(path, **args)
            with pilot._host_lock(self.state), watchdog.HashChainLog(self.state / pilot._HOST_LEDGER) as log:
                remedy.claim_locked(log, self.events(), approved)
            # Claim-without-activity represents controller loss before admission.
            with self.assertRaises(ValueError):
                remedy.assert_claim_state(self.events(), approved["binding"],
                                          approved["authorization_sha256"], phase="unclaimed")
            other, _, other_args = self.make_auth()
            other_approved = remedy.validate_authorization(other, **other_args)
            with pilot._host_lock(self.state), watchdog.HashChainLog(self.state / pilot._HOST_LEDGER) as log, \
                 self.assertRaises(ValueError):
                remedy.claim_locked(log, self.events(), other_approved)
            self.assertEqual(sum(e["kind"] == "observed_remediation_claimed" for e in self.events()), 1)

    def test_valid_authorization_cannot_select_a_shadow_host_ledger(self):
        with self.patches():
            path, _, args = self.make_auth()
            before = (self.state / pilot._HOST_LEDGER).read_bytes()
            shadow = self.root / "unbound-shadow-state"
            with patch.object(pilot, "_git_identity"), self.assertRaisesRegex(
                    ValueError, "authorized host-state"):
                remedy.launch(**args, authorization=path, phase2=self.signal_dir,
                              psa=self.psa, state_dir=shadow)
            self.assertFalse(shadow.exists())
            self.assertEqual((self.state / pilot._HOST_LEDGER).read_bytes(), before)

    def test_prospective_closure_bytes_must_fit_before_creation(self):
        document = {"schema": "SYNTHETIC_CLOSURE_SIZE_ONLY", "completed": False}
        expected_size = len(identity.canonical_json(document) + b"\n")
        path = self.root / "virtual-closure.json"
        pilot._write_new_json(path, document)
        self.assertEqual(path.stat().st_size, expected_size)
        prior = {"old_output_bytes": 100, "old_auxiliary_output_bytes": 20}
        tail = {"wall_seconds": 1, "cpu_seconds": 2}
        charge = {"charged_new_wall_seconds": 5, "charged_new_cpu_seconds": 40,
                  "charged_total_output_bytes": 120 + 30 + expected_size}
        self.assertFalse(remedy._tail_exceeds_charge(prior, tail, charge, 30, expected_size))
        self.assertTrue(remedy._tail_exceeds_charge(prior, tail, charge, 31, expected_size))

    def test_two_spawn_claimants_cannot_both_claim_exception(self):
        with self.patches():
            approved = []
            for _ in range(2):
                path, _, args = self.make_auth()
                approved.append(remedy.validate_authorization(path, **args))
            payload = self.root / "claim-race.json"
            payload.write_text(json.dumps({"packet": self.packet, "state": str(self.state),
                                           "approved": approved}))
        context = multiprocessing.get_context("spawn")
        barrier = context.Barrier(2)
        children = [context.Process(target=claim_racer, args=(str(payload), i, barrier)) for i in range(2)]
        for child in children:
            child.start()
        for child in children:
            child.join(timeout=15)
            if child.is_alive():
                child.kill()
                child.join()
                self.fail(f"Claim contender did not terminate; evidence retained at {self.root}")
            self.assertEqual(child.exitcode, 0)
        results = [json.loads((self.state / f"contender-{i}.json").read_text()) for i in range(2)]
        self.assertEqual(sum(r["claimed"] for r in results), 1, json.dumps(results))
        self.assertEqual(sum(e["kind"] == "observed_remediation_claimed" for e in self.events()), 1)

    def test_claim_process_crash_and_complete_ledger_suffix_loss_fail_closed(self):
        with self.patches():
            path, _, args = self.make_auth()
            approved = remedy.validate_authorization(path, **args)
            payload = self.root / "claim-crash.json"
            payload.write_text(json.dumps({"packet": self.packet, "state": str(self.state),
                                           "approved": approved}))
        child = multiprocessing.get_context("spawn").Process(target=claim_and_exit, args=(str(payload),))
        child.start()
        child.join(timeout=15)
        if child.is_alive():
            child.kill()
            child.join()
            self.fail(f"Claim-crash process remained alive; retained {self.root}")
        self.assertEqual(child.exitcode, 19)
        with self.patches():
            ledger = self.state / pilot._HOST_LEDGER
            original = ledger.read_bytes()
            (self.root / "host-ledger-before-whole-tail-loss.jsonl").write_bytes(original)
            self.assertEqual(self.events()[-1]["kind"], "observed_remediation_claimed")
            ledger.write_bytes(b"".join(original.splitlines(keepends=True)[:-1]))
            # A complete removed line is still a valid hash-chain prefix. A
            # separate exclusive claim receipt must nevertheless reject reuse.
            watchdog.verify_hash_chain(ledger)
            other_path, _, other_args = self.make_auth()
            other_approved = remedy.validate_authorization(other_path, **other_args)
            with pilot._host_lock(self.state), watchdog.HashChainLog(ledger) as log, \
                 self.assertRaises((ValueError, OSError)):
                remedy.claim_locked(log, self.events(), other_approved)

    def run_activity(self, scenario="normal", *, native=False):
        path, auth, args = self.make_auth()
        payload = self.root / f"payload-{args['run_id']}.json"
        payload.write_text(json.dumps({"schema": SYNTHETIC_SCHEMA, "scenario": scenario,
                                       "packet": self.packet, "source": str(self.source),
                                       "prior_info": self.prior_info, "state": str(self.state)}))
        saved_launch = pilot._launch_supervised

        def supervise(command, **kwargs):
            limits = kwargs["limits"]
            values = {"wall_seconds": min(30, limits.wall_seconds),
                      "cpu_seconds": min(30, limits.cpu_seconds),
                      "case_seconds": 30, "oracle_seconds": 30,
                      "aggregate_rss_bytes": 512 * 1024**2,
                      "run_disk_bytes": 32 * 1024**2, "poll_seconds": 0.05}
            if not native:
                values.update({"memory_enforcement_backend": "SAMPLED_ONLY",
                               "reserve_free_disk_bytes": 1, "host_memory_free_percent_stop": None,
                               "boot_volume_path": None, "boot_reserve_free_disk_bytes": None,
                               "minimum_boot_free_disk_bytes": None, "swap_volume_path": None,
                               "swap_volume_reserve_free_disk_bytes": None,
                               "minimum_swap_volume_free_disk_bytes": None,
                               "swap_growth_stop_bytes": None, "require_ac_power": False,
                               "require_thermal_normal": False, "require_sleep_assertion": False})
            kwargs["limits"] = replace(limits, **values)
            return saved_launch([sys.executable, str(Path(__file__).resolve()),
                                 "--synthetic-remediation-child", str(payload)], **kwargs)

        check = {"head": {"head_sha": self.head, "working_tree": "SYNTHETIC_ONLY"},
                 "phase2": str(self.signal_dir), "psa": str(self.psa),
                 "run_parent": str(self.parent), "runtime": identity.h3_runtime_manifest(),
                 "implementation": runner.implementation_identity()}
        with patch.object(pilot, "_git_identity"), \
             patch.object(remedy, "_identity_preflight", return_value=check), \
             patch.object(pilot, "_launch_supervised", side_effect=supervise):
            try:
                result = remedy.launch(**args, authorization=path, phase2=self.signal_dir,
                                       psa=self.psa, state_dir=self.state)
            finally:
                run = args["run_dir"]
                lease = run / pilot._LEASE
                diagnostic = {"run_directory": str(run), "scenario": scenario}
                if lease.exists():
                    diagnostic["lease"] = json.loads(lease.read_text())
                    pid = diagnostic["lease"].get("process_group_id")
                    if isinstance(pid, int) and pid > 1:
                        diagnostic["remaining_group"] = [asdict(p) for p in watchdog.sample_process_group(pid)]
                (self.root / f"post-run-process-group-{args['run_id']}.json").write_text(json.dumps(diagnostic))
        return args["run_dir"], result, auth

    def test_complete_suffix_joint_report_and_original_six_are_immutable(self):
        with self.patches():
            run, result, _ = self.run_activity()
            self.assertEqual(result["status"], "COMPLETED", json.dumps(result))
            joint = result["joint_verification"]
            self.assertTrue(joint["completed"])
            self.assertEqual(joint["OLD"]["rows"], 6)
            self.assertEqual(joint["NEW"]["rows"], 41)
            self.assertEqual(joint["TOTAL"]["unique_rows"], 47)
            self.assertEqual(joint["TOTAL"]["trials"], 9400)
            self.assertFalse(joint["single_continuous_run"])
            self.assertFalse(joint["full_population_U95_supported"])
            events = [json.loads(line)["event"] for line in (run / runner.EVIDENCE).read_text().splitlines()]
            actual = [e["graph_id"] for e in events if e["kind"] == "graph_result"]
            self.assertEqual(actual, [r["graph_id"] for r in self.packet["suffix_rows"]])
            self.assertEqual({p.name: identity.sha256_file(p) for p in self.old_run.iterdir()}, self.old_hashes)
            with watchdog.HashChainLog(self.state / pilot._HOST_LEDGER) as log:
                log.append({"kind": "unrelated_future_audit", "payload": "synthetic" * 10000})
            # Shared-ledger growth after closure is not this activity's output.
            self.assertTrue(remedy.verify_joint(run, state_dir=self.state)["completed"])
            account = run / remedy.ACCOUNT_FILE
            account.write_bytes(account.read_bytes() + b" ")
            with self.assertRaises(ValueError):
                remedy.verify_joint(run, state_dir=self.state)

    def test_unknown_child_stops_and_exception_cannot_be_claimed_again(self):
        with self.patches():
            try:
                run, result, _ = self.run_activity("unknown_child")
                self.assertFalse(result["joint_verification"]["completed"])
            except ValueError:
                runs = [p for p in self.parent.iterdir() if p.name != self.old_id]
                self.assertEqual(len(runs), 1)
                run = runs[0]
            summary = json.loads((run / "h3-summary.json").read_text())
            self.assertEqual(summary["status"], "STOPPED_BY_WATCHDOG", json.dumps(summary))
            self.assertEqual(summary["watchdog"]["reason"], "UNKNOWN_PROCESS_GROUP_MEMBER")
            self.assertFalse(summary["resume_allowed"])
            path, _, args = self.make_auth()
            with self.assertRaises(ValueError):
                remedy.assert_claim_state(self.events(), remedy.validate_authorization(path, **args)["binding"],
                                          identity.sha256_file(path), phase="unclaimed")

    def test_child_exit_preserves_terminal_and_cannot_be_success(self):
        with self.patches():
            try:
                _, result, _ = self.run_activity("child_exit")
                self.assertFalse(result["joint_verification"]["completed"])
            except (ValueError, OSError):
                pass
            runs = [p for p in self.parent.iterdir() if p.name != self.old_id]
            self.assertEqual(len(runs), 1)
            summary = json.loads((runs[0] / "h3-summary.json").read_text())
            self.assertNotEqual(summary["status"], "COMPLETED", json.dumps(summary))
            self.assertFalse(summary["resume_allowed"])
            self.assertEqual(sum(e["kind"] == "observed_remediation_claimed" for e in self.events()), 1)

    def test_injected_write_failure_and_synthetic_marker_never_become_joint_success(self):
        with self.patches():
            run, result, _ = self.run_activity("write_failure")
            self.assertFalse(result["joint_verification"]["completed"])
            terminal = json.loads((run / "runner-terminal.json").read_text())
            self.assertEqual(terminal["failure_category"], "OPERATIONAL_IO")
            self.assertEqual(terminal["rows_completed"], 0)
        # Independent synthetic history for the one synthetic-marker fault.
        self.setUp()
        with self.patches(), self.assertRaisesRegex(ValueError, "non-synthetic"):
            self.run_activity("synthetic_marker")

    def test_cumulative_CPU_and_output_faults_stop_without_success(self):
        for scenario in ("CPU", "OUTPUT"):
            if scenario == "OUTPUT":
                self.setUp()
            with self.patches(), ExitStack() as stack:
                saved_extra = remedy._extra_bytes
                saved_meter = remedy.ControllerMeter
                if scenario == "OUTPUT":
                    def oversized(run_dir, *args, _saved_extra=saved_extra):
                        value = _saved_extra(run_dir, *args)
                        return value + (1 << 30) if run_dir.exists() else value
                    stack.enter_context(patch.object(remedy, "_extra_bytes", side_effect=oversized))
                else:
                    class ExhaustedMeter:
                        def __init__(self, factory=saved_meter):
                            self.actual = factory()

                        def snapshot(self, run_dir=None):
                            value = self.actual.snapshot(run_dir)
                            if run_dir is not None and run_dir.exists():
                                value["cpu_seconds"] = 15000
                            return value
                    stack.enter_context(patch.object(remedy, "ControllerMeter", ExhaustedMeter))
                with self.assertRaises((ValueError, remedy.RemediationBudgetError)):
                    self.run_activity()
                runs = [p for p in self.parent.iterdir() if p.name != self.old_id]
                self.assertEqual(len(runs), 1)
                summary = json.loads((runs[0] / "h3-summary.json").read_text())
                self.assertEqual(summary["status"], "STOPPED_BY_WATCHDOG", json.dumps(summary))
                self.assertEqual(summary["watchdog"]["reason"],
                                 "REMEDIATION_CUMULATIVE_BUDGET_OR_ACCOUNTING_STOP")
                self.assertEqual(sum(e["kind"] == "observed_remediation_claimed" for e in self.events()), 1)

    def test_tail_overrun_cannot_be_erased_by_removing_whole_violation_line(self):
        with self.patches():
            saved_meter = remedy.ControllerMeter

            class OverrunAfterAccount:
                def __init__(self):
                    self.actual = saved_meter()

                def snapshot(self, run_dir=None):
                    snapshot = self.actual.snapshot(run_dir)
                    if run_dir is not None and (run_dir / remedy.ACCOUNT_FILE).exists():
                        snapshot["wall_seconds"] += 10
                    return snapshot

            with patch.object(remedy, "ControllerMeter", OverrunAfterAccount), \
                 self.assertRaisesRegex(ValueError, "Closing work"):
                self.run_activity()
            run = next(p for p in self.parent.iterdir() if p.name != self.old_id)
            self.assertTrue((run / remedy.ACCOUNT_FILE).exists())
            self.assertFalse((run / remedy.CLOSED_FILE).exists())
            ledger = self.state / pilot._HOST_LEDGER
            original = ledger.read_bytes()
            self.assertEqual(self.events()[-1]["kind"], "observed_remediation_violation")
            self.assertEqual(self.events()[-1]["reason"], "FINAL_AUDIT_OR_ACCOUNTING_FAILED")
            (self.root / "ledger-before-violation-tail-loss.jsonl").write_bytes(original)
            lines = original.splitlines(keepends=True)
            while json.loads(lines[-1])["event"]["kind"] == "observed_remediation_violation":
                lines.pop()
            ledger.write_bytes(b"".join(lines))
            watchdog.verify_hash_chain(ledger)
            with self.assertRaises((ValueError, pilot.H3PilotError)):
                remedy.verify_joint(run, state_dir=self.state)

    def test_preflight_budget_refusal_consumes_claim_without_creating_results(self):
        with self.patches():
            path, _, args = self.make_auth()
            with patch.object(pilot, "_git_identity"), \
                 patch.object(remedy, "_original_budget", return_value={
                     **self.prior_info, "old_wall_charge_seconds": 14400}), \
                 patch.object(remedy, "_identity_preflight", return_value={}), \
                 self.assertRaises(remedy.RemediationBudgetError):
                remedy.launch(**args, authorization=path, phase2=self.signal_dir,
                              psa=self.psa, state_dir=self.state)
            self.assertFalse(args["run_dir"].exists())
            self.assertEqual(self.events()[-1]["kind"], "observed_remediation_admission_failed")
            with self.assertRaises(ValueError):
                remedy.assert_claim_state(self.events(), remedy.bindings(
                    self.head, str(uuid.uuid4()), self.parent / str(uuid.uuid4()), self.old_run),
                    "0" * 64, phase="unclaimed")

    @unittest.skipUnless(sys.platform == "darwin", "three fixed native macOS synthetic trials")
    def test_fixed_three_native_supervised_suffix_trials_no_failure_retry(self):
        # Exactly three predeclared independent synthetic histories. The first
        # failure raises immediately; all fixtures/logs survive without teardown.
        for trial in range(3):
            if trial:
                self.setUp()
            with self.patches():
                run, result, _ = self.run_activity(native=True)
                self.assertEqual(result["status"], "COMPLETED", json.dumps({
                    "trial": trial + 1, "run": str(run), "result": result}))
                self.assertTrue(result["joint_verification"]["completed"])
                summary = json.loads((run / "h3-summary.json").read_text())
                self.assertEqual(summary["watchdog"]["usage"]["sleep_assertion"], "CAFFEINATE_ACTIVE")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--synthetic-remediation-child":
        raise SystemExit(synthetic_child(Path(sys.argv[2])))
    unittest.main()
