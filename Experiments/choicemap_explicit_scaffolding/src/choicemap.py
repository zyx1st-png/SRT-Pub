"""Explicit ChoiceMap candidate records, dominance filtering, and commitment gate."""
from __future__ import annotations

from dataclasses import dataclass, asdict
import math
from typing import Iterable


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    action_sequence: tuple[str, ...]
    expected_current_return: float
    worst_case_current_return: float
    estimated_information_gain: float
    estimated_resource_cost: float
    irreversibility_level: int
    estimated_local_option_loss: float
    regime_support: tuple[float, ...]
    is_probe: bool
    is_commitment: bool

    def to_log(self) -> dict:
        row = asdict(self)
        row["action_sequence"] = "|".join(self.action_sequence)
        row["regime_support"] = "|".join(f"{x:.8f}" for x in self.regime_support)
        return row


def entropy(probabilities: Iterable[float]) -> float:
    return -sum(p * math.log(p) for p in probabilities if p > 0)


def posterior_from_observations(observations: tuple[int, ...], reliability: float = 0.78,
                                regime_count: int = 3) -> tuple[float, ...]:
    weights = [1.0 / regime_count] * regime_count
    for obs in observations:
        for z in range(regime_count):
            weights[z] *= reliability if z == obs else (1.0 - reliability) / (regime_count - 1)
        total = sum(weights)
        weights = [w / total for w in weights]
    return tuple(weights)


def dominates(a: Candidate, b: Candidate) -> bool:
    higher_a = (a.expected_current_return, a.worst_case_current_return, a.estimated_information_gain)
    higher_b = (b.expected_current_return, b.worst_case_current_return, b.estimated_information_gain)
    lower_a = (a.estimated_resource_cost, a.irreversibility_level, a.estimated_local_option_loss)
    lower_b = (b.estimated_resource_cost, b.irreversibility_level, b.estimated_local_option_loss)
    no_worse = all(x >= y for x, y in zip(higher_a, higher_b)) and all(x <= y for x, y in zip(lower_a, lower_b))
    strictly = any(x > y for x, y in zip(higher_a, higher_b)) or any(x < y for x, y in zip(lower_a, lower_b))
    return no_worse and strictly


def non_dominated(candidates: list[Candidate]) -> list[Candidate]:
    return [c for c in candidates if not any(dominates(other, c) for other in candidates if other != c)]


def commitment_blocked(candidate: Candidate, posterior: tuple[float, ...], entropy_threshold: float,
                       top_gap_threshold: float, downside_threshold: float) -> bool:
    if not candidate.is_commitment or candidate.irreversibility_level < 2:
        return False
    ranked = sorted(posterior, reverse=True)
    action_disagreement = sum(p > 0.10 for p in posterior) > 1
    downside = candidate.expected_current_return - candidate.worst_case_current_return
    return (
        entropy(posterior) > entropy_threshold
        or ranked[0] - ranked[1] < top_gap_threshold
        or action_disagreement
        or downside > downside_threshold
    )

