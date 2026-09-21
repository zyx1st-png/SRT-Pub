---
id: SRT-GRG-R1-HKB-SOURCE-PROTOCOL-ACCESS-FEASIBILITY-20260921
type: audit
status: active
record_stage: hkb_source_protocol_access_feasibility_complete
date: 2026-09-21
layer: operations
epistemic_layer: experimental
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
comparative_claim: none
named_comparator: none
n_mode_triggered: false
dependency:
  - Materials/2026/SRC_2026_09_21_CoordinationDynamics_HKB_R1C_Candidate.md
  - Materials/2026/SRC_2026_09_21_HKB_Post2020_Normalization_Reanalysis.md
  - Operations/Audits/SRT_GRG_R1_NONRNN_R1C_CANDIDATE_SELECTION_PASS1_2026-09-21.md
tags: [GRG, GRGR1, HKB, R1c, ProtocolFeasibility, DataAccess, RelativePhase, Perturbation, Normalization]
---

# GRG-R1 HKB source / protocol-access feasibility audit

## 0. Verdict

~~~text
SOURCE CLOSE-READ = PASS

PROTOCOL RECONSTRUCTION = PASS

GRG VARIABLE TYPING = PASS

ANALYSIS-VALIDITY GUARD = PASS / MATERIAL REVISION REQUIRED
  old whole-trial phase normalization is not sufficient by default;
  half-cycle / component-aware normalization must be carried forward.

PUBLIC RAW TRAJECTORY ACCESS = NO-GO / NOT LOCATED

PARTICIPANT-LEVEL SUPPLEMENTARY OUTCOME ACCESS = YES / INSUFFICIENT FOR RAW R1c REANALYSIS

HISTORICAL AUTHOR-HELD DATA ROUTE = PLAUSIBLE / EVIDENCED
CURRENT AUTHORIZED RAW-DATA ROUTE = NOT ESTABLISHED

NEW HUMAN EXPERIMENT = NOT AUTHORIZED
SIMULATION-AS-CONFIRMATION = NOT AUTHORIZED
R1c NEW EXECUTION = HOLD
R1d / O4 = BLOCKED
CANONICAL EDIT = NO
~~~

The HKB candidate survives source / protocol reconstruction, but it does not currently pass the data-access gate for a new trajectory-level GRG execution.

## 1. Source package actually closed

Primary theory / transition anchors already owned in the HKB candidate SourceCard:

- Kelso 1984 — frequency-driven transition / critical behavior;
- Haken, Kelso & Bunz 1985 — relative phase as collective variable / order-parameter model;
- Post, Peper, Daffertshofer & Beek 2000, DOI 10.1007/s004220000177 — perturbation-relaxation / stochastic stability route.

The present feasibility pass closes the method and measurement burden with:

- Post, Peper & Beek 2000, DOI 10.1007/s004220000185 — frequency × amplitude perturbation experiment;
- de Poel, Roerdink, Peper & Beek 2020, DOI 10.3390/brainsci10100724 — reanalysis of the original Post data using tightened phase normalization.

Important correction:

the detailed perturbation-method reconstruction in this pass is anchored primarily to the 2000 frequency/amplitude experiment and its 2020 reanalysis. Do not attribute every method detail to DOI 10.1007/s004220000177 without a separate method-level check.

## 2. Exact experimental object

### Bearer / participant

Original dataset:

~~~text
6 healthy female right-handed participants
age 20-27
~~~

This small sample limits population-level inference but does not by itself invalidate within-person perturbation dynamics.

### Component variables

Required component-level state:

~~~text
left angular position
right angular position
left angular velocity
right angular velocity
performed movement amplitude
performed movement frequency
oscillation centre / local offset
~~~

These are not nuisance variables by definition.

### External control variables

~~~text
coordination instruction:
  in-phase / anti-phase

pacing / cycling frequency:
  unpaced preferred condition
  and paced 0.75..2.25 Hz in 0.25-Hz steps

amplitude instruction:
  free amplitude
  or prescribed 0.1 / 0.2 / 0.3 rad
~~~

Guard:

~~~text
control parameter != maintained organization O
~~~

### Candidate maintained O

~~~text
relative-phase coordination regime
~~~

Operational observable:

