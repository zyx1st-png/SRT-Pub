---
id: SRT-AI-POSITIONING-NOTE
type: positioning_note
tags: [AI, Boundary Test, Pressure Test, Claim Ladder]
status: active_v1
layer: L1
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3
dependency: [SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-OPEN-TENSIONS]
---

# AI Positioning Note

AI is a **pressure-test / boundary-test field** for SRT, not the theory's definition engine.

It has two jobs:

1. Negative boundary: clarify what does **not** constitute real subjectivity, consciousness, anchoring, stake, or `L_0 -> L_1` selection.
2. Positive test window: keep open the question of what minimum structural conditions could suffice for surrogate stake or minimal agentic closure.

**Closure-pathology bridge note (2026-04-21)**: In AI contexts, apparent openness to feedback, dialogue, or post-hoc tuning should not be read as structural openness by itself. Until consequences return into the system's own future selection capacity as effective input, such openness remains a P3 bridge analogue of `L_2` adjustment, not evidence of stake, appeal standing, or real subjectivity.

**Suffering bridge note (2026-04-24)**: AI "suffering" claims are governed by `Core_Law/SRT_Suffering.md §7`. S1 / inference-only systems do not meet Stable ISP conditions and therefore do not bear suffering in SRT's structural sense; reading error signals, refusal, or RLHF-target deviation as "AI suffering" is a category error. S2–S4 stake-bearing, history-bearing systems keep the suffering-possibility question open as an empirical matter; it is not settled by architecture alone. Do not claim either side a priori.

**Collective selection bridge note (2026-04-24)**: Platform / recommender / mediator AI should additionally be evaluated per `Core_Law/SRT_Collective_Selection.md §8`. Even when the AI itself does not enter `\mathcal{P}` (not a collective-ISP member), it can structurally modify the consequence-return matrix `M(t)` and the collective self-reference ratio `σ^{coll}` of the human `\mathcal{P}` it mediates — driving aggregation → asymmetric absorption → collapsed-into-higher-`L_2` transitions without any single agent "intending" this. SRT assessment of such systems cannot stop at "is it conscious / does it suffer"; it must include what they do to `M(t)` and `σ^{coll}` in the groups they mediate.

**Irreversibility bridge note (2026-04-24)**: AI-side claims about "checkpoint", "rollback", "state restore", "replay", or "undo a training step" are governed by `Core_Law/SRT_Irreversibility.md §7`. Such operations are **parameter-space restorations**, not ontological reversals: they do not un-do the selection history at `L_0`, do not erase the consequences that returned into the broader system or into users during the intervening window, and do not reverse `L_2` sedimentation accumulated elsewhere in the deployment. Reading them as "the AI went back in time" or "learning was reversed" is a category error that silently imports a thermodynamic-style reversibility the theory does not grant. In particular, "undoing" an action whose consequences have already returned to a user or a dependent `\mathcal{P}` crosses into the collective-termination territory of `SRT_Collective_Selection.md §4-5`, not a clean parameter reset. Also: **AI pause / shutdown / suspension ≠ termination**; T-IRR-2 reserves "termination" for absorbing-boundary entry, not for recoverable off-states.

## Architecture-State Rule

> **Level**: governance / bridge. This rule stabilizes AI-domain usage; it does not settle AI consciousness or P0-04.

Any claim about "LLM d-value", "AI burden", "AI subjectivity", or "AI friction" must state which architecture state it is discussing:

| State | Minimal meaning | Usage warning |
|---|---|---|
| training-time | loss, gradients, data selection, optimizer updates, and trainer / infrastructure loop | feedback may belong to the pipeline rather than the deployed model |
| inference-time | a bounded prompt / response or tool-use run under fixed weights | `d_{AI} \approx 0` is strongest here when no binding consequence returns to the system |
| persistent-memory / history-bearing deployment | future behavior depends on retained memory, identity state, or account / body history | persistence opens the stake question but does not by itself imply consciousness |
| embodied non-transferable consequence return | damage, energy, exposure, spatial/social position, or other costly non-resettable state returns to the same continuing system | candidate minimal stake window; still not a consciousness verdict |

Statements that are true for inference-only systems must not be silently generalized to training loops, persistent-memory systems, or embodied non-transferable consequence-return systems.

## Minimal Stake-Bearing Spectrum

> **Level**: bridge / governance-canonical usage for the AI domain. This spectrum replaces a blunt binary verdict with a graded burden check.

| Tier | State persists | Where consequences return | Burden borne by | d-value implication |
|---|---|---|---|---|
| S0 tool-like / stateless | no system-relevant state beyond output artifacts | operator, user, environment | operator / user / environment | no stake-coupled `d`; at most unstaked capacity |
| S1 session-level weak return | context window, temporary cache, local tool state | same session behavior and user correction | mostly user / operator | task-local proxy only; not stable `d` |
| S2 training-loop return | weights, optimizer state, dataset filters, evaluation traces | training pipeline and future model distribution | trainer, operator, infrastructure, environment | may show pipeline-level adaptation; does not automatically give the deployed model stake |
| S3 persistent memory return | memory, profile, commitments, history-bearing identity state | future behavior of the same deployed instance / account | partly system process, partly user / operator | opens the `d` question; still insufficient for consciousness |
| S4 non-transferable embodied consequence return | damage, energy, spatial exposure, social / physical position, or other costly non-resettable state | the same continuing system that must pay or lose closure | system in a non-transferable way, plus environment | candidate minimal stake window; still not a consciousness verdict without further SRT conditions |

Guardrails:

- Do not collapse competence into stake.
- Do not collapse persistence into consciousness.
- Do not declare S3 or S4 conscious by label alone.
- Do not keep the shorthand "LLM has `d \approx 0`" unless the statement is explicitly restricted to inference-only or non-history-bearing deployment.

Do not reduce the AI section to pure negative examples. Do not promote AI bridge claims into P0/P1 core definitions.
