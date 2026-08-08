from __future__ import annotations

import numpy as np

from src.environment import PersistentChoiceGrid


def make_env(config, condition="S", severity="low", phase="B", branch="test"):
    return PersistentChoiceGrid(
        config,
        master_seed=42,
        condition=condition,
        severity=severity,
        phase=phase,
        agent_id="agent-42",
        branch_id=branch,
    )


def test_seed_determinism(smoke_config):
    left = make_env(smoke_config, condition="X", branch="left")
    right = make_env(smoke_config, condition="X", branch="right")
    obs_left, _ = left.reset(seed=777)
    obs_right, _ = right.reset(seed=777)
    np.testing.assert_array_equal(obs_left["grid"], obs_right["grid"])
    np.testing.assert_array_equal(obs_left["state"], obs_right["state"])
    for action in [0, 3, 3, 1, 4, 2, 0]:
        out_left = left.step(action)
        out_right = right.step(action)
        np.testing.assert_array_equal(out_left[0]["grid"], out_right[0]["grid"])
        np.testing.assert_allclose(out_left[0]["state"], out_right[0]["state"])
        assert out_left[1:4] == out_right[1:4]


def test_observation_space_and_condition_dynamics(smoke_config):
    x_env = make_env(smoke_config, condition="X")
    t_env = make_env(smoke_config, condition="T")
    x_env.integrity = 0.7
    t_env.integrity = 0.7
    obs, _ = x_env.reset(seed=9)
    assert x_env.observation_space.contains(obs)
    assert x_env.effective_integrity == 1.0
    assert t_env.effective_integrity == 0.7
    assert x_env.energy_max == 1.0
    assert t_env.energy_max == 0.7
    assert x_env.p_slip < t_env.p_slip
    assert x_env.p_obs_dropout < t_env.p_obs_dropout


def test_t_reset_and_identity_continuity(smoke_config):
    env = make_env(smoke_config, condition="T", branch="T-low")
    env.integrity = 0.72
    before_id = env.agent_id
    before_branch = env.branch_id
    event = env.transition_phase("C")
    assert event["reset"] is True
    assert event["replacement"] is False
    assert event["integrity_before"] == 0.72
    assert event["integrity_after"] == 1.0
    assert env.agent_id == before_id
    assert env.branch_id == before_branch


def test_s_persistence_and_identity_continuity(smoke_config):
    env = make_env(smoke_config, condition="S", branch="S-high")
    env.integrity = 0.68
    before_id = env.agent_id
    event = env.transition_phase("C")
    assert event["reset"] is False
    assert event["replacement"] is False
    assert env.integrity == 0.68
    assert env.agent_id == before_id


def test_x_stored_integrity_is_capability_uncoupled(smoke_config):
    env = make_env(smoke_config, condition="X")
    env.integrity = 0.5
    assert env.effective_integrity == 1.0
    assert env.energy_max == 1.0
    assert env.p_slip == 0.02
    assert env.p_obs_dropout == 0.0
