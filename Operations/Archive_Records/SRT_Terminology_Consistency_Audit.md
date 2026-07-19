---
id: SRT-TERMINOLOGY-CONSISTENCY-AUDIT-2026-04-27
type: terminology_audit
tags:
  - SRT
  - Terminology
  - Consistency
  - Audit
  - L0
  - L1
  - L2
  - Psi_f
  - d-value
  - theta
  - Ghost-Operator
  - Subjecthood
  - Agency
status: active_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - CANONICAL_REGISTRY.md
  - Philosophy/SRT_Philosophy_Foundations_CompactCore.md
  - Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Core/SRT_Validation_Template.md
  - Experiments/SRT_Experimental_Roadmap_v1.md
machine_summary: >
  Root-level terminology consistency audit for SRT. It records canonical terms, allowed aliases,
  forbidden overreadings, domain-specific usage, and owner files for L0, L1, L2, Psi_f, d-value,
  theta, G_hat_theta / Ghost Operator, subjecthood, consciousness, agency, responsibility,
  selection, manifestation, hardening, and validation language.
---

# SRT Terminology Consistency Audit

> **Purpose**: Make SRT terminology easier for humans and machines to read consistently.  
> **Status**: Audit / routing file. It does not define canonical primitives by itself.  
> **Rule**: Prefer canonical terms in formal writing; use aliases only when their scope and risks are clear.

---

## 0. Why this audit exists

SRT now has many connected files across Philosophy, Core, AI, Neuroscience, Experiments, and Ethics. This creates a risk of semantic drift:

```text
same concept -> many aliases -> unclear scope -> overclaim risk
```

This audit provides a first-pass map:

```text
canonical term;
allowed aliases;
forbidden overreadings;
domain-specific usage;
owner file;
cleanup status.
```

---

## 1. High-priority terminology table

| Canonical term | Allowed aliases | Forbidden overreadings | Domain-specific usage | Owner / route | Cleanup status |
|---|---|---|---|---|---|
| `L_0` | latent field, modal field of selectability, possibility field, latent domain | hidden object-world, mystical substance, already-existing invisible inventory | Philosophy: modal selectability; AI: search / candidate space only by analogy; physics: not a direct physical container | Philosophy Compact Core; Axiom guardrails | guarded; monitor aliases |
| `L_1` | manifestation, anchoring, selected reality, manifest event | mere subjective belief, arbitrary construction, canonical public truth by default | Philosophy: manifest anchoring; neuroscience: conscious-content candidate; AI: not proven for current systems | Philosophy Compact Core; Subjecthood Interface | guarded |
| `L_2` | hardening, stabilization, sedimentation, automation, constraint domain | moral legitimacy, final truth, natural goodness, mere memory | Social: institutions/norms; cognitive: habits/schemas; physics: stable constraint descriptions | Core L2 files; Social/Political guardrails | guarded; monitor moral overreadings |
| `Psi_f` | ontological friction, selection cost, transition cost, constraint resistance | one single cost, mere prediction error, literal suffering, only Fisher metric | Core: selection friction; information geometry: Fisher slice; ethics/social: hidden burden/friction export | Psi_f canonical; Core24; Axiom guardrails | needs canonical cross-check |
| `d-value` | concern bandwidth, existential stake, non-substitutability weight, value-gradient | salience, preference intensity, utility, reward, moral goodness | Ethics: moral intensity not legitimacy; AI: stake threshold; neuroscience: concern-weighted anchoring | d-value canonical; Ethics guardrails; Subjecthood Interface | needs canonical cross-check |
| `theta` / `θ` | operator constraint, observer constraint, embodiment parameter, constraint profile | subjective will, arbitrary choice, human opinion | Philosophy: selection condition; AI: architecture / policy / memory constraints by analogy | Foundations Compact Core; Axioms | guarded |
| `G_hat_theta` / `Ĝ_θ` | Ghost Operator, selection operator, actualization operator | magical agent, conscious chooser, homunculus | Core: operator mapping; philosophy: manifestation under constraint; AI: not an inner self | Core / Foundations | monitor poetic usage |
| selection | filtering, choosing, stabilization, actualization, candidate selection | consciousness, free will, moral endorsement, subjective invention | Broad cross-domain term; must state level | Core / Philosophy Compact Core | guarded |
| manifestation | anchoring, selected event, `L_1` realization | hallucination equals public truth, mind creates object | Philosophy: local vs public reality must be distinguished | Philosophy Compact Core | guarded |
| hardening | stabilization, sedimentation, constraint formation, `L_2` formation | moral progress, legitimacy, finality | Social/political: institutionalization; cognitive: automation | Core / Social/Political guardrails | guarded |
| subjecthood | continuing perspective, bounded concern-field, S4 | consciousness content, self-report, intelligence, tool use | AI/Neuro: high threshold; Ethics: prerequisite for responsibility | Subjecthood Interface | guarded |
| consciousness | conscious content, integrated conscious field, thick `L_1` | all selection, all integration, all access, all reportability | Neuroscience: content/field; AI: not inferred from language | Neuroscience Compact Core; AI rubric | guarded |
| agency | meta-selection, action ownership, policy revision, S5 | output, automation, causal contribution, tool use | AI: A0-A3; Ethics: selectable alternatives | AI Agency Note; Subjecthood Interface | guarded |
| responsibility | answerability, repair obligation, S6 | causation, harm magnitude, blame, outcome responsibility alone | Ethics/AI: requires agency, norm access, alternatives, repair path | Ethics guardrails; AI Agency Note | guarded |
| legitimacy | justified stabilization, normatively valid `L_2` | stability, legality, efficiency, persistence | Political/social: must check friction export and future selectability | Social/Political guardrails | guarded |
| validation | non-reductive verification, proxy package, structural convergence | unfalsifiability, beyond measurement, proof by metaphor | Core/Experiments: must include proxy, baseline, failure condition | Core Validation Template; Experimental Roadmap | active |

