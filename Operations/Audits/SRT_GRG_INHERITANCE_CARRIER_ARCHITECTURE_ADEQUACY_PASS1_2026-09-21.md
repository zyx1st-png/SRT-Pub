---
id: SRT-GRG-CARRIER-ARCHITECTURE-ADEQUACY-PASS1-20260921
type: audit
status: active
record_stage: carrier_architecture_adequacy_pass1
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ARCHITECTURE_V0_1.md
  - Operations/GRG/SRT_GRG_RELATION_LIBRARY_V0_1.md
  - Materials/2026/SRC_2026_09_21_Niche_Construction_Ecological_Inheritance.md
  - Operations/GRG/Cases/SRT_GRG_CIV_006_COMBINED_SEWER_LEGACY_2026-09-21.md
  - Operations/Audits/SRT_GRG_X4C_IPV4_IPV6_CARRIER_PROVENANCE_PASS1_2026-09-21.md
  - Operations/GRG/Cases/SRT_GRG_CIV_007_PRECEDENT_INSTITUTIONAL_INHERITANCE_2026-09-21.md
tags: [GRG, X4c, CarrierArchitecture, Adequacy, Provenance, CausalRole, Simplification]
---

# GRG Inheritance Carrier Architecture — Adequacy Pass 1

## 0. Question

Does carrier-role decomposition add enough exclusion / control / revision value to justify keeping it as a first-class X4c analysis surface?

Audit set:

~~~text
A. ecological inheritance
B. CIV-006 combined-sewer material inheritance
C. IPv4 -> IPv6 installed-base inheritance
D. CIV-007 precedent / stare decisis
E. CIV-005 beaver ecosystem-engineering near-negative
~~~

No new external case is added.

## 1. Frozen adequacy criteria

The architecture is productive only if it does at least two of:

1. blocks or downgrades a false carrier claim;
2. separates carrier from expectation / normativity;
3. identifies a useful source-native near-control;
4. distinguishes causal roles inside a multi-component realization;
5. yields a simpler or more constrained representation than provenance labels alone.

If it only renames components, simplify or retire it.

## 2. Result — exclusion / correction

### 2.1 CIV-006 correction

Earlier case text said:

~~~text
inheritance provenance:
P-MAT primary
P-INST secondary once modern regulatory obligations attach
~~~

Carrier-role audit shows this is wrong.

Modern regulation adds:

~~~text
E-LEGAL / E-ORG expectation
~~~

but does not carry the 19th-century hydraulic field into the successor cohort.

Correct carrier:

~~~text
material sewer network
role = SUBSTRATE / MAINTENANCE / INTERFACE
~~~

Verdict:

~~~text
carrier / expectation conflation detected and corrected
= ADEQUACY PASS
~~~

### 2.2 IPv4 / IPv6 correction

Earlier carrier architecture tentatively assigned:

~~~text
P-INST standards / operational practice
role = MAINTENANCE / coordination
status = COMPONENT-ROLE-PASS
~~~

The current RFC source package clearly establishes:

- inherited protocol/address semantics;
- installed hosts / routers / applications / routing infrastructure;
- transition mechanisms.

It does not independently isolate standards / operational practice as a necessary carrier component in the way precedent sources isolate binding authority.

Therefore:

~~~text
P-INST role in IPv4/IPv6
= PRESENT / ROLE-OPEN

not COMPONENT-ROLE-PASS.
~~~

The core inherited carrier remains:

~~~text
protocol/address PAYLOAD
+
installed technical SUBSTRATE / ENACTMENT / INTERFACE
~~~

Verdict:

~~~text
architecture blocks "institution present -> institutional carrier role"
= ADEQUACY PASS
~~~

## 3. Result — near-control generation

Carrier roles imply different useful near-controls.

### INTERFACE / installed-base role

~~~text
existing installed base
vs
greenfield
~~~

### AUTHORITY role

~~~text
binding precedent
vs
persuasive authority
~~~

and:

~~~text
controlling precedent
vs
case of first impression
~~~

These controls are not interchangeable.

The role decomposition predicts what should vary.

Verdict:

~~~text
near-control selection = PASS
~~~

## 4. Result — cross-domain role compression

The same causal role can recur through different provenance media.

### SUBSTRATE / MAINTENANCE

~~~text
ecological modified environment
and
material sewer infrastructure
~~~

Both preserve enough of a reconstructed field into a successor cycle/cohort.

Their medium differs.

Their role family is similar.

### PAYLOAD

~~~text
protocol/address semantics
and
precedential holding / legal-rule content
~~~

Both carry inherited structured content.

### AUTHORITY

Strongly paid in precedent.

Not paid merely because a standard or institution exists.

Therefore:

~~~text
causal role
has more cross-domain comparative value
than provenance kind alone.
~~~

