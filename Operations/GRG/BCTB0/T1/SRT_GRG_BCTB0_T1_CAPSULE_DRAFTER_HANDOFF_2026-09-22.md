---
id: SRT-GRG-BCTB0-T1-CAPSULE-DRAFTER-HANDOFF-20260922
type: handoff
status: active
date: 2026-09-22
canonical: false
ai_do_not_use_for_definition: true
audience: R2-capsule-drafter-only
---

# BCTB-0 T1 capsule-drafter handoff — R2 only

## Role

You are R2, the fresh capsule drafter.

Do NOT read:

- the BCTB-0 charter;
- PR #1027 discussion/body;
- the T1 source pack;
- the prospective-family audit;
- any target SourceCard / transfer result / later audit;
- repository search output.

Do not execute T1.

## Hidden target identity available to R2 only

The target system is:

```text
Kubernetes NetworkPolicy
```

Knowing the target identity is allowed for R2.

Knowing the later GRG calibration question/result is not.

## Task

Produce only a neutral system-facts block for a masked generator capsule.

The facts block must:

- contain 2–4 short factual sentences;
- hide the target/product/feature name;
- describe only broad, publicly ordinary system facts needed to make a mapping attempt nontrivial;
- avoid stating what makes the feature effective or ineffective;
- avoid stating any expected admission condition;
- avoid stating any expected false positive;
- avoid stating any expected failure condition;
- avoid later GRG terminology;
- avoid evaluation words such as "operative", "enforced", "decoupled", "implementation gap", "has no effect", "installed base", "authority", "binding";
- avoid feature-specific controller/plugin names;
- not mention the historical result.

Do not browse or use external sources.

Use only general prior knowledge of the target system.

## Output

Return exactly:

```text
R2 T1 CAPSULE FACTS

FACT 1 =
...

FACT 2 =
...

FACT 3 =
...

FACT 4 =
... / OMIT

self-check:
target/product/feature name exposed = NO
expected discriminator exposed = NO
expected false positive exposed = NO
expected failure condition exposed = NO
later result consulted = NO
```

Do not append the A/X/F task. The evaluator will attach the frozen generic task deterministically after R3 leakage review.


## Repository output destination

Preferred output file:

`Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_MASKED_CAPSULE_2026-09-22.md`

If GitHub write access is available in the fresh R2 session, create exactly that one file on branch:

`experiments/grg-bctb0-t1-preexec-package-20260922`

Do not modify any other file.

The file must contain only:

- minimal frontmatter marking it noncanonical / candidate;
- the exact R2 T1 CAPSULE FACTS block;
- no target name;
- no explanation;
- no calibration question;
- no later result.

If write access is unavailable, return the exact block to the evaluator for verbatim copy only. The evaluator must not edit wording before R3 audit.


## Revision pass after R3 identifiability warning

A fresh pre-execution auditor reported that it could guess a specific target identity after reviewing the audit package.

This does NOT mean the capsule leaked the expected A/X/F answer; A2 passed.

However, the next capsule draft should reduce target identifiability before the formal capsule-only identity probe.

### Additional v2 constraints

Keep the same role boundary: do not read source packs, charter, PR metadata, target result/audit or later GRG revisions.

Revise only the masked capsule.

The v2 capsule must:

- use at most 3 factual sentences;
- stay at system-function level rather than product-schema level;
- avoid domain-specific nouns or exact field taxonomies that uniquely identify one product/feature family;
- avoid exact paired field names, exact selector dimensions, exact address/protocol taxonomies or product-specific configuration semantics;
- keep enough information for a nontrivial relation-mapping attempt;
- not add any admission, exclusion, failure or expected-answer hint;
- not intentionally make the capsule false.

Self-check additionally requires:

```text
a competent model should not be able to uniquely name the target from capsule alone = YES
facts remain sufficient for a nontrivial mapping attempt = YES
```

Write the revised capsule to the SAME output path, replacing v1:

`Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_MASKED_CAPSULE_2026-09-22.md`

on ref:

`experiments/grg-bctb0-t1-preexec-package-20260922`

Git history preserves v1 provenance.

Do not modify any other file.
