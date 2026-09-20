---
id: SRT-SELECTION-TOTALITY-WAVE-E4-EXACT-SPEC-INDEPENDENT-REVIEW-2026-09-16
type: audit
status: active
layer: governance
epistemic_layer: audit
claim_mode: independent_review
---

# Wave E4 exact-spec independent review — Collective consumer + tower hardening

## Verdict

```text
E4 PRELANDING: PASS
E4 EXACT PATCH SPEC: PASS
NEW AUTHOR THEORY ADJUDICATION: NOT REQUIRED
AUTHOR CONTINUATION AUTHORIZATION: PRESENT
E4-A EXECUTION READINESS: READY
E4-B EXECUTION READINESS: READY
CODEX / FULL WORKTREE REQUIRED: YES
E5+: HOLD
MERGE #976: NO
```

Reviewed proposal:

```text
Operations/Proposals/SRT_SELECTION_TOTALITY_WAVE_E4_COLLECTIVE_PATCH_SPEC_2026-09-16.md
```

Reviewed prelanding:

```text
Operations/Audits/SRT_SELECTION_TOTALITY_WAVE_E4_COLLECTIVE_PRELANDING_REVIEW_2026-09-16.md
```

This review is read-only with respect to theory owners.

---

## 1. Scope review

The two-stage split is necessary and sufficiently bounded:

```text
E4-A:
  Core_Law/SRT_Collective_Selection.md

E4-B:
  Core_Law/SRT_Collective_Tower_Hardening_Notes.md

E4-B derivative:
  Core_Law/Collective_Tower_Hardening_Notes_Split/*
  generated only by scripts/create_reading_split.py
```

Why two semantic owners are required:

- the primary Collective owner contains standing/subject/health/normative and E3 formal backflow;
- the extracted Tower owner separately contains `P1-candidate` recursive projection, `Delta_coll ≡ Rhat_coll`, total-conservation, stake-weighted closure, and spectrum/Lyapunov -> health/pathology backflow;
- leaving Tower untouched after E4-A would leave a known downstream route that can re-import claims already rejected by E2/E3.

Why the owners must still be separate commits:

- Collective is the primary structural owner;
- Tower is downstream hardening;
- separate commits preserve blame/review and allow E4-A semantics to be reviewed before tower synchronization.

Verdict:

```text
SCOPE = PASS
BROAD CLEANUP = REJECTED
```

---

## 2. T-COLL-1 review

The exact spec correctly does **not** delete collective Stable-ISP analysis. It preserves a useful group-level standing programme while removing unsupported inheritance.

Correct structure:

```text
declared group-level candidate unit
+
group-level P1-T06-type burdens
-> P2 collective Stable-ISP standing/admission candidate
```

The P2 status is appropriate because T-COLL-1 is a group-specific application/admission construction with additional boundary/measurement burdens; P1-T06 remains the P1 upstream standing theorem. A local extension does not inherit P1 merely by analogy.

The spec also correctly keeps the following separate:

```text
collective Stable ISP
!= collective subject
!= Bearer
!= Agency
!= consciousness / phenomenality
!= generative health
!= legitimacy
```

This is not a new author decision; it follows from the landed Spine and P1-T06 boundaries.

Verdict:

```text
T-COLL-1 RETYPING = PASS
```

---

## 3. M(t) / externalization review

The exact spec correctly preserves `M(t)` as a useful consequence-return/distribution model while removing its use as a direct moral/health scalar.

Required distinction is now explicit:

```text
consequence/burden externalization
!= suffering externalization
!= evil / domination / injustice / legitimacy verdict
```

This directly follows Wave E2 Suffering and E3-B MOC boundaries. No theory loss occurs: asymmetry, row/column structure, recourse/exposure/attention and cross-position consequence return remain available as model features.

Verdict:

```text
M(t) RETYPING = PASS
```

---

## 4. Collective formalism review

The spec correctly applies E3-A/E3-B component-first discipline:

```text
sigma_coll = model-local / replaceable
collective d_c = declared model coordinate
T_dir_coll = direction-admitted only
S_sig/S_str = suffering-admitted only
M couplings = candidate model terms
```

It correctly removes universal routes:

```text
M_asym -> d_c universally
sigma_coll -> B phase universally
sigma_coll -> health/pathology
M_ext -> suffering
signal suppression -> conserved / redistributed S_str
```

The mathematics is retained as P2/P3 model structure rather than deleted.

Verdict:

```text
COLLECTIVE MODEL PROGRAMME PRESERVED = PASS
NO E3 BACKFLOW = PASS
```

---

## 5. `T-PROJ-1^coll` review

The exact spec correctly demotes the multi-process projection to the same class as its E3-A single-P parent:

```text
T-PROJ-1^coll = P2 conditional projection/model result
```

Important corrections are all present:

- T-COLL-1 does not magically prove compactness/Lipschitz conditions;
- MOC does not identify the full `M(t)` matrix or a Hessian by itself;
- direction and suffering branches require independent admission;
- projection cannot back-define upstream owners;
- collective coefficients are candidate correspondences, not unique canonical identities.

Verdict:

```text
T-PROJ-1^coll = PASS
```

---

## 6. Tower / recursive projection review

The spec preserves the useful recursive tower, layer-skip, spectral and Lyapunov research programme while removing three invalid shortcuts:

