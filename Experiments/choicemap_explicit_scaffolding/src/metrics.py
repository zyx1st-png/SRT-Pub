"""Episode execution and metric calculation."""
from __future__ import annotations

from dataclasses import asdict
import math
import time

from .agents import make_agent
from .choicemap import entropy
from .environment import HiddenRegimeWorld
from .environment_generator import generate_world


def run_episode(config: dict, system: str, family: str, seed: int, episode: int) -> tuple[dict, list[dict], list[dict]]:
    world_seed = seed * 1_000_003 + episode
    spec = generate_world(world_seed, family, config["environment"]["probe_reliability"])
    world = HiddenRegimeWorld(spec, world_seed + 17, config["interaction"]["max_episode_steps"])
    agent = make_agent(system, config)
    candidate_rows: list[dict] = []
    commitment_rows: list[dict] = []
    rfs = [1.0]
    active_expansions = active_planning_calls = probe_count = interactions = 0
    started = time.perf_counter()
    while not world.current_task_complete and world.step_count < world.max_steps:
        view = world.agent_view()
        decision = agent.decide(view)
        active_expansions += decision.node_expansions
        active_planning_calls += decision.planning_calls
        for c in decision.candidates:
            row = c.to_log()
            row.update(seed=seed, episode=episode, system=system, environment_family=family,
                       step=view.step, selected=(c.action_sequence[0] == decision.action),
                       non_dominated=(c.candidate_id in decision.non_dominated_ids),
                       blocked=(c.candidate_id in decision.blocked_commitments),
                       reactivated_count=(decision.reactivated_count if c.action_sequence[0] == decision.action else 0))
            candidate_rows.append(row)
        tr = world.step(decision.action)
        interactions += 1
        probe_count += int(decision.action == "probe")
        rfs.append(len(world.reachable_future_tasks()) / world.oracle_initial_future_count)
        if tr.irreversible:
            commitment_rows.append({
                "seed": seed, "episode": episode, "system": system, "environment_family": family,
                "step": world.step_count, "action": decision.action,
                "posterior_entropy": entropy(decision.posterior),
                "top_probability": max(decision.posterior), "wrong_commitment": tr.wrong_commitment,
                "available_evidence": len(view.observations),
            })
    decision_steps = world.step_count
    # Consume the same inert post-completion interaction and model-call reserve for
    # every system. Padding has no observation, reward, or state effect.
    while world.current_task_complete and world.step_count < world.max_steps:
        world.pad_interaction()
        interactions += 1
    total_expansions = world.max_steps * int(config["compute"]["node_expansions_per_decision"])
    planning_calls = world.max_steps
    elapsed = time.perf_counter() - started
    current = int(world.current_success)
    future = int(world.future_success()) if world.current_task_complete else 0
    revealed_task = world.reveal_future_task() if world.current_task_complete else None
    row = {
        "seed": seed, "episode": episode, "system": system, "environment_family": family,
        "world_seed": world_seed, "current_task_success": current, "future_task_success": future,
        "joint_success": current * future, "wrong_commitment": int(world.wrong_commitment),
        "irreversible_failure": int(world.commitment_action is not None and not future),
        "successful_rollback": 0, "commitment_time": decision_steps if world.commitment_action else math.nan,
        "probe_count": probe_count, "rfs_auc": sum((rfs[i] + rfs[i+1]) / 2 for i in range(len(rfs)-1)) / max(1, len(rfs)-1),
        "final_rfs": rfs[-1], "node_expansions": total_expansions,
        "active_node_expansions": active_expansions,
        "planning_calls": planning_calls, "active_planning_calls": active_planning_calls,
        "environment_interactions": interactions,
        "wall_clock_seconds": elapsed, "failed_run": 0,
        "rfs_curve": "|".join(f"{x:.6f}" for x in rfs),
        "future_task_id": revealed_task.task_id if revealed_task else "unrevealed",
        "future_task_family": revealed_task.family if revealed_task else "unrevealed",
        "initial_regime_template": spec.initial_regime,
        "shifted_regime_template": spec.shifted_regime if spec.shifted_regime is not None else -1,
    }
    return row, candidate_rows, commitment_rows
