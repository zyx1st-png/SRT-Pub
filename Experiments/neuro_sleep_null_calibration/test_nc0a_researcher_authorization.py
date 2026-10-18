"""Researcher-gate tests use synthetic records and bounded nonformal workers."""

from __future__ import annotations

import base64
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
import json
import plistlib
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
import uuid
from unittest import mock

import nc0a_execution_engine as engine
import nc0a_watchdog as watchdog
from nc0a_execution_engine import ExecutionError
from nc0a_researcher_authorization import (
    MEMORY_RISK, PACKAGE_FORMAT, ResearcherAuthorizationError,
    canonical_bytes, commitment_sha256, validate_package,
    validate_remote_audit_anchor, validate_remote_precommit,
    validate_remote_review,
)
from nc0a_watchdog import HashChainLog, WatchdogError, verify_hash_chain


GIB = 1024 ** 3
RESEARCHER_LOGIN = "researcher-account"


def _b64(value: dict) -> str:
    return base64.b64encode(canonical_bytes(value)).decode("ascii")


def _comment(comment_id: int, login: str, body: str, created: datetime) -> dict:
    url = f"https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-{comment_id}"
    return {"html_url": url,
            "issue_url": "https://api.github.com/repos/zyx1st-png/SRT-Pub/issues/1114",
            "user": {"login": login}, "body": body,
            "created_at": created.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")}


def fixture_context(run_dir: Path) -> dict:
    data = {"mount_point": "/System/Volumes/Data", "filesystem": "APFS",
            "internal": True, "volume_uuid": "AAAA-1111", "device_identifier": "disk3s5"}
    vm = {"mount_point": "/System/Volumes/VM", "filesystem": "APFS",
          "internal": True, "volume_uuid": "BBBB-2222", "device_identifier": "disk3s6"}
    sources = {name: hashlib.sha256(name.encode()).hexdigest()
               for name in ("engine", "watchdog", "contract", "graphs", "authorization")}
    return {
        "head_sha": "1" * 40,
        "clean_tree": True,
        "preregistration_sha256": "a" * 64,
        "resource_amendment_sha256": "b" * 64,
        "runtime_lock_sha256": "c" * 64,
        "protocol_sha256": "d" * 64,
        "seed_manifest_sha256": "e" * 64,
        "watchdog_contract_sha256": "f" * 64,
        "watchdog_source_sha256": "0" * 64,
        "source_sha256": sources,
        "environment": {
            "host_identifier": "host-fingerprint",
            "physical_ram_bytes": 16 * GIB,
            "python": "3.11.15",
            "runtime_lock_sha256": "c" * 64,
            "machine": "arm64",
        },
        "data_volume": data,
        "vm_volume": vm,
        "output_volume": data,
        "output_directory": str(run_dir.resolve()),
        "scientific_protocol": {
            "formal_cases": 16, "chains_per_case": 8,
            "long_chain_proposals": 44_937_216,
            "oracle_streams": 16, "total_oracle_proposals": 16_000,
            "comparisons": 48, "seed_root": 20261009,
            "mixing_interpretation": "MIXING-UNRESOLVED",
        },
        "current_data_free_bytes": 50 * GIB,
        "current_vm_free_bytes": 50 * GIB,
        "current_host_memory_pressure": {"free_percent": 35},
        "current_macos_native_state": {"ac_power": True, "thermal_normal": True},
    }


def make_package(run_dir: Path, *, wall_seconds: int = 72 * 3600,
                 cpu_seconds: int = 288 * 3600) -> tuple[dict, dict]:
    context = fixture_context(run_dir)
    now = datetime.now(timezone.utc)
    confirmed = now - timedelta(minutes=5)
    reviews = [
        {"reviewer_id": "model-alpha", "reviewer_type": "AI_MODEL",
         "reviewed_head_sha": context["head_sha"],
         "decision": "NO_BLOCKING_FINDINGS_FOR_NC0A_EXECUTION",
         "scope": ["methods", "statistics"], "blocking_findings": [],
         "human_peer_review": False,
         "github_comment_url": "https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-101"},
        {"reviewer_id": "model-beta", "reviewer_type": "AI_MODEL",
         "reviewed_head_sha": context["head_sha"],
         "decision": "NO_BLOCKING_FINDINGS_FOR_NC0A_EXECUTION",
         "scope": ["implementation"], "blocking_findings": [],
         "human_peer_review": False,
         "github_comment_url": "https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-102"},
    ]
    policy = {
        "version": "NC0A_MACOS_RESEARCHER_RESOURCE_POLICY_V1",
        "memory_backend": "MACOS_SAMPLED_PRESSURE",
        "macos_memory_semantics": MEMORY_RISK,
        "output_directory": str(run_dir.resolve()),
        "output_volume": context["data_volume"],
        "internal_volumes": {"data": context["data_volume"], "vm": context["vm_volume"]},
        "baseline_measurement": {
            "measured_at_utc": confirmed.isoformat(),
            "data_free_bytes": 50 * GIB, "vm_free_bytes": 50 * GIB,
            "host_memory_free_percent": 35, "swap_total_bytes": 14 * GIB,
            "swap_used_bytes": 13 * GIB, "swap_free_bytes": 1 * GIB,
        },
        "limits": {
            "max_workers": 4, "wall_seconds": wall_seconds,
            "cpu_seconds": cpu_seconds, "per_case_seconds": 12 * 3600,
            "oracle_seconds": 1800, "sampled_rss_bytes": 4 * GIB,
            "host_free_percent_stop": 20, "swap_growth_bytes": 2 * GIB,
            "data_min_free_bytes": 40 * GIB, "data_reserve_bytes": 30 * GIB,
            "vm_min_free_bytes": 40 * GIB, "vm_reserve_bytes": 30 * GIB,
            "run_output_cap_bytes": 4 * GIB, "run_output_reserve_bytes": 30 * GIB,
            "max_attempts_per_case": 2,
        },
        "require_ac_power": True,
        "require_normal_thermal_state": True,
        "require_sleep_assertion": True,
        "recovery_rule": "TASK_LEVEL_FROM_ZERO_SAME_SEED_NO_OUTCOME_DEPENDENT_RETRY",
    }
    commitment = {
        "format": "NC0A_RESEARCHER_AUTHORIZED_COMMITMENT_V1",
        "experiment_uuid": str(uuid.uuid4()),
        "researcher": {
            "name": "Researcher Test Fixture",
            "github_login": RESEARCHER_LOGIN,
            "decision": "I_APPROVE_FORMAL_NC0A_AND_ACCEPT_THE_RECORDED_LIMITS_AND_RISKS",
            "confirmed_at_utc": confirmed.isoformat(),
            "confirmation_phrase": "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS",
        },
        "repository": {
            "head_sha": context["head_sha"], "clean_tree": True,
            "preregistration_sha256": context["preregistration_sha256"],
            "resource_amendment_sha256": context["resource_amendment_sha256"],
            "runtime_lock_sha256": context["runtime_lock_sha256"],
            "protocol_sha256": context["protocol_sha256"],
            "seed_manifest_sha256": context["seed_manifest_sha256"],
            "watchdog_contract_sha256": context["watchdog_contract_sha256"],
            "watchdog_source_sha256": context["watchdog_source_sha256"],
            "source_sha256": context["source_sha256"],
        },
        "environment": deepcopy(context["environment"]),
        "scientific_protocol": deepcopy(context["scientific_protocol"]),
        "independent_science_reviews": reviews,
        "resource_policy": policy,
        "risk_acknowledgements": {
            "macos_sampled_memory_is_not_a_hard_limit": True,
            "transient_memory_peaks_can_be_missed": True,
            "T_PS_A_remains_unresolved": True,
            "NC0a_budget_does_not_clear_G0_or_T1": True,
            "all_passes_retain_MIXING_UNRESOLVED": True,
            "prior_informal_result_exposure_is_disclosed": True,
            "no_outcome_dependent_seed_change_retry_or_threshold_change": True,
            "researcher_accepts_execution_risk_without_third_party_authorization": True,
            "AI_review_is_not_external_human_peer_review": True,
        },
    }
    package = {
        "format": PACKAGE_FORMAT,
        "commitment": commitment,
        "commitment_sha256": commitment_sha256(commitment),
        "precommit_comment_url": "https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-103",
    }
    return package, context


def fake_remote_comments(package: dict, *, audit_body: str | None = None) -> dict[str, dict]:
    commitment = package["commitment"]
    confirmed = datetime.fromisoformat(commitment["researcher"]["confirmed_at_utc"])
    precommit_time = confirmed + timedelta(seconds=2)
    comments = {}
    for review in commitment["independent_science_reviews"]:
        record = {k: v for k, v in review.items() if k != "github_comment_url"}
        url = review["github_comment_url"]
        comment_id = int(url.rsplit("-", 1)[1])
        comments[url] = _comment(
            comment_id, "review-bot",
            "NC0A_INDEPENDENT_REVIEW_JSON_BASE64=" + _b64(record), confirmed + timedelta(seconds=1))
    pre_url = package["precommit_comment_url"]
    pre_id = int(pre_url.rsplit("-", 1)[1])
    comments[pre_url] = _comment(
        pre_id, RESEARCHER_LOGIN,
        "NC0A_RESEARCHER_PRECOMMIT_JSON_BASE64=" + _b64(commitment), precommit_time)
    if audit_body:
        audit_url = "https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-104"
        comments[audit_url] = _comment(104, RESEARCHER_LOGIN, audit_body,
                                       precommit_time + timedelta(seconds=1))
    return comments


class ResearcherAuthorizationSchemaTests(unittest.TestCase):
    def test_output_directory_maps_by_device_to_internal_volume_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            directory_name = str(directory.resolve())
            original_stat = os.stat
            volumes = {
                "/System/Volumes/Data": (101, {
                    "MountPoint": "/System/Volumes/Data", "FilesystemName": "apfs",
                    "Internal": True, "VolumeUUID": "DATA-UUID",
                    "DeviceIdentifier": "disk3s5"}),
                "/System/Volumes/VM": (202, {
                    "MountPoint": "/System/Volumes/VM", "FilesystemName": "apfs",
                    "Internal": True, "VolumeUUID": "VM-UUID",
                    "DeviceIdentifier": "disk3s6"}),
            }

            def fake_stat(path, *args, **kwargs):
                name = os.fspath(path)
                if name == directory_name:
                    return SimpleNamespace(st_dev=101)
                for mount, (device, _) in volumes.items():
                    if name == mount:
                        return SimpleNamespace(st_dev=device)
                return original_stat(path, *args, **kwargs)

            def fake_diskutil(args, **kwargs):
                payload = plistlib.dumps(volumes[args[-1]][1])
                return SimpleNamespace(stdout=payload)

            with mock.patch.object(engine.os, "stat", side_effect=fake_stat), \
                    mock.patch.object(engine.subprocess, "run", side_effect=fake_diskutil):
                identity = engine._disk_volume_identity(directory)
            self.assertEqual(identity["mount_point"], "/System/Volumes/Data")
            self.assertEqual(identity["volume_uuid"], "DATA-UUID")
            self.assertTrue(identity["internal"])

    def test_output_directory_on_unreviewed_volume_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            directory_name = str(directory.resolve())
            original_stat = os.stat
            devices = {"/System/Volumes/Data": 101,
                       "/System/Volumes/VM": 202}
            records = {
                "/System/Volumes/Data": {"MountPoint": "/System/Volumes/Data",
                    "FilesystemName": "apfs", "Internal": True,
                    "VolumeUUID": "DATA-UUID", "DeviceIdentifier": "disk3s5"},
                "/System/Volumes/VM": {"MountPoint": "/System/Volumes/VM",
                    "FilesystemName": "apfs", "Internal": True,
                    "VolumeUUID": "VM-UUID", "DeviceIdentifier": "disk3s6"},
            }

            def fake_stat(path, *args, **kwargs):
                name = os.fspath(path)
                if name == directory_name:
                    return SimpleNamespace(st_dev=303)
                if name in devices:
                    return SimpleNamespace(st_dev=devices[name])
                return original_stat(path, *args, **kwargs)

            def fake_diskutil(args, **kwargs):
                return SimpleNamespace(stdout=plistlib.dumps(records[args[-1]]))

            with mock.patch.object(engine.os, "stat", side_effect=fake_stat), \
                    mock.patch.object(engine.subprocess, "run", side_effect=fake_diskutil):
                with self.assertRaisesRegex(ExecutionError, "not on either reviewed internal"):
                    engine._disk_volume_identity(directory)

    def test_exact_plan_passes_schema_but_does_not_claim_external_authorization(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir)
            result = validate_package(package, context=context, run_dir=run_dir)
            self.assertEqual(result["status"], "SCHEMA_AND_IDENTITY_VALID_NOT_EXECUTION_AUTHORIZATION")
            self.assertFalse(result["third_party_authorization"])
            self.assertFalse(result["external_human_peer_review"])

    def test_tampered_commitment_hash_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir)
            package["commitment"]["resource_policy"]["limits"]["wall_seconds"] -= 1
            with self.assertRaisesRegex(ResearcherAuthorizationError, "SHA-256 mismatch"):
                validate_package(package, context=context, run_dir=run_dir)

    def test_scientific_identity_or_scale_change_is_rejected_even_after_rehash(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir)
            package["commitment"]["repository"]["head_sha"] = "2" * 40
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "HEAD"):
                validate_package(package, context=context, run_dir=run_dir)
            package, context = make_package(run_dir)
            package["commitment"]["scientific_protocol"]["comparisons"] = 47
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "Scientific scale"):
                validate_package(package, context=context, run_dir=run_dir)

    def test_resource_budget_cannot_exceed_candidate_ceilings_or_lower_disk_floor(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir, wall_seconds=72 * 3600 + 1)
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "72-hour"):
                validate_package(package, context=context, run_dir=run_dir)
            package, context = make_package(run_dir)
            package["commitment"]["resource_policy"]["limits"]["data_min_free_bytes"] = 39 * GIB
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "40 GiB"):
                validate_package(package, context=context, run_dir=run_dir)

    def test_sampled_memory_risk_cannot_be_relabelled_as_hard_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir)
            package["commitment"]["resource_policy"]["macos_memory_semantics"] = "HARD_LIMIT"
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "risk may not be weakened"):
                validate_package(package, context=context, run_dir=run_dir)

    def test_distinct_current_head_reviews_cover_required_scopes(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir)
            package["commitment"]["independent_science_reviews"][1]["reviewer_id"] = "model-alpha"
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "distinct nonempty identities"):
                validate_package(package, context=context, run_dir=run_dir)
            package, context = make_package(run_dir)
            package["commitment"]["independent_science_reviews"][1]["reviewed_head_sha"] = "9" * 40
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "exact frozen HEAD"):
                validate_package(package, context=context, run_dir=run_dir)

    def test_ai_review_cannot_claim_human_peer_review_and_blocker_stops(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir)
            package["commitment"]["independent_science_reviews"][0]["human_peer_review"] = True
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "cannot be labeled human peer"):
                validate_package(package, context=context, run_dir=run_dir)
            package, context = make_package(run_dir)
            package["commitment"]["independent_science_reviews"][0]["blocking_findings"] = ["open defect"]
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "open blocking findings"):
                validate_package(package, context=context, run_dir=run_dir)

    def test_current_storage_and_exact_output_volume_are_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir)
            context["current_data_free_bytes"] = 39 * GIB
            with self.assertRaisesRegex(ResearcherAuthorizationError, "below the signed launch floors"):
                validate_package(package, context=context, run_dir=run_dir)
            package, context = make_package(run_dir)
            package["commitment"]["resource_policy"]["output_directory"] = str(Path(tmp) / "other")
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "output path"):
                validate_package(package, context=context, run_dir=run_dir)

    def test_public_precommit_and_review_markers_bind_exact_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, _ = make_package(run_dir)
            comments = fake_remote_comments(package)
            validate_remote_precommit(package, comments[package["precommit_comment_url"]])
            review = package["commitment"]["independent_science_reviews"][0]
            validate_remote_review(review, comments[review["github_comment_url"]])
            comments[package["precommit_comment_url"]]["body"] += "tamper"
            with self.assertRaisesRegex(ResearcherAuthorizationError, "Malformed"):
                validate_remote_precommit(package, comments[package["precommit_comment_url"]])

    def test_researcher_cannot_supply_their_own_human_review_comment(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, _ = make_package(run_dir)
            review = package["commitment"]["independent_science_reviews"][0]
            review["reviewer_type"] = "HUMAN_REVIEWER"
            review["human_peer_review"] = False
            record = {k: v for k, v in review.items() if k != "github_comment_url"}
            comment = _comment(
                int(review["github_comment_url"].rsplit("-", 1)[1]),
                RESEARCHER_LOGIN,
                "NC0A_INDEPENDENT_REVIEW_JSON_BASE64=" + _b64(record),
                datetime.fromisoformat(
                    package["commitment"]["researcher"]["confirmed_at_utc"]) + timedelta(seconds=1))
            with self.assertRaisesRegex(ExecutionError, "own GitHub comment"):
                engine._verify_researcher_remote_records(
                    package,
                    lambda url: (comment if url == review["github_comment_url"] else
                                 fake_remote_comments(package)[url]))

    def test_only_pr_1114_top_level_comment_urls_are_accepted(self):
        with self.assertRaisesRegex(ResearcherAuthorizationError, "PR #1114"):
            from nc0a_researcher_authorization import parse_github_comment_url
            parse_github_comment_url("https://github.com/zyx1st-png/SRT-Pub/issues/1114")

    def test_remote_pr_head_must_match_the_reviewed_commit(self):
        with self.assertRaisesRegex(ExecutionError, "GitHub PR #1114 HEAD"):
            engine._verify_current_remote_pr_head(
                "1" * 40, lambda: {"head": {"sha": "2" * 40}})
        engine._verify_current_remote_pr_head(
            "1" * 40, lambda: {"head": {"sha": "1" * 40}})

    def test_missing_or_old_host_baseline_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            package, context = make_package(run_dir)
            package["commitment"]["resource_policy"]["baseline_measurement"]["data_free_bytes"] = 39 * GIB
            package["commitment_sha256"] = commitment_sha256(package["commitment"])
            with self.assertRaisesRegex(ResearcherAuthorizationError, "baseline does not satisfy"):
                validate_package(package, context=context, run_dir=run_dir)


class WatchdogStdoutRecoveryCompatibilityTests(unittest.TestCase):
    def test_legacy_watchdog_stdout_digest_is_paired_by_invocation_order(self):
        with tempfile.TemporaryDirectory(prefix="nc0a-stdout-legacy-") as tmp:
            root = Path(tmp)
            stdout = root / "runner.stdout.01.log"
            payload = b"legacy watchdog runner output\n"
            stdout.write_bytes(payload)
            log = HashChainLog(root / "watchdog.jsonl")
            try:
                log.append({"event": "run_started", "pid": 101, "pgid": 101})
                log.append({"event": "runner_exited", "returncode": 17,
                            "usage": {"wall_seconds": 1.0, "cpu_seconds": 1.0,
                                      "runner_stdout_sha256": hashlib.sha256(
                                          payload).hexdigest()}})
            finally:
                log.close()
            self.assertEqual(
                engine._verify_researcher_stdout_history(
                    root, [{"invocation": 1, "watchdog_started": True}]),
                {"runner.stdout.01.log"})


class ResearcherAuthorizedLauncherTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="nc0a-researcher-gate-")
        self.base = Path(self.tmp.name)
        self.run_dir = (self.base / "run").resolve()
        self.package, self.context = make_package(self.run_dir)
        self.package_path = self.base / "commitment.json"
        self.package_path.write_bytes(canonical_bytes(self.package) + b"\n")
        self.comments = fake_remote_comments(self.package)
        self.calls = 0

    def tearDown(self):
        self.tmp.cleanup()

    def comment_fetcher(self, url: str) -> dict:
        return self.comments[url]

    def comment_lister(self) -> list[dict]:
        return list(self.comments.values())

    def fake_supervisor(self, command, root, limits, invocation):
        self.calls += 1
        usage = {"wall_seconds": 2.0, "cpu_seconds": 3.0,
                 "peak_aggregate_rss_bytes": 123456, "run_directory_bytes": 4096}
        stdout_path = Path(root) / f"runner.stdout.{invocation:02d}.log"
        stdout_bytes = f"fake watchdog invocation {invocation}\n".encode()
        stdout_path.write_bytes(stdout_bytes)
        stdout_sha256 = hashlib.sha256(stdout_bytes).hexdigest()
        log = HashChainLog(Path(root) / "watchdog.jsonl")
        try:
            log.append({"event": "run_started", "utc": "test",
                        "invocation": invocation, "pid": 10,
                        "pgid": 10, "limits": {"wall_seconds": limits.wall_seconds}})
            log.append({"event": "runner_exited", "invocation": invocation,
                        "returncode": 17, "usage": {
                            **usage, "runner_stdout_sha256": stdout_sha256}})
        finally:
            log.close()
        # No formal result is created: the launcher must preserve this as an
        # incomplete/non-successful run rather than treating a child exit as NC-0a.
        return {"status": "failed", "returncode": 17, "usage": usage,
                "command": command}

    def launch_patches(self):
        return mock.patch.multiple(
            engine,
            _assert_clean_source_tree=mock.DEFAULT,
            _researcher_context=mock.DEFAULT,
            _verify_runtime_lock=mock.DEFAULT,
            _verify_current_remote_pr_head=mock.DEFAULT,
            validate_macos_sampled_backend=mock.DEFAULT,
            sample_host_memory_pressure=mock.DEFAULT,
            _supervise_named=mock.DEFAULT,
        )

    def test_complete_gate_reuses_watchdog_and_never_calls_science_directly(self):
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            patched["_supervise_named"].side_effect = self.fake_supervisor
            result = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)
        self.assertEqual(self.calls, 1)
        self.assertIn("--researcher-runner-internal", result["watchdog"].get("command", []))
        self.assertEqual(result["run_integrity"], "NOT_COMPLETE")
        self.assertNotEqual(result["run_integrity"], "VERIFIED_COMPLETE")
        self.assertFalse(result["third_party_authorization"])
        self.assertTrue(Path(result["audit_summary_path"]).is_file())
        self.assertEqual(verify_hash_chain(self.run_dir / "researcher_authorization.jsonl")[0], 4)

    def test_wrong_typed_confirmation_blocks_before_files_or_supervisor(self):
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            with self.assertRaisesRegex(engine.ExecutionError, "Typed researcher confirmation"):
                engine.launch_researcher_authorized(
                    self.package_path, self.run_dir, "yes",
                    comment_fetcher=self.comment_fetcher,
                    comment_lister=self.comment_lister)
        self.assertEqual(self.calls, 0)
        self.assertFalse(self.run_dir.exists())

    def test_symlinked_output_path_is_rejected_before_resolution(self):
        target = self.base / "real-run"
        target.mkdir()
        link = self.base / "run-link"
        link.symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ExecutionError, "symlink"):
            engine._resolved_non_symlink_path(link)

    def test_symlinked_run_log_is_rejected_before_hashchain_open(self):
        self.run_dir.mkdir()
        outside = self.base / "outside.jsonl"
        outside.write_text("outside evidence\n", encoding="utf-8")
        (self.run_dir / "researcher_authorization.jsonl").symlink_to(outside)
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            with self.assertRaisesRegex(ExecutionError, "cannot be symlinks"):
                engine.launch_researcher_authorized(
                    self.package_path, self.run_dir,
                    "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                    self.package["commitment"]["experiment_uuid"],
                    comment_fetcher=self.comment_fetcher,
                    comment_lister=self.comment_lister)
        self.assertEqual(outside.read_text(encoding="utf-8"), "outside evidence\n")

    def test_current_head_and_reviews_are_checked_before_watchdog(self):
        bad = deepcopy(self.context)
        bad["head_sha"] = "f" * 40
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = bad
            with self.assertRaisesRegex(engine.ExecutionError, "HEAD"):
                engine.launch_researcher_authorized(
                    self.package_path, self.run_dir,
                    "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                    self.package["commitment"]["experiment_uuid"],
                    comment_fetcher=self.comment_fetcher,
                    comment_lister=self.comment_lister)
        self.assertEqual(self.calls, 0)

    def test_audit_anchor_allows_same_run_resume_and_tracks_cumulative_cost(self):
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            patched["_supervise_named"].side_effect = self.fake_supervisor
            first = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)
            anchor_url = "https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-104"
            self.comments.update(fake_remote_comments(self.package,
                                                      audit_body=first["github_anchor_body"]))
            second = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                resume_anchor_url=anchor_url, comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)
        self.assertEqual(second["invocation"], 2)
        self.assertEqual(second["cumulative_wall_seconds"], 4.0)
        self.assertEqual(second["cumulative_cpu_seconds"], 6.0)
        self.assertEqual(self.calls, 2)

    def test_actual_watchdog_failure_stdout_public_anchor_and_same_uuid_resume(self):
        class AliveAssertion:
            @staticmethod
            def poll():
                return None

        real_disk_usage = watchdog.shutil.disk_usage

        def disk_usage(path):
            if str(path) in ("/System/Volumes/Data", "/System/Volumes/VM"):
                return SimpleNamespace(total=100 * GIB, used=50 * GIB, free=50 * GIB)
            return real_disk_usage(path)

        native = {
            "swap_total_bytes": 14 * GIB, "swap_used_bytes": 10 * GIB,
            "swap_free_bytes": 4 * GIB, "ac_power": True,
            "thermal_normal": True, "thermal_warning_level": 0,
            "performance_warning_level": 0,
        }
        script = (
            "import json, os, sys; "
            "json.dump({'format':'NC0A_PROCESS_ROLE_REGISTRY_V1', "
            "'launch_token':os.environ['NC0A_WATCHDOG_LAUNCH_TOKEN'], "
            "'runner_pid':os.getpid(), 'roles':{}}, "
            "open(os.environ['NC0A_PROCESS_ROLE_REGISTRY'],'w')); "
            "print('bounded watchdog worker', sys.argv[1], flush=True); "
            "raise SystemExit(17 if sys.argv[1] == '1' else 0)"
        )
        command_invocations = []

        def test_worker_command(*_args):
            invocation = len(command_invocations) + 1
            command_invocations.append(invocation)
            return [sys.executable, "-c", script, str(invocation)]

        engine_patches = {
            "_assert_clean_source_tree": mock.DEFAULT,
            "_researcher_context": mock.DEFAULT,
            "_verify_runtime_lock": mock.DEFAULT,
            "_verify_current_remote_pr_head": mock.DEFAULT,
            "validate_macos_sampled_backend": mock.DEFAULT,
            "sample_host_memory_pressure": mock.DEFAULT,
            "_researcher_runner_command": mock.DEFAULT,
        }
        watchdog_patches = {
            "validate_macos_sampled_backend": mock.DEFAULT,
            "sample_host_memory_pressure": mock.DEFAULT,
            "sample_macos_native_state": mock.DEFAULT,
            "_start_sleep_assertion": mock.DEFAULT,
            "_stop_sleep_assertion": mock.DEFAULT,
        }
        with mock.patch.multiple(engine, **engine_patches) as engine_mock, \
             mock.patch.multiple(watchdog, **watchdog_patches) as watchdog_mock, \
             mock.patch.object(watchdog.shutil, "disk_usage", side_effect=disk_usage):
            engine_mock["_researcher_context"].return_value = self.context
            engine_mock["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            engine_mock["_researcher_runner_command"].side_effect = test_worker_command
            watchdog_mock["validate_macos_sampled_backend"].return_value = {
                **native, "boot_volume_free_bytes": 50 * GIB,
                "swap_volume_free_bytes": 50 * GIB,
            }
            watchdog_mock["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            watchdog_mock["sample_macos_native_state"].return_value = native
            watchdog_mock["_start_sleep_assertion"].return_value = AliveAssertion()
            watchdog_mock["_stop_sleep_assertion"].return_value = None

            first = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)

            stdout_path = self.run_dir / "runner.stdout.01.log"
            self.assertTrue(stdout_path.is_file())
            self.assertEqual(first["watchdog"]["status"], "failed")
            self.assertEqual(first["run_integrity"], "NOT_COMPLETE")
            stdout_digest = hashlib.sha256(stdout_path.read_bytes()).hexdigest()
            watchdog_rows, _ = engine._read_chain_rows(self.run_dir / "watchdog.jsonl")
            terminal = [row["event"] for row in watchdog_rows
                        if row["event"].get("event") == "runner_exited"][-1]
            self.assertEqual(terminal["invocation"], 1)
            self.assertEqual(terminal["usage"]["runner_stdout_sha256"], stdout_digest)
            audit_rows, _ = engine._read_chain_rows(
                self.run_dir / "researcher_authorization.jsonl")
            self.assertEqual(audit_rows[-1]["event"]["event"], "invocation_finished")
            self.assertEqual(audit_rows[-1]["event"]["status"], "failed")

            anchor_url = "https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-104"
            self.comments.update(fake_remote_comments(
                self.package, audit_body=first["github_anchor_body"]))
            second = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                resume_anchor_url=anchor_url,
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)

        self.assertEqual(command_invocations, [1, 2])
        self.assertEqual(second["experiment_uuid"],
                         self.package["commitment"]["experiment_uuid"])
        self.assertEqual(second["invocation"], 2)
        self.assertEqual(second["watchdog"]["status"], "completed")
        self.assertEqual(second["run_integrity"], "NOT_COMPLETE")
        self.assertEqual(second["watchdog"]["returncode"], 0)
        self.assertTrue((self.run_dir / "runner.stdout.01.log").is_file())
        self.assertTrue((self.run_dir / "runner.stdout.02.log").is_file())
        self.assertFalse(any(self.run_dir.glob(".nc0a-process-roles-*.json")))
        self.assertFalse((self.run_dir / ".watchdog-emergency.reserve").exists())
        self.assertGreaterEqual(
            second["cumulative_wall_seconds"],
            first["cumulative_wall_seconds"] +
            second["watchdog"]["usage"]["wall_seconds"])

    def test_resume_rejects_stdout_with_noncanonical_invocation_number(self):
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            patched["_supervise_named"].side_effect = self.fake_supervisor
            first = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)
        self.comments.update(fake_remote_comments(
            self.package, audit_body=first["github_anchor_body"]))
        (self.run_dir / "runner.stdout.0001.log").write_text("unbound\n")
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            with self.assertRaisesRegex(ExecutionError, "not canonical"):
                engine.launch_researcher_authorized(
                    self.package_path, self.run_dir,
                    "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                    self.package["commitment"]["experiment_uuid"],
                    resume_anchor_url="https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-104",
                    comment_fetcher=self.comment_fetcher,
                    comment_lister=self.comment_lister)
        self.assertEqual(self.calls, 1)

    def test_resume_still_rejects_unrecognized_run_files(self):
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            patched["_supervise_named"].side_effect = self.fake_supervisor
            first = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)
        self.comments.update(fake_remote_comments(
            self.package, audit_body=first["github_anchor_body"]))
        (self.run_dir / "unexpected-output.bin").write_bytes(b"not watchdog output\n")
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            with self.assertRaisesRegex(ExecutionError, "unrecognized files"):
                engine.launch_researcher_authorized(
                    self.package_path, self.run_dir,
                    "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                    self.package["commitment"]["experiment_uuid"],
                    resume_anchor_url="https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-104",
                    comment_fetcher=self.comment_fetcher,
                    comment_lister=self.comment_lister)
        self.assertEqual(self.calls, 1)

    def test_resume_rejects_modified_watchdog_stdout(self):
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            patched["_supervise_named"].side_effect = self.fake_supervisor
            first = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)
        self.comments.update(fake_remote_comments(
            self.package, audit_body=first["github_anchor_body"]))
        with (self.run_dir / "runner.stdout.01.log").open("ab") as output:
            output.write(b"tampered\n")
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            with self.assertRaisesRegex(ExecutionError, "stdout hash differs"):
                engine.launch_researcher_authorized(
                    self.package_path, self.run_dir,
                    "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                    self.package["commitment"]["experiment_uuid"],
                    resume_anchor_url="https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-104",
                    comment_fetcher=self.comment_fetcher,
                    comment_lister=self.comment_lister)
        self.assertEqual(self.calls, 1)

    def test_truncated_watchdog_hash_chain_blocks_resume(self):
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            patched["_supervise_named"].side_effect = self.fake_supervisor
            first = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)
        log_path = self.run_dir / "watchdog.jsonl"
        data = log_path.read_bytes()
        log_path.write_bytes(data[:-1])
        self.comments.update(fake_remote_comments(self.package,
                                                  audit_body=first["github_anchor_body"]))
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            with self.assertRaises((ExecutionError, WatchdogError)):
                engine.launch_researcher_authorized(
                    self.package_path, self.run_dir,
                    "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                    self.package["commitment"]["experiment_uuid"],
                    resume_anchor_url="https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-104",
                    comment_fetcher=self.comment_fetcher,
                    comment_lister=self.comment_lister)
        self.assertEqual(self.calls, 1)

    def test_public_audit_anchor_blocks_replay_after_local_chain_deletion(self):
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            patched["_supervise_named"].side_effect = self.fake_supervisor
            first = engine.launch_researcher_authorized(
                self.package_path, self.run_dir,
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                self.package["commitment"]["experiment_uuid"],
                comment_fetcher=self.comment_fetcher,
                comment_lister=self.comment_lister)
        anchor_url = "https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-104"
        self.comments.update(fake_remote_comments(self.package,
                                                  audit_body=first["github_anchor_body"]))
        (self.run_dir / "researcher_authorization.jsonl").unlink()
        watchdog_path = self.run_dir / "watchdog.jsonl"
        if watchdog_path.exists():
            watchdog_path.unlink()
        (self.run_dir / "runner.stdout.01.log").unlink()
        with self.launch_patches() as patched:
            patched["_researcher_context"].return_value = self.context
            patched["sample_host_memory_pressure"].return_value = {"free_percent": 35}
            with self.assertRaisesRegex(ExecutionError, "possible log loss/replay"):
                engine.launch_researcher_authorized(
                    self.package_path, self.run_dir,
                    "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                    self.package["commitment"]["experiment_uuid"],
                    resume_anchor_url=anchor_url,
                    comment_fetcher=self.comment_fetcher,
                    comment_lister=self.comment_lister)
        self.assertEqual(self.calls, 1)


