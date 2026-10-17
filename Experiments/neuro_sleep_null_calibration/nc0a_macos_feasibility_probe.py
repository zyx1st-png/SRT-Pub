"""Bounded, nonformal Apple Silicon NC-0a resource probe.

This uses a distinct engineering seed, at most 5,000 proposals per worker in
parallel mode, or one chain ending at 4E in chain mode. It never runs the
16-case/128-chain formal battery, and its output is not NC-0a evidence.
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
from nc0a_contract_runner import save_report_once, synthetic_chain
from synthetic_graphs import make_synthetic_graph, synthetic_seed


PROBE_ROOT = 8062026
PROBE_N = 3900
PROBE_CHAIN_INDEX = 0
MAX_WORKER_PROPOSALS = 5000
MAX_CHECKPOINT_MULTIPLIER = 4


def _usage() -> dict:
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return {"cpu_seconds": usage.ru_utime + usage.ru_stime,
            "maxrss_bytes": int(usage.ru_maxrss)}  # Darwin reports bytes.


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
    with ProcessPoolExecutor(max_workers=workers,
                             mp_context=multiprocessing.get_context("spawn")) as pool:
        futures = [pool.submit(_worker, fixture.n, family, fixture.edges, index, attempts)
                   for index in range(workers)]
        results = sorted((future.result() for future in as_completed(futures)),
                         key=lambda result: result["worker_index"])
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
    checkpoints = tuple(value for value in (1, 2, MAX_CHECKPOINT_MULTIPLIER)
                        if value <= checkpoint_multiplier)
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("parallel", "chain"))
    parser.add_argument("--family", choices=("ba-like", "factor-mst"), required=True)
    parser.add_argument("--workers", type=int, choices=(1, 2, 4, 8))
    parser.add_argument("--attempts-per-worker", type=int, default=MAX_WORKER_PROPOSALS)
    parser.add_argument("--checkpoint-multiplier", type=int, choices=(1, 2, 4), default=4)
    parser.add_argument("--report-dir", type=Path)
    args = parser.parse_args()
    if sys.platform != "darwin" or platform.machine() != "arm64":
        parser.error("This bounded probe is reviewed only for macOS/Apple Silicon")
    if args.mode == "parallel":
        if args.workers is None or args.report_dir is not None:
            parser.error("Parallel probe needs --workers and no --report-dir")
        if not 1 <= args.attempts_per_worker <= MAX_WORKER_PROPOSALS:
            parser.error("Proposal count exceeds the nonformal cap")
        result = parallel_probe(args.family, args.workers, args.attempts_per_worker)
    else:
        if args.workers is not None or args.report_dir is None:
            parser.error("Chain probe needs --report-dir and no --workers")
        result = chain_probe(args.family, args.report_dir, args.checkpoint_multiplier)
    result.update({"status": "NONFORMAL_ENGINEERING_PROBE", "seed_root": PROBE_ROOT,
                   "host": platform.platform(), "python": sys.version.split()[0],
                   "pid": os.getpid()})
    print(json.dumps(result, sort_keys=True, allow_nan=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
