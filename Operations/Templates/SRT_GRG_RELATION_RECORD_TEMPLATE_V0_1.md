---
id: SRT-GRG-RELATION-RECORD-TEMPLATE-V0-1
type: template
status: archived
version: v0.1
date: 2026-09-21
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Proposals/SRT_GRG_RESEARCH_FRAMEWORK_V0_1_2026-09-21.md
  - Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md
tags: [GRG, Template, RelationRecord, CrossDomain, Evidence, Objectification]
---

# Template — GRG Relation Record v0.1

> Legacy schema retained for existing relation-record provenance. New process-first GRG records use `Operations/Templates/SRT_GRG_GENERATIVE_TRANSFORMATION_RECORD_TEMPLATE_V0_2.md`.
>
> Do not use this file as the primary schema for new foundational work.

Use one record for one source-native candidate relation when maintaining a legacy record.

Do not start from an SRT label and search for a matching example.

## A. Identity

~~~text
record_id =
domain =
source-native name =
source / dataset / case =
record status = candidate / active / narrowed / split / retired
mapping status = M0 / M1 / M2 / M3 / M4 / M5
M3 independent-match basis =
M4 pre-result transfer basis =
target selected before decisive source/outcome inspection? =
target-domain ordinary-practice comparator =
~~~

## B. Source-native account

~~~text
what happens =
participants / components =
mechanism as stated by the source/domain =
scale / grain =
time structure =
position(s) =
boundary conditions =
~~~

State the source-native explanation before GRG mapping.

## C. Evidence

~~~text
evidence family = E1..E10
source reliability =
causal leverage =
replication / robustness =
measurement dependence =
major confounds =
transportability =
~~~

Do not compress these into one confidence score by default.

## D. Objectification declaration

~~~text
unit / object =
boundary =
grain / timescale =
normalization =
aggregation / pooling =
proxy / representation =
archive / inclusion rule =
what is lost or hidden =
~~~

## E. Generative relation candidate

~~~text
prior / component process =
formation =
retained / maintained organization =
maintenance provenance =
inheritance carrier architecture, if applicable =
architecture cardinality = SINGLE-COMPONENT / MULTI-COMPONENT / n.a.
carrier components =
component provenance metadata = P-MAT / P-ECO / P-INST / P-INFO / other / n.a.
component causal role(s) = use Role Library where applicable; source-local role only if needed
role evidence / near-control =
component status = COMPONENT-ROLE-PASS / ROLE-CANDIDATE-PRE-ADMISSION / PRESENT-ROLE-OPEN / NOT-ESTABLISHED / FAIL
persistence process = PASSIVE-PERSISTENCE / ACTIVE-MAINTENANCE / RECURRENT-REPRODUCTION / MIXED / OPEN
minimal role set sufficient for X4c =
architecture sufficiency = PASS / OPEN / FAIL
successor cohort / later participant, if applicable =
later process conditioned =
claimed dependency direction =
withdrawal / perturbation condition =
failure condition =
~~~

Reusable X4c carrier-role owner:

Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ROLE_LIBRARY_V0_1.md

Guard:

~~~text
MAINTENANCE persistence process
!=
carrier component role

Admission-order guard:

~~~text
carrier-role plausibility
!=
X4c admission

if successor boundary / field transmission is OPEN:
use ROLE-CANDIDATE / PRE-ADMISSION,
not COMPONENT-ROLE-PASS.
~~~
~~~

## F. GRG burden mapping

~~~text
candidate G-burden(s) =
sub-burden(s), if any =
what is actually paid =
what is not paid =
nearest false-positive mapping =
~~~

Example guard:

~~~text
R1a retained imprint
!= R1c causal re-entry

X4c persistence
!= successor inheritance
~~~

## G. Generative expectation

~~~text
typed relation =
structural expectation =
C0 embodied/enacted realization, if any =
C1 model-mediated realization, if any =
what would count as mismatch =
~~~

Do not infer goodness from expectation.

## G.1 Generative expectation provenance

Where a relation carries a structural expectation, type its provenance:

~~~text
E-MAT = material / infrastructural constraint
E-TECH = technical / interface constraint
E-LEGAL = legal / regulatory requirement
E-ORG = organizational / institutional rule-in-use
E-NORM = social / normative expectation
E-BIO = biological / viability relation
E-MODEL = model-mediated / analytic expectation
E-MIXED = multiple layers
~~~

Record separately:

~~~text
expectation provenance =
structural expectation =
expectation failure =
multiple provenance layers? =
~~~

Guard:

~~~text
material expectation != legal obligation
legal obligation != moral legitimacy
technical compatibility != social norm
~~~

## H. Normativity interface — only if warranted

~~~text
indexed position =
affected bearer(s), if established =
scale =
time horizon =
G-stronger / G-weaker dimension =
externalized consequence =
conflicting positions =
additional moral / legitimacy premise required =
~~~

If not warranted, write:

~~~text
normativity mapping = NOT OPENED
~~~

## I. Cross-domain comparison

| Compared record | Shared burden | Mechanism difference | Evidence difference | Mapping status | Important mismatch |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## J. Revision pressure

~~~text
what would narrow this record =
what would split it =
what would falsify the GRG mapping =
what domain evidence would force GRG revision =
~~~

## K. Transfer candidate

~~~text
unseen domain / case =
pre-result question changed =
control / variable / distinction changed =
what result would count as failure =
~~~

Retrospective renaming is not transfer.

~~~text
M3 recurrence != M4 transfer gain.

M3 may be earned by an independently evidenced source-native match
after the relation was frozen.

M4 requires prospective target-domain gain:
a new variable / control / distinction / failure expectation
specified before decisive target-source/outcome inspection,
and not already supplied by ordinary target-domain practice.
~~~

## L. Provenance

~~~text
source-derived =
author adjudication =
machine synthesis =
current canonical constraint =
open =
~~~

## M. Compact summary

~~~text
source-native relation =
GRG candidate =
burden paid =
evidence =
mapping status =
generative expectation =
normativity status =
strongest guard =
next action =
~~~
