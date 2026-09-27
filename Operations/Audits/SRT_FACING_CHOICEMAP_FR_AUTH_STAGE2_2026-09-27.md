---
id: SRT-FACING-CHOICEMAP-FR-AUTH-STAGE2-20260927
type: audit
status: draft
canonical: false
layer: operations
epistemic_layer: os
claim_mode: author_confrontation_stage2
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_FACING_CHOICEMAP_REVERSE_INFERENCE_2026-09-27.md
  - Operations/Proposals/SRT_FACING_HUMAN_IN_LOOP_GENERATIVE_CONFRONTATION_METHOD_V0_3_2026-09-27.md
  - Operations/_SRT_CHOICEMAP_TRACE_WORKFLOW.md
  - Operations/_SRT_CHOICE_TRACE_LOG.md
  - Operations/Audits/SRT_ACTIVE_VS_SECOND_ORDER_SELECTION_RECONCILIATION_2026-09-11.md
  - 01_Source_Intuition/SRT_CHOICEMAP_EMBODIED_POSITION_SECOND_ORDER_SELECTION_CONTINUATION_2026-08-09.md
tags: [Facing, ChoiceMap, FRAUTH, GenerativeProcess, Breakout, ReverseInference]
---

# ChoiceMap FACE-REC — FR-AUTH stage 2 machine candidates

## 0. Provenance boundary

The following author decisions were already preserved **before** the machine candidates below were revealed:

```text
A1. ChoiceMap is a method/tool that uses L2-facing choice traces
    to reconstruct L1-facing subject-level generative selection,
    then uses the constructed L1-facing account to understand L0-facing primitive Selection.

A2. L1-facing generative selection is not directly recorded or observed.

A3. language, symbols, explicit choices and other directly recordable material
    are L2-facing evidence for this reconstruction task.

A4. L1-facing is not a stable latent preference vector.
    It is a dynamic process that repeatedly generates / recuts
    objects, comparison scales, candidate spaces and direction.
```

Everything below is **machine candidate analysis after blind capture**.

## 1. Machine candidate recut M1 — ChoiceMap's primary datum is a transformation, not an option

The original product surface naturally makes the data look like:

```text
prompt -> options -> author chooses option
```

But under the author's recut, the higher-value datum is:

```text
presented L2 grammar / cut
+ perturbation to that grammar
-> author's response transformation
-> new L2 trace.
```

Therefore the minimal record unit should not be merely:

```text
chosen option = A
```

but something closer to:

```text
offered cut
-> accepted / rejected / merged / split / reframed / breakout / root-return
-> resulting new cut.
```

The inferential target is not the content of the choice but the **rule by which the subject changes the field in which choice becomes possible**.

Status: MACHINE CANDIDATE.

## 2. Machine candidate recut M2 — L1-facing is a generator / recutter, not a hidden state description

A stable latent-preference model would ask:

```text
what does this subject prefer?
```

The author-adjudicated dynamic reading instead asks:

```text
how does this subject generate what counts as an object,
a comparison, a candidate, a scale, a relevant difference,
or a direction in this situation?
```

Thus a ChoiceMap L1 reconstruction should model a **generative transformation process** rather than only a hidden vector of weights.

Candidate abstract form:

```text
L1_G :
  (current L2 scaffold,
   retained history,
   disturbance / question,
   current formed position)
    ->
  (re-cut,
   comparison formation,
   candidate-space formation,
   directionally non-neutral actualisation)
```

This notation is local to this audit and has no canonical authority.

Status: MACHINE CANDIDATE.

## 3. Machine candidate recut M3 — breakout is a privileged identification event

The existing ChoiceMap workflow already distinguishes:

- `dimension_miss`;
- `level_miss`;
- `format_miss`;
- `root_miss`;
- `domain_shift`.

Under the author's current reconstruction, these are not merely dialogue-management events.

They are especially informative when:

```text
machine-provided L2 grammar
fails to express the latent L1 generative organization
->
author has to generate a different L2 grammar.
```

Therefore:

```text
ordinary choice inside offered grammar
= weak-to-moderate inverse evidence;

stable choice across perturbations
= stronger evidence;

author-generated recut / breakout
= potentially high-information evidence about L1 generation.
```

