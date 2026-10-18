"""Bounded, nonformal Apple Silicon NC-0a resource probe.

This uses a distinct engineering seed, at most 5,000 proposals per worker in
parallel mode, or at most four 8E chains in parallel-chain mode. It never runs
the 16-case/128-chain formal battery, and its output is not NC-0a evidence.
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed
import argparse
from hashlib import sha256
import json
import multiprocessing
import os
from pathlib import Path
import platform
import random
import resource
import sys
import time

from connected_swap import ConnectedDegreeSwap
import nc0a_execution_engine as execution_engine
from nc0a_contract_runner import save_report_once, synthetic_chain
from nc0a_execution_engine import ProcessRoleRegistry
from nc0a_watchdog import guard_watchdog_parent
from synthetic_graphs import SyntheticGraph, make_synthetic_graph, synthetic_seed


PROBE_ROOT = 8062026
R11_LONG_PROBE_ROOT = 20261018
PROBE_N = 3900
PROBE_CHAIN_INDEX = 0
MAX_WORKER_PROPOSALS = 5000
MAX_CHECKPOINT_MULTIPLIER = 8


def _usage() -> dict:
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return {"cpu_seconds": usage.ru_utime + usage.ru_stime,
            "maxrss_bytes": int(usage.ru_maxrss)}  # Darwin reports bytes.


def _checkpoint_schedule(multiplier: int) -> tuple[int, ...]:
    allowed = (1, 2, 4, 8, 32)
    if multiplier not in allowed:
        raise ValueError("Unsupported probe checkpoint multiplier")
    return tuple(value for value in allowed if value <= multiplier)


def _worker(n: int, family: str, edges: tuple, index: int, attempts: int) -> dict:
    graph = ConnectedDegreeSwap(n, edges)
    seed = synthetic_seed(family, n, kind="chain",
                          chain_index=index, root=PROBE_ROOT)
    rng = random.Random(seed)
    before = _usage()
    started = time.perf_counter()
    for _ in range(attempts):
        graph.propose(rng, audit_local=True)
    after = _usage()
    return {"worker_index": index, "seed": seed, "attempts": attempts,
            "accepted": graph.accepted,
            "wall_seconds": time.perf_counter() - started,
            "cpu_seconds": after["cpu_seconds"] - before["cpu_seconds"],
            "worker_historical_maxrss_bytes": after["maxrss_bytes"]}


def parallel_probe(family: str, workers: int, attempts: int) -> dict:
    started = time.perf_counter()
    fixture = make_synthetic_graph(PROBE_N, family, root=PROBE_ROOT)
    fixture_seconds = time.perf_counter() - started
    registry = execution_engine._ACTIVE_PROCESS_ROLE_REGISTRY
    try:
        with ProcessPoolExecutor(max_workers=workers,
                                 mp_context=multiprocessing.get_context("spawn")) as pool:
            futures = []
            for index in range(workers):
                futures.append(pool.submit(_worker, fixture.n, family, fixture.edges,
                                           index, attempts))
                if registry is not None:
                    registry.sync_pool(pool)
            results = sorted((future.result() for future in as_completed(futures)),
                             key=lambda result: result["worker_index"])
    finally:
        if registry is not None:
            registry.clear_pool()
    elapsed = time.perf_counter() - started
    total = workers * attempts
    return {"mode": "parallel", "family": family, "n": PROBE_N,
            "fixture_sha256": fixture.fingerprint(), "edges": fixture.m,
            "workers": workers, "attempts_per_worker": attempts,
            "total_attempts": total,
            "fixture_generation_seconds": fixture_seconds,
            "wall_seconds_including_generation_and_pool": elapsed,
            "aggregate_proposals_per_wall_second": total / elapsed,
            "sum_worker_cpu_seconds": sum(row["cpu_seconds"] for row in results),
            "sum_worker_historical_maxrss_bytes": sum(
                row["worker_historical_maxrss_bytes"] for row in results),
            "parent_historical_maxrss_bytes": _usage()["maxrss_bytes"],
            "workers_detail": results}


def chain_probe(family: str, report_dir: Path, checkpoint_multiplier: int) -> dict:
    started = time.perf_counter()
    fixture = make_synthetic_graph(PROBE_N, family, root=PROBE_ROOT)
    fixture_seconds = time.perf_counter() - started
    attempts = checkpoint_multiplier * fixture.m
    checkpoints = _checkpoint_schedule(checkpoint_multiplier)
    chain = synthetic_chain(PROBE_N, family, PROBE_CHAIN_INDEX,
                            root=PROBE_ROOT, fixture=fixture,
                            checkpoints=checkpoints,
                            max_wall_seconds=180, max_proposals=attempts)
    compute_seconds = time.perf_counter() - started - fixture_seconds
    report_dir.mkdir(parents=True, exist_ok=True)
    report = {"status": "NONFORMAL_ENGINEERING_PROBE", "seed_root": PROBE_ROOT,
              "chain": chain}
    destination = report_dir / "chain_probe.json"
    save_started = time.perf_counter()
    digest = save_report_once(destination, report)
    save_seconds = time.perf_counter() - save_started
    if sha256(destination.read_bytes()).hexdigest() != digest:
        raise RuntimeError("Saved probe report failed SHA-256 verification")
    return {"mode": "chain", "family": family, "n": PROBE_N,
            "fixture_sha256": fixture.fingerprint(), "edges": fixture.m,
            "chain_index": PROBE_CHAIN_INDEX, "seed_root": PROBE_ROOT,
            "attempts": attempts, "checkpoint_multipliers": checkpoints,
            "accepted_at_endpoint": chain["checkpoints"][str(checkpoint_multiplier)]["accepted"],
            "fixture_generation_seconds": fixture_seconds,
            "chain_with_checkpoint_metrics_seconds": compute_seconds,
            "aggregate_proposals_per_chain_second": attempts / compute_seconds,
            "report_save_and_fsync_seconds": save_seconds,
            "report_bytes": destination.stat().st_size,
            "report_sha256": digest,
            "process_historical_maxrss_bytes": _usage()["maxrss_bytes"]}


def _parallel_chain_worker(fixture: SyntheticGraph, index: int,
                           checkpoint_multiplier: int, seed_root: int,
                           max_wall_seconds: int) -> dict:
    before = _usage()
    started = time.perf_counter()
    checkpoints = _checkpoint_schedule(checkpoint_multiplier)
    chain = synthetic_chain(
        fixture.n, fixture.family, index, root=seed_root,
        fixture=fixture, checkpoints=checkpoints,
        max_wall_seconds=max_wall_seconds,
        max_proposals=checkpoint_multiplier * fixture.m)
    after = _usage()
    stable = {key: value for key, value in chain.items()
              if key != "elapsed_wall_seconds"}
    stable_bytes = json.dumps(stable, sort_keys=True, separators=(",", ":"),
                              allow_nan=False).encode("utf-8")
    return {"chain": chain, "wall_seconds": time.perf_counter() - started,
            "cpu_seconds": after["cpu_seconds"] - before["cpu_seconds"],
            "worker_historical_maxrss_bytes": after["maxrss_bytes"],
            "stable_result_sha256": sha256(stable_bytes).hexdigest()}


def parallel_chain_probe(family: str, workers: int, report_dir: Path,
                         checkpoint_multiplier: int, *,
                         seed_root: int = PROBE_ROOT,
                         max_wall_seconds: int = 360) -> dict:
    if checkpoint_multiplier == 32:
        if (seed_root != R11_LONG_PROBE_ROOT or family != "factor-mst" or
                workers != 4 or max_wall_seconds != 1200):
            raise ValueError("32E is reserved for the fixed four-worker R11 factor-MST probe")
    elif (seed_root != PROBE_ROOT or checkpoint_multiplier not in (1, 2, 4, 8) or
          max_wall_seconds != 360):
        raise ValueError("Non-long probes remain on the bounded 1/2/4/8E profile")
    started = time.perf_counter()
    fixture = make_synthetic_graph(PROBE_N, family, root=seed_root)
    fixture_seconds = time.perf_counter() - started
    checkpoints = _checkpoint_schedule(checkpoint_multiplier)
    report_dir.mkdir(parents=True, exist_ok=True)
    registry = execution_engine._ACTIVE_PROCESS_ROLE_REGISTRY
    try:
        with ProcessPoolExecutor(max_workers=workers,
                                 mp_context=multiprocessing.get_context("spawn")) as pool:
            futures = {}
            for index in range(workers):
                futures[pool.submit(_parallel_chain_worker, fixture, index,
                                    checkpoint_multiplier, seed_root,
                                    max_wall_seconds)] = index
                if registry is not None:
                    registry.sync_pool(pool)
            rows = []
            for future in as_completed(futures):
                index = futures[future]
                result = future.result()
                report_path = report_dir / f"chain-{index:02d}.json"
                report_sha = save_report_once(report_path, result["chain"])
                if sha256(report_path.read_bytes()).hexdigest() != report_sha:
                    raise RuntimeError("Saved parallel chain failed SHA-256 verification")
                rows.append({"chain_index": index,
                             "seed": result["chain"]["seed"],
                             "attempts": checkpoint_multiplier * fixture.m,
                             "accepted": result["chain"]["checkpoints"][
                                 str(checkpoint_multiplier)]["accepted"],
                             "accepted_fraction": result["chain"]["checkpoints"][
                                 str(checkpoint_multiplier)]["accepted"] /
                                 (checkpoint_multiplier * fixture.m),
                             "wall_seconds": result["wall_seconds"],
                             "cpu_seconds": result["cpu_seconds"],
                             "worker_historical_maxrss_bytes": result[
                                 "worker_historical_maxrss_bytes"],
                             "report_bytes": report_path.stat().st_size,
                             "report_sha256": report_sha,
                             "stable_result_sha256": result["stable_result_sha256"],
                             "checkpoint_metrics": {
                                 key: result["chain"]["checkpoints"][key]["metrics"]
                                 for key in map(str, checkpoints)}})
    finally:
        if registry is not None:
            registry.clear_pool()
    elapsed = time.perf_counter() - started
    rows.sort(key=lambda row: row["chain_index"])
    total = workers * checkpoint_multiplier * fixture.m
    return {"mode": "parallel-chain", "family": family, "n": fixture.n,
            "fixture_sha256": fixture.fingerprint(), "edges": fixture.m,
            "workers": workers, "checkpoint_multipliers": checkpoints,
            "seed_root": seed_root, "total_attempts": total,
            "fixture_generation_seconds": fixture_seconds,
            "wall_seconds_including_generation_pool_and_result_writes": elapsed,
            "aggregate_proposals_per_wall_second": total / elapsed,
            "sum_worker_cpu_seconds": sum(row["cpu_seconds"] for row in rows),
            "sum_worker_historical_maxrss_bytes": sum(
                row["worker_historical_maxrss_bytes"] for row in rows),
            "chains": rows}


def configure_watchdog_process_identity() -> None:
    token = os.environ.get("NC0A_WATCHDOG_LAUNCH_TOKEN", "")
    parent = os.environ.get("NC0A_WATCHDOG_PARENT_PID", "")
    registry_path = Path(os.environ.get("NC0A_PROCESS_ROLE_REGISTRY", ""))
    if token or parent or registry_path != Path("."):
        if parent != str(os.getppid()) or not registry_path.is_absolute() or \
           registry_path.parent.resolve() != Path.cwd().resolve():
            raise RuntimeError("Probe process-role registry is not bound to its watchdog run")
        execution_engine._ACTIVE_PROCESS_ROLE_REGISTRY = ProcessRoleRegistry(
            registry_path, token, os.getpid())
        guard_watchdog_parent(int(parent))


def main() -> int:
    configure_watchdog_process_identity()
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("parallel", "chain", "parallel-chain", "long-chain"))
    parser.add_argument("--family", choices=("ba-like", "factor-mst"))
    parser.add_argument("--workers", type=int, choices=(1, 2, 4, 8))
    parser.add_argument("--attempts-per-worker", type=int, default=MAX_WORKER_PROPOSALS)
    parser.add_argument("--checkpoint-multiplier", type=int, choices=(1, 2, 4, 8), default=4)
    parser.add_argument("--report-dir", type=Path)
    args = parser.parse_args()
    if sys.platform != "darwin" or platform.machine() != "arm64":
        parser.error("This bounded probe is reviewed only for macOS/Apple Silicon")
    if args.mode == "long-chain":
        if (args.family != "factor-mst" or args.workers != 4 or
                args.report_dir is None or args.attempts_per_worker != MAX_WORKER_PROPOSALS or
                args.checkpoint_multiplier != 4):
            parser.error("long-chain is fixed to one N=3900 factor-MST, four chains, fixed seed, and 32E")
        result = parallel_chain_probe(
            "factor-mst", 4, args.report_dir, 32,
            seed_root=R11_LONG_PROBE_ROOT, max_wall_seconds=1200)
    elif args.mode == "parallel":
        if args.family is None:
            parser.error("parallel mode requires --family")
        if args.workers is None or args.report_dir is not None:
            parser.error("Parallel probe needs --workers and no --report-dir")
        if not 1 <= args.attempts_per_worker <= MAX_WORKER_PROPOSALS:
            parser.error("Proposal count exceeds the nonformal cap")
        result = parallel_probe(args.family, args.workers, args.attempts_per_worker)
    elif args.mode == "chain":
        if args.family is None:
            parser.error("chain mode requires --family")
        if args.workers is not None or args.report_dir is None:
            parser.error("Chain probe needs --report-dir and no --workers")
        result = chain_probe(args.family, args.report_dir, args.checkpoint_multiplier)
    else:
        if args.family is None:
            parser.error("parallel-chain mode requires --family")
        if args.workers is None or not 1 <= args.workers <= 4 or args.report_dir is None:
            parser.error("Parallel-chain probe needs 1..4 workers and a report directory")
        result = parallel_chain_probe(args.family, args.workers, args.report_dir,
                                      args.checkpoint_multiplier)
    result.update({"status": "NONFORMAL_ENGINEERING_PROBE",
                   "host": platform.platform(), "python": sys.version.split()[0],
                   "pid": os.getpid()})
    result.setdefault("seed_root", PROBE_ROOT)
    print(json.dumps(result, sort_keys=True, allow_nan=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
