"""Micro-only NC-0a contract tests: do NOT run full 16x8x32E battery."""
import random
import unittest

from connected_swap import ConnectedDegreeSwap
from nc0a_contract_runner import (
    NC0aContractError, contract_seed_manifest, oracle_trace,
    synthetic_chain, screen_case, validate_full_battery,
)
from synthetic_graphs import make_synthetic_graph


class ContractTests(unittest.TestCase):
    def test_local_audit_does_not_change_rng_or_graph(self):
        fixture = make_synthetic_graph(40, "er-like")
        a = ConnectedDegreeSwap(40, fixture.edges)
        b = ConnectedDegreeSwap(40, fixture.edges)
        r1 = random.Random(98765)
        r2 = random.Random(98765)
        audits = 0
        for _ in range(600):
            audits += int(a.propose(r1, audit_local=True))
            b.propose(r2)
        self.assertEqual(a.fingerprint(), b.fingerprint())
        self.assertEqual(a.accepted, b.accepted)
        self.assertEqual(a.accepted, audits)
        a.assert_invariants()
        b.assert_invariants()

    def test_micro_chain_has_metrics_every_checkpoint_and_local_audit(self):
        result = synthetic_chain(
            40, "er-like", 0, checkpoints=(1, 2),
            max_wall_seconds=20.0, max_proposals=640)
        self.assertEqual(set(result["checkpoints"]), {"1", "2"})
        self.assertEqual(result["mixing_status"], "MIXING-UNRESOLVED")
        self.assertEqual(result["audit"]["full_connectivity_checkpoints"], 2)
        final = result["checkpoints"]["2"]
        self.assertEqual(final["attempts"], 640)
        self.assertEqual(final["accepted"], final["audited_accepted_swaps"])
        self.assertEqual(final["attempts"], final["accepted"] +
                         final["rejected_overlap"] +
                         final["rejected_duplicate"] +
                         final["rejected_disconnect"])
        self.assertEqual(set(final["metrics"]),
                         {"triangles", "assortativity", "edge_overlap"})

    def test_oracle_is_an_independent_stream(self):
        fixture = make_synthetic_graph(40, "er-like")
        trace = oracle_trace(40, "er-like", attempts=40,
                             max_wall_seconds=20.0, max_proposals=100)
        self.assertEqual(trace["fixture_sha256"], fixture.fingerprint())
        self.assertEqual(trace["attempts"], 40)
        self.assertEqual(trace["oracle_mismatches"], 0)
        self.assertEqual(trace["accepted_local_audits"], trace["accepted"])

    def test_budget_fails_closed(self):
        with self.assertRaises(NC0aContractError):
            synthetic_chain(40, "er-like", 0, checkpoints=(1, 2),
                            max_wall_seconds=20.0, max_proposals=639)

    def test_manifest_has_16_distinct_fixture_and_128_chain_seeds(self):
        manifest = contract_seed_manifest()
        self.assertEqual(len(manifest["cases"]), 16)
        self.assertEqual(manifest["total_chains"], 128)
        self.assertEqual(manifest["oracle_streams"], 16)
        seeds = [s for cell in manifest["cases"].values()
                 for s in [cell["fixture_seed"], cell["bfs_seed"],
                           *cell["chain_seeds"]]]
        self.assertEqual(len(seeds), len(set(seeds)))

    def test_stagnant_data_can_pass_but_never_certifies_mixing(self):
        # Analytic stand-in for R5's three-state slow chain: 8 chains exhibit
        # NO drift in all three metrics. This is not a convergence certificate.
        baseline = {"triangles": 0.0,
                    "assortativity": 0.3, "edge_overlap": 1.0}
        chains = []
        for i in range(8):
            chains.append({
                "n": 340, "family": "er-like", "chain_index": i,
                "checkpoints": {
                    "4": {"metrics": baseline},
                    "32": {"metrics": baseline},
                }
            })
        result = screen_case(chains, require_full_contract=False)
        self.assertTrue(result["anomaly_screen_pass"])
        self.assertEqual(result["mixing_status"], "MIXING-UNRESOLVED")
        self.assertFalse(result["note"].startswith("stationary"))

    def test_atomic_report_does_not_overwrite(self):
        from tempfile import TemporaryDirectory
        from pathlib import Path
        from hashlib import sha256
        from nc0a_contract_runner import save_report_once
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "micro.json"
            checksum = save_report_once(path, {"synthetic": True})
            self.assertEqual(sha256(path.read_bytes()).hexdigest(), checksum)
            self.assertTrue(Path(str(path) + ".sha256").exists())
            with self.assertRaises(NC0aContractError):
                save_report_once(path, {"synthetic": False})

    def test_formal_case_seed_and_audits_cannot_be_bypassed(self):
        # Full-size cases are NEVER run here: synthetic stand-in metadata
        # intentionally lacks valid seed/audit/fixture provenance and fails.
        payloads = [{"n": 340, "family": "er-like", "chain_index": i,
                     "checkpoints": {"4": {"metrics": {}},
                                     "32": {"metrics": {}}}}
                    for i in range(8)]
        with self.assertRaises(NC0aContractError):
            screen_case(payloads, require_full_contract=True)

    def test_r5_three_state_exact_slow_chain_pass_does_not_certify_mixing(self):
        # R5 independent review's *non-formal* counterexample: 8 universal
        # vertices force almost every edge; among four other special vertices
        # only three matching realizations are possible. These are not among
        # the 16 prespecified NC-0a fixtures. No biological data are used.
        import math
        from synthetic_graphs import metrics
        n = 340
        edges = sorted(
            {(u, v) for u in range(8) for v in range(u + 1, n)}
            | {(8, 9), (10, 11)}
        )
        e = len(edges)
        self.assertEqual(e, 2686)
        p_leave = 1 / math.comb(e, 2)
        tv_4 = (2 / 3) * (1 - 1.5 * p_leave) ** (4 * e)
        tv_32 = (2 / 3) * (1 - 1.5 * p_leave) ** (32 * e)
        self.assertGreater(tv_4, 0.66)
        self.assertGreater(tv_32, 0.64)
        results, total_accepted = [], 0
        for index in range(8):
            g = ConnectedDegreeSwap(n, edges)
            rng = random.Random(2026101200 + index)
            checkpoints = {}
            for step in range(1, 32 * e + 1):
                g.propose(rng, audit_local=True)
                if step in (4 * e, 32 * e):
                    g.assert_invariants()
                    checkpoints[str(step // e)] = {
                        "metrics": metrics(n, g.edges, edges)}
            total_accepted += g.accepted
            results.append({
                "n": n, "family": "er-like",
                "chain_index": index, "checkpoints": checkpoints,
            })
        self.assertEqual(total_accepted, 1)
        screened = screen_case(results, require_full_contract=False)
        self.assertTrue(screened["anomaly_screen_pass"])
        self.assertEqual(screened["mixing_status"], "MIXING-UNRESOLVED")
        self.assertTrue(all(
            not data["passed_anomaly_screen"] is False
            for data in screened["metrics"].values()
        ))

    def test_even_all_screen_passes_do_not_waive_oracle(self):
        from nc0a_contract_runner import FORMAL_N, METRICS
        from synthetic_graphs import FAMILIES
        screens = [{
            "n": n, "family": family,
            "metrics": {m: {"passed_anomaly_screen": True} for m in METRICS},
            "anomaly_screen_pass": True,
        } for n in FORMAL_N for family in FAMILIES]
        with self.assertRaises(NC0aContractError):
            validate_full_battery(screens, oracle_reports=None)

    def test_missing_cases_cannot_be_upgraded_to_battery_pass(self):
        with self.assertRaises(NC0aContractError):
            validate_full_battery([])


if __name__ == "__main__":
    unittest.main()
