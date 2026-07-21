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

## Option A — Keep the strong theorem, grounded in an independent neutral baseline `K₀`

Amend the Proof Sketch so "a.s. termination of neutral `P`" is derived from an **independently specified neutral baseline kernel `K₀`** with `P_{K₀}(τ<∞)=1`, rather than from a simultaneous conjunction of premises. The absorption `P_{K₀}(τ<∞)=1` may be established by **any one** of three alternative sufficient packages (do **not** require them all together):

- **A1** — uniform conditional hazard lower bound `h_t ≥ δ > 0`;
- **A2** — divergent cumulative conditional hazard along surviving histories (`Σ h_t = ∞`);
- **A3** — Markov absorption (all nonempty states transient / no other closed recurrent class).

Each package internally supplies reachability, so reachability is not a separate premise.

- **Pros**: preserves the strong statement "stable ISP ⇒ ε≠0" *once* `K₀`-absorption is proved; makes the proof valid.
- **Cost**: `P_{K₀}(τ<∞)=1` is **not** currently established from irreversibility alone; it must be proved from `K₀`'s geometry via A1/A2/A3.
- **Introduces ε-like premise?** **Undecided — `E` pending the `K₀` definition (revised from Proof-Audit-1.0/1.1).** The earlier claim that "P2/P4/P6 are ε-co-referential" is **withdrawn**: A1/A2/A3 could each follow from an independently specified unbiased kernel/geometry, or could collapse into ε_pg's `B≥2 ≻ B≤1` bias — that is exactly what a `K₀` definition would settle. Not asserted as ε here.
- **Impact**:
  - *P1-T07*: proof rewritten around `K₀`; statement unchanged; ε-status of the baseline is the open question.
  - *T-COLL-3*: needs a collective baseline `K₀^{coll}` with `P_{K₀^{coll}}(τ<∞)=1`, else it still does not close.
  - *ν_block*: its "positivity guaranteed by P1-T07" (`Irreversibility.md:240`) becomes "positivity guaranteed **given** `K₀`-absorption" — must be re-scoped.
- **Minimal edit scope**: P1-T07 Proof Sketch + a `K₀` premises block; `Irreversibility.md §4/§4.5` positivity clause; T-COLL-3 proof; `Irreversibility.md:240` line.

## Option B — Demote to a conditional theorem (leading minimal candidate, pending definitions)

Restate as: *under `L_0` irreversibility, **for a process whose neutral dynamics have divergent conditional death hazard and reachable `∅`**, a stable ISP requires anti-closure bias.* This is the honest form already latent in `L0_Metaphysics:202` (the **local** askability prior).

**Preconditions (must be discharged before Option B can be stated as a theorem):**
1. **Choose the stability semantics** — S1 (pathwise) / S2 (a.s.) / S3 (positive-survival) (audit §2). The conditional's meaning changes with the choice.
2. **Define "ε-neutral" as a property of an independently specified transition kernel** (e.g. no bias between `B≥2` and `B≤1` branches in the writeback), **not** as a survival outcome — otherwise the conditional is circular.
3. **Prove absorption under that neutral kernel** — i.e. that the declared-neutral baseline actually terminates a.s. (else the premise is vacuous or smuggles ε).

