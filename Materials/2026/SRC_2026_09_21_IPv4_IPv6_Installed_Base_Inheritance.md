---
source_id: SRC-2026-09-21-IPV4-IPV6-INSTALLED-BASE-INHERITANCE
id: SRC-2026-09-21-IPV4-IPV6-INSTALLED-BASE-INHERITANCE
title: "IETF RFCs — IPv4 installed base and IPv6 transition / coexistence"
source_type: standards_transition_source_bundle
domain: internet_protocol_transition
date_added: "2026-09-21"
evidence_level: source_native_standards_operational_guidance
reliability_level: high_for_transition_and_installed_base_claims
srt_relevance: very_high_for_GRG_X4c_carrier_provenance
integration_priority: very_high
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags: [GRG, X4c, IPv4, IPv6, InstalledBase, PINFO, PMIXED, Internet]
---

# SourceCard — IPv4 installed base and IPv6 transition

## 1. Source bundle

Primary IETF / RFC Editor sources:

- RFC 4213 — Basic Transition Mechanisms for IPv6 Hosts and Routers.
- RFC 4038 — Application Aspects of IPv6 Transition.
- RFC 6180 — Guidelines for Using IPv6 Transition Mechanisms during IPv6 Deployment.
- RFC 9386 — IPv6 Deployment Status.

Public routes:

https://www.rfc-editor.org/info/rfc4213/

https://www.rfc-editor.org/info/rfc4038/

https://www.rfc-editor.org/info/rfc6180/

https://www.rfc-editor.org/rfc/rfc9386.html

## 2. Source-native installed-base burden

RFC 4213 states that successful IPv6 transition depends on compatibility with the large installed base of IPv4 hosts and routers.

It defines transition mechanisms including:

- dual stack;
- configured tunneling over IPv4 routing infrastructure.

The source explicitly anticipates long coexistence with IPv4.

## 3. Successor-cohort constraint

RFC 6180 distinguishes:

~~~text
greenfield networks
from
networks with existing IPv4 devices and users.
~~~

The existing-network case faces different deployment choices.

Dual stack, IPv4-as-a-service, translation and other transition approaches exist because successor deployments enter a non-blank field.

This is stronger than:

~~~text
IPv6 has a protocol specification.
~~~

## 4. Application-level inherited field

RFC 4038 explains that application migration also depends on the existing IPv4-based Internet, protocol stacks and legacy applications.

A network or OS can gain IPv6 capability while applications remain IPv4-oriented.

Therefore the inherited field exists across several layers:

- addressing;
- network routing;
- host stacks;
- applications;
- DNS / naming behavior;
- operational practices.

## 5. X3b / X4c separation

### X3b

~~~text
current interoperability expectation
+ operative implementation
-> actual IPv4/IPv6 communication possibilities
~~~

### X4c

~~~text
prior installed IPv4 field
+ later deployment cohort
-> transition choices are conditioned by inherited compatibility requirements
~~~

The two can coexist.

They are not identical.

## 6. Carrier provenance result

The frozen candidate asked whether P-INFO could carry X4c.

Source-native result:

~~~text
P-INFO alone = NOT ESTABLISHED
~~~

Reason:

The inherited field is not carried only by protocol descriptions or symbolic representations.

It is materially / technically instantiated in:

- deployed hosts;
- routers;
- routing infrastructure;
- applications;
- address dependencies;
- operational configurations.

Standards and operational practice also maintain the field.

Current carrier architecture after adequacy Pass 1:

~~~text
cardinality = MULTI-COMPONENT

P-INFO:
role = PAYLOAD
status = COMPONENT-ROLE-PASS

P-MAT:
role = SUBSTRATE / ENACTMENT / INTERFACE
status = COMPONENT-ROLE-PASS

P-INST:
proposed role = MAINTENANCE / operational coordination
status = PRESENT / ROLE-OPEN

architecture sufficiency = PASS
~~~

Historical `P-MIXED` language is superseded by the explicit component-role architecture.

No new relation is created.

## 7. Negative controls

### Specification without installed base

A protocol text with negligible deployment does not pay X4c.

### Current compliance only

Two current participants following the same active protocol may pay X3b without paying successor inheritance.

### Greenfield network

RFC 6180's explicit greenfield distinction is a useful source-native near-control:

~~~text
greenfield environment
-> no inherited IPv4 user/device burden of the same kind.
~~~

This helps show that the installed-base burden is not just a synonym for protocol interoperability.

## 8. Pressure on X4c

The case supports:

~~~text
prior deployed field F
+ multi-component carrier architecture C
+ successor operators / devices
+ changed later migration / interoperability possibilities
~~~

It therefore supports X4c while narrowing carrier provenance.

## 9. Expectation provenance

Current interoperability / transition expectations are primarily:

~~~text
E-TECH
~~~

with standards / operational layers:

~~~text
E-ORG / E-MIXED
~~~

Do not infer moral normativity.

## 10. Integration target

Operations/Audits/SRT_GRG_X4C_IPV4_IPV6_CARRIER_PROVENANCE_PASS1_2026-09-21.md

Superseding carrier-schema audit:

Operations/Audits/SRT_GRG_INHERITANCE_CARRIER_ARCHITECTURE_ADEQUACY_PASS1_2026-09-21.md
