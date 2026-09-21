---
id: SRT-GRG-INHERITANCE-CARRIER-ROLE-CENSUS-PASS1-20260921
type: audit
status: active
record_stage: carrier_role_census_pass1
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ARCHITECTURE_V0_1.md
  - Operations/Audits/SRT_GRG_INHERITANCE_CARRIER_ARCHITECTURE_ADEQUACY_PASS1_2026-09-21.md
  - Materials/2026/SRC_2026_09_21_Niche_Construction_Ecological_Inheritance.md
  - Operations/GRG/Cases/SRT_GRG_CIV_006_COMBINED_SEWER_LEGACY_2026-09-21.md
  - Operations/Audits/SRT_GRG_X4C_IPV4_IPV6_CARRIER_PROVENANCE_PASS1_2026-09-21.md
  - Operations/GRG/Cases/SRT_GRG_CIV_007_PRECEDENT_INSTITUTIONAL_INHERITANCE_2026-09-21.md
tags: [GRG, X4c, CarrierRole, Census, Simplification, RoleLibrary]
---

# GRG X4c inheritance carrier-role census — Pass 1

## 0. Purpose

This is the bounded census authorized after carrier-architecture adequacy Pass 1.

No new external case is added.

Question:

> Are the current carrier roles recurrent and discriminating enough to justify a reusable Role Library?

Candidate vocabulary inherited from Carrier Architecture v0.1:

~~~text
PAYLOAD
SUBSTRATE
AUTHORITY
ENACTMENT
MAINTENANCE
REPRODUCTION
INTERFACE
~~~

## 1. Admission rule for a reusable role

A role enters a reusable Role Library only if it meets either:

### Route R — recurrence

~~~text
paid in >= 2 independent source-native carrier records
+
non-identity from adjacent roles is clear
+
it predicts at least one useful exclusion / control / failure condition
~~~

or:

### Route D — uniquely discriminating specialization

~~~text
paid in 1 strong source-native record
+
the role is necessary to explain a contrast that adjacent roles cannot explain
+
there is a strong near-control isolating the role
~~~

Route D permits a specialized library entry.

It does not imply broad recurrence.

## 2. Paid-role census

Only paid roles count.

ROLE-OPEN proposals do not count.

| Role | Ecological inheritance | CIV-006 sewer | IPv4/IPv6 | CIV-007 precedent | Paid recurrence |
|---|---|---|---|---|---:|
| SUBSTRATE | PASS | PASS | PASS | — | 3 |
| PAYLOAD | — | — | PASS | PASS | 2 |
| INTERFACE | — | PASS | PASS | — | 2 |
| AUTHORITY | — | — | — | PASS | 1 |
| ENACTMENT | — | — | PASS | — | 1 |
| MAINTENANCE | PASS* | PASS* | ROLE-OPEN | — | 2 nominal |
| REPRODUCTION | — | — | — | — | 0 |

Asterisks on MAINTENANCE are deliberate.

Its status requires semantic review before counting it as a component role.

## 3. SUBSTRATE

Working meaning:

~~~text
a component materially / environmentally preserves enough of F
for the successor cohort to encounter the inherited field.
~~~

Paid records:

1. ecological inheritance — modified environmental state;
2. CIV-006 — maintained material hydraulic network;
3. IPv4/IPv6 — installed hosts / routers / applications / routing infrastructure.

### Non-identity

~~~text
SUBSTRATE
!=
PAYLOAD
~~~

A substrate can preserve a field without carrying a symbolic rule/content payload.

~~~text
SUBSTRATE
!=
INTERFACE
~~~

A substrate can persist without the claimed successor access/compatibility pathway being established.

### Predicted failure condition

~~~text
remove / lose persistence of the substrate
while holding the reconstruction history fixed
->
successor cohort no longer encounters enough of F
->
X4c inheritance burden weakens or fails.
~~~

### Verdict

