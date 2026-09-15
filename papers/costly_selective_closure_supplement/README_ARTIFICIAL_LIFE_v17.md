---
id: CSC-SUPPLEMENT-V17-ARTIFICIAL-LIFE-NOTE
type: submission_note
status: draft
version: v17
target_venue: Artificial Life
derived_from: papers/costly_selective_closure_supplement/README.md
---

# Costly Selective Closure — Artificial Life v17 Supplement Note

This file is the **v17 submission-facing note** for the existing reproduction package. It does not alter the experiment code, committed result files, statistical tests, or the historical v16 Adaptive Behavior supplement README.

## 1. Why this note exists

The v16 manuscript used an older paper-local notation for the four-part Costly Selective Closure heuristic:

- `d` — selective bandwidth;
- `Ψ_f` — maintenance cost;
- `η` — hysteretic memory;
- `V` — irreversible vulnerability.

Subsequent SRT repository development assigned different canonical meanings to some of those symbols, especially bare `d`. The Artificial Life v17 candidate therefore **de-couples the manuscript from SRT canonical notation** and uses a manuscript-local descriptive profile instead:

- **B — selective breadth**;
- **M — maintenance burden**;
- **H — historical retention**;
- **V — irreversible vulnerability**.

This is a notation and claim-boundary cleanup. It does **not** change the experiment.

## 2. What is actually tested

The experiment tests one operational contrast relevant to **V**:

```text
terminal-run / one-life condition
vs
cheap-restoration / resettable condition
```

The matched real-stake and resettable regimes share the programmed reward function, observation space and feature specification, energy dynamics, policy architecture, training schedule, and seeds. Their programmed regime difference is the depletion transition: terminate versus restore.

The experiment does **not** independently manipulate or validate B, M, and H. Those remain dimensions of the broader heuristic.

## 3. Organizational levels

For v17, three levels must be kept explicit:

- **episode-token** — the currently running episode; depletion may terminate it;
- **controller-lineage** — policy weights persist and continue learning across episodes;
- **training process** — repeated episodes generate the learning pressure.

Therefore, the experiment does not physically destroy the learned controller when an episode-token terminates. Its claim is narrower: changing whether episode-token failure is terminal or cheaply reversible changes the learned controller in this environment.

## 4. Historical package compatibility

The following existing assets remain authoritative for reproducing the reported experiment:

- `run_main.py`
- `run_zero_penalty.py`
- `run_lives_gradient.py`
- `run_payoff_sweep.py`
- `run_common_state_probe.py`
- `src/csc_experiment.py`
- `src/csc_robustness.py`
- `src/csc_probe.py`
- `results/*.json`
- `figures/figure2_design.*`
- `figures/figure3_results.*`
- `figures/figure4_common_state_probe.*`

The historical `figure1_framework.*` and its generator retain the v16 notation and are **not used by the v17 manuscript candidate**.

## 5. Review distribution

For journal review, provide the supplement as a static review package or through an access route that does not expose reviewer identity through logs or permissions. Do not require reviewers to authenticate through an identity-bearing repository workflow.

The historical root README contains the exact and qualitative reproduction requirements. This v17 note should be included alongside it or used as the submission-facing entry note.

## 6. Empirical scope guard

The supported empirical conclusion is:

> Within the reported survival-coupled reinforcement-learning architecture, the terminate-versus-restore intervention causally changes learned policy and strongly changes the persistence of costly cooperation.

The package does not establish that episode termination creates life, that physical irreversibility is universally required for life, or that the full four-dimensional CSC heuristic has been validated.
