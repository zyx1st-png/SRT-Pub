"""Invariant-only validation for CSC Experiment 2.

This script intentionally avoids confirmatory seeds 1..30 and does not report
behavioral effect sizes. It checks only locked design mechanics before the full
confirmatory run.
"""
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))
import csc_experiment as ce  # noqa: E402
import csc_recoverability as cr  # noqa: E402


def force_depletion(env: cr.RecoverabilityEnv):
    env.energy[:] = 0.1
    # rest/rest: metabolic -1 + gain +0.5 = -0.4, so both agents deplete.
    rewards, done, failures, _mutual = env.step(np.array([2, 2], dtype=int), bonus_active=False)
    return rewards, done, failures


def check_condition(name, duration):
    rng = np.random.default_rng(9001)
    env = cr.RecoverabilityEnv(duration, rng)
    env.reset()

    assert ce.T_HORIZON == 50
    assert cr.FAILURE_PENALTY == 0.0
    assert cr.DAMAGE_MULTIPLIER == 0.75
    assert env.obs(0).shape == (ce.N_FEATURES,)
    assert ce.N_FEATURES == 12

    rewards, done, failures = force_depletion(env)
    assert failures == 2
    assert done is False, f"{name}: depletion must not terminate episode"
    assert np.allclose(rewards, [ce.REWARD[(2, 2)], ce.REWARD[(2, 2)]])
    assert np.allclose(env.energy, [ce.E_0, ce.E_0]), f"{name}: rescue must be E0"

    if duration is None:
        assert np.all(env.damage_remaining == -1)
    else:
        assert np.all(env.damage_remaining == duration)

    if duration == 0:
        assert env.gain_multiplier(0) == 1.0
        assert env.gain_multiplier(1) == 1.0
    else:
        assert env.gain_multiplier(0) == cr.DAMAGE_MULTIPLIER
        assert env.gain_multiplier(1) == cr.DAMAGE_MULTIPLIER

    # Verify finite damage lasts exactly tau subsequent steps when no new
    # depletion occurs. Use high energy so timer behavior is isolated.
    if duration not in (None, 0):
        env.energy[:] = 100.0
        for expected_before in range(duration, 0, -1):
            assert np.all(env.damage_remaining == expected_before)
            env.step(np.array([0, 0], dtype=int), bonus_active=False)
        assert np.all(env.damage_remaining == 0)
        assert env.gain_multiplier(0) == 1.0

        # A repeated depletion refreshes the timer to full duration.
        env.damage_remaining[:] = 1
        env.energy[:] = 0.1
        env.step(np.array([2, 2], dtype=int), bonus_active=False)
        assert np.all(env.damage_remaining == duration)

    if duration is None:
        env.energy[:] = 100.0
        for _ in range(3):
            env.step(np.array([0, 0], dtype=int), bonus_active=False)
            assert np.all(env.damage_remaining == -1)


def check_fixed_horizon():
    # Smoke seeds are explicitly outside the preregistered confirmatory set.
    cfg = dict(train_eps=2, withdraw_eps=2, window=1, lr=0.04, lr_w=0.04, gamma=0.97)
    for idx, condition in enumerate(cr.CONDITION_ORDER):
        result = cr.train_condition(condition, seed=9001 + idx, cfg=cfg)
        assert result["post_len"] == 50.0, f"{condition}: fixed horizon violated"


def check_shared_locked_parameters():
    assert list(cr.RECOVERY_DURATIONS.keys()) == cr.CONDITION_ORDER
    assert cr.RECOVERY_DURATIONS == {
        "tau0": 0,
        "tau5": 5,
        "tau15": 15,
        "tau_inf": None,
    }
    assert cr.FAILURE_PENALTY == 0.0
    assert cr.DAMAGE_MULTIPLIER == 0.75
    assert cr.N_PERMUTATIONS == 20_000
    assert cr.N_BOOTSTRAP == 10_000


def main():
    check_shared_locked_parameters()
    for name, duration in cr.RECOVERY_DURATIONS.items():
        check_condition(name, duration)
    check_fixed_horizon()
    print("PASS: all preregistered Experiment 2 invariants hold")
    print("No confirmatory seeds 1..30 were executed by this test.")


if __name__ == "__main__":
    main()
