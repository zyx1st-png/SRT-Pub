from __future__ import annotations

import hashlib
import json
from typing import Mapping

import torch
import torch.nn.functional as F


def deterministic_texture(
    index: int,
    seed: int,
    lowres: int = 7,
    size: int = 28,
) -> torch.Tensor:
    generator = torch.Generator(device="cpu")
    mixed_seed = (int(seed) * 1_000_003 + int(index) * 97_409) % (2**63 - 1)
    generator.manual_seed(mixed_seed)
    low = torch.rand((1, 1, lowres, lowres), generator=generator)
    texture = F.interpolate(low, size=(size, size), mode="bilinear", align_corners=False)
    return texture[0]


def apply_background_shift(
    image: torch.Tensor,
    index: int,
    seed: int,
    lowres: int,
    amplitude: float,
    mask_threshold: float,
) -> torch.Tensor:
    texture = deterministic_texture(index=index, seed=seed, lowres=lowres, size=image.shape[-1])
    mask = (image < mask_threshold).to(image.dtype)
    shifted = image + amplitude * texture * mask
    return shifted.clamp_(0.0, 1.0)


def precompute_background_shift_uint8(
    images_uint8: torch.Tensor,
    indices: torch.Tensor,
    seed: int,
    lowres: int,
    amplitude: float,
    mask_threshold: float,
    chunk_size: int = 1024,
) -> torch.Tensor:
    """Vectorized, deterministic cache equivalent in role to per-index texture generation."""
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
            low, size=(images_uint8.shape[-2], images_uint8.shape[-1]), mode="bilinear", align_corners=False
        )
        image = images_uint8[start:stop].to(torch.float32).unsqueeze(1) / 255.0
        mask = (image < mask_threshold).to(image.dtype)
        shifted = torch.clamp(image + amplitude * texture * mask, 0.0, 1.0)
        outputs.append(torch.round(shifted * 255.0).to(torch.uint8).squeeze(1))
    return torch.cat(outputs, dim=0)


def remap_label(label: int, label_map: Mapping[int, int] | Mapping[str, int]) -> int:
    if label in label_map:
        return int(label_map[label])
    key = str(label)
    return int(label_map.get(key, label))


def shift_definition_hash(shift_config: dict) -> str:
    payload = json.dumps(shift_config, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()