~~~text
phi_rel = phi_right - phi_left
~~~

This is a relation constructed from component trajectories.

Its status as candidate O depends on robust organization / stability evidence, not merely dimensional reduction.

### Perturbation operator

Mechanical arrest of the right arm:

~~~text
near peak elbow extension
where velocity is near zero
full arrest for one quarter of a movement cycle
approximately 90-degree coordination displacement
randomized between cycles 12 and 17
~~~

The experiment perturbs a physical component and thereby displaces the coordination relation.

Therefore:

~~~text
component perturbation
!= direct isolated intervention on O
~~~

Any GRG causal language must retain this mediation fact.

### Consequence / return variables

At least two source-native stability families:

~~~text
stationary:
  SD(relative phase)

perturbation recovery:
  return trajectory
  relaxation exponent lambda
~~~

For R1c, the relaxation family is the more direct source-native causal probe.

## 3. Measurement pipeline required before any GRG use

### Signal processing

Source method:

~~~text
angular displacement
-> numerical differentiation to velocity
-> bidirectional second-order Butterworth low-pass filtering
   cutoff = 25 Hz
-> cycle / half-cycle segmentation
-> position / velocity normalization
-> continuous phase
-> relative phase
~~~

Sampling:

~~~text
300 Hz
~~~

### Critical 2020 correction

The original whole-trial normalization is vulnerable when a perturbation changes:

- movement amplitude;
- oscillation centre;
- local trajectory geometry.

de Poel et al. therefore normalize / centre successive half cycles separately before phase determination.

For this programme:

~~~text
half-cycle / local component-aware normalization
= mandatory primary analysis route for any future raw-data execution
~~~

The old whole-trial normalization may be retained only as a declared sensitivity comparator.

This is not cosmetic preprocessing. It changes which trials are considered analyzable and changes the inferred amplitude dependence of stability.

## 4. Relaxation reconstruction

The historical analysis defines a post-perturbation return signal relative to the pre-perturbation coordination state and estimates a relaxation strength.

A generic source-faithful form is:

~~~text
relative-phase displacement after perturbation
-> return trajectory toward pre-perturbation coordination
-> exponential or damped-relaxation fit
-> lambda as return / stability parameter
~~~

The exact historical fitting choices must be preserved as source provenance.

A future GRG execution should additionally preregister a robustness layer rather than choosing fit family after outcome inspection.

Minimum robustness set:

1. half-cycle-normalized phase;
2. explicit performed amplitude and frequency;
3. local oscillation-centre shift;
4. fit-quality criterion;
5. identical exclusion rules across coordination / frequency / amplitude conditions;
6. sensitivity to the historical fit-start rule.

## 5. GRG variable declaration

The candidate now supports a clean pre-result declaration:

~~~text
component state
= limb position / velocity / amplitude / frequency / centre

external control parameter
= pacing / instruction / prescribed amplitude condition

maintained O
= relative-phase coordination regime

perturbation
= mechanical right-arm arrest causing phase displacement

later process / consequence
= post-release component trajectory
  + relative-phase relaxation
  + stability / transition
~~~

Maintenance provenance:

~~~text
MIXED / COUPLED
~~~

Reason:

- ongoing organismic coupling regenerates the coordination;
- pacing / instruction define experimental boundary conditions;
- the perturbation is externally imposed;
- relative phase is not continuously externally clamped.

## 6. What would count as R1c evidence

The minimum causal burden is not:

~~~text
relative phase exists
or
relative phase is low-dimensional
or
HKB fits the mean pattern
~~~

A source-level HKB R1c case requires:

~~~text
maintained coordination regime
+ controlled perturbation
+ component-aware measurement
-> regime-sensitive post-perturbation transition / relaxation
that is not exhausted by generic component rebound,
performed amplitude, performed frequency or measurement artifact.
~~~

This remains compatible with ordinary coordination-dynamics explanation.

It is a GRG realization test, not a distinctiveness test.

## 7. Hard failure conditions

A future HKB R1c execution fails for GRG purposes if any of the following obtains.

### F1 — normalization collapse

The coordination-specific relaxation effect disappears or materially changes sign / ordering under the tightened half-cycle normalization.

Interpretation:

