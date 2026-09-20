---
id: SRT-GRG-R1-NEURO-TRANSFER-PILOT-PREREG-20260920
type: preregistration
status: frozen
date: 2026-09-20
layer: experiments
epistemic_layer: experimental
claim_mode: prediction
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Proposals/SRT_GRG_R1_NEUROSCIENCE_TRANSFER_PILOT_CHARTER_2026-09-20.md
---

# GRG-R1 neuroscience transfer pilot — implementation preregistration

> Frozen before target simulation execution.

## 1. Task

Synthetic sequential context-composition task.

Input sequence length = 5.

Input dimension = 6:

- t0: one-hot feature-selector cue over input dims 0..2;
- t1: one-hot operation cue over input dims 3..4;
- t2,t3,t4: binary observations x1,x2,x3 presented serially in input dim 5.

There are six compositional contexts:

~~~text
(feature 1, identity)
(feature 2, identity)
(feature 3, identity)
(feature 1, invert)
(feature 2, invert)
(feature 3, invert)
~~~

Target:

~~~text
identity: selected bit
invert:   1 - selected bit
~~~

Base training uses the first five contexts.

The held-out transfer context is fixed before execution:

~~~text
(feature 3, invert)
~~~

No alternative held-out context may be substituted after seeing results.

## 2. Network

~~~text
model: tanh recurrent neural network
hidden units: 32
output: one sigmoid binary response from final hidden state
loss: binary cross entropy with logits
optimizer: Adam
learning rate: 0.01
batch size: 128
training seeds: 0..11 in each history class
~~~

Initialization seed equals the declared network seed within each history class.

## 3. Histories

Structured S:

~~~text
stage S1: identity contexts for features 1,2,3 — 300 updates
stage S2: invert contexts for features 1,2 — 300 updates
stage S3: all five base contexts — 600 updates
total = 1200 updates
~~~

Direct D:

~~~text
all five base contexts — 1200 updates
~~~

Training examples are generated on-line.

Base competence gate:

~~~text
held-out base-task accuracy >= 0.95
~~~

A network failing this gate is ineligible.

Primary pilot requires at least 8 eligible S and at least 8 eligible D networks.

## 4. O identification

Use 1,500 held-out base-task trials per eligible network, balanced as closely as possible across the five base contexts.

Decision-state representation = final hidden state after t4 in the intact network.

Context label = five-way base context identity.

Use 4-fold stratified cross-validation.

Within each fold:

1. fit multinomial logistic regression from hidden state to context;
2. take the fitted coefficient matrix;
3. center coefficients across classes;
4. compute its right-singular vectors;
5. use the first k vectors as candidate O_k for k in {1,2,3,4};
6. project train/test hidden states into O_k;
7. fit a second multinomial logistic regression on projected training states;
8. score test context accuracy.

Let A_k be mean held-out accuracy across the four folds.

Choose:

~~~text
k* = smallest k in {1,2,3,4} such that A_k >= 0.90 * A_4.
~~~

Then refit the context decoder on all 1,500 trials and freeze the first k* right-singular vectors as O.

O admission gate:

~~~text
A_k* >= 0.80.
~~~

Networks failing O admission remain reported but are not used in the primary O-withdrawal comparison.

## 5. Intervention interval

Interventions begin after the operation cue has entered the network.

Apply after recurrent updates at:

~~~text
t = 1,2,3,4
~~~

Do not intervene at t0.

## 6. Interventions

I0 intact.

I-O targeted:

~~~text
h <- h - O O^T h
~~~

at every intervention time.

I-R random control:

- rank = k*;
- 8 independently drawn orthonormal random subspaces per network;
- same intervention interval;
- random bases independent of task and target labels.

I-N magnitude control:

- isotropic Gaussian hidden-state perturbation;
- sigma calibrated from held-out base trials so mean displacement norm matches I-O within 10%;
- same intervention interval.

If magnitude matching misses the 10% tolerance after one deterministic rescaling pass, the network's noise-control arm is invalid.

## 7. Transfer evaluation and fine-tuning

For each eligible network and intervention arm:

- start from the identical frozen base-trained weights;
- use the held-out context (feature 3, invert) only;
- intervention remains active during target fine-tuning;
- fine-tune for 80 Adam updates;
- batch size 128;
- learning rate 0.005;
- use the same per-network target batch seed schedule across I0, I-O, I-N and all I-R arms.

Evaluation checkpoints:

~~~text
update 0, 5, 10, 20, 40, 60, 80
~~~

Each checkpoint uses a fixed 1,024-trial target evaluation set per network seed, generated before intervention-arm training and reused across arms.

## 8. Primary metric

Primary metric per intervention arm:

~~~text
AUC_0_80
= trapezoidal area under target accuracy vs update-number curve
  at checkpoints 0,5,10,20,40,60,80,
  normalized by the 0..80 update range.
~~~

Higher is better.

Define impairment:

~~~text
Delta_O = AUC_I0 - AUC_IO
Delta_R = AUC_I0 - mean(AUC_IR over 8 random bases)
Delta_N = AUC_I0 - AUC_IN
~~~

Primary contrasts:

~~~text
C_R = Delta_O - Delta_R
C_N = Delta_O - Delta_N
~~~

## 9. Primary PASS rule

Use independently trained network seed as the inferential unit.

Pool all eligible O-admitted networks across S and D for the primary realization test.

Bootstrap 95% confidence intervals over network seeds with 10,000 resamples using fixed bootstrap seed 20260920.

PILOT-PASS requires all:

~~~text
eligible S >= 8
eligible D >= 8
median C_R >= 0.03
median C_N >= 0.03
bootstrap 95% CI of mean C_R entirely > 0
bootstrap 95% CI of mean C_N entirely > 0
no semantic drift
~~~

If execution is otherwise valid but these are not all met:

~~~text
PILOT-NULL
~~~

## 10. Secondary metrics

Report without using them to rescue the primary verdict:

- zero-shot target accuracy at update 0;
- updates to >= 0.85 target accuracy, censored at >80;
- base-task accuracy under each intervention;
- context decoding A_1..A_4 and selected k*;
- O-targeted displacement norm and matched noise displacement norm;
- S vs D differences in O admission, k*, context-decoding strength, intact target AUC and Delta_O.

## 11. Interpretation

A PASS shows only:

> a GRG-R1-inspired organization-specific withdrawal design generated a valid causal distinction in this synthetic recurrent system.

A PASS does not establish SRT distinctiveness because recurrent-network science may already contain closely related subspace-ablation logic.

A later productive-adequacy review must therefore separately ask whether the GRG transfer changed the domain question / controls enough to count as transfer gain rather than retrospective relabeling.

## 12. Immutable-after-run fields

After target execution begins, do not change:

- held-out context;
- network size;
- history schedules;
- competence threshold;
- O extraction algorithm;
- O admission threshold;
- intervention times;
- random-control count;
- target fine-tuning schedule;
- AUC metric;
- PASS thresholds;
- bootstrap rule.

Any change requires a new version and the present run remains reported under v0.1.
