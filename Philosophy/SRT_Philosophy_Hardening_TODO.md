---
id: SRT-PHIL-HARDENING-TODO
type: hardening-plan
tags: [Philosophy, TODO, Hardening, Claim Hygiene, Refactor, PH-SS]
status: active_v5
layer: L1
epistemic_layer: bridge
claim_mode: guide
claim_level: P5
canonical: false
dependency:
  - SRT-PHILOSOPHY-README
  - SRT-PHIL-HARDENING-SOFT-SPOTS-2026-04-27
  - SRT-PHIL-PH-SS-OBJECTION-CROSSWALK-2026-04-27
  - SRT-PHIL-PH-SS-HARDENING-EXECUTION-PLAN-2026-04-27
  - SRT-PHIL-SELECTION-REALISM-LAYERED-REALISM-PATCH-2026-04-27
  - SRT-PHIL-AXIOMS-PH-SS-GUARDRAILS-2026-04-27
  - SRT-PHIL-OBJECTION-LEDGER-PH-SS-EXTENSION-2026-04-27
  - SRT-ETHICS-PH-SS-GUARDRAILS-2026-04-27
  - SRT-SOCIAL-POLITICAL-PH-SS-GUARDRAILS-2026-04-27
  - SRT-PHIL-OBJECTION-LEDGER
  - SRT-PHIL-FOUNDATIONS-COMPACT-CORE
  - SRT-PHIL-AXIOMS
---

# SRT Philosophy — Hardening TODO

> **Purpose**: Convert known soft spots in the Philosophy folder into concrete hardening tasks.
>
> **Rule**: A task is done only when the relevant claim has layer, scope, formula role, strongest objection, and narrowing / withdrawal condition.

---

## 0. Current highest-value hardening direction

The Philosophy section is not weak because it lacks bold ideas. It is soft where strong slogans outrun their layer conditions.

Main strategy:

> Keep the sharp SRT slogans, but attach layer, threshold, cost, failure mode, and withdrawal conditions to each one.

### 2026-04-27 PH-SS integration status

The PH-SS hardening sequence has been added and partially merged into the main short entry point:

```text
00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md      -> created
01_PH_SS_Objection_Crosswalk.md                       -> created
02_PH_SS_Hardening_Execution_Plan.md                   -> created
03_Selection_Realism_Layered_Realism_CompactPatch.md  -> created
SRT_Philosophy_Foundations_CompactCore.md             -> upgraded to active_v4
_PHILOSOPHY_MACHINE_INDEX.md                          -> created / active_v3
_SRT_Phil_Axioms_PH_SS_Guardrails.md                   -> created
SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md     -> created (O-Phil-11..20)
SRT_Ethics_PH_SS_Guardrails.md                         -> created
SRT_Social_Political_PH_SS_Guardrails.md               -> created
SRT_Social_Economics_CompactCore.md                    -> direct pointer added / active_v2
SRT_Political_Philosophy_CompactCore.md                -> direct pointer added / active_v2
```

Current hardened reading now visible in Compact Core:

> **SRT = selection realism + layered realism + anti-relativist constraint realism.**

---

## 1. Priority table

| Priority | Soft spot | Risk | Target file | Status |
|---|---|---|---|---|
| P0 | PH-SS-01: `L_0` ontology | hidden-world / modal mysticism | Compact Core, `_SRT_Phil_Axioms.md`, Core_Law L0 | compact core v4 hardened; axiom companion done; direct axiom merge pending |
| P0 | PH-SS-02: selection-before-existence | temporal priority / circularity | Compact Core, `_SRT_Phil_Axioms.md`, Foundations | compact core v4 hardened; axiom companion done; direct axiom merge pending |
| P0 | PH-SS-03: reality strength | hallucination / fact flattening | Compact Core, Foundations | compact core v4 hardened; axiom companion done; long file pending |
| P0 | PH-SS-04: subjective idealism | mind creates reality | Compact Core, README, Objection Ledger | compact core v4 hardened; O-Phil extension done |
| P0 | PH-SS-05: `Psi_f` layer confusion | concept equivocation / math metaphor | Compact Core, `_SRT_Phil_Axioms.md`, `Psi_f` canonical links | compact core v4 layer-typed; axiom companion done; canonical cross-check pending |
| P0 | PH-SS-10: consciousness threshold | panpsychism / over-attribution | Compact Core, AI, Neuroscience | compact core v4 threshold added; axiom companion done; O-Phil extension done; cross-domain files pending |
| P1 | PH-SS-06: normativity jump | is-ought gap / oppression legitimation | Ethics, Political Philosophy | compact core v4 guardrail added; axiom companion done; ethics companion done; political compact pointer done |
| P1 | PH-SS-07: purpose/teleology | mystical purpose | Compact Core, Core 24, Foundations | compact core v4 hardened; O-Phil extension done; Core 24 cross-link pending |
| P1 | PH-SS-08: `d-value` philosophy | preference-reduction | Compact Core, `d-value` canonical links | compact core v4 added; O-Phil extension done; ethics companion done; canonical cross-check pending |
| P1 | PH-SS-09: social ontology | mere construction / individualism | Social Economics, Political Philosophy | compact core v4 added; O-Phil extension done; social-political companion done; social compact pointer done |
| P1 | PH-SS-11: validation | unfalsifiability | Compact Core, Core 24, Claim Ladder | compact core v4 added; O-Phil extension done; Core 24 pending |
| P1 | PH-SS-12: anti-relativism | anything-goes | Compact Core, README, Political Philosophy | compact core v4 hardened; O-Phil extension done; social-political companion done; political compact pointer done |
| P2 | old preserved sections | duplicate / outdated claims | `_SRT_Phil_Axioms.md`, Foundations | pending refactor |
| P2 | tradition comparison | unclear novelty | Compact Core or new comparison file | pending |