~~~text
REUSABLE CORE ROLE = PASS
Route R
~~~

## 4. PAYLOAD

Working meaning:

~~~text
a component carries structured inherited content
whose identity matters to the successor field.
~~~

Paid records:

1. IPv4/IPv6 — protocol/address semantics;
2. precedent — holding / legal-rule content.

### Non-identity

~~~text
PAYLOAD
!=
SUBSTRATE
~~~

The same physical / institutional substrate could carry different content.

~~~text
PAYLOAD
!=
AUTHORITY
~~~

Content availability does not establish binding force.

Precedent gives the cleanest contrast.

### Predicted near-control

~~~text
hold carrier / authority context approximately fixed
while changing or removing the inherited content
->
successor field should change if PAYLOAD is causal.
~~~

Source-native support:

- persuasive / binding distinction shows content availability alone is insufficient;
- IPv4 installed base shows symbolic protocol description alone is insufficient.

### Verdict

~~~text
REUSABLE CORE ROLE = PASS
Route R
~~~

## 5. INTERFACE

Working meaning:

~~~text
a component determines or materially conditions
how the successor process can access, interoperate with,
work through, bypass or replace the inherited field.
~~~

Paid records:

1. CIV-006 — later operation / retrofit must work through, around or replace inherited hydraulic network;
2. IPv4/IPv6 — installed technical field conditions successor compatibility and migration routes.

### Non-identity

~~~text
INTERFACE
!=
SUBSTRATE
~~~

Persistence of an inherited field does not specify how successors couple to it.

~~~text
INTERFACE
!=
PAYLOAD
~~~

Compatibility / access may be constrained by topology or implementation even when inherited symbolic content is unchanged.

### Predicted near-control

Strong existing example:

~~~text
existing installed base
vs
greenfield
~~~

Generalized failure test:

~~~text
if successor access / compatibility / transition possibilities
do not differ when the claimed interface component is removed/bypassed,
INTERFACE is not paid.
~~~

### Verdict

~~~text
REUSABLE CORE ROLE = PASS
Route R
~~~

## 6. AUTHORITY

Working meaning:

~~~text
a component changes mandatory / binding / admissible force
without merely changing informational availability.
~~~

Paid record:

- precedent / stare decisis.

Strong source-native near-controls:

~~~text
binding precedent
vs
persuasive authority

controlling precedent
vs
case of first impression
~~~

### Non-identity

~~~text
AUTHORITY
!=
PAYLOAD
~~~

The same or similar reasoning may be informationally available while binding force differs.

~~~text
AUTHORITY
!=
ENACTMENT
~~~

A rule can be operative without being an authority relation.

### Verdict

AUTHORITY has only one paid case but unusually strong discriminating controls.

~~~text
SPECIALIZED REUSABLE ROLE = PASS
Route D
broad recurrence = NOT ESTABLISHED
~~~

It may enter a Role Library as SPECIALIZED, not CORE.

## 7. ENACTMENT

Current paid record:

- IPv4/IPv6 installed technical field.

Working phrase in v0.1:

~~~text
makes an abstract rule / specification operative in practice
~~~

Problem:

This burden is already close to:

- X3b operative expectation regime;
- INTERFACE when implementation changes successor accessibility;
- ordinary implementation / realization language.

No second X4c carrier case pays it independently.

No unique near-control in the current X4c record isolates ENACTMENT from INTERFACE / implementation.

Verdict:

~~~text
REUSABLE ROLE = NOT EARNED

status =
CASE-LOCAL / NARROW

do not place in Role Library v0.1.
~~~

Future source-native evidence could reopen it.

## 8. MAINTENANCE

Nominally appears in:

- ecological inheritance;
- CIV-006;
- proposed IPv4 institutional component (ROLE-OPEN).

But the word is semantically overloaded.

### Ecological case

The source establishes persistence of a modified environment.

That does not require an independently identified component performing active maintenance.

### Sewer case

