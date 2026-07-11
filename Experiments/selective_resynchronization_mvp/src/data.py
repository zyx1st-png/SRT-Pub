from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision.datasets import FashionMNIST

from .shifts import apply_background_shift, precompute_background_shift_uint8, remap_label
from .utils import canonical_json, sha256_bytes, sha256_file, write_json


PARTITIONS = ("train", "validation", "probe", "test")


@dataclass(frozen=True)
class DataArtifacts:
    split_manifest: Path
    probe_manifest: Path
    split_hash: str
    probe_hash: str


class FashionPhaseDataset(Dataset):
    def __init__(
        self,
        base: FashionMNIST,
        indices: Iterable[int],
        phase: str,
        partition: str,
        shift_config: dict[str, Any],
        no_shift: bool = False,
        shift_cache_root: Path | None = None,
    ) -> None:
        self.base = base
        self.indices = np.asarray(list(indices), dtype=np.int64)
        self.phase = phase
        self.partition = partition
        self.shift_config = shift_config
        self.no_shift = no_shift
        self.shifted_data: torch.Tensor | None = None
        if self.phase in {"B", "C"} and not self.no_shift and shift_cache_root is not None:
            cache_payload = {
                "generator_version": shift_config.get("generator_version", "hashed_lcg_v1"),
                "partition": partition,
                "indices": self.indices.tolist(),
                "seed": int(shift_config["texture_seeds"][partition]),
                "lowres": int(shift_config["lowres"]),
                "amplitude": float(shift_config["amplitude"]),
                "mask_threshold": float(shift_config["mask_threshold"]),
            }
            cache_key = sha256_bytes(canonical_json(cache_payload).encode())[:20]
            shift_cache_root.mkdir(parents=True, exist_ok=True)
            cache_path = shift_cache_root / f"{partition}_{cache_key}.pt"
            if cache_path.exists():
                self.shifted_data = torch.load(cache_path, map_location="cpu", weights_only=True)
            else:
                self.shifted_data = precompute_background_shift_uint8(
                    images_uint8=self.base.data[self.indices],
                    indices=torch.as_tensor(self.indices, dtype=torch.int64),
                    seed=int(shift_config["texture_seeds"][partition]),
                    lowres=int(shift_config["lowres"]),
                    amplitude=float(shift_config["amplitude"]),
                    mask_threshold=float(shift_config["mask_threshold"]),
                )
                torch.save(self.shifted_data, cache_path)

    def __len__(self) -> int:
        return int(self.indices.size)

    def __getitem__(self, offset: int):
        index = int(self.indices[offset])
        if self.shifted_data is not None:
            image = self.shifted_data[offset].to(torch.float32).unsqueeze(0) / 255.0
        else:
            image = self.base.data[index].to(torch.float32).unsqueeze(0) / 255.0
        label = int(self.base.targets[index])
        if self.phase in {"B", "C"} and not self.no_shift and self.shifted_data is None:
            seed = int(self.shift_config["texture_seeds"][self.partition])
            image = apply_background_shift(
                image=image,
                index=index,
                seed=seed,
                lowres=int(self.shift_config["lowres"]),
                amplitude=float(self.shift_config["amplitude"]),
                mask_threshold=float(self.shift_config["mask_threshold"]),
            )
        if self.phase == "C":
            label = remap_label(label, self.shift_config["label_map"])
        return image, label, index


