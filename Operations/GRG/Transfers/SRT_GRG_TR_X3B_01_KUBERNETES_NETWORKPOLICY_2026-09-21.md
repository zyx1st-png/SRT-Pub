---
id: SRT-GRG-TR-X3B-01-KUBERNETES-NETWORKPOLICY-20260921
type: grg_transfer_record
status: active
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/GRG/SRT_GRG_RELATION_LIBRARY_V0_1.md
  - Materials/2026/SRC_2026_09_21_Kubernetes_NetworkPolicy_Enforcement.md
tags: [GRG, Transfer, X3b, Kubernetes, NetworkPolicy, M3, M4]
---

# TR-X3B-01 — Kubernetes NetworkPolicy

## 0. Transfer class

~~~text
relation frozen before target close-read = YES
target/domain separately preregistered before source search = NO
target outcome hidden before transfer prediction = not applicable / documentation case
eligible use = independent M3 semantic/source match
strong prospective M4 evidence = NO
~~~

This record must not be described as a preregistered target-domain prediction.

## 1. Frozen GRG burden

X3b before target close-read:

~~~text
typed/shared expectation
+ operative embodiment / maintenance provenance
+ evidence that participant action possibilities / accessibility
  are actually changed through the claimed channel
~~~

Guard:

~~~text
X3a articulated expectation
does not entail
X3b operative expectation regime.
~~~

## 2. Source-native target distinction

Kubernetes provides a NetworkPolicy API object for specifying allowed traffic relations.

Official documentation states that NetworkPolicy is implemented by the network plugin.

A NetworkPolicy resource created without an implementation/controller that enforces it has no traffic effect.

Source-native topology:

~~~text
policy object / rules
-> supporting network implementation
-> packet / connection filtering
-> changed pod connectivity possibilities
~~~

Built-in near-miss:

~~~text
policy object / API present
+
no enforcing implementation
->
no NetworkPolicy effect
~~~

## 3. GRG mapping

~~~text
NetworkPolicy object / spec
-> X3a articulated expectation

network plugin/controller enforcement
-> X3b operative expectation embodiment

changed allowed / denied connections
-> changed participant accessibility / action possibilities
~~~

Provenance:

~~~text
P-TECH
~~~

The mapping requires no change to Kubernetes's mechanism.

## 4. Semantic invariance

Compared with prior X3b domains:

~~~text
Nepal irrigation:
rules-in-use + monitoring / sanctions

Montreal:
legal-organizational implementation

Internet standards:
implementation / interoperability

Kubernetes:
technical enforcement implementation
~~~

The shared burden remains:

~~~text
represented / shared expectation
!=
operative constraint

operative carrier
-> actual possibility relation changes
~~~

Verdict:

~~~text
semantic invariance = PASS
~~~

## 5. Source-native ownership / absorption

Kubernetes documentation already makes the decisive distinction explicitly.

GRG does not contribute:

- NetworkPolicy semantics;
- controller / CNI enforcement mechanism;
- networking implementation details;
- a new Kubernetes security control.

Therefore:

~~~text
target-domain mechanism = fully source-native
GRG explanatory novelty in Kubernetes = NONE ESTABLISHED
~~~

## 6. M-status

~~~text
M3 independently evidenced relation match = PASS

Reason:
the already-frozen X3b admission burden is independently instantiated
in a technical execution system with an explicit source-native near-miss.

M4 transfer-generating match = NO / ABSORBED

Reason:
the target domain already asks and documents the same specification-versus-enforcement distinction.
No GRG-generated target-domain variable/control/distinction is newly added.
~~~

## 7. Programme consequence

X3b can now be treated as more than a social/institutional metaphor.

But:

~~~text
cross-domain recurrence
!= GRG scientific distinctiveness
~~~

Next X3b work should test whether the relation predicts a useful distinction in a domain where the distinction is not already explicit in ordinary practice.

## 8. Compact verdict

~~~text
X3b -> Kubernetes
semantic match = PASS
source-native evidence = PASS
negative-control structure = PASS
M3 = PASS
M4 = NO / ABSORBED
canonical consequence = NONE
~~~
