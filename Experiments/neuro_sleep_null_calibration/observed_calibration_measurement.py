"""Measured legacy source reconstruction + shared canonical 200-Q contract.

No null/swap routine is imported. The one-entry cache contains raw frame arrays,
never correlations, graphs, partitions or Q. All returned signal diagnostics and
Q vectors are private run artifacts, not publication-ready data.
"""
from __future__ import annotations

import ctypes
import os
import resource
import sys
import time
import warnings
from pathlib import Path

import riken_source_identity as identity
from g0_q_protocol import canonical_louvain_q_vector, seed_vector_sha256


class MeasurementError(RuntimeError):
    """Unknown metrology or cache integrity: stop, never auto-retry."""


class PhaseRecords(dict):
    """Publish completed/aborted phase meters before moving to the next phase."""
    def __init__(self, sink=None):
        super().__init__()
        self.sink = sink

    def __setitem__(self, key, value):
        if key in self:
            raise MeasurementError("Duplicate phase meter")
        if self.sink is not None:
            self.sink(key, value)
        super().__setitem__(key, value)


def process_counters() -> dict:
    """Native process bytes are OS-attributed disk I/O, not device throughput.

    ru_inblock/oublock are operation counts and are never relabeled as bytes.
    RUSAGE_INFO_V2 layout follows the macOS SDK sys/resource.h.
    """
    usage = resource.getrusage(resource.RUSAGE_SELF)
    result = {"block_input_operations": usage.ru_inblock,
              "block_output_operations": usage.ru_oublock,
              "lifetime_ru_maxrss_bytes": int(usage.ru_maxrss *
                                              (1 if sys.platform == "darwin" else 1024))}
    if sys.platform == "darwin":
        fields = ("user_time", "system_time", "pkg_idle_wkups", "interrupt_wkups",
                  "pageins", "wired_size", "resident_size", "phys_footprint",
                  "proc_start_abstime", "proc_exit_abstime", "child_user_time",
                  "child_system_time", "child_pkg_idle_wkups", "child_interrupt_wkups",
                  "child_pageins", "child_elapsed_abstime", "diskio_bytesread",
                  "diskio_byteswritten")

        class RusageInfoV2(ctypes.Structure):
            _fields_ = [("uuid", ctypes.c_ubyte * 16)] + [
                (name, ctypes.c_uint64) for name in fields]

        info = RusageInfoV2()
        function = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True).proc_pid_rusage
        function.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_void_p]
        function.restype = ctypes.c_int
        if function(os.getpid(), 2, ctypes.byref(info)) != 0:
            raise MeasurementError("macOS native process I/O counters unavailable")
        result.update({"native_io_semantics": "macOS RUSAGE_INFO_V2 process-attributed bytes",
                       "read_bytes": int(info.diskio_bytesread),
                       "write_bytes": int(info.diskio_byteswritten),
                       "current_process_rss_bytes": int(info.resident_size)})
    elif sys.platform.startswith("linux"):
        data = dict(line.split(":", 1) for line in Path("/proc/self/io").read_text().splitlines())
        result.update({"native_io_semantics": "Linux /proc/self/io process-attributed bytes",
                       "read_bytes": int(data["read_bytes"]),
                       "write_bytes": int(data["write_bytes"]),
                       "current_process_rss_bytes": int(Path("/proc/self/statm").read_text().split()[1]) *
                       os.sysconf("SC_PAGE_SIZE")})
    else:
        raise MeasurementError("No verified native process I/O counter implementation")
    return result


class Phase:
    def __init__(self, target: dict, name: str):
        self.target, self.name = target, name

    def __enter__(self):
        self.start = process_counters()
        self.wall, self.cpu = time.perf_counter(), time.process_time()
        return self

    def __exit__(self, kind, value, traceback):
        wall, cpu = time.perf_counter() - self.wall, time.process_time() - self.cpu
        finish = process_counters()
        deltas = {key: finish[key] - self.start[key] for key in
                  ("read_bytes", "write_bytes", "block_input_operations", "block_output_operations")}
        if any(value < 0 for value in deltas.values()):
            raise MeasurementError("Native I/O counter moved backwards")
        self.target[self.name] = {"wall_seconds": wall, "process_cpu_seconds": cpu,
                                  "io_delta": deltas,
                                  "io_semantics": finish["native_io_semantics"],
                                  "process_rss_start_bytes": self.start["current_process_rss_bytes"],
                                  "process_rss_end_bytes": finish["current_process_rss_bytes"],
                                  "lifetime_ru_maxrss_bytes": finish["lifetime_ru_maxrss_bytes"],
                                  "aborted": kind is not None}


def _signature(path: Path) -> tuple:
    absolute = Path(os.path.abspath(path))
    if path.is_symlink() or path.resolve(strict=True) != absolute or not path.is_file():
        raise identity.IdentityEvidenceError("Raw source path is missing, redirected or symlinked")
    st = path.stat()
    return st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns


