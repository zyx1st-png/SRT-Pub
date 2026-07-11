from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from torchvision.datasets import FashionMNIST

from .utils import canonical_json, sha256_file, write_json


def precompute_background_shift_uint8(
    images_uint8: torch.Tensor,
    indices: torch.Tensor,
    seed: int,
    lowres: int,
    amplitude: float,
    mask_threshold: float,
    chunk_size: int = 1024,
) -> torch.Tensor:
    outputs = []
    cells = torch.arange(lowres * lowres, dtype=torch.int64).reshape(1, lowres, lowres)
    prime = 2_147_483_647
    for start in range(0, len(indices), chunk_size):
        stop = min(len(indices), start + chunk_size)
        idx = indices[start:stop].to(torch.int64).reshape(-1, 1, 1)
        hashed = torch.remainder(
            idx * 1_103_515_245 + cells * 12_345 + int(seed) * 2_654_435_761,
            prime,
        )
        low = hashed.to(torch.float32).unsqueeze(1) / float(prime)
        texture = F.interpolate(
            low,
            size=(images_uint8.shape[-2], images_uint8.shape[-1]),
            mode="bilinear",
            align_corners=False,
        )
        image = images_uint8[start:stop].to(torch.float32).unsqueeze(1) / 255.0
        mask = (image < mask_threshold).to(image.dtype)
        shifted = torch.clamp(image + amplitude * texture * mask, 0.0, 1.0)
        outputs.append(torch.round(shifted * 255.0).to(torch.uint8).squeeze(1))
    return torch.cat(outputs, dim=0)


class PhaseDataset(Dataset):
    def __init__(
        self,
        base: FashionMNIST,
        indices: Iterable[int],
        partition: str,
        shift_config: dict[str, Any],
        shifted: bool,
        cache_root: Path,
    ) -> None:
        self.base = base
        self.indices = np.asarray(list(indices), dtype=np.int64)
        self.partition = partition
        self.shift_config = shift_config
        self.shifted_data: torch.Tensor | None = None
        if shifted:
            payload = {
                "generator_version": shift_config["generator_version"],
                "partition": partition,
                "indices": self.indices.tolist(),
                "seed": int(shift_config["texture_seeds"][partition]),
                "lowres": int(shift_config["lowres"]),
                "amplitude": float(shift_config["amplitude"]),
                "mask_threshold": float(shift_config["mask_threshold"]),
            }
            key = __import__("hashlib").sha256(canonical_json(payload).encode()).hexdigest()[:20]
            cache_root.mkdir(parents=True, exist_ok=True)
            cache_path = cache_root / f"{partition}_{key}.pt"
            if cache_path.exists():
                self.shifted_data = torch.load(cache_path, map_location="cpu", weights_only=True)
            else:
                self.shifted_data = precompute_background_shift_uint8(
                    base.data[self.indices],
                    torch.as_tensor(self.indices),
                    int(shift_config["texture_seeds"][partition]),
                    int(shift_config["lowres"]),
                    float(shift_config["amplitude"]),
                    float(shift_config["mask_threshold"]),
                )
                torch.save(self.shifted_data, cache_path)

    def __len__(self) -> int:
        return len(self.indices)

    def __getitem__(self, offset: int):
        index = int(self.indices[offset])
        if self.shifted_data is None:
            image = self.base.data[index].float().unsqueeze(0) / 255.0
        else:
            image = self.shifted_data[offset].float().unsqueeze(0) / 255.0
        label = int(self.base.targets[index])
        return image, label, index, 1.0


class DataManager:
    def __init__(self, experiment_root: Path, config: dict[str, Any]) -> None:
        self.root = experiment_root
        self.config = config
        source_data = (experiment_root / config["source_data_root"]).resolve()
        self.train_base = FashionMNIST(source_data, train=True, download=True)
        self.test_base = FashionMNIST(source_data, train=False, download=True)
        source_split = (experiment_root / config["source_split_manifest"]).resolve()
        source_probe = (experiment_root / config["source_probe_manifest"]).resolve()
        manifest_root = experiment_root / "manifests"
        manifest_root.mkdir(parents=True, exist_ok=True)
        self.split_path = manifest_root / "dataset_splits.json"
        self.probe_path = manifest_root / "probe_ids.json"
        if not self.split_path.exists():
            write_json(self.split_path, json.loads(source_split.read_text()), overwrite=False)
        if not self.probe_path.exists():
            write_json(self.probe_path, json.loads(source_probe.read_text()), overwrite=False)
        if sha256_file(self.split_path) != sha256_file(source_split):
            raise RuntimeError("Copied split manifest differs from v1 source")
        if sha256_file(self.probe_path) != sha256_file(source_probe):
            raise RuntimeError("Copied probe manifest differs from v1 source")
        raw_splits = json.loads(self.split_path.read_text())
        raw_probes = json.loads(self.probe_path.read_text())
        self.splits = {key: np.asarray(value, dtype=np.int64) for key, value in raw_splits.items()}
        self.probes = {key: np.asarray(value, dtype=np.int64) for key, value in raw_probes.items()}
        self.cache_root = source_data / "shift_cache"
        self._cache: dict[tuple[str, str, bool], PhaseDataset] = {}

    def dataset(self, phase: str, partition: str, fisher: bool = False) -> PhaseDataset:
        key = (phase, partition, fisher)
        if key in self._cache:
            return self._cache[key]
        base = self.test_base if partition == "test" else self.train_base
        if partition == "probe":
            indices = self.probes["fisher_probe" if fisher else "metric_probe"]
        else:
            indices = self.splits[partition]
        dataset = PhaseDataset(
            base,
            indices,
            partition,
            self.config["shift"],
            shifted=phase == "B",
            cache_root=self.cache_root,
        )
        self._cache[key] = dataset
        return dataset

    def loader(
        self,
        phase: str,
        partition: str,
        seed: int,
        shuffle: bool = False,
        fisher: bool = False,
        batch_size: int | None = None,
    ) -> DataLoader:
        generator = torch.Generator(device="cpu").manual_seed(seed)
        return DataLoader(
            self.dataset(phase, partition, fisher=fisher),
            batch_size=batch_size or (int(self.config["batch_size"]) if partition == "train" else 256),
            shuffle=shuffle,
            generator=generator,
            num_workers=int(self.config.get("num_workers", 0)),
            drop_last=False,
        )
