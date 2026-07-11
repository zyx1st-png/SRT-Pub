"""Deterministic generator for the 16-node hidden-regime world."""
from __future__ import annotations

from dataclasses import dataclass
import random


FAMILIES = (
    "Stable-Reversible",
    "Hidden-Reversible",
    "Hidden-Irreversible",
    "Hidden-Irreversible-Shift",
)


@dataclass(frozen=True)
class WorldSpec:
    seed: int
    family: str
    node_count: int
    graph: dict[int, tuple[int, ...]]
    regime_count: int
    initial_regime: int
    shifted_regime: int | None
    probe_reliability: float
    irreversible: bool
    hidden: bool


def generate_world(seed: int, family: str, probe_reliability: float = 0.78) -> WorldSpec:
    if family not in FAMILIES:
        raise ValueError(f"unknown family: {family}")
    rng = random.Random(seed)
    # 0 start; 1-3 probes; 4-6 commitments; 7 current goal; 8-15 future targets.
    graph: dict[int, tuple[int, ...]] = {
        0: (1, 2, 3, 4, 5, 6),
        1: (0, 4), 2: (0, 5), 3: (0, 6),
        4: (7, 8, 9, 10), 5: (7, 11, 12, 13), 6: (7, 14, 15),
        7: tuple(range(8, 16)),
    }
    for node in range(8, 16):
        graph[node] = (7,)
    initial = rng.randrange(3)
    shifted = (initial + 1 + rng.randrange(2)) % 3 if family.endswith("Shift") else None
    return WorldSpec(
        seed=seed,
        family=family,
        node_count=16,
        graph=graph,
        regime_count=3,
        initial_regime=initial,
        shifted_regime=shifted,
        probe_reliability=(0.96 if family == "Stable-Reversible" else probe_reliability),
        irreversible=("Irreversible" in family),
        hidden=(family != "Stable-Reversible"),
    )

