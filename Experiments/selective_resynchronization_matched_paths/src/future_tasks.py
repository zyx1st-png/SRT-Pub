from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms import InterpolationMode
from torchvision.transforms.functional import rotate

from .data import DataManager, PhaseDataset
from .metrics import Evaluation, balanced_accuracy


TASKS = [
    "rotation20",
    "class_imbalance_4to1",
    "partial_label_permutation",
    "parity_regrouping",
]
TASK_OFFSETS = {task: (index + 1) * 10_000 for index, task in enumerate(TASKS)}


class FutureDataset(Dataset):
    def __init__(
        self,
        base: PhaseDataset,
        task: str,
        partition: str,
        seed: int,
        future_config: dict[str, Any],
    ) -> None:
        if task not in TASKS:
            raise ValueError(task)
        self.base = base
        self.task = task
        self.partition = partition
        self.future_config = future_config
        rng = np.random.default_rng(seed + TASK_OFFSETS[task] + len(partition))
        offsets = np.arange(len(base), dtype=np.int64)
        if partition == "train" and task == "class_imbalance_4to1":
            labels = np.asarray([int(base.base.targets[int(index)]) for index in base.indices])
            high = set(int(value) for value in future_config["imbalance_low_classes"])
            weights = np.asarray(
                [
                    float(future_config["imbalance_high_weight"])
                    if int(label) in high
                    else float(future_config["imbalance_low_weight"])
                    for label in labels
                ],
                dtype=float,
            )
            weights /= weights.sum()
            offsets = rng.choice(offsets, size=len(offsets), replace=True, p=weights)
        elif partition == "train":
            offsets = rng.permutation(offsets)
        self.offsets = offsets
        self.data_order_hash = hashlib.sha256(offsets.tobytes()).hexdigest()

    def __len__(self) -> int:
        return len(self.offsets)

    def __getitem__(self, item: int):
        image, original_label, index, _ = self.base[int(self.offsets[item])]
        label = int(original_label)
        weight = 1.0
        if self.task == "rotation20":
            image = rotate(
                image,
                angle=float(self.future_config["rotation_degrees"]),
                interpolation=InterpolationMode.BILINEAR,
                fill=0.0,
            )
        elif self.task == "class_imbalance_4to1":
            high = set(int(value) for value in self.future_config["imbalance_low_classes"])
            raw_weight = (
                float(self.future_config["imbalance_high_weight"])
                if label in high
                else float(self.future_config["imbalance_low_weight"])
            )
            mean_weight = 0.5 * (
                float(self.future_config["imbalance_high_weight"])
                + float(self.future_config["imbalance_low_weight"])
            )
            weight = raw_weight / mean_weight
        elif self.task == "partial_label_permutation":
            mapping = self.future_config["label_map"]
            label = int(mapping.get(label, mapping.get(str(label), label)))
        elif self.task == "parity_regrouping":
            label = (
                int(self.future_config["parity_even_label"])
                if label % 2 == 0
                else int(self.future_config["parity_odd_label"])
            )
        return image, label, index, weight


def make_future_loader(
    data: DataManager,
    task: str,
    partition: str,
    seed: int,
    config: dict[str, Any],
) -> tuple[DataLoader, str]:
    dataset = FutureDataset(
        data.dataset("B", partition),
        task,
        partition,
        seed,
        config["future"],
    )
    loader = DataLoader(
        dataset,
        batch_size=int(config["batch_size"]) if partition == "train" else 256,
        shuffle=False,
        num_workers=int(config.get("num_workers", 0)),
        drop_last=False,
    )
    return loader, dataset.data_order_hash


def task_utility(task: str, evaluation: Evaluation) -> float:
    predictions = evaluation.probabilities.argmax(axis=1)
    if task == "class_imbalance_4to1":
        return -float(evaluation.loss)
    if task == "partial_label_permutation":
        return balanced_accuracy(evaluation.labels, predictions, classes=[0, 2, 4, 6])
    return float(evaluation.balanced_accuracy)


def task_threshold_reached(task: str, evaluation: Evaluation, threshold: float) -> bool:
    if task == "class_imbalance_4to1":
        return evaluation.loss <= threshold
    return task_utility(task, evaluation) >= threshold


def verify_future_branch_identity(records: list[dict[str, Any]]) -> None:
    if not records:
        raise ValueError("No future branch records")
    by_seed_task: dict[tuple[int, str], list[dict[str, Any]]] = {}
    for record in records:
        by_seed_task.setdefault((int(record["seed"]), record["future_task"]), []).append(record)
    for key, group in by_seed_task.items():
        if len({record["data_order_hash"] for record in group}) != 1:
            raise RuntimeError(f"Future data order differs across paths for {key}")
        if len({int(record["budget_updates"]) for record in group}) != 1:
            raise RuntimeError(f"Future budget differs across paths for {key}")
    for record in records:
        if record["branch_start_state_dict_sha256"] != record["matched_B_state_dict_sha256"]:
            raise RuntimeError("Future branch did not start from its frozen matched B state")


def future_definition_hash(config: dict[str, Any]) -> str:
    payload = {"tasks": config["future_tasks"], "future": config["future"], "epochs": config["epochs"]["future"]}
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
