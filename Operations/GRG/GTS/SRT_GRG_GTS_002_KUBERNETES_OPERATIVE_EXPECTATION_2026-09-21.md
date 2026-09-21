---
id: SRT-GRG-GTS-002-KUBERNETES-OPERATIVE-EXPECTATION-20260921
type: grg_transformation_record
status: active
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Templates/SRT_GRG_GENERATIVE_TRANSFORMATION_RECORD_TEMPLATE_V0_2.md
  - Operations/Proposals/SRT_GRG_EVIDENCE_GENERATIVE_PROVENANCE_V0_1_2026-09-21.md
  - Operations/GRG/Transfers/SRT_GRG_TR_X3B_01_KUBERNETES_NETWORKPOLICY_2026-09-21.md
  - Operations/GRG/NegativeControls/SRT_GRG_NEG_X3B_FORMAL_DECOUPLING_2026-09-21.md
  - Materials/2026/SRC_2026_09_21_Kubernetes_NetworkPolicy_Enforcement.md
tags: [GRG, GTS, X3b, Kubernetes, NetworkPolicy, M3, Absorbed]
---

# GTS-002 — Kubernetes NetworkPolicy: representation versus operative constraint

## 0. Bounded role

This record tests structural recurrence and target-domain absorption.

It does not claim that Kubernetes itself requires a new vertical explanation.

## 1. Research question / objectification

~~~text
question =
does the X3b burden survive in Kubernetes without changing
the source-native mechanism?

O_R =
NetworkPolicy resource
+ enforcement implementation
+ allowed / denied connectivity relation

strongest reasonable horizontal / target-domain baseline =
ordinary Kubernetes networking practice already distinguishes
policy specification from enforcement and connectivity effect.

domain-internal verticality =
NOT ESTABLISHED / NOT NEEDED.
Within Kubernetes the relevant distinction is already source-native.

cross-objectification question =
does a previously frozen burden recur across mechanisms:
represented expectation
!= operative constraint?
~~~

## 2. Source-native transformation

~~~text
NetworkPolicy resource / rules
-> supporting network implementation
-> packet / connection filtering
-> changed pod connectivity possibilities.
~~~

Near-miss:

~~~text
policy represented
+ no enforcing implementation
-> no NetworkPolicy traffic effect.
~~~

This distinction belongs to Kubernetes practice.

## 3. GTS views

~~~text
history-input = NOT OPENED
reconstruction-output =
source-local only:
operative enforcement changes connectivity reachability

local-locus = NOT OPENED
operative positionality = NOT OPENED
reason =
the target record does not need GRG locus / position claims.
~~~

## 4. Testable burden

~~~text
source-native discriminator =
represented policy without enforcement
vs
represented policy with enforcement.

P_G status =
SOURCE-NATIVE / NOT GRG-GENERATED.

M4-E0 =
ABSORBED.
The mature target domain already owns the discriminator.
~~~

## 5. Generative Order / E_G

~~~text
Generative Order = NOT OPENED
E_G = NOT OPENED

reason =
the previously proposed order merely redescribed
the operative NetworkPolicy mechanism;
"remove enforcement -> hollow/destroy the order"
was an analytic restatement of the source-native failure condition,
not a new discriminating E_G burden.
~~~

Real-use finding:

~~~text
GO / E_G should not be opened merely because an operative mechanism exists.
A positive E_G record needs non-analytic order-relative discrimination.
~~~

## 6. Cross-objectification recurrence

Prior family surfaces include:

~~~text
institutional / irrigation:
rules-in-use + monitoring / sanctions
-> participant option constraints

Internet standards:
implemented protocol/interface
-> interoperability possibilities

Kubernetes:
represented policy + enforcement
-> connectivity possibilities.
~~~

Current reconciliation:

~~~text
shared burden =
represented/shared expectation
!= operative constraint

XG2 mechanism-change survival = PASS
XG3 exclusion/failure retention = PASS
XG4 source-native mechanism ownership = PASS

XG1 independent recurrence =
PARTIAL / NARROWED.

Reason:
institutional irrigation provides a materially different lineage,
but Internet standards and Kubernetes may represent diffused
engineering recurrence rather than two independent replications.
Do not count them twice as independent recurrence.

family-level M3 = RETAIN
because at least one non-engineering source-native recurrence remains;
this GTS alone does not independently establish the whole family.
~~~

## 7. Evidence-generative provenance — #1025 owner applied

~~~text
O_R =
policy / enforcement / connectivity cut

independently evidenced O_W =
YES, SOURCE-NATIVE:
the policy object plus enforcing implementation
functions as an operative rule/interface in cluster behavior.

O_R != O_W:
the research cut describing that mechanism
is not what makes the policy operative.

tested GRG intervention involved in generating evidence? =
NO

evidence purpose =
discovery:
  source-native specification/enforcement distinction

robustness:
  formal-decoupling negative control pressures the stronger burden

attribution:
  source-native mechanism ownership remains Kubernetes-side

claims evidence may pay =
source fidelity;
bounded structural recurrence;
M4-E0 absorption;
family-level M3 support

claims evidence may NOT independently pay =
prospective GRG gain;
scientific distinctiveness;
independent replication for every engineering surface

recurrence provenance =
institutional irrigation vs engineering surfaces:
at least partly INDEPENDENT

Internet standards vs Kubernetes:
potentially DIFFUSED recurrence / shared engineering lineage

alternative-generation audit =
policy-without-enforcement is a source-native alternative;
GRG did not generate it.

real failure condition retained? =
YES:
formal rule presence without operative coupling fails X3b.
~~~

## 8. Verdict

~~~text
GTS-002 = USEFUL BOUNDED MIGRATION

M3 structural family support = RETAIN
M4 = NO / ABSORBED

main schema gain =
explicit domain-internal non-verticality
+ recurrence-provenance warning
+ evidence-credit boundary

E_G gain = NONE / NOT OPENED

canonical consequence = NONE
~~~