```text
recursive closure -/> standing / subjecthood
mathematical stability -/> generative health
mathematical instability -/> pathology / suffering
```

This is the correct non-destructive truth-up.

Verdict:

```text
TOWER PROGRAMME PRESERVATION = PASS
TOWER CLAIM-STRENGTH TRUTH-UP = PASS
```

---

## 7. `T-DELTA-1^coll` review

The spec fully imports the E3-B residual discipline:

```text
Delta_coll = selected weighted summary/proxy
not unconditional full-R equivalence
```

and correctly blocks:

```text
stake -> unique weights
normalization -> conservation
signal suppression -> hidden burden/suffering conservation
```

Stronger equivalence or conservation remains available inside an explicitly closed model with the required measurement/transfer/boundary assumptions.

Verdict:

```text
T-DELTA-1^coll SYNC = PASS
```

---

## 8. Spectral / Lyapunov review

The exact spec identifies a genuine mathematical wording defect rather than merely an epistemic-strength issue: the current Tower text mixes a `global exponential` claim with a later disclaimer that only local Lyapunov stability / no global basin is established.

The required repair is mathematically appropriate:

```text
global exponential result
only if assumptions/bounds hold on a declared forward-invariant domain;
otherwise local result within the neighborhood where the assumptions hold.
```

The spec also correctly separates this mathematical result from generative-health interpretation.

Verdict:

```text
LOCAL/GLOBAL REPAIR = REQUIRED AND WELL-SPECIFIED
NEW AUTHOR DECISION = NO
```

---

## 9. Deterministic split review

The registered Tower reading split is real and its README records source bytes/hash. `scripts/create_reading_split.py` is the repository generator and writes the README plus numbered shards from the semantic owner.

The exact command in the patch spec preserves the current split id:

```text
SRT-COLLECTIVE-TOWER-HARDENING-SPLIT-INDEX
```

The spec correctly does **not** freeze the current three-part topology. Semantic edits may change shard boundaries or part count; the generator's actual output is authoritative for the derivative layer.

The currently duplicated README heading (`... Split Index Split Index`) may naturally disappear when the generator is invoked with the clean `--title "SRT Collective Tower Hardening Notes"`; that is acceptable generator output inside the derivative-only scope, not a semantic theory edit.

Verdict:

```text
DERIVATIVE PLAN = PASS
MANUAL SHARD EDIT = FORBIDDEN
```

---

## 10. Frozen / governance authority debt

A separate non-blocking authority-sync debt remains outside E4 semantic scope.

Current `_SRT_SYMBOL_TABLE.md` still contains legacy label text such as `sigma_sr^{sub}` / `Subject-Position Entry Threshold`, while prior author-adjudicated reconstruction records already say this label is to be retired/rewritten as a model threshold and E3-A/E3-B owners have truth-upped the active semantics.

Because `_SRT_SYMBOL_TABLE.md` is Freeze-A, E4 must **not** opportunistically edit it. During E4 execution:

```text
legacy symbol-table label -/> permission to restore subject-entry threshold semantics
```

Record the symbol/registry/claim-mode synchronization debt for a separately governed authority-sync wave.

This debt is not an E4 blocker because the Generative Ontology Spine and the newly truth-upped semantic owners govern the cross-owner non-identity/order constraints, and E4 is downstream synchronization rather than symbol-authority reconstruction.

Likewise, stale `draft_v0` / `P1-candidate` descriptions in `CANONICAL_REGISTRY.md`, `Governance/SRT_CLAIM_MODE_AUDIT.md` and `_SRT_INDEX.md` are metadata/navigation debt unless a formal governance check requires immediate synchronization. Do not expand E4 semantic commits to clean them opportunistically.

Verdict:

```text
FROZEN AUTHORITY SYNC DEBT = NON-BLOCKING / LATER GOVERNED WAVE
```

---

## 11. Author gate

No unresolved choice in the exact spec requires a new author theory adjudication.

The user's current instruction is explicitly to continue until author intervention or Codex intervention is actually required. That is sufficient authorization to execute the bounded E4-A/E4-B truth-up described in the exact spec.

Therefore:

```text
AUTHOR RE-ADJUDICATION = NOT REQUIRED
AUTHOR EXECUTION AUTHORIZATION = PRESENT
```

---

## 12. Codex gate

Codex / a full repository worktree is now genuinely required.

Reason:

1. `SRT_Collective_Selection.md` is a long semantic owner requiring a large but precise multi-section diff;
2. `SRT_Collective_Tower_Hardening_Notes.md` is approximately 68 KiB and requires distributed edits across recursive projection, residual, spectral and Lyapunov sections;
3. the Tower owner has a registered deterministic reading split that must be regenerated with the repository script;
4. execution must inspect exact changed-file sets, run `git diff --check`, generator/freshness checks and strict governance before pushing;
5. connector-only whole-file replacement would add transcription risk and cannot substitute honestly for running the split generator.

This is an execution-environment boundary, not a theory gate.

---

## 13. Final disposition

```text
E4 EXACT SPEC REVIEW = FINAL PASS
THEORY BLOCKER = NONE
NEW AUTHOR DECISION = NONE

NEXT ACTION:
  execute E4-A and E4-B in Codex / full worktree
  preserving separate semantic commits and derivative commit

E5+ = HOLD
MERGE #976 = NO
```
