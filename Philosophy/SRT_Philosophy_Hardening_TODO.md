---
id: SRT-PHIL-HARDENING-TODO
type: hardening-plan
tags: [Philosophy, TODO, Hardening, Claim Hygiene, Refactor, PH-SS]
status: active_v4
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
| P1 | PH-SS-06: normativity jump | is-ought gap / oppression legitimation | Ethics, Political Philosophy | compact core v4 guardrail added; axiom companion done; ethics companion done |
| P1 | PH-SS-07: purpose/teleology | mystical purpose | Compact Core, Core 24, Foundations | compact core v4 hardened; O-Phil extension done; Core 24 cross-link pending |
| P1 | PH-SS-08: `d-value` philosophy | preference-reduction | Compact Core, `d-value` canonical links | compact core v4 added; O-Phil extension done; ethics companion done; canonical cross-check pending |
| P1 | PH-SS-09: social ontology | mere construction / individualism | Social Economics, Political Philosophy | compact core v4 added; O-Phil extension done; social-political companion done |
| P1 | PH-SS-11: validation | unfalsifiability | Compact Core, Core 24, Claim Ladder | compact core v4 added; O-Phil extension done; Core 24 pending |
| P1 | PH-SS-12: anti-relativism | anything-goes | Compact Core, README, Political Philosophy | compact core v4 hardened; O-Phil extension done; social-political companion done |
| P2 | old preserved sections | duplicate / outdated claims | `_SRT_Phil_Axioms.md`, Foundations | pending refactor |
| P2 | tradition comparison | unclear novelty | Compact Core or new comparison file | pending |

---

## 2. Task H-Phil-1 — Harden existence levels

### Problem

`Existence ≡ Being Selected` is philosophically powerful but can be misread as:

- human observers create the universe;
- unobserved entities do not exist;
- hallucinations and physical objects have the same status;
- SRT is subjective idealism.

### Done condition

- Compact Core includes E1–E4. **Done in Compact Core v4.**
- Axiom companion contains `Def-Phil-Reality-Strength`. **Done.**
- `_SRT_Phil_Axioms.md` directly references E1–E4 near Ax-Phil-1. **Pending direct merge.**
- Strong existence claims specify which E-level they mean.

---

## 3. Task H-Phil-2 — Operationalize `Psi_f` resistance

### Done condition

- Compact Core includes proxies and layer typing. **Done in Compact Core v4.**
- Axiom companion contains `Def-Phil-PsiF-Layers`. **Done.**
- Objection extension contains `O-Phil-14`. **Done.**
- Any philosophy file appealing to `Psi_f` says whether it means subjective difficulty, operational resistance, or canonical friction. **Ongoing.**

---

## 4. Task H-Phil-3 — Clarify `L_1` as anchoring event

### Done condition

- Compact Core includes anchoring distinction. **Done in Compact Core v4.**
- Foundations long file avoids language implying `L_1` is a second substance. **Pending.**
- Objection Ledger O-Phil-1 references anchoring explicitly. **Existing ledger covers; extension adds surrounding guardrails.**

---

## 5. Task H-Phil-4 — Subjecthood threshold

### Done condition

- Compact Core includes threshold model. **Done in Compact Core v4.**
- Axiom companion contains `Def-Phil-Subjecthood-Threshold`. **Done.**
- Objection extension contains `O-Phil-18`. **Done.**
- Any micro-selection paragraph says micro-selection does not entail subjecthood. **Ongoing.**

---

## 6. Task H-Phil-5 — Formula-role cleanup

### Done condition

- Compact Core formula roles are labeled or converted into prose where safer. **Mostly done in Compact Core v4.**
- Objection extension contains formula-risk objections where relevant (`O-Phil-14`, `O-Phil-19`). **Done.**
- Ethics companion includes poetic-math guardrails. **Done.**
- `_SRT_Phil_Axioms.md` formula roles are labeled. **Pending.**
- Main ethics / political formulas with strong language are labeled directly. **Pending direct merge.**

---

## 7. Task H-Phil-6 — Unify paradox theory

### Done condition

- Compact Core uses unified diagnostic. **Done in Compact Core v4.**
- `_SRT_Phil_Axioms.md` old paradox formulas are replaced or annotated. **Pending.**
- Foundations long file points to unified diagnostic. **Pending.**

---

## 8. Task H-Phil-7 — Moral legitimacy ladder