def _dataset(handle, suffix):
    import h5py

    names = []
    handle.visit(names.append)
    suffix = suffix.strip("/").lower()
    exact = [name for name in names if name.strip("/").lower() == suffix]
    names = exact or [name for name in names if name.strip("/").lower().endswith("/" + suffix)]
    if not names or not isinstance(handle[names[0]], h5py.Dataset):
        raise identity.IdentityEvidenceError("Required HDF5 dataset is absent")
    return handle[names[0]]


class RawWindowCache:
    """Exactly one immutable, size-bounded raw window, bound to source and frames.

    The cap is retained cache bytes, not a process hard limit: HDF5/NumPy
    temporaries are additionally supervised by sampled process-tree RSS.
    """
    def __init__(self, max_bytes: int):
        if type(max_bytes) is not int or max_bytes <= 0:
            raise ValueError("Cache byte cap must be a positive integer")
        self.max_bytes = max_bytes
        self.entry = None
        self.hits = self.misses = self.evictions = 0

    @property
    def retained_bytes(self) -> int:
        return 0 if self.entry is None else self.entry[2].nbytes

    def get(self, path: Path, *, source_sha: str, state: str, window: int,
            frame_sha: str):
        import h5py
        import numpy as np

        if state not in identity.STATES or type(window) is not int or window < 0:
            raise identity.IdentityEvidenceError("Invalid raw source window coordinate")
        signature = _signature(path)
        key = (str(path), source_sha, state, window, frame_sha)
        if self.entry is not None:
            old_key, old_signature, values = self.entry
            if old_key[0] == key[0] and old_signature != signature:
                raise identity.IdentityEvidenceError("Source changed while raw window cache was resident")
            if old_key == key:
                self.hits += 1
                return values, {"hit": True, "logical_hdf5_array_bytes": 0,
                                "window_array_bytes": values.nbytes,
                                "retained_cache_bytes": self.retained_bytes}
            self.evictions += 1
            self.entry = None  # evict before allocation; no second retained window
            del values
        self.misses += 1
        with h5py.File(path, "r") as handle:
            signal = _dataset(handle, "spike_smoothed")
            refs = np.asarray(_dataset(handle, "frame/used_frame")[()]).reshape(-1)
            if len(refs) != 2 or signal.ndim != 2:
                raise identity.IdentityEvidenceError("Source dataset dimensions differ")
            all_frames = np.asarray(handle[refs[identity.STATES.index(state)]][()]).reshape(-1).astype(np.int64) - 1
            begin, end = window * identity.WINDOW_SIZE, (window + 1) * identity.WINDOW_SIZE
            if (end > len(all_frames) or np.any(all_frames < 0) or
                    np.any(all_frames >= signal.shape[0])):
                raise identity.IdentityEvidenceError("Source frame window is invalid")
            frames = all_frames[begin:end]
            if identity.hash_int64(frames) != frame_sha:
                raise identity.IdentityEvidenceError("Source frame identity differs from fixed task")
            expected_bytes = len(frames) * int(signal.shape[1]) * 8
            if expected_bytes > self.max_bytes:
                raise MeasurementError("One raw window exceeds the frozen cache byte cap")
            if np.all(np.diff(frames) >= 0):
                values = np.asarray(signal[frames.tolist(), :], dtype=np.float64).T
            else:
                order = np.argsort(frames, kind="stable")
                sorted_values = np.asarray(signal[frames[order].tolist(), :], dtype=np.float64).T
                values = np.empty_like(sorted_values)
                values[:, order] = sorted_values
            if values.nbytes != expected_bytes or _signature(path) != signature:
                raise identity.IdentityEvidenceError("Raw source changed during window load")
        values.setflags(write=False)
        self.entry = key, signature, values
        return values, {"hit": False, "logical_hdf5_array_bytes": expected_bytes,
                        "window_array_bytes": expected_bytes,
                        "retained_cache_bytes": self.retained_bytes}


