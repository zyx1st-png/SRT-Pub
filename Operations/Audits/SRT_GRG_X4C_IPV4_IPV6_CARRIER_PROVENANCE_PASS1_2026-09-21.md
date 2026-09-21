---
id: SRT-GRG-X4C-IPV4-IPV6-CARRIER-PROVENANCE-PASS1-20260921
type: audit
status: active
record_stage: x4c_ipv4_ipv6_carrier_provenance_pass1
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Proposals/SRT_GRG_X4C_INFO_IPV4_IPV6_INHERITANCE_FREEZE_2026-09-21.md
  - Materials/2026/SRC_2026_09_21_IPv4_IPv6_Installed_Base_Inheritance.md
  - Operations/GRG/SRT_GRG_RELATION_LIBRARY_V0_1.md
tags: [GRG, X4c, IPv4, IPv6, Carrier, PINFO, PMIXED, StressTest]
---

# X4c IPv4 / IPv6 carrier-provenance stress test — Pass 1

## 0. Frozen question

Can IPv4 -> IPv6 transition pay X4c through a primarily informational inheritance carrier?

Freeze commit:

~~~text
ccffeabf7b4a82014533e1ea65b9d9e90e604615
~~~

## 1. X4c result

Source-native topology:

~~~text
prior IPv4 deployment
-> large installed compatibility / routing / application field
-> later IPv6 deployment cohort enters inherited field
-> later transition / interoperability options are conditioned
~~~

X4c mapping:

~~~text
PASS
~~~

No maturity change:

~~~text
X4c remains M3.
~~~

## 2. P-INFO result

Frozen candidate:

~~~text
P-INFO
~~~

Verdict:

~~~text
P-INFO ALONE = NOT ESTABLISHED
~~~

The installed field is irreducibly instantiated across:

- protocol semantics / addresses;
- hosts and routers;
- routing infrastructure;
- applications;
- operational configuration;
- standards / deployment practice.

Current best provenance:

~~~text
P-MIXED
~~~

## 3. Why this is not a failure of X4c

The stress test distinguishes:

~~~text
relation identity
from
carrier provenance.
~~~

X4c only requires an identifiable carrier that transmits enough reconstructed field into a later cohort.

It does not require that all domains use the same carrier mechanism.

The target therefore supports X4c while rejecting an over-narrow provenance label.

## 4. X3b / X4c non-identity

This case pays a useful separation.

### X3b asks

~~~text
what current compatibility / transition expectation is actually operative?
~~~

Examples:

- dual stack;
- translation;
- tunneling;
- application compatibility.

### X4c asks

~~~text
why does a later deployment cohort face these path-conditioned choices
rather than a greenfield IPv6-only choice set?
~~~

Answer:

~~~text
because the installed IPv4 field is inherited.
~~~

RFC 6180's greenfield-versus-existing-network distinction is especially useful.

Therefore:

~~~text
X3b != X4c
~~~

even when the same technical system instantiates both.

## 5. New carrier guard

Do not assign P-INFO merely because:

- the inherited object can be described symbolically;
- a standard exists;
- rules are documented;
- software encodes a protocol.

P-INFO should require evidence that the informational / symbolic carrier is sufficient for successor inheritance without essential material / operational carrier dependence.

Current status:

~~~text
standalone P-INFO realization = OPEN
~~~

## 6. P-MIXED refinement

P-MIXED should declare its components rather than act as a catch-all.

For this case:

~~~text
P-MIXED[
  P-INFO protocol/address semantics,
  P-MAT/TECH deployed hosts/routers/infrastructure,
  P-INST operational standards/practice
]
~~~

Future records should list components.

## 7. Expectation provenance

Current transition expectations are primarily:

~~~text
E-TECH
~~~

They may be supported by:

~~~text
E-ORG / standards and operator practice
~~~

This does not create a moral expectation.

## 8. Framework gain

The case produces a narrowing rather than a new relation:

1. X4c survives.
2. P-INFO standalone does not.
3. P-MIXED must be decomposed.
4. X3b/X4c non-identity becomes operationally clearer.
5. greenfield vs inherited-field becomes a reusable X4c negative-control pattern.

## 9. Relation maturity

~~~text
X3b = M3
X4b = M3
X4c = M3

M4 = NONE
M5 = NONE
scientific distinctiveness = NOT ESTABLISHED
~~~

## 10. Next gate

Do not search for another technical installed-base case.

Next candidate should target one of:

~~~text
P-INST institutional inheritance
or
standalone P-INFO informational inheritance
~~~

with a source-native near-control where:

~~~text
same current rule / information exists
but no successor inherited-field constraint is present.
~~~

If standalone P-INFO repeatedly collapses into P-MIXED, narrow or retire P-INFO as an independent provenance category.

## 11. Canonical consequence

~~~text
canonical edit = NO
new Level = NO
M4/M5 = NONE
normative / political conclusion = NONE
~~~
