---
id: SRT-GRG-INHERITANCE-CARRIER-ARCHITECTURE-V0-1-20260921
type: research_architecture
status: active
version: v0.1
date: 2026-09-21
layer: meta
epistemic_layer: os
claim_mode: research_programme
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/GRG/SRT_GRG_RELATION_LIBRARY_V0_1.md
  - Operations/Audits/SRT_GRG_CIV006_X4C_INHERITANCE_CROSSSURFACE_PASS1_2026-09-21.md
  - Operations/Audits/SRT_GRG_X4C_IPV4_IPV6_CARRIER_PROVENANCE_PASS1_2026-09-21.md
  - Operations/Audits/SRT_GRG_X4C_PRECEDENT_PINST_CARRIER_PASS1_2026-09-21.md
tags: [GRG, X4c, CarrierArchitecture, Provenance, Inheritance, Composition]
---

# GRG Inheritance Carrier Architecture v0.1

## 0. Role

This surface types **how an X4c reconstructed field is carried into a successor cohort / cycle**.

It does not define a new GRG relation.

It replaces an overly simple reading of inheritance provenance as mutually exclusive labels.

Core correction:

~~~text
carrier provenance
!= one mandatory single label

carrier provenance
= compositional architecture when evidence requires it.
~~~

## 1. X4c remains the relation

X4c admission remains:

~~~text
reconstructed field F
+ inheritance carrier architecture C
+ successor cohort / later participant
+ successor enters under F without making original reconstruction choice
+ F materially changes later action / accessibility /
  maintenance / transition possibilities.
~~~

This file types C.

It does not modify the relation topology itself.

## 2. Carrier component record

Represent a carrier architecture as:

~~~text
C = {c1, c2, ... cn}

ci = <
  source-native component,
  provenance kind,
  causal role,
  role evidence / near-control,
  standalone sufficiency status
>
~~~

The purpose is to prevent:

~~~text
"mixed"
from becoming
"everything mattered somehow."
~~~

## 3. Provenance kinds

Current non-exhaustive kinds:

~~~text
P-MAT
= material / infrastructural component

P-ECO
= ecological / environmental component

P-INST
= institutional authority / rule / organizational component

P-INFO
= informational / symbolic content component

P-MIXED
= shorthand only for an explicitly decomposed multi-component architecture
~~~

These are operational provenance kinds.

They are not ontology entities.

Future source-native cases may require refinement.

## 4. Causal-role vocabulary

Roles are source-sensitive.

Current recurring roles include:

~~~text
PAYLOAD
= carries content / rule / configuration / inherited specification

SUBSTRATE
= materially or environmentally preserves the field

AUTHORITY
= determines binding / admissibility / mandatory force

ENACTMENT
= makes an abstract rule / specification operative in practice

MAINTENANCE
= keeps the carrier / field available across later cycles

REPRODUCTION
= recreates enough of the carrier into a successor cycle

INTERFACE
= determines compatibility / access between successor process and inherited field
~~~

This list is not exhaustive.

Do not force every case into every role.

## 5. Sufficiency / evidence status

For each component, distinguish:

~~~text
STANDALONE-PASS
= source evidence supports this component architecture as sufficient
  for the declared X4c inheritance burden.

COMPONENT-ROLE-PASS
= the component has an independently supported causal role
  inside a mixed carrier, but standalone sufficiency is not established.

PRESENT / ROLE-OPEN
= component is present but its causal role is not separately established.

NOT-ESTABLISHED
= requested standalone or role claim is not paid.

FAIL
= evidence contradicts the proposed role / provenance claim.
~~~

No status changes X4c maturity by itself.

## 6. Worked carrier architectures

### 6.1 Ecological inheritance

~~~text
C = {
  c1:
    provenance = P-ECO
    role = SUBSTRATE / MAINTENANCE
    evidence = modified environmental state persists into later organisms
    status = STANDALONE-PASS for current source-native ecological case family
}
~~~

### 6.2 CIV-006 combined-sewer legacy

~~~text
C = {
  c1:
    provenance = P-MAT
    role = SUBSTRATE / MAINTENANCE / INTERFACE
    evidence = maintained material hydraulic network
               conditions successor operation / retrofit
    status = STANDALONE-PASS for declared material-inheritance burden
}
~~~

