from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))

import csc_experiment as ce  # noqa: E402
import csc_consequence_scope as e4  # noqa: E402


def assert_close_policy(a, b, tol=1e-10):
    for name in ("W1", "b1", "W2", "b2"):
        av = getattr(a, name)
        bv = getattr(b, name)
        if not np.allclose(av, bv, atol=tol, rtol=tol):
            raise AssertionError(f"policy mismatch in {name}")


def test_k0_update_equivalence():
    rng = np.random.default_rng(31)
    policies = [ce.Policy(rng), ce.Policy(rng)]
    env = e4.ConsequenceScopeEnv("individual", 0, rng)
    trajs, _coop, _diag = e4.run_episode(policies, env, rng, bonus_active=False)

    for i in range(2):
        p_orig = policies[i].copy()
        p_e4 = policies[i].copy()
        legacy = []
        for tr in trajs[i]:
            x, h, p = tr["cache"]
            legacy.append((x, h, p, tr["action"], tr["reward"]))
        p_orig.update(legacy, lr=0.04, gamma=0.97)
        e4._update_fixed_horizon(p_e4, trajs[i], lr=0.04, gamma=0.97)
        assert_close_policy(p_orig, p_e4)


def force_failure(scope: str, latency: int):
    rng = np.random.default_rng(32)
    env = e4.ConsequenceScopeEnv(scope, latency, rng)
    env.reset()
    env.energy[:] = [0.2, 6.0]
    active = env.active_mask().copy()
    actions = np.array([0, 1], dtype=int)
    _rewards, done, failed, _cats, _mutual, _eligible = env.step(actions, active, False)
    assert not done
    assert failed == [0]
    assert env.energy[0] == ce.E_0
    if scope == "individual":
        assert env.recovery_remaining.tolist() == [latency, 0]
    else:
        assert env.recovery_remaining.tolist() == [latency, latency]
    return env


def test_exact_timer_semantics():
    for latency in (2, 5, 10):
        for scope in e4.SCOPES:
            env = force_failure(scope, latency)
            seen = []
            for _ in range(latency):
                active = env.active_mask().copy()
                seen.append(bool(not active[0]))
                actions = np.array([2 if not active[0] else 1, 2 if not active[1] else 1], dtype=int)
                env.step(actions, active, False)
            assert seen == [True] * latency
            assert env.active_mask()[0]
            if scope == "shared":
                assert env.active_mask()[1]


def test_shared_refresh_on_recovery_depletion():
    rng = np.random.default_rng(33)
    env = e4.ConsequenceScopeEnv("shared", 5, rng)
    env.reset()
    env.energy[:] = [0.2, 0.4]
    active = env.active_mask().copy()
    _r, done, failed, _cats, _m, _e = env.step(np.array([0, 1], dtype=int), active, False)
    assert not done
    assert 0 in failed
    assert env.recovery_remaining.tolist() == [5, 5]

    # Force a later depletion while shared recovery is active; this must rescue
    # only the actually depleted unit and refresh the common recovery timer.
    env.energy[1] = 0.1
    active = env.active_mask().copy()
    _r, done, failed, _cats, _m, _e = env.step(np.array([2, 2], dtype=int), active, False)
    assert not done
    assert 1 in failed
    assert env.energy[1] == ce.E_0
    assert env.recovery_remaining.tolist() == [5, 5]


def test_fixed_horizon_and_no_termination():
    cfg = {"train_eps": 2, "withdraw_eps": 2, "window": 1, "lr": 0.04, "lr_w": 0.04, "gamma": 0.97}
    for scope in e4.SCOPES:
        for k in e4.LATENCIES:
            row = e4.train_condition(scope, k, 34, cfg)
            assert row["scope"] == scope
            assert row["latency"] == k
            assert len(row["post_diags"]) == 1


def test_common_bank():
    bank = e4.build_common_state_bank()
    assert len(bank) == 2000
    for x0, x1 in bank[:10]:
        assert x0.shape == (ce.N_FEATURES,)
        assert x1.shape == (ce.N_FEATURES,)


def test_seed_guard():
    smoke = {0, 31, 34, 99, 131, 2001}
    assert smoke.isdisjoint(set(e4.CONFIRMATORY_SEEDS))
    assert e4.CONFIRMATORY_SEEDS == list(range(101, 131))


def main():
    test_k0_update_equivalence()
    test_exact_timer_semantics()
    test_shared_refresh_on_recovery_depletion()
    test_fixed_horizon_and_no_termination()
    test_common_bank()
    test_seed_guard()
    print("E4 invariant suite PASS")
    print("No confirmatory seeds 101..130 were executed")


if __name__ == "__main__":
    main()
