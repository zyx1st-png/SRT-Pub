---
source_id: SRC-2026-09-21-COORDINATION-DYNAMICS-HKB-R1C-CANDIDATE
id: SRC-2026-09-21-COORDINATION-DYNAMICS-HKB-R1C-CANDIDATE
title: "HKB coordination dynamics — relative phase, control parameter and perturbation-relaxation"
source_type: primary_theory_plus_primary_experiment_bundle
domain: human_bimanual_coordination_nonlinear_dynamics
primary_authors: "J. A. Scott Kelso; Hermann Haken; H. Bunz; A. A. Post; C. E. Peper; A. Daffertshofer; P. J. Beek"
date_added: "2026-09-21"
evidence_level: primary_1985_fulltext_close_read_plus_primary_experimental_abstracts
reliability_level: high_for_HKB_order_parameter_model_and_basic_frequency_transition; moderate_high_for_perturbation_relaxation_routing_without_full_2000_article_close_read
srt_relevance: very_high_for_non_RNN_GRG_R1b_R1c_candidate_selection
integration_priority: high
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags: [HKB, CoordinationDynamics, RelativePhase, OrderParameter, Perturbation, Relaxation, GRGR1]
---

# SourceCard — HKB coordination dynamics as a non-RNN GRG-R1c candidate

## 1. Source bundle

Primary anchors:

- Kelso (1984), Phase transitions and critical behavior in human bimanual coordination, American Journal of Physiology, DOI 10.1152/ajpregu.1984.246.6.R1000.
- Haken, Kelso & Bunz (1985), A theoretical model of phase transitions in human hand movements, Biological Cybernetics 51:347-356, DOI 10.1007/BF00336922.
- Post, Peper, Daffertshofer & Beek (2000), Relative phase dynamics in perturbed interlimb coordination: stability and stochasticity, Biological Cybernetics 83:443-459, DOI 10.1007/s004220000177.
- Post et al. follow-up on frequency/amplitude separation, PMID 11130585.

The 1985 HKB paper was available as full text and close-read for the load-bearing order-parameter claims. The perturbation papers are routed from primary abstracts in this pass; a future execution charter must close-read the full perturbation method first.

## 2. Source-native phenomenon

Human bimanual rhythmic coordination can sustain both:

~~~text
in-phase coordination
and
anti-phase coordination
~~~

at lower cycling frequencies.

When cycling frequency is increased, anti-phase coordination loses stability and an abrupt transition to in-phase coordination occurs. The transition shows a control-parameter / bifurcation structure rather than requiring an independently posited discrete switch.

The 1985 HKB model reproduces this behavior with a potential over relative phase.

## 3. Order parameter

Relative phase is defined as:

~~~text
phi = phi_2 - phi_1
~~~

where phi_1 and phi_2 are phases of the component hand motions.

HKB proposes relative phase as an order parameter because:

- it reflects cooperativity among the component motions;
- subsystem configuration specifies the phase relation;
- conversely, the phase relation specifies the spatiotemporal ordering of the subsystems;
- it is relatively invariant across scalar changes where many component-level quantities vary.

This is a source-native macro/relational variable, not a GRG invention.

## 4. Control parameter

Movement cycling frequency serves as an experimentally manipulated scaling variable.

The model relates increasing movement frequency to changes in the potential landscape / stability of coordination states. At a critical regime, anti-phase loses stability and the system moves to the in-phase attractor.

Guard:

~~~text
control parameter != order parameter
~~~

External pacing / frequency changes the stability landscape; relative phase characterizes the coordinative organization.

This distinction is directly useful for GRG because a variable that drives a transition must not automatically be called the maintained organization O.

## 5. Perturbation / relaxation evidence

Post et al. 2000 explicitly studied HKB stability under mechanical perturbation.

Primary abstract routing:

~~~text
perform in-phase or anti-phase coordination
at several movement frequencies
-> apply mechanical perturbation
-> measure continuous relative-phase relaxation
-> estimate stability / stochastic HKB parameters
~~~

The follow-up frequency/amplitude study separated frequency and amplitude effects and used both relative-phase variability and post-perturbation relaxation as stability measures.

This supplies a source-native R1c candidate:

~~~text
maintained coordination organization
-> perturb coordination
-> observe return / relaxation / loss of stability
~~~

## 6. Maintenance provenance

For the experimental HKB paradigm, maintenance provenance is best typed as:

~~~text
MIXED / COUPLED
~~~

Reason:

- the relative-phase coordination is maintained by the coupled human neuromuscular system;
- the experiment externally imposes instructions / pacing frequency;
- mechanical perturbation is externally applied;
- the experiment does not externally clamp relative phase itself in the same sense as Bowler's repeated eigenvalue resets.

Therefore:

~~~text
endogenous coordination under externally controlled boundary / pacing conditions
~~~

is more accurate than either pure endogenous or pure exogenous-clamp labeling.

## 7. GRG-R1 typing

### R1a retained imprint

Not the main burden.

The paradigm is about ongoing coordination, not primarily a historical marker.

### R1b maintained scaffold

Strong candidate.

Relative phase describes a maintained coordination regime with identifiable stability properties.

### R1c causal re-entry

Strong candidate for protocol reconstruction.

Perturbation-relaxation gives a direct way to ask whether the coordinative organization constrains subsequent component trajectories / return dynamics.

However, the future GRG protocol must not infer macro causal independence merely from model fit.

### R1d prospective transfer

Not established and not authorized.

No new context/transfer target should be imported into this candidate.

## 8. Why this is genuinely different from the toy RNN route

RNN route:

~~~text
training history
-> persistent operator marker
-> candidate later learning effect
~~~

HKB route:

~~~text
ongoing component coupling
-> maintained relational coordination
-> controlled destabilization / perturbation
-> relaxation, transition or loss of coordination
~~~

Thus the candidate tests GRG-R1c on continuous self-organization rather than sedimented historical structure.

## 9. GRG-specific pre-result distinction

GRG adds a required four-way declaration before any new analysis:

~~~text
component variables
!= control parameter
!= maintained order parameter / coordination
!= perturbation operator
~~~

For HKB:

~~~text
component variables = individual limb trajectories / phases / amplitudes
control parameter = pacing / cycling frequency
candidate O = relative-phase coordination regime
perturbation = mechanical phase-displacing perturbation
outcome = relaxation / stability / transition
~~~

This decomposition must be fixed before result inspection.

## 10. Failure / anti-overclaim guards

Do not infer:

- relative phase is an ontologically independent substance;
- HKB proves GRG or SRT;
- every low-dimensional collective variable is an order parameter;
- behavioral order parameter = One / Bearer / subject;
- successful HKB model fit proves macro-to-micro causal autonomy;
- external pacing is endogenous maintenance;
- perturbation recovery proves R1d transfer.

## 11. Candidate status

~~~text
candidate domain = bimanual coordination dynamics
R1b source-native basis = YES
R1c perturbation basis = YES
maintenance provenance = MIXED / COUPLED
non-RNN = YES
new experiment authorization = NO
next = protocol / access feasibility audit only
~~~
