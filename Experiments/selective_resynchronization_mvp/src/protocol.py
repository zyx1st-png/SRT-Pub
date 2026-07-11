from __future__ import annotations

import json
import math
import shutil
import time
from dataclasses import asdict, dataclass, fields
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch

from .data import DataArtifacts, make_loader, phase_dataset, prepare_data
from .fisher import diagonal_empirical_fisher_burden
from .metrics import (
    Evaluation,
    evaluate,
    gradient_disagreement,
    group_parameter_distance,
    parameter_distance,
    parameter_snapshot,
    predictive_kl,
)
from .models import build_model, count_parameters
from .representations import linear_cka, subspace_overlap, temporal_permutation_overlaps
from .shifts import shift_definition_hash
from .training import ScientificFailure, build_optimizer, train_epoch
from .utils import (
    append_jsonl,
    choose_device,
    environment_info,
    git_sha,
    load_yaml,
    make_read_only,
    make_writable,
    set_global_seed,
    sha256_file,
    sha256_paths,
    utc_now,
    write_json,
)


@dataclass(frozen=True)
class ABArtifacts:
    seed: int
    condition: str
    no_shift: bool
    a_end_validation_accuracy: float
    b_rows: tuple[dict[str, Any], ...]
    z_a: np.ndarray
    z_open: np.ndarray
    z_stable: np.ndarray


def assert_ab_only_schema() -> None:
    forbidden = {"c", "c_accuracy", "c_loss", "q_c", "c_outcomes"}
    names = {field.name.lower() for field in fields(ABArtifacts)}
    if names & forbidden or any(name.startswith("c_") for name in names):
        raise AssertionError(f"C-stage field leaked into ABArtifacts: {sorted(names & forbidden)}")


def _row_for_epoch(rows: tuple[dict[str, Any], ...], epoch: int) -> dict[str, Any]:
    selected = [row for row in rows if int(row["phase_epoch"]) == epoch]
    if len(selected) != 1:
        raise ValueError(f"Expected one B row for epoch {epoch}, got {len(selected)}")
    return selected[0]


def _area(rows: list[dict[str, Any]], key: str, baseline: float = 0.0, absolute: bool = False) -> float:
    values = np.asarray([float(row[key]) - baseline for row in rows], dtype=np.float64)
    if absolute:
        values = np.abs(values)
    if len(values) == 1:
        return float(values[0])
    return float(np.trapezoid(values, dx=1.0))


def robust_z(value: float, key: str, constants: dict[str, Any]) -> float:
    item = constants["features"][key]
    return float((value - float(item["median"])) / float(item["scale"]))