class ResearcherInternalRunnerIdentityTests(unittest.TestCase):
    """Exercise the real runner identity gate, stopping before case execution."""

    class DispatchReached(Exception):
        pass

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="nc0a-internal-runner-")
        self.root = Path(self.tmp.name) / "run"
        self.root.mkdir()
        self.snapshot_path = self.root / "researcher_authorization.json"
        self.package, self.context = make_package(self.root)
        self.commitment = deepcopy(self.package["commitment"])
        self.commitment_sha = self.package["commitment_sha256"]
        self._write_snapshot(self.commitment, self.commitment_sha)
        self.role_path = self.root / "process_roles.json"
        self.token = "a" * 64
        self.max_attempts = self.commitment["resource_policy"]["limits"][
            "max_attempts_per_case"]
        self._old_registry = engine._ACTIVE_PROCESS_ROLE_REGISTRY
        self._old_environment = engine._ACTIVE_EXECUTION_ENVIRONMENT

    def tearDown(self):
        engine._ACTIVE_PROCESS_ROLE_REGISTRY = self._old_registry
        engine._ACTIVE_EXECUTION_ENVIRONMENT = self._old_environment
        self.tmp.cleanup()

    def _write_snapshot(self, commitment: dict, commitment_sha: str) -> None:
        value = {"format": PACKAGE_FORMAT, "commitment": commitment,
                 "commitment_sha256": commitment_sha}
        self.snapshot_path.write_bytes(canonical_bytes(value) + b"\n")

    def _runner_environment(self):
        return mock.patch.dict(os.environ, {
            "NC0A_WATCHDOG_LAUNCH_TOKEN": self.token,
            "NC0A_WATCHDOG_PARENT_PID": str(os.getppid()),
            "NC0A_PROCESS_ROLE_REGISTRY": str(self.role_path),
        })

    def _identity_gate_patches(self):
        return (
            mock.patch.object(engine, "_git_head", return_value=self.context["head_sha"]),
            mock.patch.object(engine, "_assert_clean_source_tree"),
            mock.patch.object(engine, "guard_watchdog_parent"),
        )

    def test_valid_commitment_enters_dispatch_without_running_science(self):
        patches = self._identity_gate_patches()
        with self._runner_environment(), patches[0], patches[1], patches[2], \
                mock.patch.object(engine, "_run_battery_core",
                                  side_effect=self.DispatchReached) as dispatch:
            with self.assertRaises(self.DispatchReached):
                engine._researcher_runner_entry(
                    str(self.root), str(self.snapshot_path), self.commitment_sha,
                    self.max_attempts)

        dispatch.assert_called_once()
        args, kwargs = dispatch.call_args
        self.assertEqual(args[0], self.root.resolve())
        self.assertEqual(
            kwargs["workers"],
            self.commitment["resource_policy"]["limits"]["max_workers"])
        self.assertEqual(kwargs["formal"], True)
        self.assertEqual(kwargs["policy_hash"], self.commitment_sha)
        self.assertEqual(kwargs["head"], self.context["head_sha"])
        self.assertTrue(self.role_path.is_file())
        self.assertFalse((self.root / "cases").exists())
        self.assertFalse((self.root / "execution.jsonl").exists())

    def test_wrong_commitment_hash_and_output_directory_are_rejected_before_dispatch(self):
        scenarios = ("wrong_commitment", "wrong_hash", "wrong_directory")
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                root = Path(self.tmp.name) / scenario
                root.mkdir()
                snapshot = root / "researcher_authorization.json"
                roles = root / "process_roles.json"
                commitment = deepcopy(self.commitment)
                digest = self.commitment_sha
                if scenario == "wrong_commitment":
                    commitment["experiment_uuid"] = str(uuid.uuid4())
                    value = {"format": PACKAGE_FORMAT, "commitment": commitment,
                             "commitment_sha256": digest}
                elif scenario == "wrong_directory":
                    commitment["resource_policy"]["output_directory"] = str(
                        (Path(self.tmp.name) / "different-run").resolve())
                    digest = commitment_sha256(commitment)
                    value = {"format": PACKAGE_FORMAT, "commitment": commitment,
                             "commitment_sha256": digest}
                else:
                    value = {"format": PACKAGE_FORMAT, "commitment": commitment,
                             "commitment_sha256": digest}
                    digest = "f" * 64
                snapshot.write_bytes(canonical_bytes(value) + b"\n")
                with mock.patch.dict(os.environ, {
                        "NC0A_WATCHDOG_LAUNCH_TOKEN": self.token,
                        "NC0A_WATCHDOG_PARENT_PID": str(os.getppid()),
                        "NC0A_PROCESS_ROLE_REGISTRY": str(roles)}), \
                        mock.patch.object(engine, "_git_head",
                                          return_value=self.context["head_sha"]), \
                        mock.patch.object(engine, "_assert_clean_source_tree"), \
                        mock.patch.object(engine, "guard_watchdog_parent"), \
                        mock.patch.object(engine, "_run_battery_core") as dispatch:
                    with self.assertRaises(engine.ExecutionError):
                        engine._researcher_runner_entry(
                            str(root), str(snapshot), digest, self.max_attempts)
                dispatch.assert_not_called()
                self.assertFalse(roles.exists())

    def test_watchdog_command_arguments_reach_internal_cli_and_stop_at_stub(self):
        command = engine._researcher_runner_command(
            self.root, self.snapshot_path, self.commitment_sha, self.max_attempts)
        self.assertEqual(command[0], sys.executable)
        self.assertEqual(command[1], str(Path(engine.__file__).resolve()))
        self.assertEqual(command[2], "--researcher-runner-internal")
        self.assertEqual(command[3:], [str(self.root), str(self.snapshot_path),
                                       self.commitment_sha, str(self.max_attempts)])

        patches = self._identity_gate_patches()
        with self._runner_environment(), patches[0], patches[1], patches[2], \
                mock.patch.object(engine, "_run_battery_core",
                                  return_value={"bounded_test_dispatch": True}) as dispatch:
            result = engine.main(command[2:])

        self.assertEqual(result, 0)
        dispatch.assert_called_once()
        self.assertFalse((self.root / "cases").exists())
        self.assertFalse((self.root / "execution.jsonl").exists())


if __name__ == "__main__":
    unittest.main()
