---
id: SRT-GOV-ANTI-BLOCKING-GATE
type: governance_protocol
status: active
layer: governance
epistemic_layer: os
claim_mode: governance
canonical: false
---

# Governance Anti-Blocking Gate

## Purpose

Prevent a single governance defect from entering `main` and causing unrelated future pull requests to become blocked. The gate preserves strict governance while separating the current PR's responsibility from the health of its base and proposed merged state.

## Executable validation model

Pull-request CI evaluates four distinct scopes:

1. **Base-main health** — a detached worktree at the PR base runs the complete split-metadata check and Governance Preflight.
2. **PR-local frontmatter** — `scripts/check_frontmatter_changed.py` checks only Markdown files added or modified relative to the base.
3. **Baseline monotonicity** — `scripts/check_frontmatter_baseline_monotonic.py` rejects new warning-debt entries unless the PR carries the explicit `governance-baseline-expansion-approved` label.
4. **Proposed merged repository health** — the ordinary full Governance Preflight runs on the PR merge state.

A local pass does not imply repository health. A base failure does not automatically make a locally clean repair PR responsible for that failure.

## Failure attribution

The workflow classifies outcomes as:

```yaml
failure_scope: pr_local | baseline_expansion | base_main | merged_repository_or_infrastructure | none
base_main_health: success | failure | not-run
pr_local_frontmatter: success | failure | not-run
baseline_monotonicity: success | failure | not-run
merged_repository_preflight: success | failure | not-run
merge_disposition: normal_merge | governance_hotfix_only | do_not_merge
```

Human-readable attribution is written to the GitHub Actions step summary. Machine-readable attribution is uploaded as:

```text
governance-attribution.json
```

Detailed logs remain available in the governance diagnostics artifact.

## Frontmatter field responsibilities

`status` expresses lifecycle only:

```text
draft
active
frozen
archived
```

Other meanings use dedicated fields:

```text
file kind          -> type
version            -> version
source stage       -> source_stage
record stage       -> record_stage
pointer version    -> pointer_version
integration state  -> integration_status
```

Values such as `active_v1`, `draft_v2`, `patch_v0_1`, `source_card`, `preprint_v2`, or `author_confirmed_*` must not be stored in `status`.

## Baseline protection

The warning baseline is a debt registry, not a bypass mechanism.

Rules:

- Ordinary PRs must not add warning-baseline entries.
- Removing obsolete entries is encouraged.
- An intentional expansion requires a dedicated governance decision and the `governance-baseline-expansion-approved` label.
- The approval label permits the baseline change to be reviewed; it does not make a malformed document valid or bypass the full preflight.
- Rewriting the baseline to hide new violations is prohibited.

## Incident mode

When base `main` fails the complete Governance Preflight:

```text
REPO_BLOCKING_GOVERNANCE_INCIDENT
```

A PR may follow the hotfix path only when:

- its PR-local frontmatter check is clean;
- it does not expand baseline debt without approval;
- the proposed merged repository passes the complete preflight.

The corresponding verdict is:

```text
BASE_MAIN WAS BLOCKED; THIS PR REPAIRS IT / GOVERNANCE HOTFIX PATH
```

If base and proposed merged state both remain blocked, ordinary content merging must stop until a governance repair passes.

## Merge protection

Repository settings should require:

- `Governance Preflight / governance-preflight` as a required status check;
- pull requests for changes to `main`;
- up-to-date branch validation or a merge queue;
- no ordinary administrator bypass of required checks.

These repository settings are external GitHub configuration. Repository scripts can diagnose missing protection but cannot enforce hosting-level rules by themselves.

## Audit verdict format

Audits report one of:

```text
PR_LOCAL / LOCAL DIRTY / DO NOT MERGE
PR_LOCAL BASELINE DEBT EXPANSION / DO NOT MERGE
BASE_MAIN WAS BLOCKED; THIS PR REPAIRS IT / GOVERNANCE HOTFIX PATH
BASE_MAIN BLOCKED / HOTFIX ONLY
LOCAL FRONTMATTER CLEAN; FULL REPOSITORY OR INFRA FAILURE / DO NOT MERGE
LOCAL CLEAN / MAIN HEALTHY / NORMAL MERGE
```
