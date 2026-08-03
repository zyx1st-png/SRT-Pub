---
id: SRT-GOVERNANCE-ANTI-BLOCKING-GATE
type: governance_protocol
status: active
version: v1
layer: governance
epistemic_layer: os
claim_mode: policy
canonical: false
date: 2026-08-03
---

# Governance Anti-Blocking Gate

## Purpose

防止单个治理违规进入 `main` 后，使后续无关 PR 因同一项既有错误批量失败。防阻塞不得通过降低检查标准或扩大 warning baseline 实现。

## Validation scopes

每个 PR 同时检查：

1. `base_main`：基线分支自身是否健康，仅用于归因；
2. `pr_local`：当前 PR 新增或修改的 Markdown 是否引入新违规；
3. `merged_repository`：拟合并后的完整仓库是否通过 Governance Preflight。

最终摘要必须给出明确结论：

```text
LOCAL CLEAN / MAIN HEALTHY / NORMAL MERGE
PR_LOCAL / LOCAL DIRTY / DO NOT MERGE
BASE_MAIN BLOCKED / HOTFIX ONLY
BASE_MAIN WAS BLOCKED; THIS PR REPAIRS IT / HOTFIX PATH
```

## Frontmatter responsibilities

`status` 只表达生命周期：

```text
draft | active | frozen | archived
```

版本、类型和阶段信息分别使用：

```text
type
version
source_stage
record_stage
pointer_version
integration_status
```

不得使用 `active_v1`、`draft_v2`、`patch_v0_1`、`source_card`、`preprint_v2` 或 `author_confirmed_*` 作为 `status`。

## Standard minimums

SourceCard：

```yaml
id: SRC-...
type: material_source_card
status: active
source_stage: preprint_v2
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
```

Patch：

```yaml
id: PATCH-...
type: material_patch
status: active
version: v0_1
layer: operations
epistemic_layer: bridge
claim_mode: bridge
canonical: false
```

Integration Hook：

```yaml
id: HOOK-...
type: integration_hook
status: active
integration_status: pending
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
```

## Baseline debt ceiling

`Governance/Frontmatter_Warning_Baseline.txt` 是已知债务上限：

- 普通 PR 不得增加条目；
- 清理 PR 可以减少条目；
- 经作者明确批准的独立治理 PR，可使用 `governance-baseline-expansion-approved` 标签记录例外；
- 禁止通过重新生成 baseline 把新违规转换为已知债务。

## Main-health incident

当 `main` 的完整 preflight 失败时，暂停普通内容合并，只允许专用 governance hotfix。修复记录应包含：

```yaml
failure_scope: pr_local | base_main | legacy_baseline | infra
first_bad_commit:
introducing_pr:
affected_files:
blast_radius:
suggested_fix:
merge_disposition: block | hotfix_only | advisory
```

完整 preflight 恢复为绿色后，方可解除阻塞状态。

## Repository settings

脚本不能替代 GitHub Ruleset。仓库设置应把 `Governance Preflight / governance-preflight` 设为 required check，并要求合并前同步最新 `main` 或使用 Merge Queue。