---

## 2. Term-specific notes

### 2.1 `L_0`

Preferred formal phrase:

```text
L_0 = modal field of selectability / latent domain of possible manifestation
```

Allowed public phrase:

```text
field of possibilities
```

Avoid:

```text
hidden world;
invisible object inventory;
pre-existing completed reality behind reality;
God-like container of all things.
```

Guardrail:

> `L_0` should be read as a condition of possible manifestation, not as an object-like hidden world.

---

### 2.2 `L_1`

Preferred formal phrase:

```text
L_1 = manifest anchoring / selected manifestation under operator constraints
```

Allowed public phrase:

```text
what becomes manifest
```

Avoid:

```text
mere belief;
private fantasy;
canonical public truth by default.
```

Guardrail:

> `L_1` can be local, thin, thick, private, public, stable, or unstable. Do not flatten all `L_1` into E4 canonical reality.

---

### 2.3 `L_2`

Preferred formal phrase:

```text
L_2 = stabilized constraint domain / hardened selection history
```

Allowed public phrase:

```text
habit, norm, institution, law, model, or memory that constrains future selection
```

Avoid:

```text
moral truth;
legitimacy;
final reality;
just because stable, therefore good.
```

Guardrail:

> `L_2` reality is not `L_2` legitimacy.

---

### 2.4 `Psi_f`

Preferred formal phrase:

```text
Psi_f = selection friction / transition cost across a specified layer
```

Allowed aliases:

```text
ontological friction;
selection cost;
transition cost;
constraint resistance.
```

Use with layer typing:

```text
Psi_f^inf   information-geometric / model-update slice
Psi_f^emb   embodied / physiological / action cost
Psi_f^norm  normative / social / institutional friction
Psi_f^field stabilized field-level friction, where justified
```

Avoid:

```text
all Psi_f is Fisher metric;
all Psi_f is suffering;
all Psi_f is prediction error;
all Psi_f is one scalar.
```

Guardrail:

> Fisher information may express `Psi_f` on an information-geometric slice; it does not exhaust all embodied, ontological, or normative friction.

---

### 2.5 `d-value`

Preferred formal phrase:

```text
d-value = concern-weighted non-substitutability / existential stake bandwidth
```

Allowed aliases:

```text
concern bandwidth;
existential stake;
non-substitutability weight;
future-selectability weight.
```

Avoid:

```text
salience;
preference intensity;
reward;
utility;
moral goodness;
consciousness proof.
```

Guardrail:

> High `d-value` can mark what matters to a system; it does not automatically mark what is morally good, conscious, or legitimate.

---

### 2.6 `theta` / `θ`

Preferred formal phrase:

```text
theta = operator constraint profile
```

Allowed aliases:

```text
observer constraint;
embodied parameter;
constraint profile;
selection condition.
```

Avoid:

```text
subjective will;
free choice;
private opinion;
conscious intention.
```

Guardrail:

