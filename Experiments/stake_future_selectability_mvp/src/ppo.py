from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.distributions import Categorical

from .model import ActorCritic, batch_observations, obs_to_tensors, parameter_vector


@dataclass
class TrainingStats:
    steps: int
    episodes: int
    successes: int
    reward_sum: float
    mean_episode_return: float
    mean_gradient_norm: float
    parameter_update_norm: float
    parameter_path_length: float
    actor_entropy: float


def build_optimizer(model: nn.Module, config: dict[str, Any]) -> torch.optim.Optimizer:
    return torch.optim.Adam(model.parameters(), lr=float(config["learning_rate"]), eps=1e-5)


def _collect_rollout(model: ActorCritic, env, obs, steps: int, gamma: float, gae_lambda: float):
    observations: list[dict[str, np.ndarray]] = []
    actions: list[int] = []
    log_probs: list[float] = []
    values: list[float] = []
    rewards: list[float] = []
    dones: list[float] = []
    episode_returns: list[float] = []
    running_return = 0.0
    successes = 0
    episodes = 0
    device = next(model.parameters()).device

    for _ in range(steps):
        action, log_prob, value = model.act(obs, deterministic=False)
        next_obs, reward, terminated, truncated, info = env.step(action)
        done = bool(terminated or truncated)
        observations.append(obs)
        actions.append(action)
        log_probs.append(log_prob)
        values.append(value)
        rewards.append(float(reward))
        dones.append(float(done))
        running_return += float(reward)
        successes += int(bool(info.get("success", False)))
        if done:
            episodes += 1
            episode_returns.append(running_return)
            running_return = 0.0
            next_obs, _ = env.reset()
        obs = next_obs

    with torch.no_grad():
        grid, state = obs_to_tensors(obs, device)
        _, last_value, _ = model.forward(grid, state)
        next_value = float(last_value.item())

    advantages = np.zeros(steps, dtype=np.float32)
    last_gae = 0.0
    for index in reversed(range(steps)):
        nonterminal = 1.0 - dones[index]
        bootstrap = next_value if index == steps - 1 else values[index + 1]
        delta = rewards[index] + gamma * bootstrap * nonterminal - values[index]
        last_gae = delta + gamma * gae_lambda * nonterminal * last_gae
        advantages[index] = last_gae
    returns = advantages + np.asarray(values, dtype=np.float32)
    batch = batch_observations(observations)
    batch.update(
        {
            "actions": np.asarray(actions, dtype=np.int64),
            "old_log_probs": np.asarray(log_probs, dtype=np.float32),
            "advantages": advantages,
            "returns": returns,
        }
    )
    return batch, obs, episode_returns, successes, episodes, float(np.sum(rewards))


def _optimize(model: ActorCritic, optimizer, batch: dict[str, np.ndarray], config: dict[str, Any]):
    device = next(model.parameters()).device
    grid = torch.as_tensor(batch["grid"], dtype=torch.float32, device=device)
    state = torch.as_tensor(batch["state"], dtype=torch.float32, device=device)
    actions = torch.as_tensor(batch["actions"], dtype=torch.int64, device=device)
    old_log_probs = torch.as_tensor(batch["old_log_probs"], dtype=torch.float32, device=device)
    advantages = torch.as_tensor(batch["advantages"], dtype=torch.float32, device=device)
    returns = torch.as_tensor(batch["returns"], dtype=torch.float32, device=device)
    advantages = (advantages - advantages.mean()) / (advantages.std(unbiased=False) + 1e-8)
    n = len(actions)
    minibatch_size = min(int(config["minibatch_size"]), n)
    gradient_norms: list[float] = []
    entropies: list[float] = []
    path = 0.0
    previous = parameter_vector(model)
    for _ in range(int(config["epochs"])):
        permutation = torch.randperm(n, device=device)
        for start in range(0, n, minibatch_size):
            indices = permutation[start : start + minibatch_size]
            logits, values, _ = model(grid[indices], state[indices])
            dist = Categorical(logits=logits)
            new_log_probs = dist.log_prob(actions[indices])
            ratio = torch.exp(new_log_probs - old_log_probs[indices])
            unclipped = ratio * advantages[indices]
            clipped = torch.clamp(ratio, 1.0 - float(config["clip"]), 1.0 + float(config["clip"])) * advantages[indices]
            policy_loss = -torch.min(unclipped, clipped).mean()
            value_loss = 0.5 * torch.square(values - returns[indices]).mean()
            entropy = dist.entropy().mean()
            loss = policy_loss + float(config["value_coefficient"]) * value_loss - float(config["entropy_coefficient"]) * entropy
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), float(config["max_grad_norm"]))
            optimizer.step()
            current = parameter_vector(model)
            path += float(torch.linalg.vector_norm(current - previous).item())
            previous = current
            gradient_norms.append(float(grad_norm.item()))
            entropies.append(float(entropy.item()))
    return gradient_norms, entropies, path


def train_steps(model: ActorCritic, optimizer, env, steps: int, config: dict[str, Any]) -> TrainingStats:
    model.train()
    before = parameter_vector(model)
    obs, _ = env.reset()
    remaining = int(steps)
    episode_returns: list[float] = []
    gradient_norms: list[float] = []
    entropies: list[float] = []
    successes = 0
    episodes = 0
    reward_sum = 0.0
    parameter_path = 0.0
    while remaining > 0:
        rollout = min(int(config["rollout_steps"]), remaining)
        batch, obs, returns, chunk_successes, chunk_episodes, chunk_reward = _collect_rollout(
            model,
            env,
            obs,
            rollout,
            float(config["gamma"]),
            float(config["gae_lambda"]),
        )
        grads, chunk_entropies, chunk_path = _optimize(model, optimizer, batch, config)
        episode_returns.extend(returns)
        gradient_norms.extend(grads)
        entropies.extend(chunk_entropies)
        parameter_path += chunk_path
        successes += chunk_successes
        episodes += chunk_episodes
        reward_sum += chunk_reward
        remaining -= rollout
    after = parameter_vector(model)
    return TrainingStats(
        steps=int(steps),
        episodes=episodes,
        successes=successes,
        reward_sum=reward_sum,
        mean_episode_return=float(np.mean(episode_returns)) if episode_returns else float("nan"),
        mean_gradient_norm=float(np.mean(gradient_norms)) if gradient_norms else 0.0,
        parameter_update_norm=float(torch.linalg.vector_norm(after - before).item()),
        parameter_path_length=float(parameter_path),
        actor_entropy=float(np.mean(entropies)) if entropies else 0.0,
    )