Modern regulation may add E-LEGAL expectation provenance.

That does not make regulation the inheritance carrier.

### 6.3 IPv4 -> IPv6 installed base

~~~text
C = {
  c1:
    provenance = P-INFO
    role = PAYLOAD
    evidence = protocol / address semantics participate in inherited compatibility field
    status = COMPONENT-ROLE-PASS

  c2:
    provenance = P-MAT / technical deployment
    role = SUBSTRATE / ENACTMENT / INTERFACE
    evidence = installed hosts / routers / applications / routing infrastructure
    status = COMPONENT-ROLE-PASS

  c3:
    provenance = P-INST
    role = MAINTENANCE / operational coordination
    evidence = standards / deployment practice support coexistence
    status = COMPONENT-ROLE-PASS
}

overall = P-MIXED
P-INFO standalone = NOT-ESTABLISHED
~~~

### 6.4 CIV-007 precedent / stare decisis

~~~text
C = {
  c1:
    provenance = P-INFO
    role = PAYLOAD
    evidence = prior holding / legal rule provides inherited content
    status = COMPONENT-ROLE-PASS

  c2:
    provenance = P-INST
    role = AUTHORITY
    evidence = binding vs persuasive authority differs by hierarchy / jurisdiction
    near-control = persuasive authority / case of first impression
    status = COMPONENT-ROLE-PASS
}

overall = P-MIXED

P-INST standalone total carrier = NOT-ESTABLISHED
P-INFO standalone total carrier = NOT-ESTABLISHED
~~~

## 7. Near-control rule

Where possible, a carrier-role claim should have a near-control.

Examples:

~~~text
installed base
vs
greenfield

binding precedent
vs
persuasive authority

controlling precedent
vs
case of first impression
~~~

A near-control need not be a randomized experiment.

It must isolate enough of the proposed role to make the component claim informative.

## 8. Standalone provenance rule

Do not award a standalone provenance category because one component appears salient.

Require:

~~~text
the declared component architecture
is sufficient for successor inheritance
under the source-native case
without an essential second carrier component.
~~~

If not:

~~~text
use P-MIXED
+ decompose components
+ state causal roles.
~~~

## 9. Relation / carrier / expectation separation

Keep three layers distinct:

~~~text
relation identity:
X4c

carrier architecture:
how F reaches successor cohort

expectation provenance:
what source creates the "ought-like" / continuation burden
~~~

Therefore:

~~~text
P-INST carrier role
!=
E-LEGAL expectation

P-INFO payload
!=
E-TECH expectation

P-MAT substrate
!=
moral obligation
~~~

## 10. Failure modes

### FM-1 — label inflation

~~~text
everything with text -> P-INFO
everything with an institution -> P-INST
~~~

Reject.

### FM-2 — P-MIXED as escape hatch

~~~text
unclear mechanism -> call it mixed
~~~

Reject.

Components and roles must be listed.

### FM-3 — carrier / relation collapse

~~~text
same carrier kind
-> same GRG relation
~~~

Reject.

### FM-4 — carrier / normativity collapse

~~~text
institution carries field
-> institution is legitimate
~~~

Reject.

## 11. Programme status

~~~text
P-ECO standalone = PASS in current ecological inheritance family
P-MAT standalone = PASS in CIV-006 material inheritance

P-INFO standalone = OPEN / NOT ESTABLISHED
P-INST standalone = OPEN / NOT ESTABLISHED

P-INFO component role = PASS in mixed cases
P-INST component role = PASS in precedent mixed case

P-MIXED = valid only when decomposed
~~~

## 12. Next gate

Do not hunt standalone provenance categories merely to fill the table.

Next framework question:

> Does carrier-role decomposition improve prediction / exclusion / revision across existing cases enough to justify keeping provenance as a first-class GRG analysis surface?

A later pass should compare:

- whether role decomposition blocks false X4c admissions;
- whether it predicts which near-control is required;
- whether it exposes redundant provenance categories.

## 13. Canonical boundary

~~~text
canonical edit = NO
new ontology entity = NO
M4/M5 = NONE
scientific distinctiveness = NOT ESTABLISHED
~~~
