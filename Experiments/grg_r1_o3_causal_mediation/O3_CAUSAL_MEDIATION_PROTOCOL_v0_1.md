---
id: SRT-GRG-R1-O3-CAUSAL-MEDIATION-PROTOCOL-20260921
type: experimental_protocol
status: frozen
date: 2026-09-21
layer: experiments
epistemic_layer: experimental
claim_mode: prediction
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_GRG_R1_PRODUCTIVE_ADEQUACY_O_CRITERION_REVISION_PASS1_2026-09-20.md
  - Operations/Audits/SRT_GRG_R1_O_FEASIBILITY_SPECTRAL_FORMATION_RESULT_2026-09-20.md
  - Materials/2026/SRC_2026_09_08_Neuro_Bowler_Structured_Experience_Strategy_Dynamics.md
tags: [GRG, GRGR1, O3, CausalMediation, SpectralScaffold, RNN, TargetBlind]
---

# GRG-R1 O3 target-blind causal-mediation protocol v0.1

## 0. Scope

This protocol tests O3 only.

Current gate entering the protocol:

~~~text
O1 formation = PASS
O2 retained operator structure = candidate paid
O3 target-blind causal mediation = this protocol
O4 prospective re-entry / new transfer target = HOLD
~~~

No transfer target may be generated, selected or inspected during this protocol.

## 1. Question

Does a recurrent spectral scaffold produced by Structured history causally alter later learning on the same source-domain base task when transplanted into an otherwise naive recurrent network?

Target chain:

~~~text
history class
-> retained recurrent spectral scaffold
-> scaffold transplant before recipient learning
-> altered source-domain learning trajectory
~~~

This is stronger than decoding because the candidate O is manipulated before the measured learning process.

## 2. Source-native intervention pattern

The intervention is intentionally modeled on Bowler et al. 2026 and the public seed_weights_run.py workflow:

~~~text
trained donor recurrent weights
-> eigendecomposition
-> leading history-associated eigenvalues
-> transplant into naive recipient recurrent matrix
-> later learning under common task
~~~

This is a source-native positive-control family, not an SRT-specific mechanism claim.

## 3. Donor histories

Fresh donor seeds:

~~~text
200..211
~~~

For each seed train two networks with identical initialization:

Structured S:

~~~text
300 updates identity contexts for features 1,2,3
300 updates invert contexts for features 1,2
600 updates all five base contexts
total = 1200
~~~

Direct D:

~~~text
1200 updates all five base contexts
~~~

Base competence gate:

~~~text
held-out base accuracy >= 0.95
~~~

All 12 S and 12 D donors must pass for O3-PASS eligibility.

## 4. Frozen spectral scaffold extraction

For each donor recurrent matrix W_h:

1. compute complex eigenvalues with numpy.linalg.eigvals;
2. sort with the source-native numpy ordering:
   numpy.sort(eigenvalues)[::-1];
3. retain the first four;
4. average each complex rank across the 12 S donors to obtain scaffold_S;
5. average each complex rank across the 12 D donors to obtain scaffold_D.

No outcome-based mode selection is allowed.

The use of four eigenvalues is inherited from the source-native Bowler intervention and the prior O1 spectral feasibility family. It is not a universal GRG constant.

## 5. Recipient networks

Fresh recipient seeds:

~~~text
300..311
~~~

For each seed initialize one naive network and copy it into three arms:

~~~text
I0 = intact naive recurrent operator
IS = S-scaffold seeded recurrent operator
ID = D-scaffold seeded recurrent operator
~~~

The input layer, recurrent bias and output layer remain identical across arms at intervention time.

## 6. Frozen scaffold transplant

For IS or ID:

1. eigendecompose the recipient recurrent matrix W = V diag(e) V^-1;
2. copy e to e_new;
3. replace e_new[0:4] with scaffold_S or scaffold_D;
4. reconstruct:
   W_new = real(V diag(e_new) V^-1);
5. replace only the recurrent weight matrix.

This exactly follows the source-native intervention family closely enough for the bounded toy realization.

Record, but do not use to tune the intervention:

- Frobenius norm distance from intact W;
- spectral radius before and after;
- imaginary reconstruction residual before taking real part.

## 7. Common recipient training

After intervention, all three arms learn the same five-context base task only.

Training:

~~~text
optimizer = Adam
learning rate = 0.01
batch size = 128
updates = 600
same per-seed online training batches reused across I0, IS and ID
~~~

Evaluation checkpoints:

~~~text
0, 5, 10, 20, 40, 80, 160, 320, 600
~~~

At each checkpoint evaluate on one fixed 2048-trial balanced base-task set for that recipient seed, reused across arms.

No transfer context is evaluated.

## 8. Primary source-domain outcome

Primary metric:

~~~text
AUC_base
= trapezoidal area under held-out base accuracy vs update curve
  across the frozen checkpoints,
  normalized by the 0..600 update range.
~~~

Higher is better.

Per recipient seed define:

~~~text
C_SD = AUC_IS - AUC_ID
C_S0 = AUC_IS - AUC_I0
~~~

Inferential unit = recipient network seed.

## 9. Primary O3 PASS rule

Bootstrap 95% confidence intervals over the 12 recipient seeds with 10,000 resamples.

Fixed bootstrap seeds:

~~~text
C_SD = 20260921
C_S0 = 20260922
~~~

O3-CAUSAL-PASS requires all:

~~~text
12/12 S donors base competent
12/12 D donors base competent
12/12 recipient seeds complete

median C_SD >= 0.03
median C_S0 >= 0.03

95% bootstrap CI of mean C_SD entirely > 0
95% bootstrap CI of mean C_S0 entirely > 0
~~~

If execution is valid but the conjunction fails:

~~~text
O3-CAUSAL-NULL
~~~

If donor competence or numerical reconstruction makes the intervention unusable:

~~~text
O3-CAUSAL-INVALID
~~~

## 10. Secondary metrics — no rescue

Report without changing the primary verdict:

- accuracy at each checkpoint;
- updates to >= 0.95 accuracy, censored at >600;
- training BCE loss AUC;
- IS-ID and IS-I0 parameter-distance summaries;
- spectral radius shift;
- S vs D donor scaffold values.

A secondary positive pattern cannot rescue an O3-CAUSAL-NULL verdict.

## 11. Interpretation

PASS means only:

~~~text
a history-associated recurrent spectral scaffold,
defined before recipient learning,
causally biases later learning on the same source-domain task.
~~~

PASS would pay O3 for this bounded operator family.

PASS would not establish:

- O4 prospective transfer re-entry;
- GRG universality;
- biological implementation;
- SRT scientific distinctiveness;
- One / Bearer / consciousness / normativity.

NULL means:

Do not proceed to O4 with this spectral scaffold family in this toy system.

Do not tune mode count, scaffold ranking or recipient task after the result.

## 12. No-target / no-canonical guard

During O3:

~~~text
new transfer target = prohibited
v0.1 target reuse = prohibited
O4 = HOLD
canonical edit = NO
Level change = NO
winner-style strongest-neighbor audit = NO
~~~

Any O4/v0.2 work requires a later, separate visible charter and preregistration.
