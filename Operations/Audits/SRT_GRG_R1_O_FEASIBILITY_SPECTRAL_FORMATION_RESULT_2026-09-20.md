---
id: SRT-GRG-R1-O-FEASIBILITY-SPECTRAL-FORMATION-RESULT-20260920
type: experimental_result
status: active
date: 2026-09-20
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/grg_r1_o_feasibility/SPECTRAL_FORMATION_PROTOCOL_v0_1.md
  - Operations/Audits/SRT_GRG_R1_PRODUCTIVE_ADEQUACY_O_CRITERION_REVISION_PASS1_2026-09-20.md
tags: [GRG, GRGR1, O1, SpectralFormation, RNN, TargetBlind, Feasibility]
---

# GRG-R1 O-feasibility Pass A — spectral formation result

## Verdict

~~~text
O1-SPECTRAL-PASS
~~~

All fresh-seed networks passed base competence:

~~~text
S = 12 / 12
D = 12 / 12
base accuracy = 1.0 for every network
~~~

Frozen paired-seed history classification result:

~~~text
Leave-One-Seed-Pair-Out accuracy = 1.00
1000 within-pair label-swap permutations
permutation p = 0.000999000999000999
null mean accuracy = 0.498875
null 95% interval = [0.25, 0.75]
~~~

## Interpretation

Under the frozen top-four recurrent-eigenvalue feature, structured and direct training histories leave a reproducibly separable imprint in the current recurrent operator.

This pays the O1 formation pressure for this candidate family:

~~~text
manipulated history
-> retained operator spectral difference
~~~

O2 is also structurally plausible because the measured object is the current recurrent weight operator rather than an activity decoder.

This result does not pay O3 causal mediation or O4 prospective re-entry.

## Contrast with v0.1

v0.1 showed:

~~~text
context decodability != causal retained organization by default.
~~~

Pass A now shows:

~~~text
history can leave a current operator-level spectral imprint
even though a decoder-defined activity subspace failed the causal transfer test.
~~~

The programme should therefore continue with operator-embedded candidates rather than tuning the old decoder-O.

## Next gate

~~~text
O1 formation: PASS
O2 retained operator structure: CANDIDATE PAID
O3 target-blind causal mediation: NEXT
O4 prospective re-entry: HOLD
v0.2 target execution: HOLD
~~~

O3 must remain on the base/source-domain surface and must not inspect any new transfer target.
