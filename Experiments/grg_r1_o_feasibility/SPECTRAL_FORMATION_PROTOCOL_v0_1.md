---
id: SRT-GRG-R1-O-FEASIBILITY-SPECTRAL-FORMATION-PROTOCOL-20260920
type: experimental_protocol
status: frozen
date: 2026-09-20
layer: experiments
epistemic_layer: experimental
claim_mode: prediction
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_GRG_R1_PRODUCTIVE_ADEQUACY_O_CRITERION_REVISION_PASS1_2026-09-20.md
---

# GRG-R1 O-feasibility Pass A — spectral formation protocol

## 0. Scope

This is target-blind feasibility only.

It does not evaluate the v0.1 transfer target, any new transfer target, or GRG-R1 O4.

Question:

Can the structured-vs-direct training history leave a reproducible imprint in the current recurrent operator of the toy RNN strongly enough to pay O1 formation pressure for an operator-embedded O family?

## 1. Networks

Reuse the same architecture and base-task histories as the v0.1 pilot, but use a fresh seed set:

~~~text
S seeds = 100..111
D seeds = 100..111
~~~

Each S/D pair shares the same initialization seed.

No target-transfer batches are generated or evaluated.

Base competence gate remains >= 0.95.

## 2. Frozen spectral feature

After base training, eigendecompose the recurrent weight matrix W_h.

Sort eigenvalues by:

~~~text
descending magnitude,
then descending real part,
then descending absolute imaginary part.
~~~

Take the first four.

Feature vector:

~~~text
[real(lambda_1..4),
 abs(imag(lambda_1..4)),
 abs(lambda_1..4)]
~~~

12 dimensions total.

This feature is label-blind and fixed before result inspection.

No PCA, decoder axis or target behavior enters the feature.

## 3. Primary history-separation test

Classifier:

~~~text
logistic regression
with z-scoring fit on training folds only.
~~~

Cross-validation:

~~~text
Leave-One-Seed-Pair-Out
12 folds
test fold = S and D networks sharing one initialization seed.
~~~

Primary accuracy = 24-network held-out classification accuracy.

Permutation test:

~~~text
1000 permutations
independently swap S/D labels within each seed pair with probability 0.5
recompute the complete paired-group CV accuracy
fixed permutation RNG seed = 20260920
p = (1 + count(null_accuracy >= observed_accuracy)) / 1001
~~~

## 4. O1 feasibility rule

O1-SPECTRAL-PASS requires all:

~~~text
12/12 S and 12/12 D networks pass base competence;
paired-group CV accuracy >= 0.75;
permutation p <= 0.05.
~~~

Otherwise:

~~~text
O1-SPECTRAL-NULL
~~~

If competence fails for more than two networks in either group:

~~~text
O1-SPECTRAL-INVALID
~~~

## 5. Interpretation ceiling

PASS means only:

A manipulated training-history contrast left a reproducibly classifiable imprint in the current recurrent operator under this feature.

PASS does not establish:

- O3 causal mediation;
- order-parameter standing;
- GRG-R1 re-entry;
- SRT distinctiveness.

NULL means:

Do not proceed to a spectral O3 intervention in this toy task using this frozen feature family. Prefer another source-domain realization rather than tuning the spectral summary post hoc.

## 6. No-target guard

During this pass do not:

- generate target-transfer data;
- evaluate target AUC;
- inspect v0.1 target curves to choose spectral features;
- change the top-four rule after seeing history separation;
- add label-selected eigenmodes.

Any O3 pass, if authorized, requires a separate frozen protocol.
