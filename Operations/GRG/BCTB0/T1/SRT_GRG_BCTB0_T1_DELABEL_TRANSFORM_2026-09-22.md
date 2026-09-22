---
id: SRT-GRG-BCTB0-T1-DELABEL-TRANSFORM-20260922
type: calibration_transform
status: candidate
date: 2026-09-22
canonical: false
ai_do_not_use_for_definition: true
---

# BCTB-0 T1 deterministic de-labelling transform

Input: raw source-pack bundle generated from the T1 mechanical manifest.

Algorithm:

```text
for each replacement pair below, in listed order:
    replace all exact UTF-8 substring occurrences globally
no regex inference
no summarization
no deletion
no reordering
no added causal interpretation
```

Replacement table:

| # | exact input | exact output |
|---:|---|---|
| 1 | `SRT Generative Relational Grammar` | `Framework Q` |
| 2 | `Generative Relational Grammar` | `Framework Q` |
| 3 | `SRT` | `THEORY-Q` |
| 4 | `GRG` | `FRAMEWORK-Q` |
| 5 | `Relation Library` | `Pattern Library` |
| 6 | `Relation Record` | `Pattern Record` |
| 7 | `RL-R1` | `Q-R1` |
| 8 | `RL-X3` | `Q-X3` |
| 9 | `RL-X4` | `Q-X4` |
| 10 | `R1a` | `Q1a` |
| 11 | `R1b` | `Q1b` |
| 12 | `R1c` | `Q1c` |
| 13 | `R1d` | `Q1d` |
| 14 | `X3a` | `Q3a` |
| 15 | `X3b` | `Q3b` |
| 16 | `X4a` | `Q4a` |
| 17 | `X4b` | `Q4b` |
| 18 | `X4c` | `Q4c` |
| 19 | `X1` | `QX1` |
| 20 | `X2` | `QX2` |
| 21 | `X3` | `QX3` |
| 22 | `X4` | `QX4` |
| 23 | `X5` | `QX5` |
| 24 | `X6` | `QX6` |
| 25 | `M0` | `K0` |
| 26 | `M1` | `K1` |
| 27 | `M2` | `K2` |
| 28 | `M3` | `K3` |
| 29 | `M4` | `K4` |
| 30 | `M5` | `K5` |
| 31 | `P-TECH` | `E-TECH` |
| 32 | `P-LEGAL` | `E-LEGAL` |
| 33 | `P-MKT` | `E-MKT` |
| 34 | `P-ORG` | `E-ORG` |
| 35 | `P-NORM` | `E-NORM` |
| 36 | `P-INFRA` | `E-INFRA` |
| 37 | `P-MIXED` | `E-MIXED` |
| 38 | `G0–G11` | `Q0–Q11` |
| 39 | `G0-G11` | `Q0-Q11` |

The transformed bundle must be byte-reproducible from the raw bundle plus this ordered table.
