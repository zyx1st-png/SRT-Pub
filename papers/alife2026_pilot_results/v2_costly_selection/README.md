# Costly Selective Closure — experiment v2

> **Historical / superseded — do not use for analysis.** This is the internal
> development copy. The submission analysis and the canonical, corrected code
> live in [`../../costly_selective_closure_supplement/`](../../costly_selective_closure_supplement/).
> In particular, the Spearman permutation test in this directory is an early
> implementation (ordinal `argsort(argsort())` ranks with a global shuffle that
> ignores ties and the repeated-measures design). The supplement uses a
> tie-aware average-rank Spearman with a blocked-by-seed permutation p-value.
> Use the supplement, not this directory, for any reproduction or reporting.

Controlled successor to the original ALIFE-2026 pilot
(`../minimal_costly_selection_pilot.py`), built after the ALIFE-2026 rejection.
The original pilot's headline result was degenerate: `real` and `resettable`
regimes came out identical (persistence 100.2 == 100.2), which reviewers read
as "arbitrary numbers / confirmation bias". Diagnosis: (i) cooperation was
weakly reward-dominant so nothing decayed after bonus withdrawal, (ii) death
almost never happened (0.13–0.64/episode) so the terminate-vs-reset
manipulation never bit, (iii) the persistence metric saturated at its cap.

## What v2 changes

- **Genuine social dilemma.** PD-ordered immediate reward (T=1.4 > R=1.0 >
  P=0.6 > S=0.0): unilateral defection is tempting, so withdrawing the
  cooperation bonus creates real decay pressure.
- **Survival tied to cooperation.** Tight energy economy: only mutual
  cooperation thrives; mutual defection slowly starves. Death now happens, so
  terminate-vs-reset actually matters.
- **Single manipulated variable.** `real` and `resettable` share an *identical*
  reward function; the only difference is terminate vs reset on energy
  depletion. This isolates token-level irreversibility.
- **Independent learners** (two separate REINFORCE policies) so defection can
  genuinely emerge.
- **Continuous, non-saturating metrics** + permutation tests, 30 seeds.

## Files

| file | what |
|---|---|
| `csc_experiment.py` | main 3-regime experiment (`real` / `resettable` / `simulated`); `full` = 30 seeds, plus a `ablate_nopenalty` mode |
| `csc_robustness.py` | `gradient` (lives 1→2→4→8→∞ dose-response) and `sweep` (payoff grid) |
| `make_report.py` | regenerates `RESULTS_SUMMARY.md` from the JSONs |
| `results_full.json` | main run, matched death penalty |
| `results_nopenalty.json` | ablation: death penalty = 0 (pure return-truncation) |
| `results_gradient.json` | lives gradient (30 seeds) |
| `results_sweep.json` | payoff sweep (15 seeds) |
| `RESULTS_SUMMARY.md` | consolidated tables |

## Reproduce

Pure NumPy, no GPU, no API calls. From this directory:

```bash
python3 csc_experiment.py full             # -> results_full.json
python3 csc_experiment.py ablate_nopenalty # -> results_nopenalty.json
python3 csc_robustness.py gradient         # -> results_gradient.json
python3 csc_robustness.py sweep            # -> results_sweep.json
python3 make_report.py                     # -> RESULTS_SUMMARY.md
```

Each 30-seed condition set runs in a few minutes on a single CPU core.

## Headline result

Post-withdrawal mutual cooperation: `real` 0.55 > `simulated` 0.07 >
`resettable` 0.04 (p < 0.0001, 30 seeds), with an identical reward function.
Survives death-penalty = 0 (pure truncation, p < 0.0001), is a monotone
dose-response over allowed respawns (Spearman −0.41), and holds across all six
payoff cells of the sweep.

## Honest scope (read before citing)

This is a **mechanism demonstration**, not a validation of the full criterion.

- It isolates the causal efficacy of the vulnerability dimension `V`; it does
  **not** test `d`, `η`, or the four-dimensional criterion jointly.
- The environment is a **testbed built so that `V` can matter** (survival is
  tied to the costly behavior). The finding is the *magnitude*, the
  *dose-response*, and that reversibility erases the effect under matched
  reward — not that irreversibility matters in every environment.
- The learned cooperation is produced by many resettable episodes. So the
  learning that yields cooperation lives at the **across-episode (lineage-like)**
  level; the manipulated irreversibility is **within-episode** return-truncation.
  The experiment does not escape the units-of-selection point — it localizes it.
- The mechanism (terminating the return stream makes a reward-maximiser avoid
  that event) is close to an elementary property of RL return structure. This is
  a feature, not a bug: it is why episode-terminating RL agents carry a nonzero
  but shallow `V`, consistent with their "weakly life-like" placement — but it
  means the result should be framed as *isolating and quantifying* `V`, never as
  proof that the framework carves life-likeness.
