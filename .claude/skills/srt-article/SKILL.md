---
name: srt-article
description: SRT 作者主导的文章命题锻造、逐层发散、草稿诊断与 Choice Trace。用于梳理想法和选择框架；直接代写成稿或普通语言润色不自动进入此流程。
argument-hint: "[碎片想法或主张 | 继续 | 诊断 | 轨迹]"
---

# SRT Author-led Article Workflow

按根 AGENTS.md 与当前用户请求确定范围。`Operations/_SRT_ARTICLE_WORKFLOW.md` 是此作者主导模式的详细流程；只读当前阶段对应节，轨迹字段查 `Operations/_SRT_CHOICE_TRACE_LOG.md`。

## 入口

- 碎片/未定主张：保留 `seed_fragment` 原话，进入命题锻造。
- 草稿诊断：直接进入 §8，只报问题与位置。
- 继续：先查本次对话和已有轨迹，从未完成层继续；只问仍缺的实质选择。
- 记/补轨迹：进入 §7；事后补记标 `late_entry: true`。
- 明确要校准稿：直接执行 §5 已允许的例外，标“校准稿，非成品”，不再重复请求授权。
- 明确要直接成稿或改写：按该请求和当前可用写作能力执行，不用本模式的作者亲写约定阻断另一任务；仍守 SRT 理论、署名与发布边界。

## 作者主导模式

先锻命题，再按“思路结构 → 理论内容 → 写作手法”逐层展开。每层默认给 3–4 个边界清楚的选项，等作者选择后再生成下一层；不代选、不把多层混成资料堆。已定层不重跑。

理论内容核对 Registry §C、当前 owner 与 claim ladder；邻近理论重合按 AGENTS.md 的 U/N-mode 处理，不把旧 prompt 的“无独有增量”当作所有命题的入场禁令。

骨架交作者收敛成文，AI 可给非成文脚手架；诊断请求只交问题。作者原话与选择轨迹逐字留存，`chosen / skipped_mode / reason / closure_boundary / attack_target` 不由 AI 推断代填。缺字段留空，不为补齐格式暂停其他已授权工作。

`Operations/_SRT_ARTICLE_WORKFLOW.md` 的历史经验与 paste-ready prompts 只适用于这一模式，不决定全仓当前研究方向，也不提供外部发布许可。
