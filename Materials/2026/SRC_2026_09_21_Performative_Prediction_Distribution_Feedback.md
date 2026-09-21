---
source_id: SRC-2026-09-21-PERFORMATIVE-PREDICTION-DISTRIBUTION-FEEDBACK
id: SRC-2026-09-21-PERFORMATIVE-PREDICTION-DISTRIBUTION-FEEDBACK
title: "Perdomo et al. 2020 — Performative Prediction and model-induced distribution shift"
source_type: peer_reviewed_machine_learning_theory
domain: machine_learning_decision_feedback
primary_authors: "Juan Perdomo; Tijana Zrnic; Celestine Mendler-Dünner; Moritz Hardt"
publication: "ICML 2020 / PMLR 119"
date_published: "2020"
date_added: "2026-09-21"
evidence_level: formal_theoretical_framework_with_examples
reliability_level: high_for_source_native_performative_prediction_claims
srt_relevance: very_high_for_GRG_X4b_crossdomain_match
integration_priority: very_high
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags: [GRG, PerformativePrediction, MachineLearning, DistributionShift, Feedback, X4b, M3]
---

# SourceCard — Performative Prediction and distribution feedback

## 1. Primary source

Perdomo, J., Zrnic, T., Mendler-Dünner, C. & Hardt, M. (2020).

Performative Prediction.

Proceedings of the 37th International Conference on Machine Learning,
PMLR 119:7599–7609.

https://proceedings.mlr.press/v119/perdomo20a.html

Supporting later optimization work:

Miller, J. P., Perdomo, J. C. & Zrnic, T. (2021).

Outside the Echo Chamber: Optimizing the Performative Risk.

https://proceedings.mlr.press/v139/miller21a.html

## 2. Source-native problem

The paper begins from a failure of the standard fixed-distribution prediction picture.

When predictions support consequential decisions, deployment can change the outcome distribution the model aims to predict.

Source-native loop:

~~~text
model / prediction
-> decision / action
-> changed target / observed data distribution
-> changed risk / retraining environment
-> later model
~~~

The framework represents this through a model-dependent distribution map.

## 3. Performative stability

The paper defines performative stability as an equilibrium notion in which predictions are calibrated not against only past outcomes, but against outcomes that arise after acting on the prediction.

The source also studies retraining dynamics and conditions under which repeated retraining converges.

## 4. Pressure on GRG X4b

The source provides a non-biological realization of the burden frozen before this target close-read:

~~~text
current activity changes a later conditioning field / distribution
-> that changed field alters later learning / risk / decision conditions
~~~

This is structurally stronger than generic distribution shift because the deployed predictor participates in producing the shift.

## 5. Mechanism ownership

Performative-prediction theory owns:

- the model-dependent distribution map;
- performative risk;
- performative stability;
- retraining dynamics;
- strategic / decision-feedback mechanisms.

GRG may compare the dependency topology.

It does not own or replace these mechanisms.

## 6. Pressure on X4b wording

The existing phrase:

~~~text
recursive selective / viability feedback
~~~

is biologically colored.

The existing admission text already allowed:

~~~text
selection / viability / accessibility / transition pressures
~~~

The performative-prediction match therefore does not require changing the dependency direction, but it suggests a source-neutral programme gloss:

~~~text
recursive reconstructed-field feedback
~~~

with biological selective / viability feedback as one specialization.

Any such rename is programme-level only and must retain the original admission burden.

## 7. Maturity implication

This is independent source-native evidence outside biology.

Therefore it can pressure X4b beyond DOMAIN-LIMITED status if semantic invariance holds.

But the machine-learning literature already explicitly owns the feedback problem.

Therefore:

~~~text
possible M3 = YES
M4 = NO from this source alone
scientific distinctiveness = not established
~~~

## 8. Integration target

Operations/GRG/Transfers/SRT_GRG_TR_X4B_01_PERFORMATIVE_PREDICTION_2026-09-21.md

Operations/Audits/SRT_GRG_M3_M4_CROSSDOMAIN_TRANSFER_ABSORPTION_PASS1_2026-09-21.md
