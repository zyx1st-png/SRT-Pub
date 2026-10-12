"""NC-0a synthetic-only CONTRACT implementation candidate, not execution authority.

This module never reads biological files and has no automatic full-battery CLI.
The resource/NC-0a approval gate is external and remains NO-GO until a
separately signed-off, provenance-backed comparable PS-A time ledger exists.
Do not report a 48-comparison PASS as evidence of stationary mixing.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
import math
import platform
import random
import statistics
import time

from connected_swap import ConnectedDegreeSwap
from synthetic_graphs import FAMILIES, make_synthetic_graph, metrics, synthetic_seed
from test_anomaly_screen import PAIRED_T_CRITICAL, abs_paired_t


FORMAL_N = (100, 340, 1150, 3900)
CHECKPOINTS = (1, 2, 4, 8, 32)
CHAIN_COUNT = 8
ORACLE_PROPOSALS = 1000
METRICS = ("triangles", "assortativity", "edge_overlap")
SCREEN_FAMILY = 48


class NC0aContractError(RuntimeError):
    """Fail closed: never substitute, silently retry, or drop an invalid cell."""


def _assert_budget(deadline: float) -> None:
    if time.monotonic() > deadline:
        raise NC0aContractError("Absolute case wall-clock cap exceeded")


def _snapshot(g: ConnectedDegreeSwap, initial: tuple[tuple[int, int], ...],
              seed: int, audited_accepts: int) -> dict:
    g.assert_invariants()  # full-graph connectivity ONLY at checkpoints
    values = metrics(g.n, g.edges, initial)
    if not all(math.isfinite(v) for v in values.values()):
        raise NC0aContractError("Invalid graph metric (including assortativity)")
    if audited_accepts != g.accepted:
        raise NC0aContractError("Per-accepted local audit count mismatch")
    return {
        "attempts": g.attempts,
        "accepted": g.accepted,
        "rejected_overlap": g.rejected_overlap,
        "rejected_duplicate": g.rejected_duplicate,
        "rejected_disconnect": g.rejected_disconnect,
        "acceptance_rate": g.accepted / g.attempts,
        "audited_accepted_swaps": audited_accepts,
        "graph_sha256": g.fingerprint(),
        "seed": seed,
        "metrics": values,
    }


def synthetic_chain(n: int, family: str, chain_index: int, *,
                    root: int = 20261009,
                    checkpoints: tuple[int, ...] = CHECKPOINTS,
                    max_wall_seconds: float,
                    max_proposals: int) -> dict:
    """Deterministic checkpointed chain; a caller must supply absolute limits.

    Tiny nonformal unit tests use different checkpoints and a small N.
    The formal configuration is exactly 8 chains x 32E with fixed SHA seeds.
    Every accepted swap gets a four-endpoint local audit without a whole-graph
    BFS, and full graph connectivity is verified at every checkpoint.
    """
    if not (math.isfinite(max_wall_seconds) and max_wall_seconds > 0):
        raise ValueError("Positive finite wall-clock case limit is required")
    if max_proposals <= 0:
        raise ValueError("Positive absolute proposal limit required")
    if sorted(set(checkpoints)) != list(checkpoints) or not checkpoints:
        raise ValueError("Invalid checkpoint multipliers")
    start = time.monotonic()
    deadline = start + max_wall_seconds
    fixture = make_synthetic_graph(n, family, root=root)
    g = ConnectedDegreeSwap(n, fixture.edges)
    steps = tuple(c * g.m for c in checkpoints)
    if steps[-1] > max_proposals:
        raise NC0aContractError("Proposal budget below locked checkpoint count")
    seed = synthetic_seed(family, n, kind="chain", chain_index=chain_index,
                          root=root)
    rng = random.Random(seed)
    record = {}
    locally_audited = 0
    targets = set(steps)
    for step in range(1, steps[-1] + 1):
        if step % 1000 == 0:
            _assert_budget(deadline)
        accepted = g.propose(rng, audit_local=True)
        if accepted:
            locally_audited += 1
        if step in targets:
            _assert_budget(deadline)
            record[str(step // g.m)] = _snapshot(
                g, fixture.edges, seed, locally_audited)
    _assert_budget(deadline)
    if g.attempts != g.accepted + g.rejected_overlap + g.rejected_duplicate + g.rejected_disconnect:
        raise NC0aContractError("Exact proposal/rejection conservation failed")
    return {
        "family": family,
        "n": n,
        "chain_index": chain_index,
        "seed": seed,
        "fixture_seed": fixture.seed,
        "fixture_sha256": fixture.fingerprint(),
        "edge_count": g.m,
        "checkpoints": record,
        "elapsed_wall_seconds": time.monotonic() - start,
        "audit": {"per_accepted_local": locally_audited,
                  "full_connectivity_checkpoints": len(steps)},
        "mixing_status": "MIXING-UNRESOLVED",
    }


def oracle_trace(n: int, family: str, *, root: int = 20261009,
                 attempts: int = ORACLE_PROPOSALS,
                 max_wall_seconds: float,
                 max_proposals: int) -> dict:
    """Independent local-BFS-vs-full-connectivity oracle stream."""
    if attempts < 1 or attempts > max_proposals or max_wall_seconds <= 0:
        raise ValueError("Oracle resource cap invalid")
    start = time.monotonic()
    deadline = start + max_wall_seconds
    fixture = make_synthetic_graph(n, family, root=root)
    seed = synthetic_seed(family, n, kind="bfs-identity", root=root)
    graph = ConnectedDegreeSwap(n, fixture.edges)
    rng = random.Random(seed)
    accepted_audits = 0
    for i in range(attempts):
        if i % 100 == 0:
            _assert_budget(deadline)
        changed = graph.propose(rng, oracle=True, audit_local=True)
        accepted_audits += bool(changed)
    graph.assert_invariants()
    _assert_budget(deadline)
    if graph.attempts != attempts or graph.accepted != accepted_audits:
        raise NC0aContractError("Oracle integrity / proposal accounting failure")
    return {
        "family": family, "n": n, "fixture_sha256": fixture.fingerprint(),
        "seed": seed, "attempts": graph.attempts, "accepted": graph.accepted,
        "rejections": graph.stats(seed).rejection_count,
        "accepted_local_audits": accepted_audits,
        "oracle_mismatches": 0,  # Any mismatch raises in propose(oracle=True).
        "elapsed_wall_seconds": time.monotonic() - start,
    }


def screen_case(chains: list[dict], *,
                require_full_contract: bool = True) -> dict:
    """Never replace non-rejection with 'mixed' or equilibrium calibration."""
    if len(chains) != CHAIN_COUNT:
        raise NC0aContractError("Case requires exactly eight independent chains")
    ids = {c["chain_index"] for c in chains}
    if ids != set(range(CHAIN_COUNT)):
        raise NC0aContractError("Missing/duplicate chain IDs")
    n, family = chains[0]["n"], chains[0]["family"]
    if any(c["n"] != n or c["family"] != family for c in chains):
        raise NC0aContractError("Mixed case identities")
    if require_full_contract and (
        n not in FORMAL_N or family not in FAMILIES
    ):
        raise NC0aContractError("Not a formal preregistered case")
    if any(c["checkpoints"].get("4") is None or
           c["checkpoints"].get("32") is None for c in chains):
        raise NC0aContractError("Missing paired 4E/32E snapshots")
    output = {}
    for metric in METRICS:
        diffs = [
            c["checkpoints"]["4"]["metrics"][metric] -
            c["checkpoints"]["32"]["metrics"][metric] for c in chains
        ]
        try:
            t_value = abs_paired_t(diffs)
        except (ValueError, statistics.StatisticsError) as exc:
            raise NC0aContractError(str(exc)) from exc
        sd = statistics.stdev(diffs)
        from scipy.stats import t as student_t  # original pipeline already uses SciPy
        two_sided_p = (0.0 if t_value == math.inf else
                       float(2 * student_t.sf(t_value, df=7)))
        adjusted_p = min(1.0, SCREEN_FAMILY * two_sided_p)
        values_4 = [c["checkpoints"]["4"]["metrics"][metric] for c in chains]
        values_32 = [c["checkpoints"]["32"]["metrics"][metric] for c in chains]
        if not math.isfinite(t_value) and t_value != math.inf:
            raise NC0aContractError("Non-finite unexpected t statistic")
        passed = t_value <= PAIRED_T_CRITICAL
        output[metric] = {
            "values_at_4E": values_4,
            "values_at_32E": values_32,
            "mean_at_4E": statistics.mean(values_4),
            "mean_at_32E": statistics.mean(values_32),
            "paired_differences": diffs,
            "mean_difference": statistics.mean(diffs),
            "sd_difference": sd,
            "critical_absolute_drift": PAIRED_T_CRITICAL * sd / math.sqrt(8),
            "abs_t": t_value if math.isfinite(t_value) else "infinity",
            "two_sided_p": two_sided_p,
            "bonferroni_adjusted_p": adjusted_p,
            "passed_anomaly_screen": passed,
        }
    return {
        "n": n, "family": family, "metrics": output,
        "anomaly_screen_pass": all(v["passed_anomaly_screen"] for v in output.values()),
        "mixing_status": "MIXING-UNRESOLVED",
        "note": "This is only a low-power 4E-to-32E drift screen; not a mixing certificate.",
    }


def validate_full_battery(case_reports: list[dict]) -> dict:
    """Enforce 16 unique case screens, 48 metrics, without selective omission."""
    wanted = {(n, f) for n in FORMAL_N for f in FAMILIES}
    actual = [(r["n"], r["family"]) for r in case_reports]
    if len(actual) != len(wanted) or set(actual) != wanted:
        raise NC0aContractError("Incomplete or duplicate full battery")
    if any(set(r["metrics"]) != set(METRICS) for r in case_reports):
        raise NC0aContractError("Missing one of the 48 case/metric screens")
    return {
        "cases": 16, "comparisons": 48,
        "drift_screen_pass": all(r["anomaly_screen_pass"] for r in case_reports),
        "mixing_status": "MIXING-UNRESOLVED",
        "execution_authorized": False,  # Separate NC-0a resource / approval gate.
    }


def contract_seed_manifest(root: int = 20261009) -> dict:
    """Pure planning artifact. Does NOT construct graphs or perform swaps."""
    seeds = {}
    for n in FORMAL_N:
        for family in FAMILIES:
            seeds[f"{family}:{n}"] = {
                "fixture_seed": synthetic_seed(family, n, root=root),
                "chain_seeds": [synthetic_seed(family, n, kind="chain",
                                               chain_index=i, root=root)
                                for i in range(CHAIN_COUNT)],
                "bfs_seed": synthetic_seed(family, n, kind="bfs-identity",
                                            root=root),
            }
    return {
        "status": "REVIEW_ONLY_NOT_APPROVED",
        "synthetic_root": root,
        "python": platform.python_version(),
        "cases": seeds, "total_chains": 128, "oracle_streams": 16,
        "comparison_count": SCREEN_FAMILY,
        "no_biological_data": True,
    }


if __name__ == "__main__":
    # Running the module is harmless and cannot accidentally launch formal
    # chains. Actual NC-0a needs separately reviewed budget/provenance approval.
    print(json.dumps(contract_seed_manifest(), sort_keys=True, indent=2))
