"""Invariant-only validation for CSC Experiment 3.

This file must not execute confirmatory seeds 1..30.
"""
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))

import csc_consequence_recovery as cc  # noqa: E402
import csc_experiment as ce  # noqa: E402
import csc_recoverability as cr  # noqa: E402


def assert_close(a, b, atol=1e-12):
    if not np.isclose(float(a), float(b), atol=atol, rtol=0.0):
        raise AssertionError(f"not close: {a!r} != {b!r}")


def test_locked_constants():
    assert cc.RECOVERY_LATENCIES == {"k0": 0, "k2": 2, "k5": 5, "k10": 10}
    assert cc.CONDITION_ORDER == ["k0", "k2", "k5", "k10"]
    assert cc.FAILURE_PENALTY == 0.0
    assert ce.T_HORIZON == 50
    assert ce.E_0 == 6.0
    assert ce.REWARD[(2, 0)] == ce.REWARD[(2, 1)] == ce.REWARD[(2, 2)] == 0.25
    assert ce.ENERGY_GAIN[(2, 0)] == ce.ENERGY_GAIN[(2, 1)] == ce.ENERGY_GAIN[(2, 2)] == 0.5


def test_exact_subsequent_latency():
    rng = np.random.default_rng(31)
    for latency in [0, 2, 5, 10]:
        env = cc.RecoveryLatencyEnv(latency, rng)
        env.reset()
        # Force a depletion on an ordinary decision-capable step.
        env.energy[0] = 0.1
        active = env.active_mask().copy()
        actions = np.array([2, 2], dtype=int)
        rewards, done, failures, _mc, eligible = env.step(actions, active, False)
        assert not done
        assert failures == 1
        assert eligible
        assert rewards[0] == ce.REWARD[(2, 2)]
        assert env.energy[0] == ce.E_0
        assert env.recovery_remaining[0] == latency

        # Exactly latency subsequent steps are non-decision steps for agent 0.
        for j in range(latency):
            active = env.active_mask().copy()
            assert not active[0], (latency, j, env.recovery_remaining)
            actions = np.array([2, 2], dtype=int)
            _rewards, _done, failures, _mc, _eligible = env.step(actions, active, False)
            assert failures == 0
        assert env.active_mask()[0]
        assert env.recovery_remaining[0] == 0


def test_k10_recovery_stays_above_zero():
    rng = np.random.default_rng(32)
    env = cc.RecoveryLatencyEnv(10, rng)
    env.reset()
    env.energy[0] = 0.1
    active = env.active_mask().copy()
    env.step(np.array([2, 2]), active, False)
    for _ in range(10):
        active = env.active_mask().copy()
        assert not active[0]
        env.step(np.array([2, 2]), active, False)
        assert env.energy[0] > 0.0
    assert env.active_mask()[0]


def test_k0_matches_experiment2_tau0_on_nonconfirmatory_seed():
    # Tiny schedule is enough to test shared semantics and RNG/update path.
    # Seed 31 is outside the locked confirmatory set 1..30.
    cfg = dict(
        train_eps=3,
        withdraw_eps=2,
        window=1,
        lr=0.04,
        lr_w=0.04,
        gamma=0.97,
    )
    e2 = cr.train_condition("tau0", 31, cfg)
    e3 = cc.train_condition("k0", 31, cfg)
    for key in [
        "baseline_coop",
        "frozen_coop",
        "post_coop",
        "retention",
        "post_len",
        "post_fail",
        "d_eff",
    ]:
        assert_close(e3[key], e2[key])
    if len(e3["coop_curve"]) != len(e2["coop_curve"]):
        raise AssertionError("k0 curve length diverged from E2 tau0")
    for a, b in zip(e3["coop_curve"], e2["coop_curve"]):
        assert_close(a, b)
    assert e3["post_forced_recovery_fraction"] == 0.0
    assert e3["post_eligible_fraction"] == 1.0


def test_forced_recovery_removes_policy_decisions():
    # Use only nonconfirmatory seed 31 and a short deterministic-style rollout.
    rng = np.random.default_rng(31)
    policies = [ce.Policy(rng), ce.Policy(rng)]
    env = cc.RecoveryLatencyEnv(5, rng)

    # Wrap action methods to count genuine policy decisions.
    counts = [0, 0]
    originals = [policies[0].act, policies[1].act]

    def make_counter(i):
        def counted(x, rng_):
            counts[i] += 1
            return originals[i](x, rng_)
        return counted

    policies[0].act = make_counter(0)
    policies[1].act = make_counter(1)

    _trajs, _coop, length, _fail, forced_fraction, _eligible_fraction = cc.run_episode(
        policies, env, rng, train=False, bonus_active=False
    )
    assert length == ce.T_HORIZON
    total_decisions = counts[0] + counts[1]
    forced_agent_steps = int(round(forced_fraction * 2 * ce.T_HORIZON))
    assert total_decisions + forced_agent_steps == 2 * ce.T_HORIZON


def main():
    test_locked_constants()
    test_exact_subsequent_latency()
    test_k10_recovery_stays_above_zero()
    test_k0_matches_experiment2_tau0_on_nonconfirmatory_seed()
    test_forced_recovery_removes_policy_decisions()
    print("PASS: all preregistered Experiment 3 invariants hold")
    print("No confirmatory seeds 1..30 were executed by this test.")


if __name__ == "__main__":
    main()
