"""Bounded synthetic-only timing probes; never runs NC-0a, G0 or T1.

Default probes build the 16 synthetic fixture shapes, then measure at most
2,000 connected-swap proposals per worker on three representative sizes with
1/4/8 workers. Optional --louvain probes run only five synthetic Louvain
restarts per size and require python-louvain==0.16. Results are exploratory
engineering estimates, not formal NC-0a validation or approved budgets.
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
import argparse
import importlib.metadata
import json
import multiprocessing
import os
import platform
import random
import resource
import subprocess
import sys
import time

from connected_swap import ConnectedDegreeSwap
from nc0a_contract_runner import FORMAL_N
from synthetic_graphs import FAMILIES, make_synthetic_graph, synthetic_seed


BENCH_ROOT = 8062026
BENCH_ATTEMPTS_MAX = 5000
_WORKER_CASE = None


def _worker_init(n: int, family: str, edges: tuple) -> None:
    global _WORKER_CASE
    _WORKER_CASE = n, family, edges


def _swap_probe(index: int, attempts: int, root: int) -> dict:
    if _WORKER_CASE is None:
        raise RuntimeError("microbenchmark worker was not initialized")
    n, family, edges = _WORKER_CASE
    graph = ConnectedDegreeSwap(n, edges)
    seed = synthetic_seed(family, n, kind="chain", chain_index=index, root=root)
    rng = random.Random(seed)
    cpu0 = resource.getrusage(resource.RUSAGE_SELF)
    start = time.perf_counter()
    for _ in range(attempts):
        graph.propose(rng, audit_local=True)
    elapsed = time.perf_counter() - start
    cpu1 = resource.getrusage(resource.RUSAGE_SELF)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    return {"worker": index, "attempts": attempts,
            "accepted": graph.accepted,
            "wall_seconds": elapsed,
            "cpu_seconds": ((cpu1.ru_utime + cpu1.ru_stime) -
                            (cpu0.ru_utime + cpu0.ru_stime)),
            "peak_rss_bytes": int(rss)}


def _sample_aggregate_rss(pids: list[int]) -> int:
    pids = sorted(set(pids))
    if not pids:
        return 0
    result = subprocess.run(["/bin/ps", "-o", "rss=", "-p", ",".join(map(str, pids))],
                            capture_output=True, text=True, timeout=5)
    if result.returncode:
        return 0
    values = [int(row.strip()) for row in result.stdout.splitlines() if row.strip().isdigit()]
    return sum(values) * 1024


def run_parallel_probe(fixture, workers: int, attempts: int) -> dict:
    context = multiprocessing.get_context("spawn")
    start = time.perf_counter()
    peak_rss = 0
    with ProcessPoolExecutor(
        max_workers=workers, mp_context=context, initializer=_worker_init,
        initargs=(fixture.n, fixture.family, fixture.edges),
    ) as pool:
        futures = [pool.submit(_swap_probe, i, attempts, BENCH_ROOT)
                   for i in range(workers)]
        pending = set(futures)
        results = []
        while pending:
            pids = [os.getpid(), *getattr(pool, "_processes", {}).keys()]
            peak_rss = max(peak_rss, _sample_aggregate_rss(pids))
            done, pending = wait(pending, timeout=0.05, return_when=FIRST_COMPLETED)
            for future in done:
                results.append(future.result())
    elapsed = time.perf_counter() - start
    total_attempts = sum(row["attempts"] for row in results)
    total_cpu = sum(row["cpu_seconds"] for row in results)
    return {
        "workers": workers, "attempts_per_worker": attempts,
        "total_attempts": total_attempts,
        "wall_seconds_including_pool_start": elapsed,
        "aggregate_proposals_per_second": total_attempts / elapsed,
        "worker_cpu_seconds": total_cpu,
        "peak_sampled_aggregate_rss_bytes": peak_rss,
        "worker_results": sorted(results, key=lambda row: row["worker"]),
    }


def graph_generation_probes() -> list[dict]:
    output = []
    for n in FORMAL_N:
        for family in FAMILIES:
            start = time.perf_counter()
            fixture = make_synthetic_graph(n, family, root=BENCH_ROOT)
            elapsed = time.perf_counter() - start
            output.append({"n": n, "family": family,
                           "edges": fixture.m,
                           "fixture_sha256": fixture.fingerprint(),
                           "wall_seconds": elapsed})
            del fixture
    return output


def louvain_probes(enabled: bool) -> dict:
    if not enabled:
        return {"status": "NOT_REQUESTED"}
    try:
        import networkx as nx
        from community import community_louvain
        version = importlib.metadata.version("python-louvain")
    except Exception as exc:
        return {"status": "NOT_INSTALLED", "reason": f"{type(exc).__name__}: {exc}"}
    results = []
    for n in (1150, 3900):
        for family in ("factor-mst", "ba-like"):
            fixture = make_synthetic_graph(n, family, root=BENCH_ROOT)
            start_graph = time.perf_counter()
            graph = nx.Graph()
            graph.add_nodes_from(range(n))
            graph.add_weighted_edges_from((u, v, 1.0) for u, v in fixture.edges)
            conversion_seconds = time.perf_counter() - start_graph
            trial_seconds = []
            for repeat in range(5):
                began = time.perf_counter()
                seed = (synthetic_seed(family, n, kind="chain",
                                       chain_index=repeat, root=BENCH_ROOT) % (2**32))
                partition = community_louvain.best_partition(
                    graph, weight="weight", resolution=1.0, random_state=seed)
                q = float(community_louvain.modularity(partition, graph, weight="weight"))
                trial_seconds.append(time.perf_counter() - began)
                if not (q == q and abs(q) < float("inf")):
                    raise RuntimeError("Synthetic Louvain returned nonfinite modularity")
            results.append({"n": n, "family": family,
                            "edges": fixture.m,
                            "conversion_seconds": conversion_seconds,
                            "five_restart_seconds": trial_seconds,
                            "median_restart_seconds": sorted(trial_seconds)[2],
                            "max_restart_seconds": max(trial_seconds),
                            "fixture_sha256": fixture.fingerprint()})
    return {"status": "MEASURED_SYNTHETIC_ONLY", "python_louvain_version": version,
            "restarts_per_case": 5, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempts-per-worker", type=int, default=2000)
    parser.add_argument("--workers", type=int, nargs="+", default=[1, 4, 8],
                        choices=(1, 4, 8))
    parser.add_argument("--louvain", action="store_true",
                        help="run five synthetic python-louvain restarts on N=1150/3900")
    args = parser.parse_args()
    if not 1 <= args.attempts_per_worker <= BENCH_ATTEMPTS_MAX:
        parser.error(f"attempts per worker must be 1..{BENCH_ATTEMPTS_MAX}")
    if platform.machine() != "arm64" or sys.platform != "darwin":
        parser.error("This benchmark is currently reviewed only for macOS/Apple Silicon")
    start_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    generated = graph_generation_probes()
    fixtures = [make_synthetic_graph(n, family, root=BENCH_ROOT)
                for n in (100, 1150, 3900)
                for family in ("factor-mst", "ba-like")]
    swap = []
    for fixture in fixtures:
        for worker_count in args.workers:
            row = run_parallel_probe(fixture, worker_count,
                                     args.attempts_per_worker)
            swap.append({"n": fixture.n, "family": fixture.family,
                         "edges": fixture.m,
                         "fixture_sha256": fixture.fingerprint(), **row})
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        start_rss *= 1024
        peak_rss *= 1024
    result = {
        "status": "EXPLORATORY_SYNTHETIC_MICROBENCHMARK_NOT_FORMAL_VALIDATION",
        "runtime": {"python": sys.version, "platform": platform.platform(),
                    "machine": platform.machine(),
                    "packages": {name: _package_version(name) for name in
                                 ("numpy", "scipy", "networkx", "python-louvain")}},
        "benchmark_seed_root": BENCH_ROOT,
        "max_proposals_per_worker": args.attempts_per_worker,
        "graph_generation_16_cases": generated,
        "swap_throughput": swap,
        "process_peak_rss_bytes": int(peak_rss),
        "runtime_peak_rss_before_benchmark_bytes": int(start_rss),
        "louvain": louvain_probes(args.louvain),
        "limits": {"formal_cases": 0, "formal_chains": 0,
                   "max_worker_proposals": args.attempts_per_worker,
                   "biological_inputs": 0},
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def _package_version(name: str) -> str:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return "NOT_INSTALLED"


if __name__ == "__main__":
    raise SystemExit(main())