---

## 2. Completed companion / pointer layer

### Done

- Compact Core includes selection realism, layered realism, `L_0` guardrail, manifestational priority, E1-E4 reality strength, `Psi_f` typing, subjecthood threshold, normativity guardrail, social ontology, anti-relativism, and non-reductive validation.
- Axiom companion contains `Def-Phil-L0-Selectability`, `Def-Phil-Manifestational-Priority`, `Def-Phil-Reality-Strength`, `Def-Phil-PsiF-Layers`, `Def-Phil-Normativity-Ladder`, and `Def-Phil-Subjecthood-Threshold`.
- Objection extension contains `O-Phil-11..20`.
- Ethics companion contains moral legitimacy ladder, friction-export test, future-selectability test, responsibility recalibration, and poetic-math guardrails.
- Social-political companion contains collective `L_2`, institutional legitimacy ladder, friction-export test, future-selectability test, dehumanization as d-exclusion, market/money guardrails, and agency-alignment checks.
- Social Economics Compact Core directly links to `SRT_Social_Political_PH_SS_Guardrails.md`.
- Political Philosophy Compact Core directly links to `SRT_Social_Political_PH_SS_Guardrails.md`.

---

## 3. Still pending

| Pending task | Why still pending |
|---|---|
| Core 24 non-reductive validation cross-link | cross-domain governance step |
| AI / Neuroscience subjecthood threshold links | should be done after checking target file content |
| Tradition comparison table | optional but useful novelty defense |

---

## 4. Next recommended sequence

1. **Done**: Add PH-SS read-first map, crosswalk, execution plan, and compact patch.
2. **Done**: Promote PH-SS files in Philosophy README.
3. **Done**: Upgrade Compact Core to v4 with selection realism / layered realism.
4. **Done as companion**: `_SRT_Phil_Axioms_PH_SS_Guardrails.md` adds `L_0` selectability, manifestational priority, reality-strength levels, `Psi_f` layers, normativity ladder, subjecthood threshold.
5. **Done as companion**: `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` adds `O-Phil-11..20`.
6. **Done as companion**: `SRT_Ethics_PH_SS_Guardrails.md` adds moral legitimacy ladder, friction export, future selectability, responsibility recalibration, poetic-math guardrails.
7. **Done as companion**: `SRT_Social_Political_PH_SS_Guardrails.md` adds collective `L_2`, institutional legitimacy, market/money guardrails, friction export, reselection capacity.
8. **Done direct pointer**: `SRT_Social_Economics_CompactCore.md` and `SRT_Political_Philosophy_CompactCore.md` now point to the social-political guardrail companion.
9. **Done direct pointer (2026-04-27)**: PH-SS guardrail pointers inserted directly into all 7 long owner files: `SRT_Philosophy_Ethics.md`, `SRT_Ethics_Agency.md`, `SRT_Philosophy_Foundations.md`, `_SRT_Phil_Axioms.md`, `SRT_Philosophy_Objection_Ledger.md`, `SRT_Political_Philosophy.md`, `SRT_Social_Economics.md`. Local guardrail notes added near `T-Eth-1`, `Ax-Eth-7`, `Ax-Phil-1`, and `Existence ≡ Being Selected`.
10. **Next**: Long Foundations refactor / annex cleanup.
11. **Next**: Core 24 non-reductive validation cross-link.

---

## 5. Compact hardening slogan

> Do not make SRT less bold. Make every bold sentence pay its layer, cost, threshold, and failure condition.
