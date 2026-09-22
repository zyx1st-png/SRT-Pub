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
| 1 | `id: SRT-GRG-BCTB0-T1-SOURCE-PACK-RAW-20260922` | `id: BCTB0-T1-SOURCE-PACK-DELABELED-20260922` |
| 4 | `# BCTB-0 T1 historical source pack — raw` | `# BCTB-0 T1 historical source pack — deterministic de-labelled` |
| 5 | `SRT Generative Relational Grammar` | `Framework Q` |
| 2 | `Generative Relational Grammar` | `Framework Q` |
| 3 | `SRT` | `THEORY-Q` |
| 6 | `GRG` | `FRAMEWORK-Q` |
| 7 | `Relation Library` | `Pattern Library` |
| 8 | `Relation Record` | `Pattern Record` |
| 9 | `RL-R1` | `Q-R1` |
| 10 | `RL-X3` | `Q-X3` |
| 11 | `RL-X4` | `Q-X4` |
| 12 | `R1a` | `Q1a` |
| 13 | `R1b` | `Q1b` |
| 14 | `R1c` | `Q1c` |
| 15 | `R1d` | `Q1d` |
| 16 | `X3a` | `Q3a` |
| 17 | `X3b` | `Q3b` |
| 18 | `X4a` | `Q4a` |
| 19 | `X4b` | `Q4b` |
| 20 | `X4c` | `Q4c` |
| 21 | `X1` | `QX1` |
| 22 | `X2` | `QX2` |
| 23 | `X3` | `QX3` |
| 24 | `X4` | `QX4` |
| 25 | `X5` | `QX5` |
| 26 | `X6` | `QX6` |
| 27 | `M0` | `K0` |
| 28 | `M1` | `K1` |
| 29 | `M2` | `K2` |
| 30 | `M3` | `K3` |
| 31 | `M4` | `K4` |
| 32 | `M5` | `K5` |
| 33 | `P-TECH` | `E-TECH` |
| 34 | `P-LEGAL` | `E-LEGAL` |
| 35 | `P-MKT` | `E-MKT` |
| 36 | `P-ORG` | `E-ORG` |
| 37 | `P-NORM` | `E-NORM` |
| 38 | `P-INFRA` | `E-INFRA` |
| 39 | `P-MIXED` | `E-MIXED` |
| 40 | `G0–G11` | `Q0–Q11` |
| 41 | `G0-G11` | `Q0-Q11` |

The transformed bundle must be byte-reproducible from the raw bundle plus this ordered table.


## Reproducibility rule

The wrapper metadata is part of the transformed input and therefore must be transformed by the same declared table.

A4 PASS requires:

```text
apply all 41 replacements in order to the complete raw bundle
-> supplied de-labelled bundle byte-for-byte
```

No out-of-table wrapper edit is permitted.