def measured_graph(abs_corr, nodes, builder_factory, phases):
    """Instrument the hash-pinned historical function, then independently check topology."""
    builder, function_sha = builder_factory()
    mst_metrics = {}
    original_mst = builder.__globals__["minimum_spanning_tree"]

    def timed_mst(*args, **kwargs):
        with Phase(mst_metrics, "mst"):
            return original_mst(*args, **kwargs)

    builder.__globals__["minimum_spanning_tree"] = timed_mst
    try:
        with Phase(phases, "historical_graph_builder_inclusive"):
            graph, _ = builder(abs_corr)
    finally:
        builder.__globals__["minimum_spanning_tree"] = original_mst
    if "mst" not in mst_metrics:
        raise MeasurementError("Historical MST timing hook was not called")
    for name, meter in mst_metrics.items():
        phases[name] = meter
    parent, mst = phases["historical_graph_builder_inclusive"], phases["mst"]
    phases["edge_selection_graph_residual"] = {
        "wall_seconds": max(0.0, parent["wall_seconds"] - mst["wall_seconds"]),
        "process_cpu_seconds": max(0.0, parent["process_cpu_seconds"] - mst["process_cpu_seconds"]),
        "semantics": "builder inclusive minus MST; ranking/top-up/insertion; do not sum with parent",
    }
    with Phase(phases, "independent_graph_identity_and_canonical_representation"):
        candidate = identity.build_candidate_graph(abs_corr)
        old = {tuple(sorted((int(u), int(v)))) for u, v in graph.edges}
        new = {tuple(sorted((int(u), int(v)))) for u, v in candidate.edges}
        if (old != new or tuple(graph.nodes) != tuple(range(len(nodes))) or
                tuple(candidate.nodes) != tuple(graph.nodes) or len(old) != len(nodes) * 8):
            raise identity.IdentityEvidenceError("Observed graph topology or node identity failed")
        labeled = sorted((min(nodes[u], nodes[v]), max(nodes[u], nodes[v])) for u, v in old)
    return labeled, {"historical_function_sha256": function_sha,
                      "labeled_edge_set_sha256": identity.sha256_bytes(identity.canonical_json(labeled)),
                      "node_order_sha256": identity.hash_int64(nodes),
                      "N": len(nodes), "E": len(old), "status": "PASS"}


def measure_row(row: dict, *, source_path: Path, selected: list[int], seeds: list[int],
                cache: RawWindowCache, builder_factory, initial_phases: dict | None = None) -> dict:
    import numpy as np

    phases = initial_phases if initial_phases is not None else {}
    if (len(selected) != row["N"] or selected != sorted(set(selected)) or
            identity.hash_int64(selected) != row["selected_neuron_indices_sha256"] or
            seed_vector_sha256(seeds) != row["louvain_seed_vector_sha256"] or len(seeds) != 200):
        raise identity.IdentityEvidenceError("Observed subset or fixed seed identity failed")
    with Phase(phases, "source_hdf5_and_raw_window"):
        raw, cache_info = cache.get(source_path, source_sha=row["source_file_sha256"],
                                    state=row["state"], window=row["window_id"],
                                    frame_sha=row["source_frame_indices_sha256"])
    with Phase(phases, "correlation_and_zero_variance_diagnostics"):
        subset = raw[np.asarray(selected, dtype=np.int64), :]
        nonfinite = int(np.count_nonzero(~np.isfinite(subset)))
        constant = np.all(subset == subset[:, :1], axis=1) & np.isfinite(subset[:, 0])
        with warnings.catch_warnings(record=True) as notices:
            warnings.simplefilter("always", RuntimeWarning)
            variance = np.var(subset, axis=1)
            correlation = np.corrcoef(subset, rowvar=True)
        zero_variance = variance == 0
        generated_nonfinite = int(np.count_nonzero(~np.isfinite(correlation)))
        # Exactly the historical rule; diagnostics never drop/replace a channel.
        correlation = np.nan_to_num(correlation, nan=0.0, posinf=0.0, neginf=0.0)
        np.fill_diagonal(correlation, 0.0)
        absolute = np.abs(correlation)
        diagnostic = {
            "raw_nonfinite_values": nonfinite,
            "constant_neuron_ids": [selected[i] for i in np.flatnonzero(constant)],
            "zero_variance_neuron_ids": [selected[i] for i in np.flatnonzero(zero_variance)],
            "corrcoef_nonfinite_before_zeroing": generated_nonfinite,
            "runtime_warning_count": len(notices),
            "handling": "unchanged corrcoef -> nan_to_num(0) -> diagonal 0 -> abs",
        }
        del subset, correlation
    edges, graph_identity = measured_graph(absolute, selected, builder_factory, phases)
    del absolute
    if graph_identity["E"] != row["expected_edge_count"]:
        raise identity.IdentityEvidenceError("Observed edge count differs from frozen inventory")
    with Phase(phases, "canonical_200_Q_including_shared_representation"):
        try:
            q = canonical_louvain_q_vector(selected, edges, seeds)
        except ValueError as exc:
            if "nonfinite" in str(exc).lower():
                raise identity.IdentityEvidenceError("Confirmed nonfinite canonical Q integrity failure") from exc
            raise
    return {"schema": "SRT_OBSERVED_CALIBRATION_ROW_V1", "graph_id": row["graph_id"],
            "source_graph_identity": graph_identity, "input_identity": row,
            "original_neuron_ids": selected, "louvain_seeds": seeds,
            "labeled_edges": edges,
            "canonical": q, "phases": phases, "cache": cache_info,
            "zero_variance": diagnostic,
            "io_caveat": "native process-attributed bytes + logical arrays, not physical device bytes",
            "rss_caveat": "phase endpoints and lifetime ru_maxrss; row process-tree samples in Watchdog"}
