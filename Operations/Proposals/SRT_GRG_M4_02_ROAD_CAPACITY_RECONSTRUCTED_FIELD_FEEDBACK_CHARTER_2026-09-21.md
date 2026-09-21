---
id: SRT-GRG-M4-02-ROAD-CAPACITY-RECONSTRUCTED-FIELD-FEEDBACK-CHARTER-20260921
type: preregistration
status: active
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: research_programme
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Templates/SRT_GRG_M4_TRANSFER_CHARTER_TEMPLATE_V0_1.md
  - Operations/GRG/SRT_GRG_RELATION_LIBRARY_V0_1.md
tags: [GRG, M4, X4b, Transport, RoadCapacity, InducedDemand, ProspectiveTransfer]
---

# GRG M4-02 prospective charter — road capacity and reconstructed-field feedback

## 0. Freeze metadata

~~~text
M4 attempt id = M4-02
relation = X4b recursive reconstructed-field feedback
target domain = urban / metropolitan transportation planning
target system / case = road-capacity expansion and later traffic adaptation
date/time frozen = 2026-09-21 / before dedicated target-source audit
base commit = 9df670b08a915e4ada96a7db2a9fdb34c431c114
dedicated target-source audit performed before freeze? = NO
~~~

Known prior background that cannot be erased:

~~~text
generic public/common background:
road-capacity changes can affect traffic demand and congestion;
the phrase "induced demand" is already known at a generic level.

not yet inspected for this attempt:
whether mature transport-planning practice already owns
the exact frozen distinction, matched control and failure test below.
~~~

This attempt is valid only as a prospective design test beyond that generic background.

## 1. Frozen GRG burden

Relation definition:

~~~text
X4b — recursive reconstructed-field feedback

current activity A
-> reconstructs a typed conditioning field F
-> F changes later selection / viability / accessibility /
   distribution / transition conditions on process P
-> the A -> F -> later-P mediation is source-native and evidenced.
~~~

Target translation frozen before target-source audit:

~~~text
A = road-capacity expansion
F = generalized travel-cost / accessibility / route-capacity field
P = later traveler route, time, mode and trip-generation choices
    plus resulting network loading / congestion state
~~~

Admission burden:

1. the capacity intervention must measurably alter F;
2. later travel behavior / network loading must respond through F;
3. later congestion / utilization must differ from a matched fixed-demand / no-adaptation counterfactual;
4. generic traffic growth without A -> F mediation does not pay X4b.

Non-identities:

~~~text
more road capacity != X4b by itself
more traffic later != X4b by itself
population growth != induced feedback automatically
one-shot travel-time improvement != recursive feedback
generic path dependence != X4b
~~~

Negative control:

~~~text
same road-capacity addition
+ demand / route-choice / trip-generation response held fixed
-> first-order engineering effect only
-> does not pay the recursive later-P burden.
~~~

Current M-status:

~~~text
X4b = M3
M4 = NONE
~~~

## 2. Target-domain translation — frozen before source audit

Source-neutral target question:

> When evaluating a road-capacity intervention, does explicitly separating the immediate supply-side travel-time effect from the later reconstructed demand/accessibility feedback change the target-domain analysis in a way not already standard in transport planning?

Candidate target variables:

~~~text
F1 = generalized travel cost / travel-time accessibility change after capacity addition
P1 = vehicle trips / VKT / route loading after behavioral adaptation
P2 = congestion / travel-time state after adaptation

derived:
benefit-retention ratio
= later travel-time/cost benefit divided by immediate post-capacity benefit

feedback-rebound fraction
= share of the initial congestion/travel-time gain eroded after
  demand / route / trip adaptation.
~~~

Candidate control:

~~~text
Arm FIXED:
same network and capacity intervention;
trip table / route participation / trip-generation response held fixed
except for immediate assignment required by the source-native model.

Arm ADAPTIVE:
same network and capacity intervention;
later route / time / mode / trip-generation response allowed
through the changed generalized-cost/accessibility field.

comparison:
same first-order capacity shock,
different admission of reconstructed-field feedback.
~~~

Candidate intervention/comparison:

~~~text
before capacity addition
vs
immediate post-addition
vs
post-adaptation horizon
~~~

Expected failure mode:

~~~text
if later traffic change is explained by exogenous population/economic growth
without mediation through the capacity-induced field F,
X4b is not paid.
~~~

Semantic failure:

~~~text
if F cannot be specified independently enough to distinguish
capacity-induced reconstruction from the outcome being redescribed,
the mapping fails.
~~~

## 3. Proposed GRG transfer gain

Frozen proposed gain:

### New distinction

~~~text
first-order capacity effect
!=
recursive reconstructed-field feedback
~~~

### New control

~~~text
capacity-matched fixed-demand/no-adaptation counterfactual
vs
capacity-matched adaptive-demand/route counterfactual
~~~

### New variable

~~~text
benefit retention / rebound after adaptation,
not only immediate change in road speed/capacity.
~~~

### New failure expectation

~~~text
traffic growth after road expansion
does not count as X4b unless the A -> F -> later-P mediation is paid.
~~~

M4 requires that at least one of these changes ordinary target-domain design rather than restating standard transport practice.

## 4. M4-E0 absorption-before-execution gate

After this commit, audit mature transportation planning / transport economics / traffic-assignment practice.

Record:

~~~text
target field already owns immediate-vs-adaptive distinction? = TBD
target field already owns fixed-demand vs induced/adaptive control? = TBD
target field already owns rebound / benefit-retention concept? = TBD
target field already requires mediated induced-demand evidence? = TBD
repository-local target work already owns it? = TBD
separate replication reason exists? = NO by default
~~~

### ABSORBED rule

If mature target practice already owns the same distinction/control and there is no independent replication rationale:

~~~text
M4-02 = M4-ABSORBED
M4 = NO
STOP before duplicate simulation or empirical analysis.
~~~

### DESIGN-CANDIDATE rule

Only if at least one frozen GRG element is not already ordinary target-domain practice:

~~~text
M4-02 = M4-DESIGN-CANDIDATE
~~~

Then freeze an exact execution charter before any target outcome inspection.

## 5. No execution yet

This charter does not authorize:

- traffic simulation;
- new empirical analysis;
- policy ranking;
- transport-policy recommendation;
- source-result cherry-picking after inspection.

First run M4-E0.

## 6. Canonical boundary

~~~text
canonical edit = NO
scientific distinctiveness = NOT ESTABLISHED
M5 = NONE
policy recommendation = NONE
~~~
