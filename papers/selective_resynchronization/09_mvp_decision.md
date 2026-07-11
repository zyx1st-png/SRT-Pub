---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-DECISION-20260711
type: empirical_gate_decision
status: final_mvp_gate_v1_1_manual_audit
canonical: false
created: 2026-07-11
---

# Fashion-MNIST MVP Decision

## Decision: NO-GO

This decision applies only to the locked MVP and follows the criteria in `06_mvp_spec_lock.md`.

## Criterion audit

- GO checks: `{'positive_beta_bootstrap_excludes_zero': False, 'cv_increment_meets_threshold': False, 'beats_representation_baseline': False, 'leave_condition_stable': False, 'one_robustness_consistent': False, 'no_seed_sign_flip': False, 'score_robustness': True, 'leakage_valid': True}`;
- upheld NO-GO reason 1: the full standardized coefficient was `-0.2521`, its seed-bootstrap interval was `[-0.5667, 0.1156]`, and every leave-one-condition and leave-one-seed coefficient was negative;
- upheld NO-GO reason 2: the locked control model `M0` reached CV R-squared `0.9311`, while adding `SR_preC` changed CV R-squared by only `0.0004`, below the locked `0.01` increment boundary for this kill rule;
- automated-trigger correction: `leave_one_component_direction_flips` is not upheld because the five alternative coefficients were uniformly negative rather than sign-flipping. The raw automated JSON is preserved; removing this mistaken third label does not change the decision because either upheld major rule independently triggers NO-GO;
- Fisher status: `lose`;
- state-classification status: `{'counts': {'disorganization_or_unresolved_opening': 26, 'candidate_selective_resynchronization': 14}, 'leave_one_seed_label_agreement': 0.625, 'figure_valid': False, 'reason': 'leave-one-seed modal-label agreement below 0.70'}`.

## Consequences

- enter CIFAR-10 now: **no; await human review**;
- selective-resynchronization term: **withdraw or reframe**;
- four-state classification: **downgrade/remove**;
- Fisher: **do not privilege**;
- retained-plasticity reframe: **required for review**.

The base-model finding concerns the complete locked control set, not B accuracy alone. The negative result is therefore: this `SR_preC` operationalization supplied no stable, practically meaningful increment beyond the locked endpoint/condition controls in this Fashion-MNIST protocol.

The experiment and decision stop here. No CIFAR-10 run and no full-paper drafting is authorized without human review.
