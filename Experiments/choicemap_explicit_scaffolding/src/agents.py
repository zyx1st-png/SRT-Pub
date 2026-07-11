"""All four main systems and five preregistered ablations."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .choicemap import Candidate, commitment_blocked, entropy, non_dominated, posterior_from_observations
from .environment import AgentView
from .search import generate_candidates


SYSTEMS = (
    "Greedy", "Search", "OptionScalar", "ChoiceMap",
    "C-noProbe", "C-noReversibility", "C-noBranchMemory",
    "C-immediateCommit", "C-scalarized",
)


@dataclass
class Decision:
    action: str
    node_expansions: int
    planning_calls: int
    posterior: tuple[float, ...]
    candidates: list[Candidate]
    non_dominated_ids: tuple[str, ...]
    blocked_commitments: tuple[str, ...]
    reactivated_count: int = 0


@dataclass
class Agent:
    system: str
    node_budget: int
    entropy_threshold: float
    top_gap_threshold: float
    downside_threshold: float
    min_probe_value: float
    scalar_option_weight: float
    scalar_weights: dict[str, float]
    branch_memory: dict[str, Candidate] = field(default_factory=dict)
    previous_observation_count: int = 0

    def decide(self, view: AgentView) -> Decision:
        observations = view.observations
        if self.system == "C-noBranchMemory" and len(observations) > self.previous_observation_count:
            observations = observations[-1:]
        posterior = posterior_from_observations(observations)
        self.previous_observation_count = len(view.observations)
        use_rev = self.system != "C-noReversibility"
        search = generate_candidates(view, posterior, self.node_budget, use_rev)
        candidates = search.candidates
        nd = non_dominated(candidates)

        if self.system == "Greedy":
            action = max(candidates, key=lambda c: (c.expected_current_return if not c.is_probe else -1, -ord(c.candidate_id[-1]) if c.candidate_id[-1].isdigit() else 0)).action_sequence[0]
            return Decision(action, search.node_expansions, 1, posterior, candidates, tuple(c.candidate_id for c in nd), ())
        if self.system == "Search":
            action = max(candidates, key=lambda c: (c.expected_current_return, c.candidate_id)).action_sequence[0]
            return Decision(action, search.node_expansions, 1, posterior, candidates, tuple(c.candidate_id for c in nd), ())
        if self.system == "OptionScalar":
            action = max(candidates, key=lambda c: (c.expected_current_return - self.scalar_option_weight * c.estimated_local_option_loss, c.candidate_id)).action_sequence[0]
            return Decision(action, search.node_expansions, 1, posterior, candidates, tuple(c.candidate_id for c in nd), ())

        if self.system in ("C-immediateCommit", "C-noReversibility"):
            viable = [c for c in candidates if not c.is_probe]
            action = max(viable, key=lambda c: (c.expected_current_return, c.candidate_id)).action_sequence[0]
            return Decision(action, search.node_expansions, 1, posterior, candidates, tuple(c.candidate_id for c in nd), ())

        if self.system == "C-scalarized":
            w = self.scalar_weights
            def score(c: Candidate) -> float:
                return (w["expected"] * c.expected_current_return + w["worst"] * c.worst_case_current_return
                        + w["info"] * c.estimated_information_gain - w["cost"] * c.estimated_resource_cost
                        - w["irreversibility"] * c.irreversibility_level - w["option_loss"] * c.estimated_local_option_loss)
            action = max(candidates, key=lambda c: (score(c), c.candidate_id)).action_sequence[0]
            return Decision(action, search.node_expansions, 1, posterior, candidates, tuple(c.candidate_id for c in nd), ())

        blocked = tuple(c.candidate_id for c in nd if commitment_blocked(
            c, posterior, self.entropy_threshold, self.top_gap_threshold, self.downside_threshold
        ))
        probes = [c for c in nd if c.is_probe]
        if self.system != "C-noProbe" and blocked and probes and view.step < view.max_steps - 1:
            best_probe = max(probes, key=lambda c: c.estimated_information_gain / max(c.estimated_resource_cost, 1e-9))
            if best_probe.estimated_information_gain / best_probe.estimated_resource_cost >= self.min_probe_value:
                return Decision(best_probe.action_sequence[0], search.node_expansions, 1, posterior, candidates,
                                tuple(c.candidate_id for c in nd), blocked)

        viable = [c for c in nd if c.candidate_id not in blocked and not c.is_probe]
        if not viable:
            viable = [c for c in candidates if not c.is_probe]
        acceptable = [c for c in viable if c.worst_case_current_return >= 0.90]
        if acceptable:
            viable = acceptable
        # Locked lexicographic rule: worst-case guard, irreversibility, expected return, cost, id.
        selected = min(viable, key=lambda c: (
            c.irreversibility_level,
            -c.expected_current_return,
            c.estimated_resource_cost,
            c.candidate_id,
        ))
        prior_ids = set(self.branch_memory)
        current_ids = {c.candidate_id for c in nd}
        reactivated = len((prior_ids & current_ids) - {selected.candidate_id})
        if self.system != "C-noBranchMemory":
            self.branch_memory.update({c.candidate_id: c for c in nd if c != selected})
        return Decision(selected.action_sequence[0], search.node_expansions, 1, posterior, candidates,
                        tuple(c.candidate_id for c in nd), blocked, reactivated)


def make_agent(system: str, config: dict[str, Any]) -> Agent:
    if system not in SYSTEMS:
        raise ValueError(system)
    return Agent(
        system=system,
        node_budget=int(config["compute"]["node_expansions_per_decision"]),
        entropy_threshold=float(config["choicemap"]["entropy_threshold"]),
        top_gap_threshold=float(config["choicemap"]["top_gap_threshold"]),
        downside_threshold=float(config["choicemap"]["downside_threshold"]),
        min_probe_value=float(config["choicemap"]["min_probe_value"]),
        scalar_option_weight=float(config["baselines"]["option_scalar_weight"]),
        scalar_weights=dict(config["ablations"]["scalar_weights"]),
    )

