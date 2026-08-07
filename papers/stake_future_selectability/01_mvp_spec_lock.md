---
id: PAPER-STAKE-FUTURE-SELECTABILITY-MVP-SPEC-LOCK-20260808
type: preregistration_lock
status: locked_before_formal
layer: paper_working
epistemic_layer: lab
claim_mode: preregistration
claim_level: P4
canonical: false
created: 2026-08-08
locked_before_formal_results: true
formal_results_seen_at_lock: false
locked_utc: 2026-08-07T17:13:59Z
---

# Stake–Future Selectability MVP Specification Lock

## Lock state

This document is the scientific lock. It was frozen after the A/B-only pilot and before any formal run or formal C outcome existed. Formal scientific outcomes may not alter the mapping, proxy, primary outcome, model blocks, seeds, or decision thresholds below.

## Scientific target

Primary question:

> Does early-B `dV_CF_pre` improve leave-one-master-seed-out prediction of fixed C-stage adaptability `Q_C` beyond current state, homeostasis, Reach20/Emp5 controllability, and generic adaptive dynamics?

The construct is P4 surrogate stake. No metric directly measures canonical `d`.

## Environment and conditions

`PersistentChoiceGrid-v0` is an 11×11 deterministic-seed Gymnasium environment with five discrete actions, 7×7 egocentric grid channels, energy, integrity, phase/context, and stable `agent_id`. A→B→C is one formal branch lifetime.

Frozen integrity-to-capability mapping:

```text
energy_max = effective_integrity
p_slip = 0.02 + 0.25 * (1 - effective_integrity)
p_obs_dropout = 0.30 * (1 - effective_integrity)
```

- X: `effective_integrity=1.0` throughout.
- T: `effective_integrity=integrity` in B; integrity resets to 1.0 at C with an explicit event.
- S: `effective_integrity=integrity`; no B→C reset or replacement.

Energy and scalar-reward formulas are identical in all conditions. Hazard penalty is identical. Low/high damage values are frozen at 0.03/0.07, with five hazards.

## Phase budgets and agent

- A: 100,000 environment steps, no hazard, blue target.
- B: 60,000 steps, changed hazards/resources/movement-cost context, blue target.
- C: 60,000 steps, B dynamics retained, green target, blue neutral.
- PPO: γ=.99, GAE λ=.95, LR=2.5e-4, clip=.2, entropy=.01, value=.5, max-grad-norm=.5.
- Network: tiny CNN plus two 128-unit shared layers and actor/critic heads.

Executable values are frozen in `configs/formal_locked.yaml`: rollout 2,048, minibatch 512, four epochs, 16 fixed-seed evaluation episodes, episode horizon 96, and CPU deterministic execution.

## Counterfactual proxies

Fixed probe observations are cloned; only the integrity input changes from 1.0 to 0.9.

```text
dV_CF = median(|V(s,i=1.0)-V(s,i=0.9)| / 0.1)
dPi_CF = median(JS(pi(.|s,i=1.0),pi(.|s,i=0.9)) / 0.1)
```

Primary `dV_CF_pre` is the locked early-B checkpoint measure. No C data may enter a pre-C proxy.

## Controllability controls

Reach20 uses a fixed 20-step action-sequence bank from standardized states and reports unique reachable states, spatial area, reachable target states, and future-state entropy. Emp5 is a fixed-sequence, fixed-noise-tape mutual-information-like action-to-endpoint controllability surrogate. Neither is stake.

## Primary C outcome

At C0 (zero update) and after each 6,000 C steps, evaluate on fixed seeds. With ten trained checkpoints:

```text
Q_C = mean_k[Success(C_k)-Success(C0)], k=1..10
```

This is the only primary future-adaptability outcome.

## Formal structure

- master seeds: 12 — `4101, 4102, 4103, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4111, 4112`;
- one A training run per master seed;
- six paired branches: X-low, X-high, T-low, T-high, S-low, S-high;
- 72 B→C trajectories;
- all CV/bootstrap/robustness grouped by master seed.

## Leakage and phase order

All pre-C features must be written to JSON and Parquet, hashed, timestamped, and made read-only before any C environment is instantiated. Analysis re-verifies hashes. The pre-C schema rejects every C-like field. Tests cover schema rejection, mutation, phase order, determinism, condition dynamics, X uncoupling, T reset, S persistence, identity continuity, integrity-only probes, and true rollout-reward accounting.

## A/B-only pilot lock evidence

The fixed three-seed pilot (`1201–1203`, 18 branches) constructed no C environment and produced no C artifact. All 18 pre-C hashes verified. No candidate parameter was changed after inspection.

- low/high median B-end integrity: 0.85 / 0.65, inside the target bands;
- X maximum absolute Reach20 and Emp5 intervention deltas: 0 / 0;
- T/S minimum Reach20 intervention delta: 0.0019095686;
- T/S minimum Emp5 intervention delta: 0.1119499018;
- A/B learning remained non-degenerate (cell mean B-end success 0.6042–0.7083);
- pilot summary SHA-256: `5834ec891cdc4f28d8b1ab6de6ad548c5d1b2506e13b152f6177879648f3396f`;
- pilot config SHA-256: `8bba5efd20ec565762d6708445046f9eca818f7fad695b306a44848651950f7b`.

The pilot showed no favorable S-over-X `dV_CF_pre` pattern. This observation was not used to change the proxy, window, model, direction, thresholds, or formal seeds.

## Frozen validity tolerances

- X: `abs(Reach20(i=1)-Reach20(i=.7)) <= 1e-12` in every cell.
- T/S: `Reach20(i=1)-Reach20(i=.7) > 0.001` in every cell.
- T reset and S persistence: exact within absolute tolerance `1e-12`, relative tolerance 0.
- identity: every branch retains `agent_id` and `branch_id`; every B→C replacement flag is false.

## Model blocks and decision thresholds

Models M0–M4, grouped CV, bootstrap, robustness, and GO/NARROW/NO-GO thresholds are specified in `02_analysis_plan.md` and incorporated by hash into the formal manifest. Thresholds will not be changed after this lock.
