---
source_id: SRC-2026-09-21-PRECEDENT-BINDING-PERSUASIVE-INHERITANCE
id: SRC-2026-09-21-PRECEDENT-BINDING-PERSUASIVE-INHERITANCE
title: "US legal precedent — binding versus persuasive authority and successor adjudication"
source_type: legal_institution_source_bundle
domain: common_law_precedent
date_added: "2026-09-21"
evidence_level: official_and_legal_reference_source_native
reliability_level: high_for_binding_persuasive_precedent_distinction
srt_relevance: very_high_for_GRG_X4c_PINST
integration_priority: very_high
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags: [GRG, X4c, PINST, PINFO, Precedent, StareDecisis, Binding, Persuasive, CarrierArchitecture]
---

# SourceCard — binding versus persuasive precedent

## 1. Source bundle

Primary public legal-reference / court sources:

- Cornell Legal Information Institute — stare decisis.
- Cornell LII — binding precedent.
- Cornell LII — persuasive authority.
- Cornell LII — case law / precedent.
- U.S. Courts — Glossary of Legal Terms.
- federal appellate opinions illustrating binding precedent versus dicta / persuasive latitude.

Public routes:

https://www.law.cornell.edu/wex/stare_decisis

https://www.law.cornell.edu/wex/binding_precedent

https://www.law.cornell.edu/wex/persuasive_authority

https://www.law.cornell.edu/wex/Case_law

https://www.uscourts.gov/glossary

## 2. Source-native distinction

Stare decisis concerns adherence to precedent.

A prior decision is binding only where the deciding court has the relevant binding authority over the later court.

Otherwise the prior decision may remain available as persuasive authority.

Therefore:

~~~text
prior decision exists
!=
prior decision binds successor court
~~~

## 3. Binding precedent

Cornell LII describes binding precedent as a legal rule / principle articulated by an appellate court that lower courts within the relevant jurisdiction must follow.

The binding relation depends on court hierarchy and jurisdiction.

U.S. Courts material similarly distinguishes opinions that can serve as binding precedent.

## 4. Persuasive authority

Persuasive authority can include decisions from:

- another jurisdiction;
- a lower court;
- a court of the same rank in circumstances where it is not binding;
- other nonmandatory legal sources.

A later court may consider such reasoning without being bound by it.

Thus:

~~~text
informational / argumentative availability
can persist
without
mandatory institutional force.
~~~

## 5. Holding versus dicta

Source-native legal doctrine also distinguishes the holding / precedential rule from dicta.

Dicta may remain informative or persuasive while lacking binding force.

This reinforces:

~~~text
textual persistence
!=
institutional inheritance burden automatically.
~~~

## 6. X4c pressure

Candidate successor-inheritance topology:

~~~text
prior adjudication
-> precedential legal field
-> later court enters that field
-> binding authority changes later adjudicative option / justification structure
~~~

Later judges did not make the original adjudication.

The inherited relation can nevertheless affect what they must follow, distinguish, or seek to overrule.

## 7. Carrier architecture result

The frozen target asked whether P-INST can independently carry X4c.

Current result after carrier-architecture / role-census writeback:

~~~text
cardinality = MULTI-COMPONENT

P-INFO:
role = PAYLOAD / inherited holding or legal-rule content
status = COMPONENT-ROLE-PASS

P-INST:
role = AUTHORITY / binding-force selector
status = COMPONENT-ROLE-PASS

minimal paid role set =
PAYLOAD + AUTHORITY

architecture sufficiency =
PASS
~~~

Single-component P-INST and P-INFO architectures are NOT ESTABLISHED for this case.

The inherited field requires both:

~~~text
content that is inherited
+
institutional authority relation
that changes mandatory force for the successor court.
~~~

Historical `P-MIXED` wording is retired as an inheritance provenance kind.

## 8. Causal-role near-control

Binding versus persuasive authority is especially useful because it pressures the institutional component.

Conceptually:

~~~text
prior legal reasoning / decision content available
+
different authority relation
-> different successor constraint.
~~~

This does not make the two contexts literally identical in every legal respect.

It does show that informational persistence alone is insufficient.

## 9. X3b / X4c distinction

### X3b

~~~text
current operative institutional rule:
binding precedent must be followed within the declared authority relation.
~~~

### X4c

~~~text
prior holdings accumulated under that rule
form a successor legal field
that later adjudicators inherit.
~~~

The current authority rule and the inherited precedential field are distinct analytical burdens.

## 10. Greenfield analogue

A case of first impression lacks controlling precedent on the issue.

That creates a useful source-native analogue to the earlier greenfield control:

~~~text
no controlling inherited precedent
-> later court has a wider source set for constructing the rule.
~~~

This is not unrestricted discretion.

It is a near-control for the absence of a specific inherited binding field.

## 11. Normativity guard

~~~text
binding != morally correct
precedential != just
institutionally inherited != politically legitimate
~~~

This SourceCard concerns legal/institutional topology only.

## 12. Integration target

Operations/Audits/SRT_GRG_X4C_PRECEDENT_PINST_CARRIER_PASS1_2026-09-21.md

Current carrier-schema owner:

Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ARCHITECTURE_V0_1.md

Admission-order consistency owner:

Operations/Audits/SRT_GRG_X4C_POSITIVE_ADMISSION_ORDER_CONSISTENCY_PASS1_2026-09-21.md
