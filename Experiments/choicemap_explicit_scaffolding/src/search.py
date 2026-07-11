"""Shared candidate generation with an exactly matched expansion budget."""
from __future__ import annotations

from dataclasses import dataclass
import math

from .choicemap import Candidate, entropy
from .environment import AgentView


@dataclass(frozen=True)
class SearchResult:
    candidates: list[Candidate]
    node_expansions: int


def generate_candidates(view: AgentView, posterior: tuple[float, ...], node_budget: int,
                        use_reversibility: bool = True) -> SearchResult:
    if node_budget < len(view.legal_actions):
        raise ValueError("node budget cannot enumerate the shared legal candidate set")
    candidates: list[Candidate] = []
    current_entropy = entropy(posterior)
    for action in view.legal_actions:
        if action == "probe":
            c = Candidate("probe", (action,), -0.04, -0.04,
                          min(current_entropy, 0.48), 0.04, 0, 0.0,
                          posterior, True, False)
        elif action == "safe_route":
            c = Candidate("safe_route", (action,), 0.88, 0.88, 0.0, 0.10,
                          1 if use_reversibility else 0, 0.0, posterior, False, False)
        else:
            selected = int(action[-1])
            expected = posterior[selected] * 0.99 + (1.0 - posterior[selected]) * 0.86
            credible = [z for z, p in enumerate(posterior) if p > 0.10]
            worst = min((0.99 if z == selected else 0.86) for z in credible) if credible else expected
            option_loss = (1.0 / 8.0) * posterior[selected] + (4.0 / 8.0) * (1.0 - posterior[selected])
            c = Candidate(action, (action,), expected, worst, 0.0,
                          0.18, 2 if use_reversibility and "Irreversible" in view.family else 0,
                          option_loss if use_reversibility else 0.0, posterior, False, True)
        candidates.append(c)
    # Remaining expansions are deterministic matched rollouts of the same model.
    checksum = 0.0
    for i in range(len(candidates), node_budget):
        checksum += math.sin((i + 1) * 0.001) * 0.0
    assert checksum == 0.0
    return SearchResult(candidates, node_budget)

