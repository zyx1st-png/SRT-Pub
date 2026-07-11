from __future__ import annotations

import json
import shutil
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch

from .b_paths import PATHS, build_optimizer, configure_path, train_epoch
from .data import DataManager
from .endpoint_matching import freeze_matching_outputs, select_matched_group
from .metrics import (
    diagonal_empirical_fisher_burden,
    evaluate,
    gradient_disagreement,
    linear_cka,
    parameter_distance,
    parameter_snapshot,
)
from .models import build_model, unfreeze_all
from .utils import (
    append_jsonl,
    choose_device,
    environment_info,
    load_yaml,
    set_global_seed,
    sha256_file,
    state_dict_sha256,
    utc_now,
    write_json,
)


class MatchedPathRunner:
    def __init__(self, experiment_root: Path, config_path: Path, device: str | None = None) -> None:
        self.root = experiment_root.resolve()
        self.config_path = config_path.resolve()
        self.config = load_yaml(self.config_path)
        if device is not None:
            self.config["device"] = device
        self.device = choose_device(str(self.config.get("device", "auto")))
        self.output_root = (self.root / self.config["output_root"]).resolve()
        self.output_root.mkdir(parents=True, exist_ok=True)
        self.data = DataManager(self.root, self.config)

    def _a_dir(self, seed: int) -> Path:
        return self.output_root / "A" / f"seed_{seed}"

    def _b_dir(self, seed: int, path: str) -> Path:
        return self.output_root / "B" / f"seed_{seed}__path_{path}"

    def ensure_a(self, seed: int) -> Path:
        output = self._a_dir(seed)
        checkpoint_path = output / "A_end.pt"
        if checkpoint_path.exists():
            return output
        output.mkdir(parents=True, exist_ok=True)
        set_global_seed(seed)
        model = build_model().to(self.device)
        optimizer = build_optimizer(model, self.config["training"]["A"])
        train_loader = self.data.loader("A", "train", seed + 11, shuffle=True)
        validation_loader = self.data.loader("A", "validation", seed + 12)
        probe_loader = self.data.loader("A", "probe", seed + 13)
        updates = 0
        for epoch in range(1, int(self.config["epochs"]["A"]) + 1):
            train_values = train_epoch(model, train_loader, optimizer, self.device)
            updates += len(train_loader)
            validation = evaluate(model, validation_loader, self.device)
            append_jsonl(
                output / "A_metrics.jsonl",
                {
                    "seed": seed,
                    "epoch": epoch,
                    "updates": updates,
                    **train_values,
                    "validation_balanced_accuracy": validation.balanced_accuracy,
                    "validation_loss": validation.loss,
                    "validation_ece": validation.ece,
                    "timestamp_utc": utc_now(),
                },
            )
        probe = evaluate(model, probe_loader, self.device)
        state = model.state_dict()
        tensor_hash = state_dict_sha256(state)
        torch.save(
            {
                "model": state,
                "seed": seed,
                "epoch": int(self.config["epochs"]["A"]),
                "state_dict_sha256": tensor_hash,
            },
            checkpoint_path,
        )
        np.savez_compressed(output / "A_probe.npz", representations=probe.representations)
        summary = {
            "seed": seed,
            "checkpoint_path": str(checkpoint_path),
            "checkpoint_sha256": sha256_file(checkpoint_path),
            "state_dict_sha256": tensor_hash,
            "validation_balanced_accuracy": validation.balanced_accuracy,
            "validation_loss": validation.loss,
            "validation_ece": validation.ece,
            "probe_effective_rank": probe.effective_rank,
            "updates": updates,
            "device": str(self.device),
            "created_utc": utc_now(),
        }
        write_json(output / "A_summary.json", summary, overwrite=False)
        return output

    def run_b_path(self, seed: int, path: str) -> Path:
        if path not in PATHS:
            raise ValueError(path)
        output = self._b_dir(seed, path)
        complete = output / "B_complete.json"
        if complete.exists():
            return output
        output.mkdir(parents=True, exist_ok=True)
        a_dir = self.ensure_a(seed)
        a_checkpoint = torch.load(a_dir / "A_end.pt", map_location=self.device, weights_only=False)
        set_global_seed(seed)
        model = build_model().to(self.device)
        model.load_state_dict(a_checkpoint["model"])
        if state_dict_sha256(model.state_dict()) != a_checkpoint["state_dict_sha256"]:
            raise RuntimeError("Shared A state hash mismatch before B branching")
        a_parameters = parameter_snapshot(model)
        configure_path(model, path, seed)
        previous_parameters = parameter_snapshot(model)
        optimizer = build_optimizer(model, self.config["training"]["B"])
        train_loader = self.data.loader("B", "train", seed + 101, shuffle=True)
        validation_loader = self.data.loader("B", "validation", seed + 102)
        probe_loader = self.data.loader("B", "probe", seed + 103)
        gradient_loader = self.data.loader("B", "probe", seed + 104, batch_size=64)
        a_validation_loader = self.data.loader("A", "validation", seed + 105)
        replay_loader = None
        if path == "replay_full":
            replay_loader = self.data.loader("A", "train", seed + 106, shuffle=True)
        a_probe = np.load(a_dir / "A_probe.npz")["representations"]
        trajectory_path = output / "trajectory.jsonl"
        updates = 0
        previous_probe = None
        for epoch in range(0, int(self.config["epochs"]["B_max"]) + 1):
            if epoch == 0:
                train_values = {
                    "train_loss": None,
                    "train_gradient_norm": 0.0,
                    "learning_rate": float(self.config["training"]["B"]["lr"]),
                    "batches": 0,
                }
            else:
                train_values = train_epoch(
                    model,
                    train_loader,
                    optimizer,
                    self.device,
                    replay_loader=replay_loader,
                    replay_fraction=float(self.config["training"].get("replay_fraction", 0.0))
                    if replay_loader is not None
                    else 0.0,
                )
                updates += len(train_loader)
            validation = evaluate(model, validation_loader, self.device)
            probe = evaluate(model, probe_loader, self.device)
            a_validation = evaluate(model, a_validation_loader, self.device)
            disagreement, probe_gradient_norm = gradient_disagreement(model, gradient_loader, self.device)
            current_parameters = parameter_snapshot(model)
            checkpoint_path = output / f"B{epoch}.pt"
            state = model.state_dict()
            tensor_hash = state_dict_sha256(state)
            torch.save(
                {
                    "model": state,
                    "seed": seed,
                    "path": path,
                    "epoch": epoch,
                    "updates": updates,
                    "shared_A_state_dict_sha256": a_checkpoint["state_dict_sha256"],
                    "state_dict_sha256": tensor_hash,
                },
                checkpoint_path,
            )
            row = {
                "seed": seed,
                "path": path,
                "epoch": epoch,
                "updates": updates,
                "shared_A_state_dict_sha256": a_checkpoint["state_dict_sha256"],
                "checkpoint_path": str(checkpoint_path),
                "checkpoint_sha256": sha256_file(checkpoint_path),
                "state_dict_sha256": tensor_hash,
                **train_values,
                "validation_balanced_accuracy": validation.balanced_accuracy,
                "validation_loss": validation.loss,
                "validation_ece": validation.ece,
                "A_validation_balanced_accuracy": a_validation.balanced_accuracy,
                "predictive_entropy": probe.predictive_entropy,
                "representation_coherence": probe.representation_coherence,
                "effective_representation_rank": probe.effective_rank,
                "effective_rank_change_from_A": probe.effective_rank
                - float(json.loads((a_dir / "A_summary.json").read_text())["probe_effective_rank"]),
                "inactive_unit_ratio": probe.inactive_unit_ratio,
                "feature_reuse_CKA": linear_cka(a_probe, probe.representations),
                "representation_drift_from_A": 1.0 - linear_cka(a_probe, probe.representations),
                "gradient_disagreement": disagreement,
                "probe_gradient_norm": probe_gradient_norm,
                "parameter_update_norm": 0.0
                if epoch == 0
                else parameter_distance(current_parameters, previous_parameters),
                "parameter_distance_from_A": parameter_distance(current_parameters, a_parameters),
                "representation_velocity": 0.0
                if previous_probe is None
                else 1.0 - linear_cka(previous_probe.representations, probe.representations),
                "fisher_empirical_diag_burden": None,
                "uses_future_data": False,
                "timestamp_utc": utc_now(),
            }
            append_jsonl(trajectory_path, row)
            previous_parameters = current_parameters
            previous_probe = probe
        pd.DataFrame(
            [json.loads(line) for line in trajectory_path.read_text().splitlines()]
        ).to_parquet(output / "B_trajectory.parquet", index=False)
        write_json(
            complete,
            {
                "seed": seed,
                "path": path,
                "shared_A_state_dict_sha256": a_checkpoint["state_dict_sha256"],
                "uses_future_data": False,
                "completed_utc": utc_now(),
            },
            overwrite=False,
        )
        return output

    def run_ab(self) -> None:
        for seed in self.config["seeds"]:
            self.ensure_a(int(seed))
            for path in self.config["paths"]:
                print(f"AB seed={seed} path={path} device={self.device}", flush=True)
                started = time.perf_counter()
                try:
                    run_dir = self.run_b_path(int(seed), str(path))
                    write_json(
                        run_dir / "runtime.json",
                        {
                            "wall_seconds": time.perf_counter() - started,
                            "environment": environment_info(self.device),
                        },
                    )
                except Exception as error:
                    append_jsonl(
                        self.output_root / "failed_runs.jsonl",
                        {
                            "seed": seed,
                            "path": path,
                            "phase": "AB",
                            "error_type": type(error).__name__,
                            "message": str(error),
                            "timestamp_utc": utc_now(),
                        },
                    )
                    print(f"FAILED AB seed={seed} path={path}: {error}", flush=True)

    def _selected_fisher(self, selected: dict[str, Any]) -> tuple[float, int]:
        current_checkpoint = torch.load(selected["checkpoint_path"], map_location=self.device, weights_only=False)
        previous_path = Path(selected["checkpoint_path"]).parent / f"B{int(selected['epoch']) - 1}.pt"
        previous_checkpoint = torch.load(previous_path, map_location="cpu", weights_only=False)
        model = build_model().to(self.device)
        model.load_state_dict(current_checkpoint["model"])
        unfreeze_all(model)
        previous_parameters = [previous_checkpoint["model"][name].detach().cpu() for name, _ in model.named_parameters()]
        loader = self.data.loader("B", "probe", int(selected["seed"]) + 909, fisher=True, batch_size=20)
        return diagonal_empirical_fisher_burden(
            model,
            loader,
            previous_parameters,
            self.device,
            int(self.config["fisher_probe_size"]),
        )

    def collate_and_freeze(self, stage: str) -> dict[str, Any]:
        trajectories = []
        a_records = []
        for seed in self.config["seeds"]:
            a_records.append(json.loads((self._a_dir(int(seed)) / "A_summary.json").read_text()))
            for path in self.config["paths"]:
                trajectory_path = self._b_dir(int(seed), str(path)) / "B_trajectory.parquet"
                if trajectory_path.exists():
                    trajectories.append(pd.read_parquet(trajectory_path))
        if not trajectories:
            raise RuntimeError("No B trajectories are available")
        trajectory = pd.concat(trajectories, ignore_index=True)
        matched_rows = []
        balance_rows = []
        for seed in self.config["seeds"]:
            subset = trajectory[trajectory["seed"] == int(seed)].copy()
            selected = select_matched_group(int(seed), subset, self.config)
            if selected:
                for record in selected:
                    fisher, count = self._selected_fisher(record)
                    record["fisher_empirical_diag_burden"] = fisher
                    record["fisher_sample_count"] = count
                    matched_rows.append(record)
                first = selected[0]
                balance_rows.append(
                    {
                        "seed": seed,
                        "matched": True,
                        "accuracy_range": first["accuracy_range"],
                        "nll_range": first["nll_range"],
                        "ece_range": first["ece_range"],
                        "selected_epoch_range": first["selected_epoch_range"],
                        "selected_representation_drift_range": first[
                            "selected_representation_drift_range"
                        ],
                    }
                )
            else:
                balance_rows.append(
                    {
                        "seed": seed,
                        "matched": False,
                        "accuracy_range": None,
                        "nll_range": None,
                        "ece_range": None,
                        "selected_epoch_range": None,
                        "selected_representation_drift_range": None,
                    }
                )
        matched = pd.DataFrame(matched_rows)
        balance = pd.DataFrame(balance_rows)
        collated_root = self.root / "outputs" / stage
        collated_root.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(a_records).to_csv(collated_root / "A_checkpoint_manifest.csv", index=False)
        trajectory.to_parquet(collated_root / "B_trajectory_metrics.parquet", index=False)
        failed_path = self.output_root / "failed_runs.jsonl"
        failures = (
            [json.loads(line) for line in failed_path.read_text().splitlines()]
            if failed_path.exists()
            else []
        )
        pd.DataFrame(
            failures,
            columns=["seed", "path", "phase", "error_type", "message", "timestamp_utc"],
        ).to_csv(collated_root / "failed_runs.csv", index=False)
        freeze = freeze_matching_outputs(self.root, stage, matched, balance)
        diversity = balance[balance["matched"]].copy()
        diversity_valid = (
            (
                diversity["selected_epoch_range"]
                >= int(self.config["matching"]["diversity_epoch_range_min"])
            )
            | (
                diversity["selected_representation_drift_range"]
                >= float(self.config["matching"]["diversity_representation_range_min"])
            )
        )
        return {
            **freeze,
            "matched_seeds": balance.loc[balance["matched"], "seed"].astype(int).tolist(),
            "diversity_fraction": float(diversity_valid.mean()) if len(diversity) else 0.0,
            "failures": len(failures),
        }