Maintenance is an ongoing process performed on / around the material carrier.

It is not clearly the causal role of the sewer component itself.

### Distinction

~~~text
carrier component role
!=
process by which carrier persistence is sustained across time.
~~~

Therefore MAINTENANCE should move out of the component-role vocabulary.

New architecture-level field:

~~~text
persistence process =
passive persistence
/ active maintenance
/ recurrent reproduction
/ mixed
/ open
~~~

Verdict:

~~~text
MAINTENANCE AS COMPONENT ROLE = RETIRE / RETYPE

MAINTENANCE AS ARCHITECTURE PERSISTENCE PROCESS = RETAIN
~~~

This is a framework simplification earned by the census.

## 9. REPRODUCTION

Current role definition:

~~~text
recreates enough of the carrier into a successor cycle
~~~

No current X4c worked carrier record independently pays REPRODUCTION as a component role.

Ecological inheritance allows persistence or reproduction in principle, but the current source record used here does not isolate a reusable reproduction mechanism role.

Verdict:

~~~text
REUSABLE ROLE = NOT EARNED

status =
OPEN / CASE-LOCAL UNTIL DIRECTLY PAID
~~~

Do not include in Role Library v0.1.

Architecture persistence-process field may later use:

~~~text
recurrent reproduction
~~~

when source-native evidence pays it.

## 10. Role census verdict

### Reusable core roles

~~~text
SUBSTRATE
PAYLOAD
INTERFACE
~~~

All satisfy Route R.

### Specialized reusable role

~~~text
AUTHORITY
~~~

Satisfies Route D through strong near-controls.

### Not admitted to reusable library

~~~text
ENACTMENT = CASE-LOCAL / NARROW
REPRODUCTION = OPEN / NOT PAID
~~~

### Retyped out of component-role vocabulary

~~~text
MAINTENANCE
-> architecture persistence-process field
~~~

## 11. Architecture revision

Carrier architecture should now separate:

### Component roles

~~~text
SUBSTRATE
PAYLOAD
INTERFACE
AUTHORITY [SPECIALIZED]
+ source-local roles where required
~~~

### Persistence process

~~~text
PASSIVE-PERSISTENCE
ACTIVE-MAINTENANCE
RECURRENT-REPRODUCTION
MIXED
OPEN
~~~

This avoids using MAINTENANCE both as:

- what a carrier component does;
- how the carrier architecture survives across time.

## 12. Does a Role Library earn creation?

Criteria:

- >= 3 reusable roles with recurrence / discrimination;
- clear non-identities;
- predicted controls / failure conditions;
- at least one role rejected or retyped by census.

Paid:

~~~text
SUBSTRATE = CORE / 3 paid records
PAYLOAD = CORE / 2 paid records
INTERFACE = CORE / 2 paid records
AUTHORITY = SPECIALIZED / strong near-control

ENACTMENT = rejected from reusable library
MAINTENANCE = retyped
REPRODUCTION = not admitted
~~~

Verdict:

~~~text
ROLE LIBRARY v0.1 = EARNED
~~~

Owner:

Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ROLE_LIBRARY_V0_1.md

The library must remain small.

It may not import every source-local role.

## 13. Relation maturity

No maturity change:

~~~text
X4c = M3
M4 = NONE
M5 = NONE
scientific distinctiveness = NOT ESTABLISHED
~~~

Role recurrence is not M4 transfer gain.

## 14. Next gate

After landing the minimal Role Library:

~~~text
test role library against one existing negative / borderline X4c record
without adding a new positive case.

Primary candidate:
CIV-005 beaver ecosystem-engineering record.

Question:
does the role library sharpen why persistence alone fails X4c
and specify exactly what evidence is missing?
~~~

Do not promote CIV-005 by analogy.

## 15. Canonical boundary

~~~text
canonical edit = NO
new ontology entity = NO
M4/M5 = NONE
scientific distinctiveness = NOT ESTABLISHED
~~~
