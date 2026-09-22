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