### Done condition

- Compact Core includes stabilization ≠ legitimacy guardrail. **Done in Compact Core v4.**
- Axiom companion contains normativity ladder. **Done.**
- Objection extension includes `O-Phil-17` and `O-Phil-20`. **Done.**
- Ethics companion contains moral legitimacy ladder, friction-export test, future-selectability test, responsibility recalibration, and poetic-math guardrails. **Done.**
- Ethics file directly distinguishes moral intensity, moral reality, and moral legitimacy. **Pending direct merge.**
- `d-value` expansion is not treated as sufficient for moral progress. **Companion done; direct ethics merge pending.**
- Structural evil / occlusion links are explicit. **Existing cross-links exist; direct integration pending.**

---

## 9. Task H-Phil-8 — Social / political legitimacy and collective L2

### Done condition

- Compact Core includes social ontology and anti-relativism guardrails. **Done in Compact Core v4.**
- Social-political companion contains collective `L_2`, recognition-enforcement-memory loop, institutional legitimacy ladder, friction-export test, future-selectability test, dehumanization as d-exclusion, market/money guardrails, and agency-alignment checks. **Done.**
- `SRT_Social_Economics_CompactCore.md` directly links to the companion. **Pending direct pointer.**
- `SRT_Political_Philosophy.md` directly links to the companion. **Pending direct pointer.**

---

## 10. Task H-Phil-9 — Refactor preserved old sections

### Problem

`_SRT_Phil_Axioms.md` and `SRT_Philosophy_Foundations.md` preserve old content that partially duplicates newer hardened sections.

### Hardening target

Split old content into:

| Section type | Treatment |
|---|---|
| current mainline | keep in Part A |
| useful expansion | move or label as Part B commentary |
| legacy duplicate | mark as legacy / superseded by Compact Core v4 |
| overstrong formula | annotate with formula role or withdrawal condition |

### Done condition

- Ax-Phil / Ax-Ph naming is harmonized.
- old paradox and ineffability formulas no longer contradict Compact Core v4.
- legacy passages are not mistaken for current strongest claims.

---

## 11. Task H-Phil-10 — Tradition comparison table

### Problem

SRT references many traditions but does not always say what is accepted, rewritten, or newly added.

### Hardening target

Create comparison table:

| Tradition | SRT accepts | SRT rewrites | SRT adds |
|---|---|---|---|
| Kant | experience is formatted | categories become dynamic `theta` | `Psi_f` and selection cost |
| Husserl | givenness matters | epoché as `L_2` gate suppression | triadic dynamics |
| Gibson / Varela | cognition is coupling | coupling is costed anchoring | payable anchoring |
| Physicalism | `L_2` description is powerful | description is not anchoring | manifestation operation |
| Panpsychism | continuity question matters | micro-selection is not subjecthood | subjecthood threshold |
| Wittgenstein | language-game stabilization | language as `L_2` closure | layer diagnostics |

### Done condition

- Add table to Compact Core or new file.
- Use it to prevent “SRT is just X” objections.

---

## 12. Next recommended sequence

1. **Done**: Add PH-SS read-first map, crosswalk, execution plan, and compact patch.
2. **Done**: Promote PH-SS files in Philosophy README.
3. **Done**: Upgrade Compact Core to v4 with selection realism / layered realism.
4. **Done as companion**: `_SRT_Phil_Axioms_PH_SS_Guardrails.md` adds `L_0` selectability, manifestational priority, reality-strength levels, `Psi_f` layers, normativity ladder, subjecthood threshold.
5. **Done as companion**: `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` adds `O-Phil-11..20`.
6. **Done as companion**: `SRT_Ethics_PH_SS_Guardrails.md` adds moral legitimacy ladder, friction export, future selectability, responsibility recalibration, poetic-math guardrails.
7. **Done as companion**: `SRT_Social_Political_PH_SS_Guardrails.md` adds collective `L_2`, institutional legitimacy, market/money guardrails, friction export, reselection capacity.
8. **Next**: Add direct pointers from main Ethics / Social Economics / Political Philosophy files to their guardrail companions.
9. **Next**: Long Foundations refactor / annex cleanup.
10. **Next**: Optional direct merge from companions into owner files after review.

---

## 13. Compact hardening slogan

> Do not make SRT less bold. Make every bold sentence pay its layer, cost, threshold, and failure condition.
