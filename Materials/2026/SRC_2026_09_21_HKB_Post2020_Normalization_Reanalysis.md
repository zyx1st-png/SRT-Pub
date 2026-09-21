---
source_id: SRC-2026-09-21-HKB-POST-2020-NORMALIZATION-REANALYSIS
id: SRC-2026-09-21-HKB-POST-2020-NORMALIZATION-REANALYSIS
title: "de Poel et al. 2020 — tightened normalization reanalysis of perturbed interlimb coordination"
source_type: peer_reviewed_primary_reanalysis_of_original_experimental_data
domain: human_bimanual_coordination_relative_phase_measurement
primary_authors: "Harjo J. de Poel; Melvyn Roerdink; C. (Lieke) E. Peper; Peter J. Beek"
publication: "Brain Sciences"
doi: "10.3390/brainsci10100724"
date_published: "2020-10-13"
date_added: "2026-09-21"
evidence_level: full_text_open_access_reanalysis_of_original_Post2000_data
reliability_level: high_for_normalization_artifact_and_reanalysis_results; bounded_for_any_GRG_mapping
srt_relevance: very_high_as_analysis_validity_pressure_for_HKB_R1c_feasibility
integration_priority: very_high
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags: [HKB, RelativePhase, Perturbation, Relaxation, Normalization, MeasurementArtifact, Amplitude, GRGR1]
---

# SourceCard — de Poel et al. 2020 normalization reanalysis

## 1. Primary source

de Poel, H. J., Roerdink, M., Peper, C. L. E. & Beek, P. J. (2020).

*A Re-Appraisal of the Effect of Amplitude on the Stability of Interlimb Coordination Based on Tightened Normalization Procedures.*

Brain Sciences 10(10):724.

DOI: 10.3390/brainsci10100724

The paper reanalyzes the original data from Post, Peper & Beek (2000), DOI 10.1007/s004220000185.

## 2. Why this source changes the HKB feasibility question

The original perturbation paradigm is attractive for GRG-R1c because it appears to offer:

~~~text
maintained relative-phase coordination
-> mechanical perturbation
-> relaxation back toward coordination
~~~

However, de Poel et al. show that the numerical construction of phase can itself be distorted by perturbation-induced changes in:

- oscillation centre;
- movement amplitude;
- local half-cycle geometry.

Therefore a post-perturbation relative-phase relaxation signal can contain analysis artifacts if position / velocity are normalized using one average over the whole trial.

For GRG, this is a decisive objectification pressure:

~~~text
measured order parameter
!= maintained organization automatically
~~~

A candidate R1c effect is admissible only if the phase construction survives the measurement transformation used to make component trajectories comparable.

## 3. Reconstructed original experiment

The reanalysis used pre-existing data from six healthy female right-handed volunteers, ages 20–27.

Apparatus:

- participants sat in a modified chair;
- each forearm moved around the elbow in the horizontal plane;
- angular displacement was measured with a hybrid potentiometer;
- sampling rate was 300 Hz;
- torque motors could block an arm based on current position / velocity.

Experimental factors:

~~~text
coordination mode:
  in-phase / anti-phase

movement frequency:
  one unpaced preferred condition
  plus paced 0.75..2.25 Hz in 0.25 Hz steps

movement amplitude:
  one free-amplitude condition
  plus prescribed 0.1, 0.2, 0.3 rad
~~~

The mechanical perturbation consisted of full arrest of the right arm near peak elbow extension, where velocity was near zero.

The arrest lasted one quarter of a movement cycle and displaced the interlimb coordination by approximately 90 degrees.

Perturbation timing was randomized between cycles 12 and 17.

This is an intervention on a component that induces a controlled coordination displacement; it is not a direct metaphysical intervention on an isolated macro variable.

## 4. Data-reduction correction

Original-style analysis normalized signals at the whole-trial level before deriving continuous phase.

de Poel et al. argue that this can generate artificial phase fluctuations when perturbation changes centre or amplitude.

Their correction:

~~~text
identify successive half cycles from angular-displacement peaks
-> centre / normalize position and velocity within each half cycle
-> then compute phase angle
-> then compute relative phase
~~~

This tightened half-cycle normalization is the relevant default for any future HKB GRG reanalysis.

The source therefore invalidates a future protocol that simply reproduces the old whole-trial normalization without an explicit robustness comparison.

## 5. Stability / relaxation variables

The source family uses at least two distinct stability measures:

~~~text
stationary variability:
  SD(relative phase)

perturbation recovery:
  relaxation exponent lambda
~~~

These must not be conflated.

The relaxation analysis attempts to isolate the return of relative phase after the mechanical displacement, while amplitude and frequency remain separate measured / manipulated quantities.

For GRG-R1c, lambda is a candidate consequence variable, not candidate O itself.

## 6. Reanalysis pressure on amplitude

The reanalysis makes performed amplitude a stronger explanatory variable than the original interpretation suggested.

Safe consequence:

~~~text
instructed amplitude
!= performed amplitude
!= relative-phase organization
~~~

A future feasibility / execution package must retain performed component amplitude and oscillation-centre changes as controls or explanatory variables.

Otherwise a relation-level relaxation effect may actually be a component-kinematic artifact.

## 7. Exclusion / robustness pressure

The reanalysis reports materially fewer excluded perturbed trials after tightened normalization than the earlier procedure.

This means exclusion rate is itself partly analysis-pipeline dependent.

Future use must therefore preregister:

- phase-normalization rule;
- return-signal start rule;
- fitting family;
- exclusion criteria;
- sensitivity to alternate normalization.

Do not choose these after observing a desired R1c effect.

## 8. Data-access evidence

The paper explicitly states that it reanalyzed the original Post et al. data and acknowledges Auke Post for conducting the experiment and making the data available.

The online supplementary material includes participant-level outcome values.

In the present 2026-09-21 feasibility search, no public repository containing the original 300 Hz raw trajectory time series was located.

Therefore:

~~~text
full-text method access = YES
participant-level supplementary outcome access = YES
public raw trajectory access = NOT LOCATED
historical author-held / shared-data route = EVIDENCED
current reusable raw-data authorization = NOT ESTABLISHED
~~~

"Not located" must not be rewritten as "no raw data exist anywhere".

## 9. GRG-R1c relevance

The source strengthens the HKB candidate only conditionally.

It supports a cleaner prospective decomposition:

~~~text
component state
  = left/right angular position, velocity, performed amplitude/frequency

external control parameter
  = pacing / cycling frequency and experimental instruction

candidate maintained O
  = relative-phase coordination regime

perturbation
  = mechanically induced component arrest / phase displacement

consequence
  = normalized relative-phase relaxation / stability / transition
~~~

But it also supplies a hard failure route:

if the apparent relation-level relaxation is not robust to component-aware phase normalization, it cannot count as evidence for R1c causal re-entry.

## 10. What this source does not license

Do not infer:

- relative phase is ontologically independent of limb trajectories;
- lambda proves downward causation;
- HKB proves GRG or SRT;
- performed amplitude can be treated as nuisance by definition;
- a low-dimensional observable is an order parameter merely because it is decodable;
- historical storage is required for R1c;
- the original raw data are publicly reusable.

## 11. Integration target

Primary writeback target:

Operations/Audits/SRT_GRG_R1_HKB_SOURCE_PROTOCOL_ACCESS_FEASIBILITY_2026-09-21.md

No canonical target is authorized.