def _stratified_take(indices: np.ndarray, labels: np.ndarray, count: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    per_class = count // 10
    remainder = count % 10
    selected: list[int] = []
    for cls in range(10):
        candidates = indices[labels[indices] == cls].copy()
        rng.shuffle(candidates)
        take = per_class + (1 if cls < remainder else 0)
        selected.extend(candidates[:take].tolist())
    rng.shuffle(selected)
    return np.asarray(selected, dtype=np.int64)


def prepare_data(
    experiment_root: Path,
    config: dict[str, Any],
    download: bool = True,
) -> tuple[FashionMNIST, FashionMNIST, dict[str, np.ndarray], dict[str, np.ndarray], DataArtifacts]:
    data_root = experiment_root / config["data_root"]
    manifest_root = experiment_root / "manifests"
    manifest_root.mkdir(parents=True, exist_ok=True)
    split_manifest = manifest_root / "dataset_splits.json"
    probe_manifest = manifest_root / "probe_ids.json"

    train_base = FashionMNIST(root=data_root, train=True, download=download)
    test_base = FashionMNIST(root=data_root, train=False, download=download)
    train_labels = np.asarray(train_base.targets, dtype=np.int64)
    test_labels = np.asarray(test_base.targets, dtype=np.int64)

    if not split_manifest.exists():
        rng = np.random.default_rng(int(config["split_seed"]))
        split: dict[str, list[int]] = {"train": [], "validation": [], "probe": []}
        for cls in range(10):
            cls_indices = np.flatnonzero(train_labels == cls)
            rng.shuffle(cls_indices)
            split["train"].extend(cls_indices[:5000].tolist())
            split["validation"].extend(cls_indices[5000:5800].tolist())
            split["probe"].extend(cls_indices[5800:6000].tolist())
        for key in split:
            split[key] = sorted(split[key])
        split["test"] = list(range(len(test_base)))
        write_json(split_manifest, split, overwrite=False)
    split_raw = __import__("json").loads(split_manifest.read_text(encoding="utf-8"))
    splits = {key: np.asarray(value, dtype=np.int64) for key, value in split_raw.items()}

    limits = config.get("limits", {})
    if limits:
        for key in PARTITIONS:
            limit = int(limits.get(key, len(splits[key])))
            labels = test_labels if key == "test" else train_labels
            if limit < len(splits[key]):
                splits[key] = _stratified_take(
                    splits[key], labels, limit, int(config["split_seed"]) + len(key)
                )

    if not probe_manifest.exists():
        metric_ids = _stratified_take(
            np.asarray(split_raw["probe"], dtype=np.int64),
            train_labels,
            int(config.get("probe_size", 256)),
            int(config["split_seed"]) + 901,
        )
        fisher_ids = _stratified_take(
            metric_ids,
            train_labels,
            int(config.get("fisher_probe_size", 20)),
            int(config["split_seed"]) + 902,
        )
        write_json(
            probe_manifest,
            {"metric_probe": metric_ids.tolist(), "fisher_probe": fisher_ids.tolist()},
            overwrite=False,
        )
    probe_raw = __import__("json").loads(probe_manifest.read_text(encoding="utf-8"))
    probes = {key: np.asarray(value, dtype=np.int64) for key, value in probe_raw.items()}

    full_probe_set = set(split_raw["probe"])
    if not set(probes["metric_probe"]).issubset(full_probe_set):
        raise RuntimeError("Metric probe IDs are not contained in the locked probe partition")
    if set(splits["train"]) & set(split_raw["validation"]):
        raise RuntimeError("Training and validation partitions overlap")

    artifacts = DataArtifacts(
        split_manifest=split_manifest,
        probe_manifest=probe_manifest,
        split_hash=sha256_file(split_manifest),
        probe_hash=sha256_file(probe_manifest),
    )
    return train_base, test_base, splits, probes, artifacts


def phase_dataset(
    train_base: FashionMNIST,
    test_base: FashionMNIST,
    splits: dict[str, np.ndarray],
    probes: dict[str, np.ndarray],
    phase: str,
    partition: str,
    shift_config: dict[str, Any],
    no_shift: bool = False,
    fisher: bool = False,
    shift_cache_root: Path | None = None,
) -> FashionPhaseDataset:
    base = test_base if partition == "test" else train_base
    if partition == "probe":
        indices = probes["fisher_probe" if fisher else "metric_probe"]
    else:
        indices = splits[partition]
    return FashionPhaseDataset(
        base=base,
        indices=indices,
        phase=phase,
        partition=partition,
        shift_config=shift_config,
        no_shift=no_shift,
        shift_cache_root=shift_cache_root,
    )


def make_loader(
    dataset: Dataset,
    batch_size: int,
    shuffle: bool,
    seed: int,
    num_workers: int = 0,
) -> DataLoader:
    generator = torch.Generator(device="cpu")
    generator.manual_seed(int(seed))
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        generator=generator,
        drop_last=False,
        persistent_workers=bool(num_workers),
    )
