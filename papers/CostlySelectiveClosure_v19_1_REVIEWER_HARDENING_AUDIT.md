---
id: CSC-V19-1-REVIEWER-HARDENING-AUDIT-2026-09-16
type: audit
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
ai_do_not_use_for_definition: true
---

# CSC v19.1 reviewer-hardening audit — 2026-09-16

## Scope

This audit records a bounded manuscript hardening cycle for:

`papers/CostlySelectiveClosure_v19_1_ArtificialLife_candidate.md`

The cycle does **not** add a new confirmatory experiment, rerun E4, retune parameters, rewrite preregistrations, or submit the manuscript externally.

## 1. E1 / E4 comparability correction

The v19 wording could be read as if the E4 `+0.030` effect had directly measured what fraction of the E1 terminal-versus-restore effect is attributable to consequence scope. v19.1 removes that implication.

The manuscript now states explicitly that E1 and E4 differ in at least:

1. policy-update semantics;
2. evaluation endpoint and state bank;
3. confirmatory seed set;
4. baseline/continuation dynamics and floor regime.

Therefore E1 and E4 magnitudes are descriptive across experiments, not a controlled causal decomposition. A matched factorial continuation design is left as future work rather than added post hoc to the present paper.

## 2. E4 manipulation-purity correction

E4 shared recovery changes more than one latent mechanism. Relative to individual recovery, it:

- removes the still-active partner's normal action opportunity; and
- removes the partner's opportunity to exploit the recovering agent.

The manuscript now calls this a **bundled shared recovery/action-opportunity architecture** and avoids treating it as a pure universal "shared fate" variable.

The existing E4 diagnostics are retained: during individual recovery the active partner chooses Solo roughly 91–96% of the time; failure triggers are nevertheless dominated by mutual-Solo states rather than the stronger asymmetric-victim category. At shared `k=10`, both agents are forced for about 60% of environment steps and additional Rest-related failures occur. These diagnostics qualify rather than replace the preregistered primary endpoint.

## 3. Post-hoc E4 individual-scope latency cross-check

A new derived record was created from the first and only E4 confirmatory artifact:

`papers/costly_selective_closure_supplement/results/consequence_scope_E4_individual_latency_exploratory.json`

Source provenance:

```text
confirmatory run: 34977281851
artifact: 10400498866
confirmatory head: 96e9a8bf0a1a45a39c7327533477e1bb76633d89
source full JSON SHA-256: 74b4452a90231dbefdac82fc18373cbecf346df75948092366cb49e6a23406b5
```

No retraining was performed. The analysis uses only the 90 individual-scope E4 rows (`30 seeds × k={2,5,10}`).

Primary common-state endpoint:

| latency | mean | median | seeds > 0.5 |
|---|---:|---:|---:|
| k=2 | 0.04006 | 0.00187 | 1/30 |
| k=5 | 0.02756 | 0.00084 | 1/30 |
| k=10 | 0.01549 | 0.00062 | 0/30 |

Exploratory blocked-by-seed tie-aware Spearman:

```text
rho = -0.4944814885
p = 0.0000499975
20,000 permutations
```

Eligible-rollout means are `0.05459`, `0.03808`, and `0.02480`, with exploratory `rho=-0.46064`, `p=0.0000499975`.

Interpretation boundary:

- this weakens the hypothesis that E3's negative direction was solely a decision-count-normalization artifact;
- it does not turn E3 into a supported positive hypothesis;
- it is not a preregistered replication of E3;
- E4 lacks `k=0`, uses new seeds and a different common state bank, and was designed for the scope contrast.

## 4. Floor / attractor reporting

The manuscript now distinguishes direction consistency from behavioral regime transition.

E4 common-state `>0.5` counts:

```text
individual: k2 1/30; k5 1/30; k10 0/30
shared:     k2 1/30; k5 2/30; k10 1/30
```

Therefore `29/30` positive collapsed contrasts are described as a coherent policy shift in a largely floor-dominated regime, not as 29 transitions into a cooperative attractor.

## 5. Figure 2 correction

New figure:

`papers/costly_selective_closure_supplement/figures/figure2_evidence_summary_v19_1.svg`

Changes:

- E1 reports endpoint means plus explicit seed heterogeneity rather than ±1 SD;
- E2 and E3 report median + IQR on clearly labelled magnified floor scales;
- E4 reports paired delta on an explicitly different axis, with mean, paired 95% CI, median and positive-seed count;
- the figure explicitly warns that cross-panel visual distance is not a common effect scale.

## 6. Methods / appendix completeness

v19.1 adds reader-facing details for:

- E3 bank generation and masked update semantics;
- E4 bank seeds `2001..2010`, four episodes per seed, untrained policies, `individual/k=0`, bonus-off, exactly 2,000 paired decision-capable states;
- E4 fixed-horizon return normalization and `/50` scaling;
- forced-agent, both-forced, exactly-one-forced, eligible-fraction, partner-action, and failure-category diagnostics;
- the exploratory cross-check's exact provenance and status.

## 7. Internal-language cleanup

Reader-facing v19.1 removes or avoids:

- `than the v18 claim`;
- `Outcome B`;
- `adjudication record`;
- `mechanism audit` as an internal lifecycle label;
- wording that implies E4 quantitatively explains a fraction of E1.

Historical provenance and internal governance files are not rewritten.

## 8. Reference spot-check

Current source spot-check confirms:

- Scott & Pitt (2023), *Artificial Life* 29(2):198–234, DOI `10.1162/artl_a_00403`;
- Tampuu et al. (2017), *PLOS ONE* 12(4):e0172395, DOI `10.1371/journal.pone.0172395`;
- Hisaki & Ono (2024), ICML / PMLR 235:18352–18373;
- Chen & Chen (2026), arXiv:2608.27843, Sixin Chen and Taizhou Chen.

No novelty claim is based on priority over these neighbors.

## 9. Submission boundary

The manuscript still contains author identity because current journal-specific anonymity requirements have not been reliably verified from the inaccessible official guideline page. Identity should be checked against the live submission interface immediately before upload rather than inferred from ALife conference rules.

External journal submission = **NOT PERFORMED**.

## Current verdict

```text
v19.1 reviewer hardening = COMPLETE AT MANUSCRIPT CONTENT LEVEL
new confirmatory experiment = NO
E4 rerun = NO
parameter retuning = NO
E5 required for current manuscript = NO
post-hoc E4 latency cross-check = EXPLORATORY ONLY
external submission = NO
```