the old effect was too dependent on measurement objectification.

### F2 — component sufficiency

Performed amplitude, frequency, oscillation-centre shift and component kinematics explain the apparent relaxation difference without residual coordination-regime dependence.

Interpretation:

no additional relation-level causal burden is earned at the declared grain.

### F3 — perturbation non-specificity

The observed return time is determined by generic mechanical arrest / release magnitude rather than the maintained coordination regime.

Interpretation:

the intervention is component damage / displacement, not a discriminating R1c test.

### F4 — fit fragility

The result depends on one post hoc fit start, exclusion rule or relaxation family and fails preregistered robustness checks.

### F5 — bearer / condition pooling

The result appears only after pooling subjects or frequency/amplitude regimes in a way that erases subject-level or condition-level reversals.

### F6 — insufficient data object

Only aggregate / participant outcome tables are available, without the raw position time series required to reconstruct phase, amplitude, centre and relaxation.

Interpretation:

new trajectory-level R1c execution is not authorized.

### F7 — source-native explanation already exhausts the gain

Even if the effect is robust, GRG adds only relabeling and changes no variable declaration, control, failure test or inference.

Interpretation:

R1c may be realized in the domain, but no GRG transfer gain is earned.

## 8. Data-access audit

### Publicly available now

Located:

- full-text 2020 reanalysis;
- full method description sufficient to reconstruct the experiment;
- supplementary participant-level outcome table associated with the reanalysis.

Not located in the bounded search:

~~~text
original 300-Hz left/right angular-displacement trajectories
trial-level perturbation timestamps
raw condition / trial identifiers sufficient for full reprocessing
~~~

Therefore:

~~~text
PUBLIC-RAW-DATA-0 = NO-GO / NOT LOCATED
~~~

This is not a universal claim that the data no longer exist.

### Evidence for a non-public reuse route

The 2020 paper explicitly states that it reanalyzed the original Post et al. dataset and acknowledges Auke Post for conducting the experiment and making the data available.

This establishes:

~~~text
historical reusable data object existed
~~~

but not:

~~~text
current access granted to this project
~~~

Therefore:

~~~text
AUTHOR / COLLABORATOR REQUEST ROUTE = PLAUSIBLE
CURRENT AUTHORIZATION = NONE
~~~

## 9. Execution decision

Because the raw trajectories are necessary to:

- recompute phase under tightened normalization;
- model performed amplitude / frequency;
- quantify oscillation-centre changes;
- reconstruct trial-level relaxation;
- run component-sufficiency controls;

the supplementary aggregate outcomes are insufficient for the intended GRG R1c execution.

Hence:

~~~text
new analysis on public aggregate data = NOT AN R1c EXECUTION
simulation replication = NOT A SUBSTITUTE
new human data collection = NOT AUTHORIZED
R1c empirical execution = HOLD
~~~

## 10. What the feasibility pass positively earns

Even with access NO-GO, the pass is productive.

### Protocol gain

The HKB route supplies a genuinely non-RNN R1c causal architecture:

~~~text
ongoing coupling
-> maintained coordination
-> component perturbation
-> regime-sensitive relaxation / transition
~~~

### GRG revision gain

It strengthens two programme rules.

First:

~~~text
R1b/R1c formation
need not be sedimented history;
it may be continuously regenerated.
~~~

Second:

~~~text
candidate O must survive its measurement / normalization interface.
~~~

This second rule is forced by the 2020 reanalysis and should generalize beyond HKB as an objectification guard.

## 11. Next authorized step

Do not weaken the question to fit public aggregate data.

Next bounded route:

~~~text
existing-data access route audit / request package
~~~

Required before any execution:

1. identify current author / institutional data-request route;
2. request or verify availability of raw bilateral angular-displacement trajectories and condition / perturbation metadata;
3. verify reuse terms / ethics / de-identification requirements;
4. if access becomes real, create a new visible raw-data analysis charter before opening files;
5. if access is unavailable, preserve HKB as source-level R1c realization pressure and move to another non-RNN candidate rather than substituting a weaker dataset.

Still blocked:

~~~text
new human experiment
simulation-as-confirmation
R1d / O4
canonical reassessment
winner-style strongest-neighbor novelty audit
~~~
