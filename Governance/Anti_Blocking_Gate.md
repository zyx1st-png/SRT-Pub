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

Prevent a single governance defect from entering `main` and causing unrelated future pull requests to become blocked. This mechanism preserves strict governance while improving failure attribution and recovery.

## Validation model

Every pull request is evaluated at two levels:

1. **PR-local validation** checks Markdown files introduced or modified relative to the PR base SHA.
2. **Repository-health validation** checks the complete proposed merged repository state.

A local pass does not imply repository health. A repository-health failure must not be attributed to the current PR when its changed files are locally clean.

The executable entry point is:

```bash
uv run python scripts/governance_preflight.py \
  --skip-write-report \
  --strict-split-metadata \
  --base-ref <PR_BASE_SHA>
```

## Failure attribution

Governance diagnostics use the following schema:

```yaml
failure_scope: pr_local | base_main | repository_check | infrastructure | none
base_ref:
local_verdict: clean | dirty | not_run
main_health: healthy | blocked | unknown
failed_steps:
merge_disposition: normal_merge | governance_hotfix_only | do_not_merge
```

Machine-readable reports are emitted as:

```text
governance-preflight-summary.json
frontmatter-pr-local.json
frontmatter-repository.json
```

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

Values such as `active_v1`, `draft_v2`, `patch_v0_1`, `source_card`, or `author_confirmed_*` must not be stored in `status`.

## Baseline protection

The warning baseline is a debt registry, not a bypass mechanism.

Rules:

- Normal content PRs must not increase governance baseline entries.
- Governance cleanup PRs should reduce baseline debt whenever possible.
- PR-local CI compares the current baseline with the base SHA and fails on every added entry.
- Rewriting the baseline to hide new violations is prohibited.
- A genuine baseline expansion requires a separately reviewed governance-mechanism change; it cannot be performed by an ordinary content PR.

## Incident mode

When the current `main` governance state is identified as blocked:

```text
REPO_BLOCKING_GOVERNANCE_INCIDENT
```

Only governance repair changes should merge until:

- the introducing defect is identified;
- affected files are repaired;
- new warnings return to zero;
- full governance preflight passes.

A locally clean PR with a repository-wide frontmatter failure receives:

```text
failure_scope: base_main
merge_disposition: governance_hotfix_only
```

## Merge protection

Repository settings should require:

- `Governance Preflight / governance-preflight` as a required status check;
- pull requests for `main` changes;
- up-to-date branch validation or a merge queue;
- no ordinary administrator bypass of required checks.

These repository settings remain an external GitHub configuration responsibility; the scripts report but cannot enforce them.

## Audit verdict format

Audits report:

```text
LOCAL CLEAN / LOCAL DIRTY / LOCAL NOT RUN
MAIN HEALTHY / MAIN BLOCKED / MAIN UNKNOWN
NORMAL MERGE / GOVERNANCE HOTFIX ONLY / DO NOT MERGE
```

The verdict distinguishes the current PR's responsibility from the health of the complete proposed repository state.
