---
id: SRT-GRG-X4C-INFO-IPV4-IPV6-INHERITANCE-FREEZE-20260921
type: preregistration
status: active
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: research_programme
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/GRG/SRT_GRG_RELATION_LIBRARY_V0_1.md
  - Operations/Audits/SRT_GRG_CIV006_X4C_INHERITANCE_CROSSSURFACE_PASS1_2026-09-21.md
  - Operations/GRG/Cases/SRT_GRG_CIV_001_INTERNET_STANDARDS_INTEROPERABILITY_2026-09-21.md
tags: [GRG, X4c, PINFO, Internet, IPv4, IPv6, Inheritance, Freeze]
---

# X4c P-INFO freeze — IPv4 / IPv6 installed-base inheritance

## 0. Freeze

~~~text
relation = X4c inherited reconstructed condition
candidate provenance = P-INFO / P-MIXED
target domain = Internet protocol transition
target system = IPv4 installed base -> IPv6 transition
date = 2026-09-21
base commit = 78e05b941cb0fa875e76910723077b8964451277
dedicated target-source inspection before freeze = NO
~~~

Known generic background that cannot be erased:

- IPv4 predates IPv6;
- IPv6 deployment has required a long transition;
- compatibility / coexistence mechanisms exist.

No decisive source-native evidence is used in this freeze.

## 1. Core discrimination

This attempt is designed to separate:

~~~text
X3b:
a current technical expectation / protocol is operatively enforced

from

X4c:
later participants inherit an installed compatibility field created by prior deployment,
such that their later migration / interoperability options are conditioned
even if they did not make the original deployment choice.
~~~

If the target only shows current protocol compliance, X4c fails.

## 2. Frozen candidate topology

~~~text
earlier IPv4 deployment A
-> installed protocol / addressing / application compatibility field F
-> informational + technical carrier C persists across later cohorts
-> later hosts / networks / operators enter an Internet already structured by F
-> later IPv6 deployment must interoperate with, translate around,
   tunnel through, dual-stack with, or otherwise manage inherited F
~~~

## 3. X4c admission burdens

Require all:

1. prior deployment reconstructed a later interoperability / addressing field;
2. an identifiable carrier persists into later deployment cohorts;
3. successor participants need not reproduce the original IPv4 choice;
4. inherited field changes later deployment / interoperability / transition possibilities;
5. the burden is stronger than "follow the current protocol."

## 4. Inheritance provenance test

Candidate:

~~~text
P-INFO = protocol / address / implementation state carried informationally
P-MAT = routers / hosts / network equipment as material support
P-INST = standards / operational practice
P-MIXED = likely if no single provenance is sufficient
~~~

Do not force P-INFO if the source-native carrier is irreducibly mixed.

## 5. Negative controls

### NC-1 — specification without installed base

~~~text
a published protocol exists
but has negligible implementation / installed compatibility burden
-> may pay X3a
-> does NOT pay X4c.
~~~

### NC-2 — current interoperability only

~~~text
participants follow the same active protocol
but no successor cohort is constrained by prior installed state
-> may pay X3b
-> does NOT pay X4c.
~~~

### NC-3 — mere age

~~~text
old protocol exists
-> not X4c unless later option structure is conditioned by inherited field.
~~~

## 6. Failure / narrowing rule

### PASS candidate

If target sources show:

~~~text
installed IPv4 field
+ successor cohort
+ transition options constrained by inherited compatibility requirements
~~~

### NARROW

If inheritance requires:

~~~text
P-MIXED technical+material+institutional carrier
~~~

rather than P-INFO alone.

### FAIL X4c mapping

If ordinary transition requirements can be fully described as current X3b operative expectation with no distinct inherited-field burden.

## 7. Maturity consequence

Even if source-native fit passes:

~~~text
X4c remains M3
~~~

This target is not opened to create M4.

It is a semantic / carrier-provenance stress test.

## 8. No canonical consequence

~~~text
canonical edit = NO
M4 = NONE
M5 = NONE
scientific distinctiveness = NOT ESTABLISHED
~~~
