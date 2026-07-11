from __future__ import annotations

import itertools
import json
from dataclasses import dataclass, fields
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from .b_paths import PATHS
from .utils import make_read_only, sha256_file, utc_now, write_json


@dataclass(frozen=True)
class BMatchInput:
    seed: int
    path: str
    epoch: int
    validation_balanced_accuracy: float
    validation_loss: float
    validation_ece: float
    previous_validation_balanced_accuracy: float
    previous_validation_loss: float
    previous_validation_ece: float
    checkpoint_path: str
    checkpoint_sha256: str
    state_dict_sha256: str


def assert_b_only_schema() -> None:
    names = {field.name.lower() for field in fields(BMatchInput)}
    forbidden = [name for name in names if name.startswith("c_") or "future" in name or name.startswith("q_")]
    if forbidden:
        raise AssertionError(f"Future field leaked into BMatchInput: {forbidden}")


def stable_candidates(trajectory: pd.DataFrame, config: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    assert_b_only_schema()
    matching = config["matching"]
    adequacy = matching["adequacy"]
    stability = matching["consecutive_stability"]
    result: dict[str, list[dict[str, Any]]] = {path: [] for path in PATHS}
    for path in PATHS:
        subset = trajectory[trajectory["path"] == path].sort_values("epoch")
        rows = {int(row.epoch): row for row in subset.itertuples()}
        for epoch in range(int(matching["candidate_epoch_min"]), int(matching["candidate_epoch_max"]) + 1):
            if epoch not in rows or epoch - 1 not in rows:
                continue
            current = rows[epoch]
            previous = rows[epoch - 1]
            adequate = all(
                [
                    current.validation_balanced_accuracy >= float(adequacy["accuracy_min"]),
                    previous.validation_balanced_accuracy >= float(adequacy["accuracy_min"]),
                    current.validation_loss <= float(adequacy["nll_max"]),
                    previous.validation_loss <= float(adequacy["nll_max"]),
                    current.validation_ece <= float(adequacy["ece_max"]),
                    previous.validation_ece <= float(adequacy["ece_max"]),
                ]
            )
            stable = all(
                [
                    abs(current.validation_balanced_accuracy - previous.validation_balanced_accuracy)
                    <= float(stability["accuracy_delta_max"]),
                    abs(current.validation_loss - previous.validation_loss)
                    <= float(stability["nll_delta_max"]),
                    abs(current.validation_ece - previous.validation_ece)
                    <= float(stability["ece_delta_max"]),
                ]
            )
            if adequate and stable:
                result[path].append(current._asdict())
    return result


def select_matched_group(seed: int, trajectory: pd.DataFrame, config: dict[str, Any]) -> list[dict[str, Any]]:
    candidates = stable_candidates(trajectory, config)
    if any(not candidates[path] for path in PATHS):
        return []
    tolerance = config["matching"]["group_tolerance"]
    valid = []
    for items in itertools.product(*(candidates[path] for path in PATHS)):
        accuracies = [float(row["validation_balanced_accuracy"]) for row in items]
        losses = [float(row["validation_loss"]) for row in items]
        eces = [float(row["validation_ece"]) for row in items]
        ranges = {
            "accuracy_range": max(accuracies) - min(accuracies),
            "nll_range": max(losses) - min(losses),
            "ece_range": max(eces) - min(eces),
        }
        if (
            ranges["accuracy_range"] <= float(tolerance["accuracy_range_max"])
            and ranges["nll_range"] <= float(tolerance["nll_range_max"])
            and ranges["ece_range"] <= float(tolerance["ece_range_max"])
        ):
            normalized = (
                ranges["accuracy_range"] / float(tolerance["accuracy_range_max"])
                + ranges["nll_range"] / float(tolerance["nll_range_max"])
                + ranges["ece_range"] / float(tolerance["ece_range_max"])
            )
            epochs = tuple(int(row["epoch"]) for row in items)
            key = (max(epochs), normalized, sum(epochs), epochs)
            valid.append((key, items, ranges, normalized))
    if not valid:
        return []
    _, items, ranges, normalized = min(valid, key=lambda item: item[0])
    selected = []
    epoch_range = max(int(row["epoch"]) for row in items) - min(int(row["epoch"]) for row in items)
    representation_range = max(float(row["representation_drift_from_A"]) for row in items) - min(
        float(row["representation_drift_from_A"]) for row in items
    )
    for path, row in zip(PATHS, items, strict=True):
        record = dict(row)
        record.update(
            {
                "seed": seed,
                "path": path,
                **ranges,
                "normalized_group_distance": normalized,
                "selected_epoch_range": epoch_range,
                "selected_representation_drift_range": representation_range,
                "uses_future_data": False,
                "selected_utc": utc_now(),
            }
        )
        selected.append(record)
    return selected


def freeze_matching_outputs(
    experiment_root: Path,
    stage: str,
    matched: pd.DataFrame,
    balance: pd.DataFrame,
) -> dict[str, Any]:
    if any("future" in column.lower() or column.lower().startswith("c_") or column.lower().startswith("q_") for column in matched.columns):
        allowed = {"uses_future_data"}
        bad = [
            column
            for column in matched.columns
            if ("future" in column.lower() or column.lower().startswith("c_") or column.lower().startswith("q_"))
            and column not in allowed
        ]
        if bad:
            raise ValueError(f"Future data fields supplied to matching freeze: {bad}")
    output_root = experiment_root / "outputs" / stage
    output_root.mkdir(parents=True, exist_ok=True)
    matched_path = output_root / "matched_B_checkpoints.parquet"
    balance_path = output_root / "endpoint_balance.csv"
    hash_path = output_root / "matching_freeze.json"
    if matched_path.exists() or hash_path.exists():
        raise FileExistsError("Matching outputs are already frozen")
    matched.to_parquet(matched_path, index=False)
    balance.to_csv(balance_path, index=False)
    payload = {
        "stage": stage,
        "created_utc": utc_now(),
        "uses_future_data": False,
        "matched_sha256": sha256_file(matched_path),
        "balance_sha256": sha256_file(balance_path),
        "matched_groups": int(matched["seed"].nunique()) if len(matched) else 0,
    }
    write_json(hash_path, payload, overwrite=False)
    for path in [matched_path, balance_path, hash_path]:
        make_read_only(path)
    return payload


def verify_matching_freeze(output_root: Path) -> dict[str, Any]:
    record = json.loads((output_root / "matching_freeze.json").read_text())
    if sha256_file(output_root / "matched_B_checkpoints.parquet") != record["matched_sha256"]:
        raise RuntimeError("Matched checkpoint table hash mismatch")
    if sha256_file(output_root / "endpoint_balance.csv") != record["balance_sha256"]:
        raise RuntimeError("Endpoint balance table hash mismatch")
    if record.get("uses_future_data") is not False:
        raise RuntimeError("Matching freeze does not certify A/B-only input")
    return record
