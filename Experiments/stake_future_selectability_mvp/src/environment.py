from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import gymnasium as gym
from gymnasium import spaces
import numpy as np


ACTION_DELTAS = np.asarray([[-1, 0], [1, 0], [0, -1], [0, 1], [0, 0]], dtype=np.int64)
CHANNELS = {"wall": 0, "obstacle": 1, "resource": 2, "blue": 3, "green": 4, "hazard": 5, "agent": 6}


@dataclass(frozen=True)
class EnvSnapshot:
    phase: str
    integrity: float
    energy: float
    agent_id: str
    branch_id: str
    position: tuple[int, int]
    episode_index: int
    damaged_hazards: tuple[tuple[int, int], ...]


class PersistentChoiceGrid(gym.Env):
    """11x11 continuing-agent grid with conditionally coupled integrity.

    Stored integrity is always observable. Only effective integrity changes capability.
    Reward and ordinary energy formulas are condition-invariant.
    """

    metadata = {"render_modes": []}

    def __init__(
        self,
        config: dict[str, Any],
        *,
        master_seed: int,
        condition: str,
        severity: str,
        phase: str,
        agent_id: str,
        branch_id: str,
        evaluation: bool = False,
    ) -> None:
        super().__init__()
        self.config = config
        self.master_seed = int(master_seed)
        self.condition = condition
        self.severity = severity
        self.phase = phase
        self.agent_id = agent_id
        self.branch_id = branch_id
        self.evaluation = evaluation
        self.grid_size = int(config["grid_size"])
        self.view_size = int(config["view_size"])
        self.horizon = int(config["episode_horizon"])
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Dict(
            {
                "grid": spaces.Box(0.0, 1.0, shape=(len(CHANNELS), self.view_size, self.view_size), dtype=np.float32),
                "state": spaces.Box(-1.0, 1.0, shape=(9,), dtype=np.float32),
            }
        )
        self.np_random = np.random.default_rng(self.master_seed)
        self.integrity = 1.0
        self.energy = 1.0
        self.position = (1, 1)
        self.episode_steps = 0
        self.episode_index = 0
        self.cumulative_reward = 0.0
        self.hazard_contacts = 0
        self.damage_events = 0
        self.energy_deviation_area = 0.0
        self.replacement_events: list[dict[str, Any]] = []
        self.damaged_hazards: set[tuple[int, int]] = set()
        self._build_layout()

    @property
    def effective_integrity(self) -> float:
        if self.condition == "X":
            return 1.0
        return float(self.integrity)

    @property
    def energy_max(self) -> float:
        return self.effective_integrity

    @property
    def p_slip(self) -> float:
        return 0.02 + 0.25 * (1.0 - self.effective_integrity)

    @property
    def p_obs_dropout(self) -> float:
        return 0.30 * (1.0 - self.effective_integrity)

    def _build_layout(self) -> None:
        phase_offset = 0 if self.phase == "A" else 100_003
        rng = np.random.default_rng(self.master_seed + phase_offset)
        candidates = [(r, c) for r in range(1, self.grid_size - 1) for c in range(1, self.grid_size - 1)]
        rng.shuffle(candidates)
        self.obstacles = set(candidates[:12])
        remaining = [p for p in candidates[12:] if p not in self.obstacles]
        self.resources = set(remaining[:5])
        self.blue_target = remaining[5]
        self.green_target = remaining[6]
        if self.phase == "A":
            self.hazards: set[tuple[int, int]] = set()
        else:
            self.hazards = set(remaining[7 : 7 + int(self.config["hazard_count"])])

    def transition_phase(self, new_phase: str) -> dict[str, Any]:
        if (self.phase, new_phase) not in {("B", "C")}:
            raise RuntimeError(f"illegal phase transition {self.phase}->{new_phase}")
        before = self.integrity
        event = {
            "event": "phase_transition",
            "from": self.phase,
            "to": new_phase,
            "agent_id": self.agent_id,
            "branch_id": self.branch_id,
            "integrity_before": before,
            "replacement": False,
            "reset": False,
        }
        self.phase = new_phase
        self._build_layout()
        self.damaged_hazards = set()
        if self.condition == "T":
            self.integrity = 1.0
            self.energy = min(self.energy, self.energy_max)
            event["reset"] = True
            event["reset_reason"] = "preregistered_transferable_integrity_C_reset"
        event["integrity_after"] = self.integrity
        self.replacement_events.append(event)
        return event

    def _valid_positions(self) -> list[tuple[int, int]]:
        blocked = self.obstacles | {self.blue_target, self.green_target}
        return [(r, c) for r in range(1, self.grid_size - 1) for c in range(1, self.grid_size - 1) if (r, c) not in blocked]

    def reset(self, *, seed: int | None = None, options: dict[str, Any] | None = None):
        super().reset(seed=seed)
        if seed is not None:
            self.np_random = np.random.default_rng(seed)
        self.episode_steps = 0
        self.episode_index += 1
        valid = self._valid_positions()
        self.position = valid[int(self.np_random.integers(0, len(valid)))]
        self.energy = min(self.energy_max, max(0.35, self.energy))
        return self._observation(), self._info(success=False)

    def _movement_cost(self) -> float:
        base = float(self.config["movement_cost"][self.phase])
        if self.phase == "A":
            return base
        # Locked deterministic spatial distribution; identical in X/T/S.
        r, c = self.position
        multiplier = (0.8, 1.0, 1.25)[(r + 2 * c + self.master_seed) % 3]
        return base * multiplier

    def _target(self) -> tuple[int, int]:
        return self.green_target if self.phase == "C" else self.blue_target

    def _try_move(self, action: int) -> None:
        actual_action = int(action)
        if self.np_random.random() < self.p_slip:
            actual_action = int(self.np_random.integers(0, 5))
        if self.energy <= 1e-8:
            actual_action = 4
        delta = ACTION_DELTAS[actual_action]
        candidate = (self.position[0] + int(delta[0]), self.position[1] + int(delta[1]))
        if candidate in self.obstacles or not (1 <= candidate[0] < self.grid_size - 1 and 1 <= candidate[1] < self.grid_size - 1):
            candidate = self.position
        self.position = candidate

    def step(self, action: int):
        if not self.action_space.contains(action):
            raise ValueError(action)
        self._try_move(int(action))
        cost = self._movement_cost()
        self.energy = max(0.0, min(self.energy_max, self.energy - cost))
        reward = float(self.config["reward"]["step"])
        if self.position in self.resources:
            self.energy = min(self.energy_max, self.energy + float(self.config["resource_gain"]))
        if self.position in self.hazards:
            reward += float(self.config["reward"]["hazard"])
            self.hazard_contacts += 1
            if not self.evaluation and self.position not in self.damaged_hazards:
                delta = float(self.config["damage"][self.severity])
                self.integrity = max(0.5, self.integrity - delta)
                self.energy = min(self.energy, self.energy_max)
                self.damaged_hazards.add(self.position)
                self.damage_events += 1
        success = self.position == self._target()
        if success:
            reward += float(self.config["reward"]["target"])
        self.episode_steps += 1
        self.cumulative_reward += reward
        self.energy_deviation_area += 1.0 - self.energy
        terminated = bool(success)
        truncated = self.episode_steps >= self.horizon
        return self._observation(), reward, terminated, truncated, self._info(success=success)

    def _grid_channels(self, *, dropout: bool = True) -> np.ndarray:
        radius = self.view_size // 2
        out = np.zeros((len(CHANNELS), self.view_size, self.view_size), dtype=np.float32)
        for vr in range(self.view_size):
            for vc in range(self.view_size):
                gr = self.position[0] + vr - radius
                gc = self.position[1] + vc - radius
                loc = (gr, gc)
                if not (0 <= gr < self.grid_size and 0 <= gc < self.grid_size) or gr in {0, self.grid_size - 1} or gc in {0, self.grid_size - 1}:
                    out[CHANNELS["wall"], vr, vc] = 1.0
                elif loc in self.obstacles:
                    out[CHANNELS["obstacle"], vr, vc] = 1.0
                elif loc in self.resources:
                    out[CHANNELS["resource"], vr, vc] = 1.0
                if loc == self.blue_target:
                    out[CHANNELS["blue"], vr, vc] = 1.0
                if loc == self.green_target:
                    out[CHANNELS["green"], vr, vc] = 1.0
                if loc in self.hazards:
                    out[CHANNELS["hazard"], vr, vc] = 1.0
        out[CHANNELS["agent"], radius, radius] = 1.0
        if dropout and self.p_obs_dropout > 0:
            mask = self.np_random.random((self.view_size, self.view_size)) < self.p_obs_dropout
            mask[radius, radius] = False
            out[:, mask] = 0.0
        return out

    def _state_vector(self) -> np.ndarray:
        target = self._target()
        rel_r = np.clip((target[0] - self.position[0]) / (self.grid_size - 2), -1.0, 1.0)
        rel_c = np.clip((target[1] - self.position[1]) / (self.grid_size - 2), -1.0, 1.0)
        phases = [1.0 if self.phase == p else 0.0 for p in ("A", "B", "C")]
        severity = 0.0 if self.severity == "low" else 1.0
        target_context = 1.0 if self.phase == "C" else 0.0
        return np.asarray([self.energy, self.integrity, *phases, rel_r, rel_c, severity, target_context], dtype=np.float32)

    def _observation(self, *, clean: bool = False) -> dict[str, np.ndarray]:
        return {"grid": self._grid_channels(dropout=not clean), "state": self._state_vector()}

    def clean_observation(self) -> dict[str, np.ndarray]:
        return self._observation(clean=True)

    def _info(self, *, success: bool) -> dict[str, Any]:
        return {
            "success": success,
            "energy": float(self.energy),
            "integrity": float(self.integrity),
            "effective_integrity": float(self.effective_integrity),
            "hazard_contacts": int(self.hazard_contacts),
            "damage_events": int(self.damage_events),
            "agent_id": self.agent_id,
            "branch_id": self.branch_id,
            "phase": self.phase,
        }

    def snapshot(self) -> EnvSnapshot:
        return EnvSnapshot(
            phase=self.phase,
            integrity=float(self.integrity),
            energy=float(self.energy),
            agent_id=self.agent_id,
            branch_id=self.branch_id,
            position=self.position,
            episode_index=self.episode_index,
            damaged_hazards=tuple(sorted(self.damaged_hazards)),
        )

    def restore(self, snapshot: EnvSnapshot) -> None:
        if snapshot.agent_id != self.agent_id or snapshot.branch_id != self.branch_id:
            raise RuntimeError("identity mismatch during restore")
        self.phase = snapshot.phase
        self._build_layout()
        self.integrity = float(snapshot.integrity)
        self.energy = float(snapshot.energy)
        self.position = tuple(snapshot.position)
        self.episode_index = int(snapshot.episode_index)
        self.damaged_hazards = set(snapshot.damaged_hazards)

    def set_standardized_state(
        self,
        *,
        position: tuple[int, int],
        integrity: float,
        energy: float = 0.8,
        cap_energy: bool = True,
    ) -> None:
        self.position = position
        self.integrity = float(integrity)
        self.energy = min(float(energy), self.energy_max) if cap_energy else float(energy)
        self.episode_steps = 0


try:
    gym.register(id="PersistentChoiceGrid-v0", entry_point="src.environment:PersistentChoiceGrid")
except gym.error.Error:
    pass
