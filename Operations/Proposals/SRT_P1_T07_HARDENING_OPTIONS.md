---
id: SRT-OPS-PROPOSAL-P1-T07-HARDENING-OPTIONS
type: proposal
status: proposal_v0_1
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-07-17
source_of_truth: "origin/main @ 14c0d7f8"
dependency:
  - SRT-OPS-AUDIT-P1-T07-PROOF-HARDENING
  - SRT-OPS-AUDIT-MAP-P1-T07-ASSUMPTIONS
tags: [Governance, Proposal, P1-T07, ProofHardening]
---

# P1-T07 Hardening — Amendment Options (proposal only)

> **Status**: non-canonical proposal memo. **Nothing here is applied.** It modifies no theorem, axiom, definition, or equation. These are candidate routes for a *later, separately authorized* theorem-amendment PR. Selection among them is the author's call and is out of scope for this pass. Basis: `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`.

## Shared preconditions for any option

Whichever option is later chosen, two items must land first (they are not optional wording fixes):

1. **Define "ε-neutral" formally**, in a way that is **not** identical to "has non-summable death hazard" (else the theorem is circular). Candidate: ε-neutral = *the writeback `A_t → A_{t+1}` applies no bias between `B≥2` and `B≤1` branches* (a condition on the transition kernel, not on the survival outcome).
2. **State the stochastic model** on `A_t` explicitly (P1-T06 is currently non-probabilistic; the proof is probabilistic — assumption-map P9).

## Option A — Keep the strong theorem, add explicit reachability + cumulative-hazard conditions

Amend the Proof Sketch so the conclusion "a.s. termination" is derived from stated premises: `∅` reachable (P2) **and** `Σ h_t = ∞` a.s. (P4), via Lévy's conditional Borel–Cantelli, **and** no neutral closed class avoiding `∅` (P6).

- **Pros**: preserves the strong statement "stable ISP ⇒ ε≠0"; makes the proof valid.
- **Cost**: the added premises are **not** currently justified from irreversibility alone; they must be independently argued. The theorem's headline strength is retained only by importing them.
- **Introduces ε-like premise?** **Yes** — P2/P4/P6 are ε-co-referential (audit §5). So this option makes P1-T07 valid **at the price of admitting it depends on an ε-grade premise**, i.e. it converts the hidden dependence into an explicit one. Honest, but it forfeits the "derived from irreversibility alone" claim.
- **Impact**:
  - *P1-T07*: proof rewritten; statement unchanged; loses the strong ε-independence reading.
  - *T-COLL-3*: needs the collective analogues of P2/P4/P6 stated independently, else it still does not close.
  - *ν_block*: its "positivity guaranteed by P1-T07" (`Irreversibility.md:240`) becomes "positivity guaranteed **given** the added premises" — must be re-scoped.
- **Minimal edit scope**: P1-T07 Proof Sketch + a premises block; `Irreversibility.md §4/§4.5` positivity clause; T-COLL-3 proof; `Irreversibility.md:240` postulate-vs-theorem line.

## Option B — Demote to a conditional theorem (leading minimal candidate, pending definitions)

Restate as: *under `L_0` irreversibility, **for a process whose neutral dynamics have divergent conditional death hazard and reachable `∅`**, a stable ISP requires anti-closure bias.* This is the honest form already latent in `L0_Metaphysics:202` (the **local** askability prior).

**Preconditions (must be discharged before Option B can be stated as a theorem):**
1. **Choose the stability semantics** — S1 (pathwise) / S2 (a.s.) / S3 (positive-survival) (audit §2). The conditional's meaning changes with the choice.
2. **Define "ε-neutral" as a property of an independently specified transition kernel** (e.g. no bias between `B≥2` and `B≤1` branches in the writeback), **not** as a survival outcome — otherwise the conditional is circular.
3. **Prove absorption under that neutral kernel** — i.e. that the declared-neutral baseline actually terminates a.s. (else the premise is vacuous or smuggles ε).

**B-lite formal candidate (relative form that could reach a clean R2):**
> Let `K₀` be an independently specified **neutral baseline kernel**. *If* `P_{K₀}(τ<∞)=1`, then any kernel `K` with positive (or almost-sure) long-run survival must **deviate from `K₀` by suppressing closure risk**; name that deviation **ISP-level anti-closure asymmetry**.
>
> This makes anti-closure a **relative** property (deviation from an a.s.-absorbing neutral baseline). It is the one route on which ε_pg could be shown *dispensable* (R2): the work is done by `K₀`'s absorption, not by an ε postulate — **provided** `P_{K₀}(τ<∞)=1` is established from `K₀`'s geometry alone.

