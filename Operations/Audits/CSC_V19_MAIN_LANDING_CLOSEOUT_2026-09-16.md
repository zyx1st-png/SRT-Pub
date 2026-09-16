---
id: CSC-V19-MAIN-LANDING-CLOSEOUT-2026-09-16
type: publication_landing_closeout
status: active
canonical: false
claim_mode: evidence
updated: 2026-09-16
---

# CSC v19 — Main Landing Closeout

## 0. Scope

This record closes the repository-integration step for the *Artificial Life* v19 publication programme after author authorization to preserve the full research provenance in `main`.

It is an operations/provenance record only. It does not modify canonical SRT, alter any preregistered hypothesis/result, reinterpret historical experiment records, or perform journal submission.

## 1. Final landing chain

The authorized landing order was executed with ordinary GitHub merge commits, without squash:

```text
main @ a149e4ed930c652dbb03311804c1398828d54681
  -> #978 v17 publication baseline
     merge commit eba60731f6f7ef70a7d538a9029968e14dba1555
  -> #979 preregistered Experiment 2 / preserved no-support result
     merge commit 555b65ea9facba93ed53da7ac581f516de9eee0a
  -> #980 preregistered Experiment 3 / preserved opposite-direction result
     merge commit 0b4c0190be6c054929d6c904b72717af8a717af4
  -> #982 consequence-scope mechanism audit + merged #983 E4 provenance
     merge commit d6d24891999cab49549c017ffe599f631f29f830
  -> #984 v19 publication reconstruction
     merge commit df4b233c4ab029bfe97b48aa94a510607456557c
```

Final publication landing head:

```text
df4b233c4ab029bfe97b48aa94a510607456557c
```

The stacked PRs were retargeted to `main` only after their immediate parent had landed, preserving the original preregistration / experiment / audit commit history instead of flattening the programme into one squash commit.

## 2. #981 / v18 disposition

PR #981 was a separate v18 publication branch from the #980 E1/E2/E3 checkpoint. It was superseded by the E4-informed v19 route and is **not** part of the final landing chain.

Final disposition:

```text
#981 = CLOSED / SUPERSEDED / NOT MERGED
head = 2a54da71c4dd118e4c8a815732978acef3ceabd5
role = historical publication-development branch / provenance only
```

Do not merge #981 merely to satisfy v19 provenance references.

The v19 files contain references such as:

```text
papers/CostlySelectiveClosure_v18_ArtificialLife_candidate.md
```

That file is not present in the final `main` tree because #981 was intentionally not merged. In the landed v19 materials, such v18 references must therefore be read as **historical development provenance pointing to the closed #981 branch/head**, not as a live `main`-tree dependency.

This clarification is intentionally recorded here rather than rewriting the already-QA'd v19 manuscript/readiness artifacts after landing. Any later publication rebuild that changes those references must regenerate the reviewer-facing artifacts and their hashes.

## 3. Historical gate text

Earlier files may still contain contemporaneous lifecycle statements such as:

```text
#978 MERGE = HOLD
#982 MERGE = AWAIT AUTHOR DECISION
MERGE #984 = READY / AWAIT AUTHOR AUTHORIZATION
```

These are preserved historical records of the state when those preregistrations, results, audits, or readiness gates were written. They are **not current merge instructions** and should not be mechanically rewritten after the fact.

Current landing truth is the chain in §1.

## 4. Current publication owner

For publication development after this landing:

```text
current publication candidate = papers/CostlySelectiveClosure_v19_ArtificialLife_candidate.md
paper title = Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents
target venue = Artificial Life
v19 role = current internal submission candidate
v18 / #981 role = superseded historical branch
```

The v19 evidence boundary remains unchanged:

```text
E1 = discovery / not preregistered / strong terminal-vs-restore result
E2 = preregistered / positive generalization not supported
E3 = preregistered / positive H1 not supported / opposite ordinal direction observed
E4 = preregistered / positive but modest consequence-scope support
E5 = not required before the current submission candidate
```

## 5. Non-actions and stop boundary

```text
canonical SRT edits = NONE
historical preregistration/result rewrites = NONE
#981 merge = NO
second E4 run = NO
parameter retuning = NO
E5 = NOT REQUIRED FOR CURRENT CANDIDATE
journal submission = NOT PERFORMED
```

Repository landing is complete. Any actual journal upload/submission is a separate external action and requires separate author authorization.