def compute_preC_features(
    artifacts: ABArtifacts,
    config: dict[str, Any],
    standardization_constants: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Compute A/B-only features. This function has no C-stage input."""
    assert_ab_only_schema()
    open_epochs = [int(value) for value in config["windows"]["B_open"]]
    stable_epochs = [int(value) for value in config["windows"]["B_stable"]]
    b_epochs = int(config["epochs"]["B"])
    rows = artifacts.b_rows
    b0 = _row_for_epoch(rows, 0)
    open_rows = [_row_for_epoch(rows, epoch) for epoch in open_epochs]
    stable_rows = [_row_for_epoch(rows, epoch) for epoch in stable_epochs]
    b_end = _row_for_epoch(rows, b_epochs)

    d_repr_peak = max(float(row["representation_drift_from_A"]) for row in open_rows)
    d_grad_peak = max(float(row["gradient_disagreement"]) for row in open_rows)
    late_grad = float(np.mean([float(row["gradient_disagreement"]) for row in stable_rows]))
    r_grad = float((d_grad_peak - late_grad) / (abs(d_grad_peak) + 1e-12))
    velocity_rows = stable_rows[1:] if len(stable_rows) > 1 else stable_rows
    v_late = float(np.mean([float(row["representation_velocity"]) for row in velocity_rows]))
    a_b = float(b_end["validation_balanced_accuracy"] - b0["validation_balanced_accuracy"])
    n_b = float(b_end["representation_drift_from_A"])
    s_b = subspace_overlap(
        artifacts.z_a,
        artifacts.z_open,
        artifacts.z_stable,
        k=int(config.get("subspace_k", 8)),
    )
    stable_x = np.asarray(stable_epochs, dtype=np.float64)
    stable_loss = np.asarray([row["validation_loss"] for row in stable_rows], dtype=np.float64)
    b_loss_slope = float(np.polyfit(stable_x, stable_loss, 1)[0]) if len(stable_rows) > 1 else 0.0

    all_adapt_rows = [_row_for_epoch(rows, epoch) for epoch in range(1, b_epochs + 1)]
    result: dict[str, Any] = {
        "seed": artifacts.seed,
        "condition": artifacts.condition,
        "no_shift": artifacts.no_shift,
        "created_utc": utc_now(),
        "uses_c_data": False,
        "d_repr_peak": d_repr_peak,
        "d_grad_peak": d_grad_peak,
        "r_grad": r_grad,
        "v_late": v_late,
        "a_B": a_b,
        "n_B": n_b,
        "S_B": s_b,
        "B_loss_slope_late": b_loss_slope,
        "A_end_validation_accuracy": artifacts.a_end_validation_accuracy,
        "B_start_validation_accuracy": float(b0["validation_balanced_accuracy"]),
        "B_end_validation_accuracy": float(b_end["validation_balanced_accuracy"]),
        "B_end_validation_loss": float(b_end["validation_loss"]),
        "B_budget_updates": int(b_end["phase_global_updates"]),
        "loss_change_area": _area(
            all_adapt_rows, "validation_loss", baseline=float(b0["validation_loss"]), absolute=True
        ),
        "gradient_norm_area": _area(all_adapt_rows, "train_gradient_norm"),
        "update_norm_area": _area(all_adapt_rows, "parameter_update_norm"),
        "parameter_distance_B_end": float(b_end["parameter_distance_from_phase_start"]),
        "predictive_KL_area": _area(all_adapt_rows, "predictive_KL_from_previous"),
        "predictive_entropy_change_area": _area(
            all_adapt_rows,
            "predictive_entropy",
            baseline=float(b0["predictive_entropy"]),
            absolute=True,
        ),
        "representation_drift_area": _area(all_adapt_rows, "representation_drift_from_A"),
        "fisher_burden_area": _area(all_adapt_rows, "fisher_empirical_diag_burden"),
        "fisher_burden_peak": max(float(row["fisher_empirical_diag_burden"]) for row in all_adapt_rows),
    }

    transformed = {
        "log1p_d_repr_peak": math.log1p(max(0.0, d_repr_peak)),
        "log1p_d_grad_peak": math.log1p(max(0.0, d_grad_peak)),
        "r_grad": r_grad,
        "v_late": v_late,
        "a_B": a_b,
        "n_B": n_b,
        "S_B": s_b,
    }
    result.update({f"transform_{key}": value for key, value in transformed.items()})
    if standardization_constants is None:
        result.update(
            {
                "opening_dimension": None,
                "stabilization_dimension": None,
                "adaptation_dimension": None,
                "nonrollback_dimension": None,
                "incorporation_dimension": None,
                "SR_preC": None,
                "standardization_hash": None,
            }
        )
        return result

    opening = 0.5 * (
        robust_z(transformed["log1p_d_repr_peak"], "log1p_d_repr_peak", standardization_constants)
        + robust_z(transformed["log1p_d_grad_peak"], "log1p_d_grad_peak", standardization_constants)
    )
    stabilization = 0.5 * (
        robust_z(r_grad, "r_grad", standardization_constants)
        - robust_z(v_late, "v_late", standardization_constants)
    )
    adaptation = robust_z(a_b, "a_B", standardization_constants)
    nonrollback = robust_z(n_b, "n_B", standardization_constants)
    incorporation = robust_z(s_b, "S_B", standardization_constants)
    score = float(np.mean([opening, stabilization, adaptation, nonrollback, incorporation]))
    result.update(
        {
            "opening_dimension": opening,
            "stabilization_dimension": stabilization,
            "adaptation_dimension": adaptation,
            "nonrollback_dimension": nonrollback,
            "incorporation_dimension": incorporation,
            "SR_preC": score,
            "standardization_hash": standardization_constants.get("file_sha256"),
        }
    )
    return result


def freeze_preC_files(run_dir: Path, record: dict[str, Any]) -> dict[str, Any]:
    if any(key.lower().startswith("c_") or key.lower() == "q_c" for key in record):
        raise ValueError("C-stage field supplied to pre-C freeze")
    json_path = run_dir / "preC_features.json"
    parquet_path = run_dir / "preC_features.parquet"
    hash_path = run_dir / "preC_features.sha256"
    if json_path.exists() or parquet_path.exists() or hash_path.exists():
        raise FileExistsError("Pre-C feature artifact already exists and cannot be overwritten")
    write_json(json_path, record, overwrite=False)
    pd.DataFrame([record]).to_parquet(parquet_path, index=False)
    digest = sha256_file(parquet_path)
    hash_record = {
        "sha256": digest,
        "parquet": parquet_path.name,
        "json_sha256": sha256_file(json_path),
        "created_utc": utc_now(),
    }
    write_json(hash_path, hash_record, overwrite=False)
    make_read_only(json_path)
    make_read_only(parquet_path)
    make_read_only(hash_path)
    return hash_record


def verify_preC_files(run_dir: Path) -> dict[str, Any]:
    hash_path = run_dir / "preC_features.sha256"
    record = json.loads(hash_path.read_text(encoding="utf-8"))
    actual = sha256_file(run_dir / record["parquet"])
    if actual != record["sha256"]:
        raise RuntimeError("Frozen pre-C feature hash mismatch")
    if sha256_file(run_dir / "preC_features.json") != record["json_sha256"]:
        raise RuntimeError("Frozen pre-C JSON hash mismatch")
    return record


class ProtocolRunner:
    def __init__(
        self,
        experiment_root: Path,
        config_path: Path,
        device: str | None = None,
        output_root_override: Path | None = None,
    ) -> None:
        self.experiment_root = experiment_root.resolve()
        self.repo_root = self.experiment_root.parents[1]
        self.config_path = config_path.resolve()
        self.config = load_yaml(self.config_path)
        if device is not None:
            self.config["device"] = device
        self.device = choose_device(str(self.config.get("device", "auto")))
        self.output_root = (
            output_root_override.resolve()
            if output_root_override is not None
            else (self.experiment_root / self.config["output_root"]).resolve()
        )
        self.output_root.mkdir(parents=True, exist_ok=True)
        (
            self.train_base,
            self.test_base,
            self.splits,
            self.probes,
            self.data_artifacts,
        ) = prepare_data(self.experiment_root, self.config, download=True)
        self.shift_hash = shift_definition_hash(self.config["shift"])
        self.standardization_constants = self._load_optional_json(
            self.config.get("standardization_constants")
        )
        self.shift_cache_root = self.experiment_root / self.config["data_root"] / "shift_cache"
        self._dataset_cache: dict[tuple, Any] = {}

    def _load_optional_json(self, relative: str | None) -> dict[str, Any] | None:
        if not relative:
            return None
        path = self.experiment_root / relative
        if not path.exists():
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        data["file_sha256"] = sha256_file(path)
        return data

    def _dataset(self, phase: str, partition: str, no_shift: bool = False, fisher: bool = False):
        key = (phase, partition, no_shift, fisher)
        if key in self._dataset_cache:
            return self._dataset_cache[key]
        dataset = phase_dataset(
            self.train_base,
            self.test_base,
            self.splits,
            self.probes,
            phase,
            partition,
            self.config["shift"],
            no_shift=no_shift,
            fisher=fisher,
            shift_cache_root=self.shift_cache_root,
        )
        self._dataset_cache[key] = dataset
        return dataset

    def _loader(
        self,
        phase: str,
        partition: str,
        seed: int,
        shuffle: bool = False,
        no_shift: bool = False,
        fisher: bool = False,
        batch_size: int | None = None,
    ):
        dataset = self._dataset(phase, partition, no_shift=no_shift, fisher=fisher)
        size = batch_size or (
            int(self.config["batch_size"]) if partition == "train" else 256
        )
        return make_loader(
            dataset,
            batch_size=size,
            shuffle=shuffle,
            seed=seed,
            num_workers=int(self.config.get("num_workers", 0)),
        )

    def _shared_a_dir(self, seed: int) -> Path:
        return self.output_root / "_shared_A" / f"seed_{seed}"

    def _run_dir(self, seed: int, condition: str) -> Path:
        return self.output_root / f"seed_{seed}__condition_{condition}"

    def ensure_shared_a(self, seed: int, force: bool = False) -> Path:
        shared = self._shared_a_dir(seed)
        checkpoint = shared / "A_end.pt"
        if checkpoint.exists() and not force:
            return shared
        if shared.exists() and force:
            shutil.rmtree(shared)
        shared.mkdir(parents=True, exist_ok=True)
        set_global_seed(seed)
        model = build_model().to(self.device)
        optimizer = build_optimizer(model, self.config["training"]["A"])
        train_loader = self._loader("A", "train", seed + 11, shuffle=True)
        validation_loader = self._loader("A", "validation", seed + 12)
        probe_loader = self._loader("A", "probe", seed + 13)
        gradient_loader = self._loader("A", "probe", seed + 14, batch_size=64)
        fisher_loader = self._loader("A", "probe", seed + 15, fisher=True, batch_size=20)
        phase_start = parameter_snapshot(model)
        previous_parameters = phase_start
        previous_probe: Evaluation | None = None
        rows = []
        representations: dict[str, np.ndarray] = {}
        global_updates = 0
        for epoch in range(1, int(self.config["epochs"]["A"]) + 1):
            train_values = train_epoch(model, train_loader, optimizer, self.device)
            global_updates += len(train_loader)
            validation = evaluate(model, validation_loader, self.device)
            probe = evaluate(model, probe_loader, self.device)
            current_parameters = parameter_snapshot(model)
            disagreement, probe_gradient_norm = gradient_disagreement(
                model, gradient_loader, self.device
            )
            fisher, fisher_count = diagonal_empirical_fisher_burden(
                model,
                fisher_loader,
                previous_parameters,
                self.device,
                int(self.config["fisher_probe_size"]),
            )
            row = {
                "timestamp_utc": utc_now(),
                "phase": "A",
                "phase_epoch": epoch,
                "phase_global_updates": global_updates,
                "phase_relative_step": global_updates,
                "global_step": global_updates,
                "seed": seed,
                "condition": "shared_A",
                "model_id": "light_cnn",
                "data_shift_id": "A_clean",
                "checkpoint_id": f"A{epoch}",
                **train_values,
                "validation_loss": validation.loss,
                "validation_accuracy": validation.accuracy,
                "validation_balanced_accuracy": validation.balanced_accuracy,
                "A_accuracy": validation.accuracy,
                "B_accuracy": None,
                "C_accuracy": None,
                "predictive_entropy": probe.predictive_entropy,
                "representation_coherence": probe.coherence,
                "gradient_disagreement": disagreement,
                "probe_gradient_norm": probe_gradient_norm,
                "parameter_update_norm": parameter_distance(current_parameters, previous_parameters),
                "parameter_distance_from_phase_start": parameter_distance(current_parameters, phase_start),
                "predictive_KL_from_previous": 0.0
                if previous_probe is None
                else predictive_kl(previous_probe.probabilities, probe.probabilities),
                "representation_drift_from_A": 0.0,
                "representation_velocity": 0.0
                if previous_probe is None
                else 1.0 - linear_cka(previous_probe.representations, probe.representations),
                "fisher_empirical_diag_burden": fisher,
                "fisher_sample_count": fisher_count,
            }
            rows.append(row)
            append_jsonl(shared / "A_metrics.jsonl", row)
            if epoch in self.config["windows"]["A"] or epoch == int(self.config["epochs"]["A"]):
                representations[f"A{epoch}"] = probe.representations
            previous_parameters = current_parameters
            previous_probe = probe
        torch.save(
            {
                "model": model.state_dict(),
                "optimizer": optimizer.state_dict(),
                "seed": seed,
                "epoch": int(self.config["epochs"]["A"]),
            },
            checkpoint,
        )
        np.savez_compressed(shared / "A_representations.npz", **representations)
        write_json(
            shared / "A_summary.json",
            {
                "seed": seed,
                "validation_accuracy": rows[-1]["validation_accuracy"],
                "validation_loss": rows[-1]["validation_loss"],
                "global_updates": global_updates,
                "parameter_count": count_parameters(model),
                "created_utc": utc_now(),
            },
        )
        return shared

    def run_ab(
        self,
        seed: int,
        condition: str,
        no_shift: bool = False,
        force: bool = False,
    ) -> Path:
        if condition not in self.config["conditions"]:
            raise ValueError(f"Unknown condition {condition}")
        run_dir = self._run_dir(seed, condition)
        if (run_dir / "AB_complete.json").exists() and not force:
            return run_dir
        if run_dir.exists() and force:
            for path in run_dir.glob("preC_features*"):
                make_writable(path)
            shutil.rmtree(run_dir)
        run_dir.mkdir(parents=True, exist_ok=True)
        shared = self.ensure_shared_a(seed, force=False)
        set_global_seed(seed)
        model = build_model().to(self.device)
        a_checkpoint = torch.load(shared / "A_end.pt", map_location=self.device, weights_only=False)
        model.load_state_dict(a_checkpoint["model"])
        settings = self.config["training"]["conditions"][condition]
        optimizer = build_optimizer(model, settings)
        train_loader = self._loader("B", "train", seed + 101, shuffle=True, no_shift=no_shift)
        validation_loader = self._loader("B", "validation", seed + 102, no_shift=no_shift)
        probe_loader = self._loader("B", "probe", seed + 103, no_shift=no_shift)
        gradient_loader = self._loader(
            "B", "probe", seed + 104, no_shift=no_shift, batch_size=64
        )
        fisher_loader = self._loader(
            "B", "probe", seed + 105, no_shift=no_shift, fisher=True, batch_size=20
        )
        a_validation_loader = self._loader("A", "validation", seed + 106)
        replay_loader = None
        if float(settings.get("replay_fraction", 0.0)) > 0:
            replay_loader = self._loader("A", "train", seed + 107, shuffle=True)

        a_reps = np.load(shared / "A_representations.npz")
        a_end_epoch = int(self.config["epochs"]["A"])
        z_a = np.asarray(a_reps[f"A{a_end_epoch}"])
        a_summary = json.loads((shared / "A_summary.json").read_text(encoding="utf-8"))
        a_rows = [json.loads(line) for line in (shared / "A_metrics.jsonl").read_text().splitlines()]
        step_path = run_dir / "step_metrics.jsonl"
        for row in a_rows:
            copied = dict(row)
            copied["condition"] = condition
            copied["no_shift"] = no_shift
            append_jsonl(step_path, copied)

        phase_start = parameter_snapshot(model)
        previous_parameters = phase_start
        probe0 = evaluate(model, probe_loader, self.device)
        validation0 = evaluate(model, validation_loader, self.device)
        a_validation0 = evaluate(model, a_validation_loader, self.device)
        disagreement0, probe_grad0 = gradient_disagreement(model, gradient_loader, self.device)
        b_rows: list[dict[str, Any]] = []
        row0 = {
            "timestamp_utc": utc_now(),
            "phase": "B",
            "phase_epoch": 0,
            "phase_global_updates": 0,
            "phase_relative_step": 0,
            "global_step": int(a_summary["global_updates"]),
            "seed": seed,
            "condition": condition,
            "no_shift": no_shift,
            "model_id": "light_cnn",
            "data_shift_id": "A_no_shift" if no_shift else self.shift_hash,
            "checkpoint_id": "B0",
            "train_loss": None,
            "train_gradient_norm": 0.0,
            "learning_rate": float(settings["lr"]),
            "validation_loss": validation0.loss,
            "validation_accuracy": validation0.accuracy,
            "validation_balanced_accuracy": validation0.balanced_accuracy,
            "A_accuracy": a_validation0.accuracy,
            "B_accuracy": validation0.accuracy,
            "C_accuracy": None,
            "predictive_entropy": probe0.predictive_entropy,
            "representation_coherence": probe0.coherence,
            "gradient_disagreement": disagreement0,
            "probe_gradient_norm": probe_grad0,
            "parameter_update_norm": 0.0,
            "parameter_distance_from_phase_start": 0.0,
            "predictive_KL_from_previous": 0.0,
            "representation_drift_from_A": 1.0 - linear_cka(z_a, probe0.representations),
            "representation_velocity": 0.0,
            "fisher_empirical_diag_burden": 0.0,
            "fisher_sample_count": int(self.config["fisher_probe_size"]),
        }
        b_rows.append(row0)
        append_jsonl(step_path, row0)
        stored_reps: dict[str, np.ndarray] = {"A_end": z_a, "B0": probe0.representations}
        previous_probe = probe0
        global_updates = 0
        try:
            for epoch in range(1, int(self.config["epochs"]["B"]) + 1):
                train_values = train_epoch(
                    model,
                    train_loader,
                    optimizer,
                    self.device,
                    replay_loader=replay_loader,
                    replay_fraction=float(settings.get("replay_fraction", 0.0)),
                )
                global_updates += len(train_loader)
                validation = evaluate(model, validation_loader, self.device)
                a_validation = evaluate(model, a_validation_loader, self.device)
                probe = evaluate(model, probe_loader, self.device)
                current_parameters = parameter_snapshot(model)
                disagreement, probe_gradient_norm = gradient_disagreement(
                    model, gradient_loader, self.device
                )
                fisher, fisher_count = diagonal_empirical_fisher_burden(
                    model,
                    fisher_loader,
                    previous_parameters,
                    self.device,
                    int(self.config["fisher_probe_size"]),
                )
                row = {
                    "timestamp_utc": utc_now(),
                    "phase": "B",
                    "phase_epoch": epoch,
                    "phase_global_updates": global_updates,
                    "phase_relative_step": global_updates,
                    "global_step": int(a_summary["global_updates"]) + global_updates,
                    "seed": seed,
                    "condition": condition,
                    "no_shift": no_shift,
                    "model_id": "light_cnn",
                    "data_shift_id": "A_no_shift" if no_shift else self.shift_hash,
                    "checkpoint_id": f"B{epoch}",
                    **train_values,
                    "validation_loss": validation.loss,
                    "validation_accuracy": validation.accuracy,
                    "validation_balanced_accuracy": validation.balanced_accuracy,
                    "A_accuracy": a_validation.accuracy,
                    "B_accuracy": validation.accuracy,
                    "C_accuracy": None,
                    "predictive_entropy": probe.predictive_entropy,
                    "representation_coherence": probe.coherence,
                    "gradient_disagreement": disagreement,
                    "probe_gradient_norm": probe_gradient_norm,
                    "parameter_update_norm": parameter_distance(current_parameters, previous_parameters),
                    "parameter_distance_from_phase_start": parameter_distance(
                        current_parameters, phase_start
                    ),
                    "predictive_KL_from_previous": predictive_kl(
                        previous_probe.probabilities, probe.probabilities
                    ),
                    "representation_drift_from_A": 1.0 - linear_cka(z_a, probe.representations),
                    "representation_velocity": 1.0
                    - linear_cka(previous_probe.representations, probe.representations),
                    "fisher_empirical_diag_burden": fisher,
                    "fisher_sample_count": fisher_count,
                }
                b_rows.append(row)
                append_jsonl(step_path, row)
                if epoch in set(self.config["windows"]["B_open"]) | set(
                    self.config["windows"]["B_stable"]
                ):
                    stored_reps[f"B{epoch}"] = probe.representations
                previous_parameters = current_parameters
                previous_probe = probe
        except ScientificFailure as exc:
            write_json(
                run_dir / "failure_record.json",
                {
                    "failure_type": "scientific",
                    "phase": "B",
                    "seed": seed,
                    "condition": condition,
                    "message": str(exc),
                    "timestamp_utc": utc_now(),
                },
            )
            raise

        open_epoch = max(int(value) for value in self.config["windows"]["B_open"])
        stable_epoch = max(int(value) for value in self.config["windows"]["B_stable"])
        artifacts = ABArtifacts(
            seed=seed,
            condition=condition,
            no_shift=no_shift,
            a_end_validation_accuracy=float(a_summary["validation_accuracy"]),
            b_rows=tuple(b_rows),
            z_a=z_a,
            z_open=stored_reps[f"B{open_epoch}"],
            z_stable=stored_reps[f"B{stable_epoch}"],
        )
        record = compute_preC_features(
            artifacts,
            self.config,
            standardization_constants=self.standardization_constants,
        )
        np.savez_compressed(run_dir / "AB_representations.npz", **stored_reps)
        hash_record = freeze_preC_files(run_dir, record)
        torch.save(
            {
                "model": model.state_dict(),
                "optimizer": optimizer.state_dict(),
                "seed": seed,
                "condition": condition,
                "epoch": int(self.config["epochs"]["B"]),
            },
            run_dir / "B_end.pt",
        )
        pd.DataFrame([json.loads(line) for line in step_path.read_text().splitlines()]).to_parquet(
            run_dir / "step_metrics_AB.parquet", index=False
        )
        write_json(
            run_dir / "AB_complete.json",
            {
                "seed": seed,
                "condition": condition,
                "no_shift": no_shift,
                "preC_hash": hash_record,
                "completed_utc": utc_now(),
                "device": str(self.device),
                "shift_hash": self.shift_hash,
                "data_split_hash": self.data_artifacts.split_hash,
                "probe_hash": self.data_artifacts.probe_hash,
            },
        )
        return run_dir

    def run_c(self, seed: int, condition: str, force: bool = False) -> Path:
        run_dir = self._run_dir(seed, condition)
        if (run_dir / "C_complete.json").exists() and not force:
            return run_dir
        if not (run_dir / "AB_complete.json").exists():
            raise RuntimeError("A/B must complete before C")
        pre_hash = verify_preC_files(run_dir)
        if force:
            for path in [run_dir / "C_outcomes.json", run_dir / "C_complete.json", run_dir / "step_metrics.parquet"]:
                if path.exists():
                    path.unlink()
        c_started = utc_now()
        set_global_seed(seed + 500_000)
        model = build_model().to(self.device)
        checkpoint = torch.load(run_dir / "B_end.pt", map_location=self.device, weights_only=False)
        model.load_state_dict(checkpoint["model"])
        settings = self.config["training"]["conditions"][condition]
        optimizer = build_optimizer(model, settings)
        optimizer.load_state_dict(checkpoint["optimizer"])

        # C loaders are constructed only after the frozen pre-C hash is verified.
        train_loader = self._loader("C", "train", seed + 201, shuffle=True)
        validation_loader = self._loader("C", "validation", seed + 202)
        probe_loader = self._loader("C", "probe", seed + 203)
        gradient_loader = self._loader("C", "probe", seed + 204, batch_size=64)
        fisher_loader = self._loader("C", "probe", seed + 205, fisher=True, batch_size=20)
        c_test_loader = self._loader("C", "test", seed + 206)
        a_validation_loader = self._loader("A", "validation", seed + 207)
        b_validation_loader = self._loader("B", "validation", seed + 208)
        a_test_loader = self._loader("A", "test", seed + 209)
        b_test_loader = self._loader("B", "test", seed + 210)
        replay_loader = None
        if float(settings.get("replay_fraction", 0.0)) > 0:
            replay_loader = self._loader("B", "train", seed + 211, shuffle=True)

        b_parameters = parameter_snapshot(model)
        c_global_offset = (
            int(self.config["epochs"]["A"]) + int(self.config["epochs"]["B"])
        ) * len(train_loader)
        previous_parameters = b_parameters
        c_probe0 = evaluate(model, probe_loader, self.device)
        c_test0 = evaluate(model, c_test_loader, self.device)
        c_validation0 = evaluate(model, validation_loader, self.device)
        a_validation0 = evaluate(model, a_validation_loader, self.device)
        b_validation0 = evaluate(model, b_validation_loader, self.device)
        disagreement0, probe_grad0 = gradient_disagreement(model, gradient_loader, self.device)
        step_path = run_dir / "step_metrics.jsonl"
        c_rows: list[dict[str, Any]] = []
        row0 = {
            "timestamp_utc": c_started,
            "phase": "C",
            "phase_epoch": 0,
            "phase_global_updates": 0,
            "phase_relative_step": 0,
            "global_step": c_global_offset,
            "seed": seed,
            "condition": condition,
            "no_shift": False,
            "model_id": "light_cnn",
            "data_shift_id": self.shift_hash + "_label_rule",
            "checkpoint_id": "C0",
            "train_loss": None,
            "train_gradient_norm": 0.0,
            "learning_rate": float(optimizer.param_groups[0]["lr"]),
            "validation_loss": c_validation0.loss,
            "validation_accuracy": c_validation0.accuracy,
            "validation_balanced_accuracy": c_validation0.balanced_accuracy,
            "A_accuracy": a_validation0.accuracy,
            "B_accuracy": b_validation0.accuracy,
            "C_accuracy": c_test0.accuracy,
            "C_balanced_accuracy": c_test0.balanced_accuracy,
            "C_changed_balanced_accuracy": c_test0.changed_balanced_accuracy,
            "C_unchanged_balanced_accuracy": c_test0.unchanged_balanced_accuracy,
            "C_test_loss": c_test0.loss,
            "predictive_entropy": c_probe0.predictive_entropy,
            "representation_coherence": c_probe0.coherence,
            "gradient_disagreement": disagreement0,
            "probe_gradient_norm": probe_grad0,
            "parameter_update_norm": 0.0,
            "parameter_distance_from_phase_start": 0.0,
            "predictive_KL_from_previous": 0.0,
            "representation_drift_from_A": None,
            "representation_velocity": 0.0,
            "fisher_empirical_diag_burden": 0.0,
            "fisher_sample_count": int(self.config["fisher_probe_size"]),
            "trunk_parameter_distance_from_B": 0.0,
            "head_parameter_distance_from_B": 0.0,
        }
        c_rows.append(row0)
        append_jsonl(step_path, row0)
        previous_probe = c_probe0
        global_updates = 0
        try:
            for epoch in range(1, int(self.config["epochs"]["C"]) + 1):
                train_values = train_epoch(
                    model,
                    train_loader,
                    optimizer,
                    self.device,
                    replay_loader=replay_loader,
                    replay_fraction=float(settings.get("replay_fraction", 0.0)),
                )
                global_updates += len(train_loader)
                validation = evaluate(model, validation_loader, self.device)
                c_test = evaluate(model, c_test_loader, self.device)
                a_validation = evaluate(model, a_validation_loader, self.device)
                b_validation = evaluate(model, b_validation_loader, self.device)
                probe = evaluate(model, probe_loader, self.device)
                current_parameters = parameter_snapshot(model)
                disagreement, probe_gradient_norm = gradient_disagreement(
                    model, gradient_loader, self.device
                )
                fisher, fisher_count = diagonal_empirical_fisher_burden(
                    model,
                    fisher_loader,
                    previous_parameters,
                    self.device,
                    int(self.config["fisher_probe_size"]),
                )
                trunk_distance, head_distance = group_parameter_distance(
                    model, current_parameters, b_parameters
                )
                row = {
                    "timestamp_utc": utc_now(),
                    "phase": "C",
                    "phase_epoch": epoch,
                    "phase_global_updates": global_updates,
                    "phase_relative_step": global_updates,
                    "global_step": c_global_offset + global_updates,
                    "seed": seed,
                    "condition": condition,
                    "no_shift": False,
                    "model_id": "light_cnn",
                    "data_shift_id": self.shift_hash + "_label_rule",
                    "checkpoint_id": f"C{epoch}",
                    **train_values,
                    "validation_loss": validation.loss,
                    "validation_accuracy": validation.accuracy,
                    "validation_balanced_accuracy": validation.balanced_accuracy,
                    "A_accuracy": a_validation.accuracy,
                    "B_accuracy": b_validation.accuracy,
                    "C_accuracy": c_test.accuracy,
                    "C_balanced_accuracy": c_test.balanced_accuracy,
                    "C_changed_balanced_accuracy": c_test.changed_balanced_accuracy,
                    "C_unchanged_balanced_accuracy": c_test.unchanged_balanced_accuracy,
                    "C_test_loss": c_test.loss,
                    "predictive_entropy": probe.predictive_entropy,
                    "representation_coherence": probe.coherence,
                    "gradient_disagreement": disagreement,
                    "probe_gradient_norm": probe_gradient_norm,
                    "parameter_update_norm": parameter_distance(current_parameters, previous_parameters),
                    "parameter_distance_from_phase_start": parameter_distance(
                        current_parameters, b_parameters
                    ),
                    "predictive_KL_from_previous": predictive_kl(
                        previous_probe.probabilities, probe.probabilities
                    ),
                    "representation_drift_from_A": None,
                    "representation_velocity": 1.0
                    - linear_cka(previous_probe.representations, probe.representations),
                    "fisher_empirical_diag_burden": fisher,
                    "fisher_sample_count": fisher_count,
                    "trunk_parameter_distance_from_B": trunk_distance,
                    "head_parameter_distance_from_B": head_distance,
                }
                c_rows.append(row)
                append_jsonl(step_path, row)
                previous_parameters = current_parameters
                previous_probe = probe
        except ScientificFailure as exc:
            write_json(
                run_dir / "failure_record.json",
                {
                    "failure_type": "scientific",
                    "phase": "C",
                    "seed": seed,
                    "condition": condition,
                    "message": str(exc),
                    "timestamp_utc": utc_now(),
                },
            )
            raise

        c_epochs = [row for row in c_rows if int(row["phase_epoch"]) > 0]
        changed0 = float(row0["C_changed_balanced_accuracy"])
        all0 = float(row0["C_balanced_accuracy"])
        unchanged0 = float(row0["C_unchanged_balanced_accuracy"])
        q_changed = float(np.mean([row["C_changed_balanced_accuracy"] - changed0 for row in c_epochs]))
        q_all = float(np.mean([row["C_balanced_accuracy"] - all0 for row in c_epochs]))
        q_unchanged = float(
            np.mean([row["C_unchanged_balanced_accuracy"] - unchanged0 for row in c_epochs])
        )
        final_a_test = evaluate(model, a_test_loader, self.device)
        final_b_test = evaluate(model, b_test_loader, self.device)
        threshold_epoch = next(
            (int(row["phase_epoch"]) for row in c_epochs if row["C_changed_balanced_accuracy"] >= 0.60),
            None,
        )
        outcomes = {
            "seed": seed,
            "condition": condition,
            "Q_C_changed_AULC_gain": q_changed,
            "Q_C_all_AULC_gain": q_all,
            "Q_C_unchanged_AULC_change": q_unchanged,
            "C0_changed_balanced_accuracy": changed0,
            "C0_all_balanced_accuracy": all0,
            "C_final_changed_balanced_accuracy": float(c_epochs[-1]["C_changed_balanced_accuracy"]),
            "C_final_all_balanced_accuracy": float(c_epochs[-1]["C_balanced_accuracy"]),
            "C_final_loss": float(c_epochs[-1]["C_test_loss"]),
            "epochs_to_changed_accuracy_0_60": threshold_epoch,
            "A_final_test_balanced_accuracy": final_a_test.balanced_accuracy,
            "B_final_test_balanced_accuracy": final_b_test.balanced_accuracy,
            "C_train_loss_variance": float(np.var([row["train_loss"] for row in c_epochs])),
            "C_final_trunk_distance_from_B": float(c_epochs[-1]["trunk_parameter_distance_from_B"]),
            "C_final_head_distance_from_B": float(c_epochs[-1]["head_parameter_distance_from_B"]),
            "preC_sha256": pre_hash["sha256"],
            "preC_created_utc": pre_hash["created_utc"],
            "C_started_utc": c_started,
            "completed_utc": utc_now(),
        }
        if outcomes["preC_created_utc"] >= outcomes["C_started_utc"]:
            raise RuntimeError("Pre-C artifact timestamp does not precede C start")
        write_json(run_dir / "C_outcomes.json", outcomes, overwrite=not (run_dir / "C_outcomes.json").exists())
        rows = [json.loads(line) for line in step_path.read_text().splitlines()]
        pd.DataFrame(rows).to_parquet(run_dir / "step_metrics.parquet", index=False)
        torch.save(
            {"model": model.state_dict(), "optimizer": optimizer.state_dict()}, run_dir / "C_end.pt"
        )
        write_json(
            run_dir / "C_complete.json",
            {
                "seed": seed,
                "condition": condition,
                "completed_utc": utc_now(),
                "preC_sha256_verified": pre_hash["sha256"],
            },
        )
        return run_dir

    def run_full(self, seed: int, condition: str, force: bool = False) -> Path:
        started = time.perf_counter()
        run_dir = self.run_ab(seed, condition, no_shift=False, force=force)
        self.run_c(seed, condition, force=force)
        write_json(
            run_dir / "run_runtime.json",
            {
                "wall_seconds": time.perf_counter() - started,
                "device": str(self.device),
                "environment": environment_info(self.device),
            },
        )
        return run_dir


def compute_pilot_standardization(
    experiment_root: Path,
    pilot_root: Path,
    output_path: Path,
) -> dict[str, Any]:
    records = []
    for path in sorted(pilot_root.glob("seed_*__condition_*/preC_features.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("uses_c_data") is not False:
            raise RuntimeError(f"Pilot standardization rejected non-A/B record: {path}")
        records.append(record)
    if len(records) != 12:
        raise RuntimeError(f"Expected 12 pilot A/B records, got {len(records)}")
    keys = [
        "log1p_d_repr_peak",
        "log1p_d_grad_peak",
        "r_grad",
        "v_late",
        "a_B",
        "n_B",
        "S_B",
    ]
    source_keys = {
        key: f"transform_{key}" for key in keys
    }
    features = {}
    for key in keys:
        values = np.asarray([record[source_keys[key]] for record in records], dtype=np.float64)
        median = float(np.median(values))
        mad = float(np.median(np.abs(values - median)))
        scale = float(1.4826 * mad + 1e-6)
        features[key] = {
            "median": median,
            "mad": mad,
            "scale": scale,
            "floor_used": bool(mad < 1e-6),
        }
    payload = {
        "created_utc": utc_now(),
        "source": "12 pilot A/B-only trajectories",
        "pilot_root": str(pilot_root),
        "c_files_read": False,
        "features": features,
    }
    write_json(output_path, payload, overwrite=True)
    payload["sha256"] = sha256_file(output_path)
    write_json(output_path, payload, overwrite=True)
    return payload


def compute_state_thresholds(
    no_shift_root: Path,
    output_path: Path,
    k: int = 8,
) -> dict[str, Any]:
    by_condition: dict[str, dict[str, list[float]]] = {}
    permutation_values: list[float] = []
    paths = sorted(no_shift_root.glob("seed_*__condition_*/preC_features.json"))
    if len(paths) != 20:
        raise RuntimeError(f"Expected 20 no-shift A/B records, got {len(paths)}")
    for path in paths:
        record = json.loads(path.read_text(encoding="utf-8"))
        condition = record["condition"]
        bucket = by_condition.setdefault(
            condition,
            {"d_repr_peak": [], "d_grad_peak": [], "v_late": [], "abs_loss_slope": []},
        )
        bucket["d_repr_peak"].append(float(record["d_repr_peak"]))
        bucket["d_grad_peak"].append(float(record["d_grad_peak"]))
        bucket["v_late"].append(float(record["v_late"]))
        bucket["abs_loss_slope"].append(abs(float(record["B_loss_slope_late"])))
        reps = np.load(path.parent / "AB_representations.npz")
        open_keys = sorted(
            [key for key in reps.files if key.startswith("B") and key not in {"B0"}],
            key=lambda value: int(value[1:]),
        )
        z_open = reps[open_keys[min(2, len(open_keys) - 1)]]
        z_stable = reps[open_keys[-1]]
        permutation_values.extend(
            temporal_permutation_overlaps(
                reps["A_end"], z_open, z_stable, k=k, permutations=100, seed=int(record["seed"])
            ).tolist()
        )
    thresholds = {
        condition: {
            key: float(np.quantile(values, 0.95)) for key, values in bucket.items()
        }
        for condition, bucket in by_condition.items()
    }
    payload = {
        "created_utc": utc_now(),
        "source": "20 no-shift A/B calibration trajectories",
        "condition_thresholds": thresholds,
        "selective_incorporation_permutation_p95": float(np.quantile(permutation_values, 0.95)),
        "B_adequacy_gain": 0.05,
        "B_adequacy_end_accuracy": 0.70,
        "uses_c_data": False,
    }
    write_json(output_path, payload, overwrite=True)
    payload["sha256"] = sha256_file(output_path)
    write_json(output_path, payload, overwrite=True)
    return payload


def create_formal_manifest(experiment_root: Path, config_path: Path) -> dict[str, Any]:
    config = load_yaml(config_path)
    required = [
        experiment_root / config["standardization_constants"],
        experiment_root / config["state_thresholds"],
        (experiment_root / config["spec_lock"]).resolve(),
        experiment_root / "manifests" / "dataset_splits.json",
        experiment_root / "manifests" / "probe_ids.json",
    ]
    for path in required:
        if not path.exists():
            raise FileNotFoundError(f"Cannot lock formal MVP; missing {path}")
    code_paths = list((experiment_root / "src").glob("*.py")) + list(
        (experiment_root / "scripts").glob("*.py")
    )
    payload = {
        "created_utc": utc_now(),
        "formal_c_results_existed_at_lock": any(
            (experiment_root / config["output_root"]).glob("*/C_outcomes.json")
        ),
        "git_sha": git_sha(experiment_root.parents[1]),
        "config": str(config_path),
        "config_sha256": sha256_file(config_path),
        "spec_sha256": sha256_file(required[2]),
        "standardization_sha256": sha256_file(required[0]),
        "state_thresholds_sha256": sha256_file(required[1]),
        "split_sha256": sha256_file(required[3]),
        "probe_sha256": sha256_file(required[4]),
        "code_tree_sha256": sha256_paths(code_paths, experiment_root),
        "seeds": config["seeds"],
        "conditions": config["conditions"],
    }
    if payload["formal_c_results_existed_at_lock"]:
        raise RuntimeError("Formal C result already exists before manifest lock")
    output = experiment_root / "manifests" / "formal_lock_manifest.json"
    write_json(output, payload, overwrite=False)
    payload["manifest_sha256"] = sha256_file(output)
    return payload
