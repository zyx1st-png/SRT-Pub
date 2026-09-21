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
  provenance metadata,
  causal role(s),
  role evidence / near-control,
  component status
>

architecture cardinality =
SINGLE-COMPONENT / MULTI-COMPONENT

minimal role set sufficient for X4c =
architecture sufficiency =
PASS / OPEN / FAIL
~~~

The purpose is to prevent:

~~~text
"mixed"
from becoming
"everything mattered somehow."
~~~

## 3. Provenance metadata

Current non-exhaustive medium / source descriptors:

~~~text
P-MAT
= material / infrastructural component

P-ECO
= ecological / environmental component

P-INST
= institutional authority / rule / organizational component

P-INFO
= informational / symbolic content component
~~~

These are component metadata.

They are not mutually exclusive carrier classes.

They do not receive relation maturity.

Historical `P-MIXED` is retired as a provenance kind.

Use instead:

~~~text
architecture cardinality =
SINGLE-COMPONENT
or
MULTI-COMPONENT
~~~

and list the actual components.

Core correction:

~~~text
provenance kind tells us what a component is / where it comes from.

causal role tells us what that component does in successor inheritance.
~~~

## 4. Causal-role vocabulary

Reusable role owner:

Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ROLE_LIBRARY_V0_1.md

Role-census owner:

Operations/Audits/SRT_GRG_INHERITANCE_CARRIER_ROLE_CENSUS_PASS1_2026-09-21.md

Current reusable roles:

~~~text
CORE:
SUBSTRATE
PAYLOAD
INTERFACE

SPECIALIZED:
AUTHORITY
~~~

Current non-admitted / retyped terms:

~~~text
ENACTMENT
= CASE-LOCAL / NARROW
= not independently distinguished from INTERFACE / implementation in current X4c records.

REPRODUCTION
= OPEN / NOT PAID as reusable component role.

MAINTENANCE
= RETYPED from component role to architecture-level persistence process.
~~~

Source-local roles may still be recorded when a mature domain requires them.

They do not become reusable library roles without a later census.

### 4.1 Persistence process

Record separately:

~~~text
persistence process =
PASSIVE-PERSISTENCE
ACTIVE-MAINTENANCE
RECURRENT-REPRODUCTION
MIXED
OPEN
~~~

This asks how carrier architecture C remains available across the successor boundary.

It is not itself a component causal role.

## 5. Sufficiency / evidence status

For each component, distinguish:

~~~text
COMPONENT-ROLE-PASS
= the component has an independently supported causal role
  in the declared carrier architecture.

COMPONENT-SUFFICIENT
= the case record supports a single-component architecture
  as sufficient for the declared X4c inheritance burden.

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
cardinality = SINGLE-COMPONENT

C = {
  c1:
    provenance metadata = P-ECO
    role = SUBSTRATE
    evidence = modified environmental state persists into later organisms
    status = COMPONENT-SUFFICIENT for this declared case family

persistence process = PASSIVE-PERSISTENCE / source-bounded
}
~~~

### 6.2 CIV-006 combined-sewer legacy

~~~text
cardinality = SINGLE-COMPONENT

C = {
  c1:
    provenance metadata = P-MAT
    role = SUBSTRATE / INTERFACE
    evidence = maintained material hydraulic network
               conditions successor operation / retrofit
    status = COMPONENT-SUFFICIENT for this declared case
}

persistence process = ACTIVE-MAINTENANCE / MIXED over long horizon
~~~

Modern regulation may add E-LEGAL expectation provenance.

That does not make regulation the inheritance carrier.

### 6.3 IPv4 -> IPv6 installed base

~~~text
cardinality = MULTI-COMPONENT

C = {
  c1:
    provenance metadata = P-INFO
    role = PAYLOAD
    evidence = protocol / address semantics participate in inherited compatibility field
    status = COMPONENT-ROLE-PASS

  c2:
    provenance metadata = P-MAT
    role = SUBSTRATE / INTERFACE
    evidence = installed hosts / routers / applications / routing infrastructure
    status = COMPONENT-ROLE-PASS

  c3:
    provenance metadata = P-INST
    proposed role = MAINTENANCE / operational coordination
    evidence = standards / deployment practice are present
    status = PRESENT / ROLE-OPEN
}

