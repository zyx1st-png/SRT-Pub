---
id: COH-CROSS-DOMAIN-BLIND-CALIBRATION-HANDOFF-V0-1-20260928
type: handoff
status: active
canonical: false
layer: operations
epistemic_layer: governance
claim_mode: blind_calibration_handoff
created: 2026-09-28
updated: 2026-09-28
dependency:
  - Operations/Proposals/COH_CONSTITUTION_OPERATION_HISTORY_EXPLANATORY_AUDIT_V0_1_2026-09-28.md
  - Operations/Templates/COH_AUDIT_RECORD_TEMPLATE_V0_1_2026-09-28.md
  - Operations/Handoffs/COH_CROSS_DOMAIN_NEUTRAL_CASE_PACKET_V0_1_2026-09-28.md
tags: [COH, BlindCalibration, IndependentReview, CrossDomain]
---

# COH v0.1 — independent blind cross-domain calibration handoff

## 0. Goal

Test whether the theory-neutral Constitution–Operation–History audit produces stable and useful distinctions across unrelated domains without importing SRT/Facing vocabulary.

## 1. Blindness rule

Before all case verdicts are frozen, DO NOT read:

~~~text
Operations/Audits/COH_CROSS_DOMAIN_CALIBRATION_SEED_V0_1_2026-09-28.md
~~~

Also do not use PR discussion that reveals producing-model verdicts.

Required read order:

~~~text
1. COH method v0.1
2. COH record template
3. neutral case packet
4. source files only where the case packet is insufficient
5. freeze all verdicts
6. commit/persist the frozen verdict record
7. only then open the seed and compare.
~~~

## 2. Scope

~~~text
READ-ONLY with respect to existing method/source files;
one new audit file is allowed for the blind result;
no canonical edits;
no SRT/Facing adjudication;
no method rewrite before comparison;
no merge decision on unrelated PRs.
~~~

## 3. Cases

Score all cases in:

`Operations/Handoffs/COH_CROSS_DOMAIN_NEUTRAL_CASE_PACKET_V0_1_2026-09-28.md`.

Domains:

~~~text
Active inference
Niche construction / ecological inheritance
Legal precedent
IPv4 / IPv6 transition
Physics / self-organization
Neuroscience
~~~

## 4. Required output per case

Use the record template and include at minimum:

~~~text
declared scale;
8-field cut;
C burden: none / C-R / C-F / bridge;
O burden: none / O-S / O-T / O-G / bridge;
H burden: none / H / bridge;
evidence/access role;
primary verdict;
confidence;
source-native distinction already present? YES / PARTLY / NO;
added clarity: HIGH / MEDIUM / LOW / NONE;
new research question generated?;
falsifier;
overreach warning, if any.
~~~

## 5. Mandatory traps

Do not assume:

~~~text
generative -> constitution;
hidden -> constitution;
emergent higher-level object -> framework constitution;
phase transition -> constitution;
past -> history;
stored -> history;
persistent -> history;
observable -> operation;
designed framework -> endogenous framework formation;
same event must have one scale-free verdict.
~~~

## 6. Independent value test

Do not merely ask whether the classification matches the seed.

For every case, answer:

~~~text
Did COH reveal a distinction that matters for explanation?
Did it change what would need to be measured or compared?
Did it generate a nontrivial research question?
Or did it merely rename distinctions already explicit in the source?
~~~

The method is allowed to add no value in a mature domain.

## 7. Freeze requirement

Before reading the seed, the blind result file must contain:

~~~text
all case verdicts;
all confidence values;
all added-clarity ratings;
all method defects noticed during blind use.
~~~

Record the pre-seed commit SHA.

## 8. Post-seed comparison

After freezing, read the seed and classify disagreements as:

~~~text
D1 cut mismatch
D2 scale mismatch
D3 C-R vs C-F ambiguity
D4 O subtype ambiguity
D5 history/persistence ambiguity
D6 evidence-vs-explanation ambiguity
D7 external-design/endogenous-generation ambiguity
D8 source ambiguity
D9 method rule defect
D10 producing-seed defect
D11 other
~~~

Do not alter the frozen verdicts after comparison.

## 9. Final method verdict

Return:

~~~text
BLIND CASE TABLE
VERDICT AGREEMENT
ADDED-CLARITY AGREEMENT
DISAGREEMENTS + CLASSES
METHOD DEFECTS
SEED DEFECTS
DOMAINS WHERE COH ADDED CLEAR VALUE
DOMAINS WHERE COH MOSTLY RELABELED EXISTING DISTINCTIONS
FAILURE CASES
GOLD-SET CANDIDATES
METHOD STATUS:
  REJECT / REVISE / RETAIN-WITH-CORRECTIONS / READY-FOR-SECOND-RUN
~~~

## 10. Independence caveat

A different session of the same model family is useful but not fully independent. Record model/session provenance if known.

Do not call the result a validated general method after one rerun.