# Costly Selective Closure — reproduction package

Anonymized supplementary material for the paper *"Costly Selective Closure: A
Comparative Heuristic for Life-Likeness in Artificial Systems."* Author(s):
**Anonymous author(s)** (double-blind submission).

> **For double-blind review, distribute this directory as a ZIP without Git history; do not link to an identity-bearing repository.**

This package contains the experiment code, the fixed result files used in the
paper, and the figure-generation script. Everything runs in pure NumPy with
Matplotlib for plotting; no external reinforcement-learning framework is used.

> The result files in `results/` are the exact ones used in the paper and in the
> figures. Re-running the experiments reproduces them up to platform- and
> NumPy-version floating-point differences; the qualitative findings are robust.

## 1. Research question

Does **token-level irreversibility** — whether a system's failure ends its own
reward-bearing existence or is cheaply undone — do causal work in shaping what an
adaptive system becomes, or is it merely an observer's label? The experiment
isolates this one dimension (the vulnerability dimension `V`) of the four-part
Costly Selective Closure heuristic (selective bandwidth `d`, maintenance cost
`Ψ_f`, hysteretic memory `η`, irreversible vulnerability `V`).

## 2. Clean causal comparison vs. auxiliary condition

- **Clean causal comparison — real-stake vs. resettable.** These two regimes
  share an *identical* reward function, observations, energy dynamics, network,
  training schedule, and seeds. They differ in **one variable only**: on energy
  depletion, the real-stake agent's run terminates, whereas the resettable agent
  is cheaply restored to full energy and continues.
- **Auxiliary condition — simulated-stake.** This regime remains resettable but
  **adds two changes**: a mortality cue in the observation and an additional
  represented-danger *reward* penalty (1.5). It is therefore **not** a
  single-variable matched condition; it tests whether representing danger can
  substitute for non-cheaply-reversible failure. Treat it as auxiliary.

## 3. Requirements

- Requires Python **3.9+**; tested here on Python 3.14.
- `numpy` and `matplotlib` only (see `requirements.txt`). No GPU.

## 4. Installation

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 5. Running

Each script writes its JSON into `results/`. From this directory:

```bash
python run_main.py            # -> results/main_results.json
python run_zero_penalty.py    # -> results/zero_penalty_results.json
python run_lives_gradient.py  # -> results/lives_gradient_results.json
python run_payoff_sweep.py    # -> results/payoff_sweep_results.json
python generate_figures.py    # -> figures/figure{1,2,3}.{svg,pdf,png}
```

## 6. Approximate runtimes (single modern CPU core)

| script | conditions | approx. time |
|---|---|---|
| `run_main.py` | 3 regimes x 30 seeds | ~3-6 min |
| `run_zero_penalty.py` | 3 regimes x 30 seeds | ~3-6 min |
| `run_lives_gradient.py` | 5 levels x 30 seeds | ~6-12 min |
| `run_payoff_sweep.py` | 6 cells x 2 regimes x 15 seeds | ~8-15 min |
| `generate_figures.py` | reads JSON only | a few seconds |

## 7. Output files

- `results/*.json` — per-seed runs, per-regime/level/cell summaries, and
  permutation-test outputs.
- `figures/figure1_framework.{svg,pdf,png}` — conceptual four-dimensional
  schematic (not calibrated).
- `figures/figure2_design.{svg,pdf,png}` — experimental design.
- `figures/figure3_results.{svg,pdf,png}` — main result, lives-gradient
  dose-response, and payoff-sweep robustness.

## 8. Rebuilding the figures from existing results only

The figures depend only on the committed JSON files, not on re-running the
experiments:

```bash
python generate_figures.py
```

All quantitative content in Figure 3 (means, bootstrap CIs, Spearman ρ,
permutation p-values, per-seed points) is read from `results/`; nothing is
hand-entered.

## 9. Random seeds

Every run is fully seeded via `numpy.random.default_rng(seed)`. The main,
zero-penalty, and lives-gradient conditions use seeds `1..30`; the payoff sweep
uses seeds `1..15` per cell. The same seed drives both policies' initialization
and all sampling within a run.

## 10. Statistical tests

The **primary test** for each real-vs-resettable comparison (the main experiment
and the zero-penalty ablation, which share seeds) is a two-sided **paired
sign-flip permutation test** on the per-seed real − resettable differences
(20,000 resamples, fixed seed), computed in `generate_figures.py` from the
result runs. A pooled/unpaired permutation test
(also 20,000 resamples) is reported as a **robustness** check. Both sit at the
test's resolution floor (~1/20001) and are stated as `p < 0.0001`; the
conclusion is unchanged between them. Figure 3(a) error bars are **95% bootstrap
confidence intervals of the mean** (10,000 resamples). The lives gradient reports
a **tie-aware** Spearman rank correlation (with a two-sided permutation p-value)
between the maximum number of lives and cooperation; the payoff sweep in
Figure 3(c) shows effect sizes (real − resettable), not per-cell significance
stars.

## 11. Where results appear in the paper

| paper location | file |
|---|---|
| §4.5 main result (real 0.55 / resettable 0.04 / simulated 0.07, paired p<0.0001) | `results/main_results.json` |
| §4.5 zero-penalty ablation (0.50 vs 0.05, paired p<0.0001) | `results/zero_penalty_results.json` |
| §4.5 lives-gradient dose-response (tie-aware Spearman -0.44, p<0.0001) | `results/lives_gradient_results.json` |
| §4.5 payoff sweep (real > resettable in 6/6 cells) | `results/payoff_sweep_results.json` |
| Figure 3 | all four result files, via `generate_figures.py` |
| Appendix (environment, reward matrix, network, schedule) | `src/csc_experiment.py`, `src/csc_robustness.py` |

## 12. Honest scope

- The experiment **isolates the causal efficacy of `V`**; it does **not**
  validate the full four-dimensional heuristic (`d` and `η` are held roughly
  fixed and are descriptive here).
- The environment is **deliberately survival-coupled**: mutual cooperation is
  the survival-promoting behavior. The finding is the magnitude of the effect,
  its dose-response, and its disappearance under a cheap restore — not a claim
  that irreversibility matters in every environment.
- The mechanism is close to an elementary property of reinforcement learning
  (terminating an agent's return stream makes a reward-maximizer avoid the
  terminating event). This is consistent with, not a substitute for, the
  paper's conceptual argument.
- **simulated-stake is auxiliary**, not part of the single-variable matched
  contrast.

## Files

```
costly_selective_closure_supplement/
├── README.md
├── requirements.txt
├── CITATION.cff
├── LICENSE
├── run_main.py
├── run_zero_penalty.py
├── run_lives_gradient.py
├── run_payoff_sweep.py
├── generate_figures.py
├── src/                # verified experiment code (unchanged algorithms)
│   ├── csc_experiment.py
│   └── csc_robustness.py
├── results/            # fixed result files used in the paper
│   ├── main_results.json
│   ├── zero_penalty_results.json
│   ├── lives_gradient_results.json
│   └── payoff_sweep_results.json
└── figures/            # generated from results/
```