**B-lite formal candidate (relative comparative proposal — NOT a completed constitutive theorem):**
> Let `K₀` be an independently specified **neutral baseline kernel**. *If* `P_{K₀}(τ<∞)=1`, then any kernel `K` with positive (or almost-sure) long-run survival must **deviate from `K₀` by suppressing closure risk**. Name that deviation **ISP-level anti-closure asymmetry**, and identify it by a **comparative** condition (at least one required):
> - `P_K(τ>t) > P_{K₀}(τ>t)` for some `t` (strictly higher survival than the neutral baseline), **or**
> - `h_t^K < h_t^{K₀}` on a **non-null** set of histories (strictly lower death hazard than baseline somewhere).
>
> This makes anti-closure a **relative** property (a measured deviation from an a.s.-absorbing neutral baseline), not an intrinsic postulate. It is the one route on which ε_pg could be shown *dispensable* (R2): the work is done by `K₀`'s absorption plus the comparative gap, not by an ε postulate — **provided** `P_{K₀}(τ<∞)=1` is established from `K₀`'s geometry alone. **Current status: a comparative *proposal*, pending (i) a construction of `K₀`, (ii) a proof of `K₀`-absorption, (iii) the S1/S2/S3 semantics.** It is not yet a theorem.

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
2. **Persistence lemma (semantics-dependent)**: fix a stability semantics — S1 (`τ=∞` pathwise) / S2 (`P(τ=∞)=1`) / S3 (`P(τ=∞)>0`); "stable ISP" is then the chosen persistence condition. **P1-T06 by itself yields *no* probabilistic survival statement** — the survival content is entirely whatever the chosen semantics fixes (this corrects the earlier "positive long-run survival from the definition", which the definition does not deliver).
3. **ε bridge**: the chosen persistence, under neutral dynamics, **requires** a closure-risk-suppressing deviation from an absorbing neutral baseline, named ε anti-closure (this is where the postulate — or, via B-lite, a relative comparative condition — enters, explicitly).

- **Pros**: maximal transparency — isolates exactly which step is definitional (lemma 2), which is irreversibility (lemma 1), and which is the ε postulate (bridge). Makes the circularity impossible to hide.
- **Cost**: most structural churn; touches the most files; risks fragmenting a claim readers currently treat as unitary.
- **Introduces ε-like premise?** **E — pending, decided at the bridge**: **yes** if the bridge is discharged by the ε postulate; **not necessarily** if the bridge is discharged by an independently constructed B-lite baseline (`K₀`-absorption + comparative deviation). Either way the decomposition *localizes* the question to the bridge — the cleanest epistemic outcome, but the heaviest edit.
- **Impact**:
  - *P1-T07*: replaced by lemma-set + bridge; the "necessity" becomes bridge-conditional.
  - *T-COLL-3*: mirror decomposition at collective scale.
  - *ν_block*: sources `ε_pg>0` to the **bridge postulate**, not to a theorem.
- **Minimal edit scope**: largest — P1-T07 section rewrite, `Irreversibility.md §3/§4/§4.5`, T-COLL-3, and cross-refs. Only worth it if the theory layer wants a permanently audit-proof structure.

## Comparison

| | Statement strength | ε honesty | Files touched | Resolves §6 contradictions | Effort |
|---|---|---|---|---|---|
| **A** | strong (unchanged) | ε-status of `K₀` is **E — pending** | medium | partial (needs `K₀`-absorption proof) | medium |
| **B** | conditional | explicit; postulate-grade *or* (via B-lite) a candidate R2 | **smallest** | **yes (1)** once preconditions met | **low edit / real proof work in preconditions** |
| **C** | decomposed | explicit + localized | largest | yes (1) | high |

## Recommendation (evaluation only — not a decision)

**Option B is the leading minimal candidate, pending semantic and kernel definition** — *not* an already-adjudicated best. It is the smallest *edit*, and its B-lite form is the only route on which `ε_pg` might be shown genuinely dispensable (R2); but it cannot be stated as a theorem until its three preconditions (choose S1/S2/S3; define ε-neutral on an independent kernel; prove that kernel absorbs a.s.) are discharged — which is real probability work, not wording. **Option C** is the most transparent long-term but the most invasive. **Option A** preserves the strong headline but requires the strongest neutral-baseline construction and absorption proof; whether it preserves ε-independence remains **E — pending on `K₀`**.

**None of A/B/C is applied here.** A later PR, separately authorized, would pick one, discharge the preconditions, and edit canonical text under the edit protocol. This pass stops at the proposal.
