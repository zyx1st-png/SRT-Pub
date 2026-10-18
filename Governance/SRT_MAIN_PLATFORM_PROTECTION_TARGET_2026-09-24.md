---
id: SRT-MAIN-PLATFORM-PROTECTION-TARGET-20260924
type: governance_target
status: active
date: 2026-09-24
updated: 2026-09-24
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency:
  - SRT-MAIN-WRITE-GOVERNANCE
tags: [GitHub, Main, Ruleset, Protection, GovernancePreflight]
---

# GitHub main platform protection target — 2026-09-24

## 0. Current verified platform state

Verified through the available GitHub connection on 2026-09-24 after merge commit `d02c8520a5a5a7a0416701f311aad18b597ead95`:

```text
default branch = main
main protected = false
branch required status checks = off
repository rulesets = []
```

Therefore:

> **platform protection is NOT ACTIVE.**

This file must not be used to claim otherwise.

The active GitHub connector can read approved repository/ruleset surfaces but exposes no administration write action for creating or editing branch rulesets. Repository documentation can define the target; platform settings must still be applied through an administration-capable GitHub surface.

## 1. Target policy for `main`

Preferred repository ruleset:

```text
target:
  branch = main

require pull request before merging:
  ON

required status check:
  governance-preflight

require latest / merge-base-current head before merge:
  ON where supported

block force push:
  ON

block deletion:
  ON

direct push:
  NOT a normal owner/admin path
```

The workflow name is `Governance Preflight`; the required job/check context is `governance-preflight`.

Do not make path-filtered preprint build workflows global required checks.

## 2. Administrator recovery

If the platform supports repository-administrator bypass, prefer the narrowest mode that preserves PR history, e.g. **for pull requests only** rather than ordinary direct-push bypass.

Recovery intent:

```text
admin may recover broken governance through a PR
admin does not use bypass as routine direct-main write authority
```

If a ruleset self-locks governance infrastructure, record the incident and immediately verify protection after recovery.

## 3. Acceptance test after platform configuration

Do not mark platform closure complete until all of the following are verified against GitHub:

1. `main` reports protected / ruleset-covered;
2. a normal owner direct push to `main` is rejected by policy;
3. a PR without `governance-preflight` success cannot merge;
4. a PR with the required current-head check can merge under the intended authorization path;
5. force push and branch deletion are blocked;
6. any admin bypass is limited to the declared recovery model.

## 4. Repository policy vs platform fact

```text
Governance/SRT_MAIN_WRITE_GOVERNANCE.md
= repository policy

this file
= desired platform contract + verification record

GitHub settings / API state
= enforcement fact
```

Do not collapse these layers.
