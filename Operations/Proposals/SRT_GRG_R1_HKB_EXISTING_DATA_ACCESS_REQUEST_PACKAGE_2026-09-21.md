---
id: SRT-GRG-R1-HKB-EXISTING-DATA-ACCESS-REQUEST-PACKAGE-20260921
type: proposal
status: active
date: 2026-09-21
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_GRG_R1_HKB_SOURCE_PROTOCOL_ACCESS_FEASIBILITY_2026-09-21.md
  - Materials/2026/SRC_2026_09_21_HKB_Post2020_Normalization_Reanalysis.md
tags: [GRG, GRGR1, HKB, DataAccess, RequestPackage, RawTrajectories]
---

# GRG-R1 HKB existing-data access request package

## 0. Purpose

This package prepares a bounded request for the original Post et al. bimanual-coordination perturbation data.

It does not authorize:

- sending the request automatically;
- opening / analyzing any received files before a new raw-data charter;
- new human data collection;
- simulation substitution;
- R1d / O4;
- canonical edits.

## 1. Preferred contact route

Primary current route:

~~~text
Harjo J. de Poel
University Medical Center Groningen / University of Groningen
current public institutional contact:
h.j.de.poel@umcg.nl
~~~

Reason:

- first author of the 2020 reanalysis;
- the 2020 paper used the original Post dataset;
- current research remains in coordination dynamics / coupled-oscillator movement science.

Secondary current routes, ordered by current legacy-data custody evidence:

~~~text
Lieke Peper
Vrije Universiteit Amsterdam / Neurocontrol
l.peper@vu.nl

Melvyn Roerdink
Vrije Universiteit Amsterdam
m.roerdink@vu.nl
~~~

Peper is an author of the original 2000 frequency/amplitude study and the 2020 reanalysis; the 2020 contribution statement also assigns resources and data-curation roles to Peper.

Institutional fallback if authors cannot identify the archive / controller:

~~~text
VU Faculty of Behavioural and Movement Sciences
Research Data Steward
research.data.fgb@vu.nl
~~~

Current public-route verification is recorded in:
`Operations/Audits/SRT_GRG_R1_HKB_PUBLIC_ACCESS_ROUTE_VERIFICATION_2026-09-21.md`.

Do not assume any individual or data steward still controls the data. The request asks for routing if they do not.

## 2. Exact data object requested

Request the smallest data package that can support a source-faithful trajectory-level reanalysis.

### Required

~~~text
raw or minimally processed bilateral angular-displacement time series
sampling timestamps / sampling-rate metadata
participant identifier pseudonyms
trial identifier
coordination mode: in-phase / anti-phase
pacing frequency condition
amplitude instruction condition
performed / derived amplitude where available
perturbation trial vs catch trial
perturbation onset / release timing or motor-command marker
arm perturbed
session / block / trial order
exclusion / quality flags if retained
~~~

### Strongly preferred

~~~text
original preprocessing scripts or formulas
peak / half-cycle indices if stored
original relative-phase series
original lambda fit outputs and fit-quality measures
mapping to participant-level supplementary outcomes
documentation of units and coordinate conventions
~~~

### Not necessary for the current question

~~~text
direct personal identifiers
video
clinical information
any data not needed for movement-trajectory reconstruction
~~~

## 3. Why raw trajectories are necessary

The 2020 reanalysis demonstrates that the phase estimate is sensitive to normalization.

The intended analysis must therefore be able to recompute:

~~~text
half-cycle normalization
continuous phase
relative phase
performed amplitude
performed frequency
oscillation-centre shifts
post-perturbation return trajectory
lambda / alternate relaxation fits
~~~

Aggregate outcome tables cannot pay this burden.

## 4. Reuse / ethics questions to ask

The request should explicitly ask:

1. whether the original raw or minimally processed data still exist;
2. who currently controls them;
3. whether they can be shared for a non-commercial scholarly reanalysis;
4. whether a data-use agreement is required;
5. whether institutional ethics / privacy review is required for secondary analysis;
6. whether participant consent or de-identification places restrictions on reuse;
7. whether a citation / acknowledgement condition applies;
8. whether analysis scripts from the 2020 reanalysis can also be shared.

Do not treat receipt of an informal file as automatic authorization for publication.

## 5. Suggested concise request

Subject:

~~~text
Request for original Post et al. interlimb-coordination perturbation data
~~~

Draft:

~~~text
Dear Dr. de Poel,

I am conducting a non-commercial theoretical and methodological study of
perturbation-relaxation in human interlimb coordination. I have been working
from Post, Peper & Beek (2000) and your 2020 Brain Sciences reanalysis
(DOI 10.3390/brainsci10100724).

The specific question requires reproducing the tightened half-cycle
normalization and separating relative-phase relaxation from performed
amplitude, frequency and oscillation-centre changes. For that reason,
the published aggregate outcomes are not sufficient.

Would the original bilateral angular-displacement time series from the
Post et al. perturbation experiment still be available for scholarly
secondary analysis? If so, I would be grateful to know the appropriate
data-access route and any data-use, ethics, de-identification, citation
or collaboration requirements.

The minimum useful package would be the de-identified bilateral movement
time series together with condition labels and perturbation timing.
If the data are held by another author or institution, a pointer to the
appropriate contact would be equally helpful.

I would not redistribute the data and would agree the reuse conditions
before analysis or publication.

Best regards,
[author]
~~~

This draft intentionally does not make an SRT / GRG novelty claim. The initial request should be intelligible and scientifically grounded without asking the data holder to endorse the theory.

## 6. Response routing

### Access granted / route identified

Do not inspect outcome data immediately.

First create:

~~~text
HKB RAW-DATA ANALYSIS CHARTER v0.1
~~~

Freeze:

- data object / exclusions;
- phase normalization;
- component controls;
- relaxation models;
- R1c failure conditions;
- subject / condition hierarchy;
- confirmatory vs exploratory outputs.

Only then open / compute target results.

### Data exist but cannot be shared

Record:

~~~text
HKB ACCESS = EXISTING / UNAVAILABLE TO THIS PROJECT
~~~

Do not weaken to aggregate analysis.

Proceed to another non-RNN R1c candidate if the programme remains active.

### Data no longer exist

Record:

~~~text
HKB ACCESS = HISTORICAL DATA LOST / NO-GO
~~~

Keep HKB as source-native R1c pressure, not an executable new test.

### No response

A non-response is not evidence that data do not exist.

After one reasonable follow-up route, record:

~~~text
CURRENT ACCESS = UNRESOLVED
~~~

and do not block the whole GRG programme indefinitely.

## 7. Current authorization

~~~text
request-package preparation = COMPLETE
current public contact routes = VERIFIED 2026-09-21
public raw trajectory repository = STILL NOT LOCATED
institutional archive fallback = IDENTIFIED
first request sent to Harjo de Poel = YES / 2026-09-21
response = PENDING
follow-up / secondary contact = NOT YET SENT
raw data access = NO
raw data opened = NO
analysis charter = NOT YET AUTHORIZED
new human experiment = NO
R1d / O4 = BLOCKED
canonical edit = NO
~~~
