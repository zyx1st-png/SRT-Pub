from __future__ import annotations

import pytest

from src.environment import PersistentChoiceGrid
from src.model import ActorCritic
from src.ppo import build_optimizer, train_steps


def test_training_reward_sum_is_real_rollout_reward(smoke_config):
    env = PersistentChoiceGrid(
        smoke_config,
        master_seed=91,
        condition="X",
        severity="low",
        phase="A",
        agent_id="agent-91",
        branch_id="reward-audit",
    )
    model = ActorCritic()
    optimizer = build_optimizer(model, smoke_config["ppo"])
    stats = train_steps(model, optimizer, env, 16, smoke_config["ppo"])
    assert stats.reward_sum == pytest.approx(env.cumulative_reward)
