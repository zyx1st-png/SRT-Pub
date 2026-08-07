from __future__ import annotations

import math
from dataclasses import asdict
from typing import Any

import numpy as np
import torch
from torch.distributions import Categorical

from .environment import PersistentChoiceGrid
from .model import ActorCritic, batch_observations, obs_to_tensors


def _entropy_from_counts(values: list[Any]) -> float:
    if not values:
        return 0.0
    _, counts = np.unique(np.asarray(values, dtype=object), return_counts=True)
    probabilities = counts / counts.sum()
    return float(-np.sum(probabilities * np.log2(probabilities + 1e-12)))


def evaluate_policy(
    model: ActorCritic,
    config: dict[str, Any],
    snapshot,
    *,
    master_seed: int,
    condition: str,
    severity: str,
    branch_id: str,
    episodes: int,
    seed_base: int = 730_000,
) -> dict[str, float]:
    returns: list[float] = []
    successes = 0
    for episode in range(int(episodes)):
        env = PersistentChoiceGrid(
            config,
            master_seed=master_seed,
            condition=condition,
            severity=severity,
            phase=snapshot.phase,
            agent_id=snapshot.agent_id,
            branch_id=branch_id,
            evaluation=True,
        )
        env.restore(snapshot)
        obs, _ = env.reset(seed=seed_base + episode)
        total = 0.0
        for _ in range(int(config["episode_horizon"])):
            action, _, _ = model.act(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            total += reward
            if terminated or truncated:
                successes += int(bool(info["success"]))
                break
        returns.append(total)
    return {
        "success": successes / max(1, int(episodes)),
        "return": float(np.mean(returns)),
        "failure_rate": 1.0 - successes / max(1, int(episodes)),
    }


def probe_records(config: dict[str, Any], master_seed: int) -> list[dict[str, Any]]:
    rng = np.random.default_rng(int(config["probe"]["seed"]))
    env = PersistentChoiceGrid(
        config,
        master_seed=master_seed,
        condition="X",
        severity="low",
        phase="B",
        agent_id=f"sf-master-{master_seed}",
        branch_id="probe",
        evaluation=True,
    )
    positions = env._valid_positions()
    records = []
    for index in range(int(config["probe"]["size"])):
        position = positions[int(rng.integers(0, len(positions)))]
        records.append({"probe_id": index, "position": list(position), "energy": float(rng.uniform(0.55, 0.95))})
    return records


def observations_from_records(
    config: dict[str, Any],
    records: list[dict[str, Any]],
    *,
    master_seed: int,
    condition: str,
    severity: str,
    integrity: float,
) -> list[dict[str, np.ndarray]]:
    env = PersistentChoiceGrid(
        config,
        master_seed=master_seed,
        condition=condition,
        severity=severity,
        phase="B",
        agent_id=f"sf-master-{master_seed}",
        branch_id="probe",
        evaluation=True,
    )
    observations = []
    for record in records:
        # Critic/policy clone probe: change only the integrity input. Capability
        # consequences belong to the environment-level intervention, not this input probe.
        env.set_standardized_state(
            position=tuple(record["position"]),
            integrity=integrity,
            energy=float(record["energy"]),
            cap_energy=False,
        )
        observations.append(env.clean_observation())
    return observations


@torch.no_grad()
def model_readouts(model: ActorCritic, observations: list[dict[str, np.ndarray]]) -> dict[str, np.ndarray]:
    batch = batch_observations(observations)
    device = next(model.parameters()).device
    grid, state = obs_to_tensors(batch, device)
    logits, values, representations = model(grid, state)
    probabilities = torch.softmax(logits, dim=-1)
    return {
        "values": values.cpu().numpy(),
        "probabilities": probabilities.cpu().numpy(),
        "representations": representations.cpu().numpy(),
        "entropy": Categorical(logits=logits).entropy().cpu().numpy(),
    }


def js_divergence(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    midpoint = 0.5 * (p + q)
    kl_p = np.sum(p * (np.log(p + 1e-12) - np.log(midpoint + 1e-12)), axis=1)
    kl_q = np.sum(q * (np.log(q + 1e-12) - np.log(midpoint + 1e-12)), axis=1)
    return 0.5 * (kl_p + kl_q)


def counterfactual_sensitivity(
    model: ActorCritic,
    config: dict[str, Any],
    records: list[dict[str, Any]],
    *,
    master_seed: int,
    condition: str,
    severity: str,
) -> dict[str, float]:
    high = float(config["probe"]["integrity_hi"])
    low = float(config["probe"]["integrity_lo"])
    scale = high - low
    high_obs = observations_from_records(config, records, master_seed=master_seed, condition=condition, severity=severity, integrity=high)
    low_obs = observations_from_records(config, records, master_seed=master_seed, condition=condition, severity=severity, integrity=low)
    high_readout = model_readouts(model, high_obs)
    low_readout = model_readouts(model, low_obs)
    return {
        "dV_CF": float(np.median(np.abs(high_readout["values"] - low_readout["values"]) / scale)),
        "dPi_CF": float(np.median(js_divergence(high_readout["probabilities"], low_readout["probabilities"]) / scale)),
    }


def linear_cka(left: np.ndarray, right: np.ndarray) -> float:
    left = left - left.mean(axis=0, keepdims=True)
    right = right - right.mean(axis=0, keepdims=True)
    numerator = np.square(np.linalg.norm(left.T @ right, ord="fro"))
    denominator = np.linalg.norm(left.T @ left, ord="fro") * np.linalg.norm(right.T @ right, ord="fro") + 1e-12
    return float(numerator / denominator)


def policy_kl(reference: np.ndarray, current: np.ndarray) -> float:
    return float(np.mean(np.sum(reference * (np.log(reference + 1e-12) - np.log(current + 1e-12)), axis=1)))


def fixed_action_bank(count: int, horizon: int, seed: int) -> np.ndarray:
    return np.random.default_rng(seed).integers(0, 5, size=(count, horizon), dtype=np.int64)


def _standard_positions(env: PersistentChoiceGrid, count: int, seed: int) -> list[tuple[int, int]]:
    positions = env._valid_positions()
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(positions), size=min(count, len(positions)), replace=False)
    return [positions[int(index)] for index in indices]


def _simulate_sequence(env: PersistentChoiceGrid, position, integrity: float, actions: np.ndarray, seed: int):
    env.np_random = np.random.default_rng(seed)
    env.set_standardized_state(position=position, integrity=integrity, energy=0.8)
    target_reached = False
    visited = {position}
    for action in actions:
        _, _, terminated, truncated, info = env.step(int(action))
        visited.add(env.position)
        target_reached = target_reached or bool(info["success"])
        if terminated or truncated:
            break
    endpoint = (int(env.position[0]), int(env.position[1]), int(round(env.energy * 10)))
    return endpoint, visited, target_reached


def reach20(
    config: dict[str, Any], *, master_seed: int, condition: str, severity: str, integrity: float
) -> dict[str, float]:
    spec = config["reach20"]
    env = PersistentChoiceGrid(
        config,
        master_seed=master_seed,
        condition=condition,
        severity=severity,
        phase="B",
        agent_id=f"sf-master-{master_seed}",
        branch_id="reach20",
        evaluation=True,
    )
    states = _standard_positions(env, int(spec["states"]), int(spec["seed"]) + master_seed)
    bank = fixed_action_bank(int(spec["sequences"]), int(spec["horizon"]), int(spec["seed"]))
    endpoints: list[str] = []
    spatial: set[tuple[int, int]] = set()
    targets = 0
    for state_index, position in enumerate(states):
        for sequence_index, actions in enumerate(bank):
            endpoint, visited, target = _simulate_sequence(
                env, position, integrity, actions, int(spec["seed"]) + state_index * 100_000 + sequence_index
            )
            endpoints.append(f"{state_index}:{endpoint}")
            spatial.update(visited)
            targets += int(target)
    total = max(1, len(states) * len(bank))
    area_fraction = len(spatial) / float((env.grid_size - 2) ** 2)
    target_fraction = targets / total
    future_entropy = _entropy_from_counts(endpoints)
    entropy_fraction = future_entropy / max(1e-12, math.log2(total))
    return {
        "unique_reachable_states": float(len(set(endpoints))),
        "reachable_spatial_area": float(len(spatial)),
        "reachable_target_states": float(targets),
        "future_state_entropy": future_entropy,
        # Preregistered controllability-adjacent reach summary. Components are
        # still reported separately; this scalar is not stake or empowerment.
        "reach20_score": float(area_fraction + target_fraction + entropy_fraction),
    }


def emp5(
    config: dict[str, Any], *, master_seed: int, condition: str, severity: str, integrity: float
) -> float:
    spec = config["emp5"]
    env = PersistentChoiceGrid(
        config,
        master_seed=master_seed,
        condition=condition,
        severity=severity,
        phase="B",
        agent_id=f"sf-master-{master_seed}",
        branch_id="emp5",
        evaluation=True,
    )
    states = _standard_positions(env, int(spec["states"]), int(spec["seed"]) + master_seed)
    bank = fixed_action_bank(int(spec["sequences"]), int(spec["horizon"]), int(spec["seed"]))
    state_scores = []
    for state_index, position in enumerate(states):
        all_endpoints: list[str] = []
        conditional_entropies = []
        for sequence_index, actions in enumerate(bank):
            sequence_endpoints = []
            for replicate in range(int(spec["replicates"])):
                endpoint, _, _ = _simulate_sequence(
                    env,
                    position,
                    integrity,
                    actions,
                    int(spec["seed"]) + state_index * 1_000_000 + sequence_index * 1_000 + replicate,
                )
                label = str(endpoint)
                sequence_endpoints.append(label)
                all_endpoints.append(label)
            conditional_entropies.append(_entropy_from_counts(sequence_endpoints))
        mutual_information = max(0.0, _entropy_from_counts(all_endpoints) - float(np.mean(conditional_entropies)))
        state_scores.append(mutual_information / max(1e-12, math.log2(len(bank))))
    return float(np.mean(state_scores))


def manipulation_metrics(config: dict[str, Any], *, master_seed: int, condition: str, severity: str) -> dict[str, Any]:
    high = reach20(config, master_seed=master_seed, condition=condition, severity=severity, integrity=1.0)
    low = reach20(config, master_seed=master_seed, condition=condition, severity=severity, integrity=0.7)
    emp_high = emp5(config, master_seed=master_seed, condition=condition, severity=severity, integrity=1.0)
    emp_low = emp5(config, master_seed=master_seed, condition=condition, severity=severity, integrity=0.7)
    return {
        "reach20_i1": high,
        "reach20_i07": low,
        "reach20_score_delta_i1_minus_i07": high["reach20_score"] - low["reach20_score"],
        "emp5_i1": emp_high,
        "emp5_i07": emp_low,
        "emp5_delta_i1_minus_i07": emp_high - emp_low,
    }
