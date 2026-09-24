---
id: SRT-GOVERNANCE-ANTI-BLOCKING-GATE
type: governance_protocol
status: active
version: v2
updated: 2026-09-24
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

脚本不能替代 GitHub Ruleset。平台实际设置是最终事实源；本节只定义目标策略与恢复纪律。

### Recommended ruleset for `main`

优先使用 repository branch ruleset，而不是依赖允许管理员普通直推的经典 branch-protection 配置：

- target：default branch / `main`；
- Require a pull request before merging；
- Require status checks to pass before merging；
- required check context：`governance-preflight`（workflow 名为 `Governance Preflight`）；
- repository administrator 可加入 bypass list，但应设为 **For pull requests only**，使管理员可在 PR 内应急绕过、不能直接 push `main`；
- 暂不要求 approving review、linear history 或 branch up-to-date；
- `Build ontological friction preprint PDF` 使用 path filters，不得作为全局 required check。

启用后应做两个实测：

```text
owner direct push to main
-> REJECTED

ordinary PR with governance-preflight success
-> MERGE ALLOWED
```

当前仓库为 public；GitHub Free 可使用 public-repository rulesets / protected branches。若未来改为 private，个人账户需要支持 private-repository protections 的付费计划后再依赖这套平台门禁。

### Workflow write discipline

任何 GitHub Actions workflow 都不得直接 commit / push `main`。

CI 写回 PR branch 也不是常规机制。若一次性 repair job 确有必要：

- 必须放在独立临时 workflow，不得替换或塞进 `.github/workflows/governance-preflight.yml`；
- bot 写入后，latest head 必须重新取得 `governance-preflight`；可由用户再推一个提交，或关闭并重新打开 PR 触发；
- 不得因为 bot 最新提交缺 check 而用 bypass 当作常规收尾。

GitHub 使用 repository `GITHUB_TOKEN` 产生的普通 push 默认不会再次触发 workflow，因此 required checks 必须以 **PR 最新 commit SHA** 为准。

### Governance control-plane changes

修改下列门禁本身的 PR 属于 governance-control-plane / hotfix 类，不得把“PR 自己修改后的 preflight 绿灯”当成唯一充分证据：

```text
.github/workflows/governance-preflight.yml
scripts/governance_preflight.py
scripts/check_frontmatter_changed.py
scripts/check_frontmatter_baseline_monotonic.py
以及其直接调用的 hard-gate checker
```

这类 PR 必须：

- 保持 bounded diff；
- 明确写出改变了哪条 gate、为何不会降低约束；
- 对照 `main` 版本人工复核；
- 合并后确认 `main` push 上的 Governance Preflight 通过。

任何临时写入 job 都不得通过修改 required workflow 本身来获得执行权限。

### Loose merge residual risk

当前不默认启用 “Require branches to be up to date before merging”。因此一个 PR 的成功检查只对应其运行时的 base/main 状态；在它等待期间若 `main` 已前移，两个分别通过的 PR 仍可能组合后使 `main` 变红。

补救纪律：

- 合并前若 `main` 已明显前移，优先 Update branch / 重新触发检查；
- 所有 push 到 `main` 继续运行 Governance Preflight；
- 若 merged `main` 变红，立即进入上文 Main-health incident：暂停普通合并，只允许 governance hotfix。

未来若迁移到支持 Merge Queue 的组织仓库，可再启用 latest-main validation / merge queue。

### Recovery

若 Ruleset 自身配置错误导致治理基础设施自锁，repository administrator 可临时编辑或停用该 Ruleset 完成恢复；恢复动作必须按 Main-health incident 留痕，并使用：

```yaml
failure_scope: infra
merge_disposition: hotfix_only
```

恢复后立即重新启用保护并验证 owner direct push 仍被拒绝。对于已损坏的 `main`，修复 PR 必须一次使 required governance gate 恢复为可通过状态；不要依赖多个连续红色 PR 分步修复。
