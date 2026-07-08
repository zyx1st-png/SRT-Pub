# Costly Selective Closure — de-risking experiment (v2)

Two independent REINFORCE learners in a survival stag-hunt / PD (T=1.4 > R=1.0 > P=0.6 > S=0.0). Only mutual cooperation thrives; mutual defection starves. Trained with a mutual-cooperation bonus, then bonus withdrawn. **Real and resettable share an identical reward function; the sole difference is terminate-vs-reset on energy depletion.**

n_seeds = 30

### Main result (matched death penalty = 2.0 in all regimes)

| regime | baseline coop | frozen coop | post-withdrawal coop | deaths/ep | d_eff | %seeds cooperate |
|---|---:|---:|---:|---:|---:|---:|
| real | 0.599 | 0.614 | 0.548 ± 0.353 | 0.36 | 1.77 | 73% |
| resettable | 0.047 | 0.049 | 0.037 ± 0.141 | 3.74 | 1.57 | 7% |
| simulated | 0.081 | 0.082 | 0.072 ± 0.223 | 3.60 | 1.50 | 10% |

Permutation tests (real vs X, two-sided):
- real_vs_resettable__frozen_coop: diff=+0.566, p=0.0000
- real_vs_resettable__post_coop: diff=+0.511, p=0.0000
- real_vs_simulated__frozen_coop: diff=+0.532, p=0.0000
- real_vs_simulated__post_coop: diff=+0.475, p=0.0000

### Robustness 1: death penalty = 0 (pure return-truncation)

| regime | baseline coop | frozen coop | post-withdrawal coop | deaths/ep | d_eff | %seeds cooperate |
|---|---:|---:|---:|---:|---:|---:|
| real | 0.573 | 0.586 | 0.495 ± 0.318 | 0.31 | 1.84 | 60% |
| resettable | 0.066 | 0.064 | 0.055 ± 0.194 | 3.71 | 1.75 | 7% |
| simulated | 0.087 | 0.087 | 0.069 ± 0.218 | 3.60 | 1.62 | 10% |

Permutation tests (real vs X, two-sided):
- real_vs_resettable__frozen_coop: diff=+0.522, p=0.0000
- real_vs_resettable__post_coop: diff=+0.440, p=0.0000
- real_vs_simulated__frozen_coop: diff=+0.499, p=0.0000
- real_vs_simulated__post_coop: diff=+0.426, p=0.0000

### Robustness 2: lives gradient (dose-response, 30 seeds)

Generalises terminate-vs-reset to a number of allowed respawns.

| allowed respawns | post-withdrawal coop | %seeds cooperate | deaths/ep |
|---|---:|---:|---:|
| L1(real) | 0.538 ± 0.359 | 67% | 0.37 |
| L2 | 0.157 ± 0.284 | 17% | 2.36 |
| L4 | 0.034 ± 0.135 | 7% | 3.76 |
| L8 | 0.034 ± 0.135 | 7% | 3.76 |
| Linf(reset) | 0.034 ± 0.135 | 7% | 3.76 |

Spearman(lives, coop) = -0.410 (monotone decrease). L1 vs Linf: diff=+0.504, p=0.0000.

### Robustness 3: payoff sweep (15 seeds), real vs resettable

| temptation T | defect net-energy | real | resettable | diff | p |
|---:|---:|---:|---:|---:|---:|
| 1.2 | -0.15 | 0.47 | 0.11 | +0.35 | 0.0240 |
| 1.2 | -0.45 | 0.77 | 0.11 | +0.65 | 0.0001 |
| 1.4 | -0.15 | 0.39 | 0.05 | +0.34 | 0.0102 |
| 1.4 | -0.45 | 0.61 | 0.05 | +0.56 | 0.0000 |
| 1.6 | -0.15 | 0.28 | 0.01 | +0.27 | 0.0062 |
| 1.6 | -0.45 | 0.52 | 0.01 | +0.51 | 0.0000 |

Real > resettable in every cell; effect is not knife-edge.

## Reading
- Real-stake stabilises costly cooperation; cheaply-resettable and simulated-stake regimes collapse to defection despite the identical reward.
- The manipulated variable is within-episode token-level irreversibility alone: removing return-truncation removes the pressure that makes costly self-maintenance worth learning. This isolates the causal efficacy of the vulnerability dimension V; it does not validate the full four-dimensional criterion, and the learning that produces cooperation still runs across many resettable episodes (see README 'Honest scope').