This is not yet a theorem or metric.

Status: MACHINE CANDIDATE with strong historical convergence.

## 4. Machine candidate recut M4 — do not infer L1 from L2 regularity alone

A repeated observable pattern can be explained by:

- stable preference;
- habit / script;
- learned language convention;
- prompt framing;
- retained L2 scaffold;
- social convention;
- model-induced option geometry;
- or a genuinely regenerating L1 process.

So:

```text
L2 regularity
-/-> unique L1 reconstruction.
```

ChoiceMap becomes informative only to the extent that it **perturbs the observable scaffold** and tests whether the subject:

- preserves the same content;
- preserves the same relation under new representation;
- rewrites the comparison scale;
- rewrites candidate-generation rules;
- changes the selectable space;
- or creates a new problem cut.

Status: MACHINE CANDIDATE / IDENTIFIABILITY GUARD.

## 5. Machine candidate recut M5 — the earlier “second-order Selection” lineage is a strong historical neighbor, not yet an identity

The 2026-08-09 lineage already required, for its stronger second-order pattern:

```text
own-consequence return
+ comparison-scale rewrite
+ selectable-space change
+ continued efficacy.
```

That is structurally close to the present L1-facing reconstruction, especially the ability to regenerate the comparison and candidate space.

But do not collapse them:

```text
ChoiceMap-inferred L1 generative process
!= automatically second-order Selection;

second-order Selection
= an already typed stronger downstream pattern with its own conditions.
```

The historical convergence is evidence that the current author recut is not an isolated new metaphor.

Status: MACHINE SOURCE-RETURN / NON-IDENTITY GUARD.

## 6. Machine candidate recut M6 — product ChoiceMap and intuition ChoiceMap may be two uses of one inverse-identification architecture

The repository currently separates:

```text
ChoiceMap product:
  preserve user's reselectability / prevent premature AI closure;

ChoiceMap intuition mining:
  machine diverges / author converges / trace choices and breakouts.
```

Candidate unification:

```text
both manipulate the L2-facing scaffold
so that the subject's own generative organization
is not replaced by the machine's closure.

product use:
  protect that generative organization;

research / intuition use:
  perturb and reconstruct that generative organization.
```

This would explain why “do not let the LLM perform the final convergence” was important even before the present Facing vocabulary existed.

Status: MACHINE CANDIDATE.

## 7. L2-as-source risk

A major regression would be:

```text
past choice traces
-> infer stable preference profile
-> use preference profile to explain future choice
-> call that L1.
```

That would make retained L2 history the explanatory source.

The author-adjudicated route instead requires:

```text
past L2 trace
+ new perturbation
-> observe whether and how the subject regenerates / revises the cut
-> reconstruct L1 process.
```

So the strongest evidence is not persistence alone but **structured transformation under perturbation**.

## 8. Provisional subtraction question

After subtracting:

- exact words;
- exact option labels;
- domain content;
- current topic;
- one fixed comparison scale;
- one fixed candidate inventory;
- stable preference interpretation;

what remains invariant across successful L1 reconstructions?

Machine candidates, not author decisions:

1. capacity to generate a distinction / cut;
2. capacity to generate a comparison relation rather than merely receive one;
3. non-neutral actualisation among generated differences;
4. capacity to reorganize the cut when the current grammar fails;
5. finite positionality: generation always occurs from a bounded formed position rather than a God-view.

No claim is made that all five are primitive, unique to SRT, or sufficient for L0.

## 9. Next author confrontation

The next author question should not ask which machine candidate is “correct” in the abstract.

The decisive question is:

> When the same L1-facing generative process is reconstructed across different topics, words, option sets and comparison scales, **what exactly do you expect to remain the same?**

Possible machine-generated families are now allowed to be shown:

- a stable **direction**;
- a stable **way of generating distinctions**;
- a stable **way of constructing comparison / relevance**;
- a stable **way of recutting when the current grammar fails**;
- none of the above as a stable object — only a recurrent generative relation / process.

The author may reject, combine, or replace all of them.