minimal paid role set =
PAYLOAD + SUBSTRATE + INTERFACE

source-local ENACTMENT wording =
NARROW / does not strengthen admission

persistence process =
MIXED / source-local

architecture sufficiency = PASS

P-INFO as a single-component architecture = NOT-ESTABLISHED
~~~

### 6.4 CIV-007 precedent / stare decisis

~~~text
cardinality = MULTI-COMPONENT

C = {
  c1:
    provenance metadata = P-INFO
    role = PAYLOAD
    evidence = prior holding / legal rule provides inherited content
    status = COMPONENT-ROLE-PASS

  c2:
    provenance metadata = P-INST
    role = AUTHORITY
    evidence = binding vs persuasive authority differs by hierarchy / jurisdiction
    near-control = persuasive authority / case of first impression
    status = COMPONENT-ROLE-PASS
}

minimal paid role set =
PAYLOAD + AUTHORITY

architecture sufficiency = PASS

single-component P-INST architecture = NOT-ESTABLISHED
single-component P-INFO architecture = NOT-ESTABLISHED
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

## 8. Architecture sufficiency rule

Do not award a provenance category a global "standalone" status.

Ask instead:

~~~text
for this source-native case,
what is the minimal component / role architecture
sufficient to transmit the reconstructed field into the successor cohort?
~~~

If one component is enough:

~~~text
cardinality = SINGLE-COMPONENT
~~~

If several are necessary:

~~~text
cardinality = MULTI-COMPONENT
~~~

Unsupported claimed components remain:

~~~text
PRESENT / ROLE-OPEN
~~~

and cannot strengthen X4c admission.

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

## 11. Programme status after role census Pass 1

Adequacy owner:

Operations/Audits/SRT_GRG_INHERITANCE_CARRIER_ARCHITECTURE_ADEQUACY_PASS1_2026-09-21.md

Role-census owner:

Operations/Audits/SRT_GRG_INHERITANCE_CARRIER_ROLE_CENSUS_PASS1_2026-09-21.md

Role Library:

Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ROLE_LIBRARY_V0_1.md

Current state:

~~~text
CARRIER ARCHITECTURE = RETAIN / PRODUCTIVE
CAUSAL-ROLE-FIRST MODEL = ACTIVE
P-MIXED AS PROVENANCE KIND = RETIRED

Role Library v0.1 = EARNED

CORE:
SUBSTRATE
PAYLOAD
INTERFACE

SPECIALIZED:
AUTHORITY

NOT ADMITTED:
ENACTMENT
REPRODUCTION

RETYPED:
MAINTENANCE -> persistence process
~~~

Current case-bounded states:

~~~text
ecological inheritance =
SINGLE-COMPONENT
P-ECO / SUBSTRATE
persistence process = PASSIVE-PERSISTENCE
architecture PASS

CIV-006 =
SINGLE-COMPONENT
P-MAT / SUBSTRATE+INTERFACE
persistence process = ACTIVE-MAINTENANCE / MIXED
architecture PASS

IPv4/IPv6 =
MULTI-COMPONENT
P-INFO / PAYLOAD = PASS
P-MAT / SUBSTRATE+INTERFACE = PASS
P-INST proposed maintenance role = ROLE-OPEN
source-local ENACTMENT = NARROW
architecture PASS

precedent =
MULTI-COMPONENT
P-INFO / PAYLOAD = PASS
P-INST / AUTHORITY = PASS
architecture PASS
~~~

No carrier role receives M0-M5 status.

## 12. Next gate

Do not hunt standalone provenance categories merely to fill the table.

Adequacy Pass 1 answered the prior question positively for the carrier architecture and negatively for provenance-kind-first classification.

The bounded role census is COMPLETE and a minimal Role Library is earned.

Next gate:

> Can the Role Library sharpen an existing negative / borderline X4c record without converting it into a positive case by analogy?

Primary target:

~~~text
CIV-005 beaver ecosystem engineering.
~~~

Use existing evidence only. Do not add a new positive case in the same step.

## 13. Canonical boundary

~~~text
canonical edit = NO
new ontology entity = NO
M4/M5 = NONE
scientific distinctiveness = NOT ESTABLISHED
~~~
