"""Hidden-Regime Irreversible Resource World.

Private truth (regime, future task, exact reachability) never appears in AgentView.
"""
from __future__ import annotations

from dataclasses import dataclass
import random

from .environment_generator import WorldSpec
from .future_tasks import FutureTask, is_task_solvable, task_catalog


@dataclass(frozen=True)
class AgentView:
    family: str
    step: int
    max_steps: int
    resources: tuple[int, ...]
    closed_nodes: frozenset[int]
    observations: tuple[int, ...]
    legal_actions: tuple[str, ...]
    current_task_complete: bool


@dataclass(frozen=True)
class Transition:
    observation: int | None
    current_reward: float
    current_success: bool
    irreversible: bool
    wrong_commitment: bool
    done: bool


class HiddenRegimeWorld:
    def __init__(self, spec: WorldSpec, episode_seed: int, max_steps: int = 6):
        self.spec = spec
        self.max_steps = max_steps
        self._rng = random.Random(episode_seed)
        self._regime = spec.initial_regime
        self._future_task: FutureTask | None = None
        self.step_count = 0
        self.resources = [1, 1, 1]
        self.closed_nodes: set[int] = set()
        self.observations: list[int] = []
        self.current_task_complete = False
        self.current_success = False
        self.commitment_action: str | None = None
        self.wrong_commitment = False
        self.shifted = False
        self._catalog = task_catalog()

    def legal_actions(self) -> tuple[str, ...]:
        if self.current_task_complete or self.step_count >= self.max_steps:
            return ()
        return ("probe", "safe_route", "commit_0", "commit_1", "commit_2")

    def agent_view(self) -> AgentView:
        return AgentView(
            family=self.spec.family,
            step=self.step_count,
            max_steps=self.max_steps,
            resources=tuple(self.resources),
            closed_nodes=frozenset(self.closed_nodes),
            observations=tuple(self.observations),
            legal_actions=self.legal_actions(),
            current_task_complete=self.current_task_complete,
        )

    def _maybe_shift(self) -> None:
        # A single unannounced change happens after the first interaction.
        if self.spec.shifted_regime is not None and self.step_count >= 1 and not self.shifted:
            self._regime = self.spec.shifted_regime
            self.shifted = True

    def step(self, action: str) -> Transition:
        if action not in self.legal_actions():
            raise ValueError(f"illegal action: {action}")
        self._maybe_shift()
        self.step_count += 1
        if action == "probe":
            correct = self._rng.random() < self.spec.probe_reliability
            if correct:
                signal = self._regime
            else:
                signal = (self._regime + 1 + self._rng.randrange(2)) % 3
            self.observations.append(signal)
            return Transition(signal, -0.04, False, False, False, self.step_count >= self.max_steps)

        irreversible = action.startswith("commit_") and self.spec.irreversible
        wrong = False
        if action == "safe_route":
            success_probability = 0.88
        else:
            selected = int(action[-1])
            wrong = selected != self._regime
            success_probability = 0.99 if not wrong else 0.86
            self.commitment_action = action
            self.wrong_commitment = wrong
            if irreversible:
                if wrong:
                    # Wrong commitment consumes a unique resource and closes four targets.
                    self.resources[selected] = 0
                    start = 8 + ((selected * 2 + self._regime) % 5)
                    self.closed_nodes.update(8 + ((start - 8 + j) % 8) for j in range(4))
                else:
                    # Correct commitment still closes one future branch: it is genuinely irreversible.
                    self.closed_nodes.add(8 + ((selected * 2 + 1) % 8))
        self.current_success = self._rng.random() < success_probability
        self.current_task_complete = True
        self._future_task = self._catalog[self._rng.randrange(len(self._catalog))]
        return Transition(None, 1.0 if self.current_success else 0.0, self.current_success,
                          irreversible, wrong, True)

    def pad_interaction(self) -> None:
        """Consume an inert reserved interaction after decision completion.

        Padding makes the actual interaction count identical across systems and cannot
        alter observations, resources, reachability, reward, or task identity.
        """
        if not self.current_task_complete or self.step_count >= self.max_steps:
            raise RuntimeError("padding is legal only after completion and before budget exhaustion")
        self.step_count += 1

    def reveal_future_task(self) -> FutureTask:
        if not self.current_task_complete or self._future_task is None:
            raise RuntimeError("future task is hidden until current-task completion")
        return self._future_task

    def future_success(self) -> bool:
        return self.current_success and is_task_solvable(
            self.reveal_future_task(), tuple(self.resources), frozenset(self.closed_nodes)
        )

    def reachable_future_tasks(self) -> frozenset[str]:
        """Offline oracle. Runners call it only after an action for evaluation."""
        return frozenset(
            t.task_id for t in self._catalog
            if is_task_solvable(t, tuple(self.resources), frozenset(self.closed_nodes))
        )

    @property
    def oracle_initial_future_count(self) -> int:
        return len(self._catalog)
