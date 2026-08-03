# Governance Anti-Blocking Gate

## Purpose

Prevent a single governance defect from entering `main` and causing unrelated future pull requests to become blocked. This mechanism preserves strict governance while improving failure attribution and recovery.

## Validation Model

Every pull request should be evaluated at two levels:

1. PR-local validation: detect files and rules introduced or modified by the current change.
2. Repository health validation: verify the complete repository state after integration remains compliant.

A local pass does not imply repository health, and repository health failures must identify their origin.

## Failure Attribution

Governance failures should classify:

```yaml
failure_scope: pr_local | base_main | legacy_baseline | infrastructure
introducing_commit:
introducing_pr:
affected_files:
new_warning_count:
retired_warning_count:
recommended_fix:
merge_state: block | governance_hotfix_only | advisory
```

## Baseline Protection

The warning baseline is a debt registry, not a bypass mechanism.

Rules:

- Normal content PRs must not increase governance baseline entries.
- Governance cleanup PRs should reduce baseline debt whenever possible.
- Adding baseline entries requires explicit justification.
- Rewriting baseline files to hide new violations is prohibited.

## Incident Mode

When `main` governance checks fail:

`REPO_BLOCKING_GOVERNANCE_INCIDENT`

Only governance repair changes should merge until:

- the introducing defect is identified;
- affected files are repaired;
- new warnings return to zero;
- full governance preflight passes.

## Merge Protection

Repository settings should require:

- governance preflight status checks;
- pull request review where appropriate;
- up-to-date branch validation or merge queue;
- no bypass through ordinary administrator merges.

## Audit Verdict Format

Audits should report:

```
LOCAL CLEAN / LOCAL DIRTY
MAIN HEALTHY / MAIN BLOCKED
NORMAL MERGE / HOTFIX ONLY / DO NOT MERGE
```