- **Pros**: matches what the mathematics actually supports (audit §8); matches the corpus's own scoping of ε as **local** and **postulate-grade**; removes the overclaim without weakening downstream *diagnostic* use (healthy-vs-lethal `L_2` uses the anti-closure *direction*, which survives as a conditional).
- **Cost**: P1-T07 is no longer an unconditional constitutive theorem; requires touching the Three-Layer Source Hierarchy framing; and the three preconditions are real mathematical work, not wording.
- **Introduces ε-like premise?** **Depends on precondition 2/3.** If `K₀`'s absorption is proved from geometry, the anti-closure deviation is defined *without* assuming ε (candidate R2). If not, the premise stays ε-co-referential (P). Open, not settled.
- **Impact**:
  - *P1-T07*: statement becomes conditional; `ε_pg` reverts to **postulate** status (consistent with `L0_Metaphysics:202`, resolving the circularity §6.1) — unless the B-lite route succeeds, in which case anti-closure becomes a derived relative property.
  - *T-COLL-3*: becomes the collective conditional analogue (with its own S1/S2/S3 choice); no longer needs to close unconditionally.
  - *ν_block*: `ε_pg>0` reads as **postulated**, not "guaranteed by P1-T07" — correcting `Irreversibility.md:240`.
- **Minimal edit scope**: P1-T07 statement + hierarchy note; `Irreversibility.md:167/240`; T-COLL-3 statement; a one-line `OPEN_TENSIONS` update. **Smallest net change that removes the overclaim** — but only after the three preconditions are met.

## Option C — Split into three lemmas + an ε bridge

Decompose the current single theorem into:
1. **Absorbing-risk lemma**: under irreversibility, `∅` is absorbing (already canonical; P1).
2. **Stable-ISP survival lemma**: a stable ISP has positive long-run survival probability (from P1-T06 cond. 4, definitional).
3. **ε bridge**: positive long-run survival under neutral dynamics **requires** non-summable-hazard suppression, named ε anti-closure (this is where the postulate enters, explicitly).

- **Pros**: maximal transparency — isolates exactly which step is definitional (lemma 2), which is irreversibility (lemma 1), and which is the ε postulate (bridge). Makes the circularity impossible to hide.
- **Cost**: most structural churn; touches the most files; risks fragmenting a claim readers currently treat as unitary.
- **Introduces ε-like premise?** **Yes, and localizes it** to the bridge — arguably the cleanest epistemic outcome, but the heaviest edit.
- **Impact**:
  - *P1-T07*: replaced by lemma-set + bridge; the "necessity" becomes bridge-conditional.
  - *T-COLL-3*: mirror decomposition at collective scale.
  - *ν_block*: sources `ε_pg>0` to the **bridge postulate**, not to a theorem.
- **Minimal edit scope**: largest — P1-T07 section rewrite, `Irreversibility.md §3/§4/§4.5`, T-COLL-3, and cross-refs. Only worth it if the theory layer wants a permanently audit-proof structure.

## Comparison

| | Statement strength | ε honesty | Files touched | Resolves §6 contradictions | Effort |
|---|---|---|---|---|---|
| **A** | strong (unchanged) | explicit dependence | medium | partial (still theorem-flavored) | medium |
| **B** | conditional | explicit; postulate-grade *or* (via B-lite) a candidate R2 | **smallest** | **yes (1)** once preconditions met | **low edit / real proof work in preconditions** |
| **C** | decomposed | explicit + localized | largest | yes (1) | high |

## Recommendation (evaluation only — not a decision)

**Option B is the leading minimal candidate, pending semantic and kernel definition** — *not* an already-adjudicated best. It is the smallest *edit*, and its B-lite form is the only route on which `ε_pg` might be shown genuinely dispensable (R2); but it cannot be stated as a theorem until its three preconditions (choose S1/S2/S3; define ε-neutral on an independent kernel; prove that kernel absorbs a.s.) are discharged — which is real probability work, not wording. **Option C** is the most transparent long-term but the most invasive. **Option A** keeps the headline only by making the ε-dependence explicit, which undercuts the "derived from irreversibility" reading it tries to preserve.

**None of A/B/C is applied here.** A later PR, separately authorized, would pick one, discharge the preconditions, and edit canonical text under the edit protocol. This pass stops at the proposal.
