---
id: SRT-DIFF-PIPELINE-GUIDE
type: framework
tags: [Pipeline, Diff, Collaboration]
status: axiomatic_hybrid_v1
dependency: [_SRT_EXPLANATION_PROTOCOL, _SRT_DOMAIN_TEMPLATE, SRT-REF-SCALING]
---

# SRT Diff Pipeline Guide

> 目标：将“外部材料 → SRT 文件级补丁提案”流程标准化，确保可追溯、可审计、可持续追加。
>
> **状态更新（2026-02-28）：** 计划 1 与计划 3 已切换为“审核通过后直接修改正文”。本文件保留用于需要补丁提案模式的场景（如审稿前评审、风险材料缓冲）。

---

## 1) 管线输入/输出定义

### 输入
- 论文链接、访谈链接、用户粘贴长文本、结构化摘要。

### 输出
- 仅写入 `diff.md`（append-only）
- 每次输出必须包含：
  1. `Target Files`
  2. `Proposed Patch (unified diff)`
  3. 分类映射（d-value 区间、能流态、`\Psi_f`）
  4. 新术语及 `[Lineage/Source]`
  5. `## 【理论边界/防误用声明】`

---

## 2) 标准执行流程（SOP）

1. **材料读取**：优先 `web_fetch`；失败则用 DOI/Crossref/可访问镜像兜底。
2. **语义抽取**：提取命题、变量、尺度、证据等级。
3. **SRT 映射**：映射到目标文件（可多文件）。
4. **符号规范化**：外部 state-space 符号 `Ω/S/...` 统一映射为 `L_0`。
5. **scaling-gap 检查**：若跨尺度缺位，向 `Core_Law/SRT_Reference_Scaling.md` 生成补丁建议。
6. **写入 `diff.md`**：按时间戳新段追加，禁止覆盖历史。
7. **提交 git**：每轮必须提交。

---

## 3) `diff.md` 段落模板（强制）

```markdown
## [YYYY-MM-DD HH:mm TZ] <Source Title>
Source: <URL/DOI/镜像说明>
Evidence-Level: <peer-reviewed|preprint|editorial|secondary>

### Target Files
- SRT/...
- SRT/...

### Proposed Patch (unified diff)
```diff
--- a/SRT/...
+++ b/SRT/...
@@ ...
+...
```

### SRT 分类映射
- d-value 区间：...
- 能流态（Energy-Flow Regime）：...
- `\Psi_f` 状态：...

### 新术语与谱系
- `<Term>`: ... `[Lineage/Source] ...`

## 4) 质量门槛（Quality Gates）

提交前必须满足：
1. diff 为 unified 格式。
2. 至少 1 个目标文件路径。
3. 分类映射三项齐全。
4. 若引入新术语，必须有 lineage。
5. 边界声明为正式 header。
6. 通过 `./scripts/run_srt_checks.sh`（若本轮涉及 SRT 文件规范调整）。

---

## 5) 常见失败与兜底

- `web_fetch 403/406`：记录抓取失败，降级为 DOI 元数据 + 可访问来源。
- 站点登录墙/反爬：标注 `Source-Level: secondary` 并说明限制。
- 编辑精确匹配失败：改用 append 写入策略，避免中断流水。

---

## 6) 审计与可追溯性

每次提交建议包含：
- 来源标题关键词
- 主题域标签（AI/Neuro/Phys/...）
- “append diff pipeline”语义

推荐 commit message 模式：
- `docs(diff): append <topic> patch proposal with SRT mapping`

---

##
