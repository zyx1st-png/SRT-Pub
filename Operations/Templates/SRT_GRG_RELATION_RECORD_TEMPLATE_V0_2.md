---
id: SRT-GRG-RELATION-RECORD-TEMPLATE-V0-2
type: template
status: active
version: v0.2
date: 2026-09-21
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Proposals/SRT_GRG_MINIMAL_ARCHITECTURE_V0_1_2026-09-21.md
  - Operations/Audits/SRT_GRG_G0_G11_FOUNDATIONAL_RETYPING_PASS1_2026-09-21.md
  - Operations/Audits/SRT_GRG_RELATION_LIBRARY_FOUNDATIONAL_RETYPING_PASS1_2026-09-21.md
  - Operations/Templates/SRT_GRG_RELATION_RECORD_TEMPLATE_V0_1.md
tags: [GRG, Template, RelationRecord, Verticality, Objectification, Evidence, ArchitectureRole]
---

# Template — GRG Relation Record v0.2

Use one record for one source-native relation candidate.

v0.2 separates:

~~~text
source-native mechanism
architecture role
horizontal / vertical status
proxy / representation
relation family
expectation
validation maturity
~~~

Do not encode all of these in one relation label.

Do not start from an SRT / GRG label and search for a matching example.

## A. Identity

~~~text
record_id =
domain =
source-native name =
source / dataset / case =
record status = candidate / active / narrowed / split / retired

architecture role =
  upstream_constraint /
  horizontal_realization /
  vertical_core /
  vh_interface /
  composite /
  expectation /
  normativity /
  reflexive /
  proxy_trace /
  validation

mapping maturity = M0 / M1 / M2 / M3 / M4 / M5
~~~

Architecture role and M-level are independent.

## B. Research-question / verticality declaration

~~~text
research question =
stabilized objectification =
what is treated as given =
what is reopened as a formation / reconstruction question =

horizontal baseline =
vertical claim, if any =
horizontal-to-vertical bridge assumption =
what evidence would distinguish the vertical claim
from a richer horizontal model =

verticality status =
  horizontal /
  vertical candidate /
  vertical supported /
  V-H interface /
  not applicable
~~~

Guard:

~~~text
vertical status
!= inherent property of an entity

vertical status
= indexed to research question + objectification
~~~

## C. Source-native account

~~~text
what happens =
participants / components =
mechanism as stated by the source/domain =
scale / grain =
time structure =
position(s), if source-native =
boundary conditions =
~~~

State the source-native explanation before GRG abstraction.

## D. Evidence

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

## E. Objectification / proxy declaration

~~~text
unit / object =
boundary =
grain / timescale =
normalization =
aggregation / pooling =
proxy / representation =
archive / inclusion rule =

what the representation preserves =
what it may hide =
what would invalidate proxy -> organization inference =
~~~

Hard guard:

~~~text
proxy / trace
!= vertical organization automatically

proxy failure
!= proof of an unspecified deeper vertical cause
~~~

## F. Formation / maintenance fields

~~~text
formation process =
formed organization =
maintenance / regeneration process =
maintenance provenance =
withdrawal / dissolution condition =
~~~

These are currently cross-cutting burdens.

Do not assume Formation or Maintenance is already a separate primitive GRG family.

## G. Generative dependency

~~~text
prior / component process =
formed organization / relation =
later process conditioned =
claimed dependency direction =
changed accessibility / transition / viability / differentiation condition =
withdrawal / perturbation condition =
failure condition =
~~~

For a vertical-core claim, state what generative condition is formed, retained or reconstructed.

## H. Architecture-family mapping

Use the current typed map where warranted:

~~~text
upstream:
  C0 non-exhaustion / non-preclosure
  C1 differential manifestation / relative backgrounding

vertical core candidates:
  R-HIST-a retained efficacy / later conditioning
  R-HIST-b recurrent reconstitution
  R-LOC local generative locus / individuation
  R-POS operative positionality
  R-RECON reconstructed generative condition

composition:
  C-MULTI multi-locus relational composition
  C-XSC cross-scale composition / recursion

expectation / normativity:
  E-B structural generative expectation
  E-C0 embodied / enacted anticipation
  E-C1 model-mediated anticipation
  N-INDEX indexed normative comparison

reflexive:
  L-REFLEX-W world / civilizational reflexive learning
  L-REFLEX-M GRG methodological self-revision

open:
  R-FORM
~~~

Record:

~~~text
candidate family / families =
composition_of =
what is actually paid =
what is not paid =
nearest false-positive mapping =
SRT-specific specialization invoked? =
~~~

Guard:

~~~text
GRG R-LOC != SRT One automatically
GRG R-POS != Selection-position automatically
R-RECON != Agency automatically
~~~

## I. Consequence typing

~~~text
CONSEQ-H generic consequence -> later conditioning =
CONSEQ-P position / locus-indexed consequence return =
CONSEQ-B same-One prospective exposure, Bearer-facing if paid =
~~~

Do not collapse all consequence return into Bearer or normativity.

## J. Generative expectation

~~~text
typed relation =
structural expectation E-B =
horizontal prediction, if applicable =
vertical generative expectation, if applicable =
E-C0 embodied / enacted realization, if any =
E-C1 model-mediated realization, if any =
what would count as mismatch =
~~~

For a strong grammar claim:

~~~text
relation -> expectation
~~~

must be derivationally traceable.

Do not infer goodness from expectation.

## K. Normativity interface — only if warranted

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

If not warranted:

~~~text
normativity mapping = NOT OPENED
~~~

## L. Composition declaration — when role = composite

~~~text
component relation 1 =
component relation 2 =
additional components =
composition rule =
new dependency burden created by composition =
why this is not just a list of components =
composition failure condition =
~~~

## M. Cross-domain comparison

| Compared record | Shared burden | Mechanism difference | Objectification difference | Architecture role | Evidence difference | Mapping status | Important mismatch |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## N. Revision pressure

~~~text
what would narrow this record =
what would split it =
what would retype architecture role =
what would falsify the GRG mapping =
what domain evidence would force GRG revision =
~~~

Allowed revision operations:

~~~text
ADMIT
RETAIN
NARROW
SPLIT
MERGE
RETYPE
RETIRE
~~~

## O. Transfer / validation

~~~text
unseen domain / case =
pre-result question changed =
control / variable / distinction changed =
what result would count as failure =

M3 independent-match basis =
M4 pre-result transfer basis =
target selected before decisive source/outcome inspection? =
target-domain ordinary-practice comparator =
~~~

Guard:

~~~text
M3 / M4
= validation maturity

M3 / M4
!= architecture role
!= ontology status
~~~

Retrospective renaming is not transfer.

## P. Reflexive-learning status

~~~text
does this case model reflexive learning as a world phenomenon? =
does it cause a GRG methodological revision? =
world realization L-REFLEX-W =
methodological revision L-REFLEX-M =
~~~

Do not identify social/scientific learning with GRG governance merely because both are reflexive.

## Q. Provenance

~~~text
source-derived =
author adjudication =
machine synthesis =
current canonical constraint =
open =
~~~

## R. Compact summary

~~~text
source-native relation =
architecture role =
verticality status =
GRG family / composition =
proxy / objectification status =
burden paid =
evidence =
mapping maturity =
generative expectation =
normativity status =
strongest guard =
revision state =
next action =
~~~
