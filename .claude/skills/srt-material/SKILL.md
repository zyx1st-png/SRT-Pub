---
name: srt-material
description: SRT 材料融合工作流（Pipeline 1）的触发器——外部材料进入仓库的权威主流程。三类时机使用：①用户发 `材料 <URL/DOI/PDF/文本/摘要/截图>` 或贴来一篇文章/论文/预印本问"这个能不能进 / 帮我审一下 / 融进去"；②发 `材料裁决 <…>` 或 `二轮裁决 <…>`（第二轮结构裁决，压成最小可承重命题）；③要把某条已归档的 B/C 材料重新评级或升格。流程=6 项审核门 → A/B/C 裁决 → SourceCard/PatchNote/Material Log/Index/Registry/IntegrationHook；A 类正文回写必须先做"去材料化改写"。绝不把媒体解释当作者结论，绝不把 B/C 材料写成 SRT 已证结论。仅想让 LLM 就某材料写一篇成品文章的，不走本 skill（走 srt-article / srt-weixin 等）。
argument-hint: "[URL/DOI/PDF/文本/摘要 | 材料裁决 <…> | 升格 <SourceCard>]"
---

# SRT 材料融合工作流（Pipeline 1 触发器）

本 skill 是 `Operations/_SRT_MATERIAL_PIPELINE.md`（Pipeline 1 / v2 结构化写入版）的**运行触发层**。
被拉起时按下面骨架驱动；**精确的审核门定义、A/B/C 门槛、产物模板以那份主文档为准**——
开工前先读它，二轮裁决另读 `Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`。
本文件只装"怎么起、按什么次序、哪些红线不能碰"，不复制全文以防漂移。

## 一句话原则（不可违反）

```
材料先归档，证据先裁决，补丁再解释，正文最后合并。
```

Pipeline 1 不负责把新材料立刻升格为 SRT 结论。它判断：材料**是否**进仓库、以**什么等级**进、
落在**哪**、如何被人/机检索、未来**是否**合并进正文。

## 开工前必读

1. `Operations/_SRT_MATERIAL_PIPELINE.md`（主流程 + 6 门 + A/B/C 门槛 + 产物模板）
2. `Operations/_SRT_MATERIAL_LOG.md`（正式状态台账；长记录从 `Operations/Material_Log/README.md` 进）
3. `STATUS.md` 的今日执行状态
4. 二轮裁决时：`Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`
5. 涉及回写正文时：目标领域文件 + 对应 canonical，先核对再落笔

## 入口判定（先做这个）

- **`材料 <…>` 或贴来原始材料** → 走标准 Pipeline 1（6 门 → A/B/C → 产物）。
- **`材料裁决 <…>` / `二轮裁决 <…>`** → 走辅助裁决工作流：审第一轮候选接口，压成**最小可承重命题**，
  给 A/B/C 建议 + 主/备/禁止落点 + 去材料化主句；结果**必须回注 Pipeline 1**，不替代它。
- **要求就材料直接写成品文章** → 不走本 skill（第一设计律不同）；指向 srt-article / srt-weixin / srt-zhihu。

## 被触发时怎么走

1. **读取材料**（按 `_SRT_MATERIAL_PIPELINE.md §2` 的输入类型要求）：
   URL 优先追一手论文/DOI；PDF 读正文图表结论不止摘要；用户摘要标二手；截图只作线索。
   **媒体报道的解释不得直接当作者结论。** 读不到全文就保留证据缺口，不脑补。
2. **过 6 项审核门**（相关性 / 增量性 / 证据等级 / 可对齐性 / 风险 / 落点清晰），逐门给结论。
3. **裁决 A/B/C**：
   - **A**（可直接融入，需同时满足主文档列的全部 A 门槛）→ 建 SourceCard + PatchNote + Material Log +
     索引 + Registry + IntegrationHook；**A 类正文回写前必须先做"去材料化改写"**——写成能脱离材料
     独立阅读的原生章节，不是"某文章说…"的材料补丁口吻。
   - **B**（延后观察）→ SourceCard + Material Log(+Watchlist)；一般不建 PatchNote / 正文 hook。
     按当前 B 子型标注（B1 = A-convertible 高优候选 / B2 = guardrail-only / B3 = public-prose-only）。
   - **C**（不融入）→ 只写 Material Log 的 C 记录，说明拒绝理由；不建正文补丁。
4. **回写与留痕**：正式状态以 `Operations/_SRT_MATERIAL_LOG.md` 为准；更新 `STATUS.md` 今日状态。

## 硬红线

- **媒体解释 ≠ 作者结论**；二手/截图证据等级低，须补可引用一手来源。
- **证据等级必须标注**（primary / peer-reviewed / preprint / review / secondary / commentary），不得混淆。
- **claim ladder 不放松**：材料带来的接口默认是桥接/证据层，**不得把 P3 假设写成已证定律**；
  拿不准 claim level 就标 `NEEDS_RETRIEVAL`，绝不编造。
- **不越级升格**：B/C 不因"看起来很对"直接当 SRT 结论；升格必须重新过门并留痕。
- **回写前核对 canonical**：任何落进正文/领域文件的命题，先对照 `CANONICAL_REGISTRY.md` 与符号表；
  不制造 Ψ_f/d/T_dir 的偷换或伪背书。
- **不另起平行流程**：SourceCard/PatchNote/Registry/Hook 都是 Pipeline 1 产物，状态冲突以台账为准。