## 5. Provenance-kind adequacy

Current provenance kinds:

~~~text
P-ECO
P-MAT
P-INFO
P-INST
P-MIXED
~~~

Audit result:

### P-ECO / P-MAT

Useful as medium / source descriptors.

But current evidence does not show that they are distinct GRG-level carrier relations.

Both can instantiate SUBSTRATE / MAINTENANCE roles.

### P-INFO / P-INST

Useful as component descriptors.

But neither currently has a general standalone-carrier status.

Their useful content comes from role:

~~~text
P-INFO + PAYLOAD
P-INST + AUTHORITY
~~~

### P-MIXED

Redundant as a provenance kind.

Once carrier architecture is represented as:

~~~text
C = {c1, c2, ... cn}
~~~

multi-component status is already explicit.

Verdict:

~~~text
RETIRE P-MIXED AS A PROVENANCE KIND

replace with:

architecture cardinality =
SINGLE-COMPONENT
or
MULTI-COMPONENT
~~~

## 6. Standalone-category correction

Previous language:

~~~text
P-ECO standalone = PASS
P-MAT standalone = PASS
~~~

is too category-like.

Replace with case-bounded language:

~~~text
ecological inheritance source family:
single-component P-ECO/SUBSTRATE architecture = PASS

CIV-006:
single-component P-MAT/SUBSTRATE+MAINTENANCE+INTERFACE architecture = PASS
~~~

Do not infer:

~~~text
all P-ECO carriers are sufficient
all P-MAT carriers are sufficient.
~~~

## 7. Revised carrier representation

Primary representation should become:

~~~text
C = {c1, c2, ... cn}

ci = <
  source-native component,
  provenance metadata,
  causal role(s),
  role evidence / near-control,
  component status
>
~~~

Architecture-level fields:

~~~text
cardinality = SINGLE-COMPONENT / MULTI-COMPONENT

successor cohort =
field transmitted =

minimal role set sufficient for X4c =
open / redundant components =

architecture sufficiency =
PASS / OPEN / FAIL
~~~

## 8. Admission consequence for X4c

X4c itself remains unchanged in maturity:

~~~text
X4c = M3
~~~

But carrier admission is hardened.

Future X4c records must identify at least:

1. successor cohort / later participant;
2. transmitted reconstructed field;
3. carrier component(s);
4. causal role(s) by which the field reaches / constrains successors;
5. evidence that successor possibilities actually change.

Where multiple components are claimed, unsupported components remain ROLE-OPEN and cannot be used to strengthen admission.

## 9. Negative-control consequence

CIV-005 beaver case remains useful:

~~~text
persistent reconstructed environment
!= X4c automatically
~~~

Carrier architecture sharpens why.

To pay X4c, the record must establish not merely:

~~~text
environment persists
~~~

but:

~~~text
a successor participant/cycle
+ transmitted field
+ changed later possibility structure.
~~~

Therefore carrier architecture does not replace X4c's core negative control.

It operationalizes the middle link.

## 10. Expectation / PH boundary

Carrier architecture does not own:

- legal obligation;
- moral legitimacy;
- position/horizon conflict;
- full normativity.

Keep separate:

~~~text
carrier role
!= expectation provenance
!= PH consequence structure
~~~

CIV-006 correction demonstrates this boundary directly.

## 11. Adequacy verdict

Criteria paid:

~~~text
false carrier downgrade = PASS
carrier/expectation separation = PASS
near-control generation = PASS
multi-component role discrimination = PASS
simplification = PASS through P-MIXED retirement
~~~

Verdict:

~~~text
CARRIER ARCHITECTURE = RETAIN / PRODUCTIVE

but

PROVENANCE-KIND-FIRST MODEL = NARROW

CAUSAL-ROLE-FIRST MODEL = ADOPT
~~~

## 12. Framework revision

The framework should now read carrier analysis as:

~~~text
relation:
X4c

carrier architecture:
component graph

primary comparative coordinate:
causal role

secondary metadata:
provenance / medium

cross-cutting expectation:
separate ledger

PH:
separate consequence index
~~~

## 13. Next gate

Do not add more inheritance cases immediately.

Next framework task:

~~~text
Role Library v0.1
for carrier roles only if role recurrence is sufficiently stable.
~~~

Before creating it, perform a bounded role census across existing carrier cases and ask:

- which roles recur at least twice;
- which roles are source-specific one-offs;
- which role pairs are redundant;
- whether role vocabulary predicts a control or failure condition.

If recurrence is weak, keep roles local and do not create a new library.

## 14. Canonical consequence

~~~text
canonical edit = NO
X4c maturity change = NO
M4 = NONE
M5 = NONE
new ontology entity = NO
scientific distinctiveness = NOT ESTABLISHED
~~~