> `theta` conditions selection without making reality arbitrary.

---

### 2.7 `G_hat_theta` / `Ĝ_θ`

Preferred formal phrase:

```text
G_hat_theta = selection / manifestation operator conditioned by theta
```

Allowed aliases:

```text
Ghost Operator;
selection operator;
actualization operator.
```

Avoid:

```text
magical ghost;
inner homunculus;
conscious chooser;
free-will entity.
```

Guardrail:

> `G_hat_theta` names the constrained mapping from latent selectability to manifestation; it is not itself a little person inside the system.

---

### 2.8 Subjecthood / consciousness / agency / responsibility

Preferred ladder:

```text
S0 selection event
S1 local L1 anchoring
S2 conscious content
S3 integrated conscious field
S4 subjecthood
S5 agency
S6 responsibility-bearing subject
```

Avoid:

```text
selection = consciousness;
conscious content = subjecthood;
agency = responsibility;
harm caused = culpability.
```

Guardrail:

> Selection is broad; consciousness is thresholded; subjecthood is continuity-bound; agency is meta-selective; responsibility is normatively constrained.

---

## 3. Preferred wording by audience

| Audience | Prefer | Avoid |
|---|---|---|
| Academic philosophy | selection realism, layered realism, manifestational priority | mind creates reality |
| Cognitive science | concern-weighted reorganization, transition friction | mystical value force |
| Neuroscience | anchoring, gating, thick/thin `L_1`, d-modulated priority | every neural selection is consciousness |
| AI | S0-S6 rubric, functional/delegated agency, subjecthood threshold | chatbot says it feels, therefore conscious |
| Ethics | moral reality / intensity / legitimacy distinction | stable norm = moral norm |
| Social/political | collective `L_2`, friction export, future-selectability | institutions are automatically agents |
| Public writing | possibilities are selected, paid for, stabilized, hardened | SRT explains everything |

---

## 4. Terms needing future scan

A future Claude Code / Codex scan should check for inconsistent usage of:

```text
possibility space vs L0;
selected reality vs L1;
hardening vs L2;
friction vs Psi_f;
concern vs d-value;
observer vs theta;
Ghost Operator vs selection operator;
consciousness vs subjecthood;
agency vs responsibility;
legitimacy vs stability.
```

Suggested future prompt:

```text
Search the repository for these aliases. Report contexts where an alias may overstate the canonical term, especially where:
- L0 sounds like a hidden object-world;
- L1 sounds like public truth by default;
- L2 sounds morally legitimate;
- Psi_f sounds identical to Fisher metric or prediction error;
- d-value sounds like salience, utility, or moral goodness;
- selection sounds like consciousness;
- AI agency sounds like moral responsibility.
Do not edit files in the first pass. Produce an audit list only.
```

---

## 5. Cleanup priority

| Priority | Cleanup target | Why |
|---|---|---|
| P0 | `Psi_f ≡ g` contexts | high risk of mathematical overclaim |
| P0 | `d-value` vs salience / morality contexts | central to ethics, AI, neuroscience |
| P0 | `selection = existence` slogans | high risk of idealist / temporal misread |
| P1 | subjecthood / consciousness / agency mixing | AI and ethics risk |
| P1 | `L_2` stability / legitimacy mixing | political philosophy risk |
| P1 | Ghost Operator poetic language | risk of mystical interpretation |
| P2 | public-facing simplifications | outreach risk but less technical |

---

## 6. Minimal term discipline rule

When writing new SRT material, use this rule:

```text
First use canonical term;
then allow alias in parentheses;
then state guardrail if the alias could mislead.
```

Example:

```text
`L_0` should be read as a modal field of selectability, not as a hidden object-world. Publicly, it can be called a field of possibilities, but that phrase must not imply a pre-existing inventory of objects.
```

---

## 7. Conclusion

SRT should preserve its strong vocabulary while preventing term drift.

The safest summary:

```text
L0 = selectable possibility, not hidden object-world;
L1 = manifest anchoring, not arbitrary belief;
L2 = stabilized constraint, not moral legitimacy;
Psi_f = typed selection friction, not one scalar cost;
d-value = concern-weighted non-substitutability, not salience or utility;
theta = constraint profile, not subjective will;
G_hat_theta = constrained selection operator, not homunculus;
subjecthood = thresholded continuity, not mere selection;
agency = meta-selection, not output;
responsibility = normatively constrained answerability, not causation alone.
```
