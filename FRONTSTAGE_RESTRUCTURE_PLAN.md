# SRT Frontstage Restructure Plan

Date: 2026-05-04
Status: proposed_v1

## Purpose

This plan reframes the public-facing structure of `SRT-Pub` so the repository no longer presents itself primarily as a governance system. The goal is to restore the theory's frontstage force while preserving the existing formal, operational, and governance infrastructure.

The new frontstage structure is:

```text
01_Source_Intuition/
02_Formal_Anchors/
03_Bridges/
04_External_Convergence/
05_Public_Release/
90_Operations/        future optional migration target
99_Governance/        future optional migration target
```

## Core principle

> Source intuition gives SRT force.
> Formal anchors give SRT hardness.
> Bridges make SRT comparable.
> External convergence gives SRT support and pressure.
> Public release gives SRT reach.
> Operations and governance keep SRT maintainable without becoming its first face.

## Why not move everything immediately?

This first pass is intentionally non-destructive.

It creates new frontstage entry layers and updates the root README, but does not move existing Core, AI, Physics, Neuroscience, Philosophy, Spirituality, Governance, or Operations files.

Reasons:

1. Avoid breaking existing internal links.
2. Preserve machine indexes and agent protocols.
3. Let the new structure be reviewed before bulk migration.
4. Keep old domain folders available while the frontstage map stabilizes.

## Layer roles

### 01 Source Intuition

Restores SRT's founding intuition: selection before existence, reality as anchored selection, subject as stabilized selection-pattern, value as consequence-bearing non-substitutability, and consciousness as thresholded rather than universal.

### 02 Formal Anchors

Houses the canonical skeleton: minimal axioms, constitutive theorems, formal axioms, equations, symbol tables, canonical `d-value`, `Psi_f`, `T_dir`, and open tensions.

### 03 Bridges

Translates SRT into neighboring theories and fields. Bridge files make SRT comparable; they do not claim proof.

### 04 External Convergence

Grades independent findings from other fields as possible support, proxy, formal constraint, differential prediction, or pressure on SRT constructs. This is not a proof folder.

### 05 Public Release

Prepares public one-pagers, talks, essays, scripts, FAQ, and visual maps. Public release is controlled outward expression, not a weaker theory.

## Migration phases

### Phase 1: Frontstage entry layer

- Create the five frontstage directories.
- Add one README to each directory.
- Update root README to make these the main reading frame.
- Do not move old files.

### Phase 2: Alias and index pass

- Add lightweight index files inside each layer.
- Map old files into new roles.
- Create a `START_HERE.md` or revise `SRT_Navigation_Map.md` to follow the new sequence.

### Phase 3: Selective migration

Only move files when all links, indexes, and references can be updated safely.

Candidate moves:

- selected public one-pagers -> `05_Public_Release/`
- selected evidence/proxy materials -> `04_External_Convergence/`
- selected source essays -> `01_Source_Intuition/`

### Phase 4: Operations / Governance downstage migration

Consider later:

```text
Operations/  -> 90_Operations/
Governance/  -> 99_Governance/
```

Only do this after all internal references are audited.

## Naming rule

Avoid naming the new evidence layer `Proofs` or `Evidence_Proving_SRT`.

Preferred:

- `04_External_Convergence`
- `External Convergence / 外部收敛证据`
- `Corroboration` if a shorter English name is needed.

## Evidence rule

External fields cannot directly prove SRT. They can:

- converge structurally;
- provide proxy measurements;
- strengthen formal anchors;
- create differential predictions;
- produce falsification pressure;
- expose weak points.

Default slogan:

> Bridge translates. Convergence strengthens. Lab tests. Governance restrains.

## Success criterion

A first-time reader should encounter SRT in this order:

1. the founding reversal;
2. the formal skeleton;
3. the cross-domain translations;
4. the external support and pressure;
5. the public-facing release materials;
6. governance and operations only when needed.
