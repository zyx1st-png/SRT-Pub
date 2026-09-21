---
source_id: SRC-2026-09-21-KUBERNETES-NETWORKPOLICY-ENFORCEMENT
id: SRC-2026-09-21-KUBERNETES-NETWORKPOLICY-ENFORCEMENT
title: "Kubernetes NetworkPolicy — specification versus enforcement"
source_type: official_technical_documentation
domain: distributed_systems_cloud_native_networking
primary_author: "Kubernetes documentation project"
date_added: "2026-09-21"
evidence_level: official_operational_specification
reliability_level: high_for_source_native_kubernetes_behavior
srt_relevance: very_high_for_GRG_X3b_crossdomain_match
integration_priority: very_high
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags: [GRG, Kubernetes, NetworkPolicy, Enforcement, X3a, X3b, M3]
---

# SourceCard — Kubernetes NetworkPolicy specification versus enforcement

## 1. Primary source

Official Kubernetes documentation:

https://kubernetes.io/docs/concepts/services-networking/network-policies/

Supporting networking overview:

https://kubernetes.io/docs/concepts/services-networking/

Public documentation checked 2026-09-21.

## 2. Source-native distinction

Kubernetes NetworkPolicy resources specify how selected pods may communicate.

But policy semantics are implemented by the cluster's networking solution.

The official documentation states that the cluster must use a network plugin that supports NetworkPolicy enforcement.

Crucially:

~~~text
NetworkPolicy resource exists
+
no controller / networking implementation that enforces it
->
no policy effect on traffic
~~~

The wider networking documentation makes the same distinction: the API may still exist even when the pod-network implementation does not implement NetworkPolicy, in which case it has no effect.

## 3. Source-native mechanism

~~~text
NetworkPolicy object / selectors / ingress-egress rules
-> network plugin/controller interprets policy
-> packet / connection filtering is actually enforced
-> pod connectivity possibilities change
~~~

The API object alone does not carry the enforcement mechanism.

## 4. Pressure on GRG X3

This independently instantiates the frozen X3a / X3b distinction:

~~~text
X3a:
policy articulation / representation

X3b:
operative enforcement that changes actual connectivity possibilities
~~~

The match was not created by changing the target-domain mechanism.

## 5. Important implementation nuance

NetworkPolicy handling can be eventual and implementation-dependent.

The official documentation notes transient inconsistency is possible while plugins process new policies, and some protocol / hostNetwork behavior is implementation-defined.

Therefore X3b should be typed by:

- enforcement implementation;
- target entities;
- affected protocol / layer;
- timing / convergence behavior.

## 6. Objectification guard

~~~text
policy object present
!= policy effect present
~~~

A configuration/API inventory is not an operational-state inventory.

## 7. GRG maturity implication

This is strong independent-domain evidence that the X3a/X3b burden is source-native outside social/legal institutions.

But Kubernetes already owns this distinction explicitly.

Therefore:

~~~text
independent match -> possible M3
GRG domain novelty -> not established
M4 -> not paid by this source
~~~

## 8. Integration target

Operations/GRG/Transfers/SRT_GRG_TR_X3B_01_KUBERNETES_NETWORKPOLICY_2026-09-21.md

Operations/Audits/SRT_GRG_M3_M4_CROSSDOMAIN_TRANSFER_ABSORPTION_PASS1_2026-09-21.md
