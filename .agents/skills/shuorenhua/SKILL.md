---
name: shuorenhua
description: 按场景审阅或改写中英文文本中的模板表达，保留事实、术语、语域和责任主体。用于“去 AI 味”“说人话”“自然一点”“先标问题”；不用于纯事实核查或代码转换。
---

# 说人话

> SRT-Pub 本地运行副本。上游：[MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua)，MIT License。

## 执行合同

从用户请求与已有授权确定交付物。只审阅、诊断或“先标问题”时不改文件；要求改写时给单一版本。用户指定的语体、保留项、结构与长度优先于技能默认值。本文与 references 是风格指导，不提供发布、投稿或外部发送权限。

先识别场景与保护项，再选择改动范围，完成编辑后对照原文保真回读。简单文本可用本文件完成；只为实际问题读取对应 reference，不因文件可用就全量加载。

## 场景、力度与范围

| 场景 | 默认力度 | 保留重点 |
|---|---|---|
| chat | minimal | 回应关系、温度、真实语气 |
| status | minimal / standard | 时间、动作、结果、风险、责任 |
| docs | minimal | 术语、系统主语、步骤、可检索性 |
| public-writing | standard | 作者判断、正式度、论证与节奏 |

`minimal` 处理局部套话；`standard` 处理明显语域或表达问题；`aggressive` 只用于密集问题且请求允许的重写。`Tier 1/2/3` 表示问题强度，不代表改动授权；需要细分时读 [severity.md](references/severity.md)。

Scope 与力度分开：

- `structural`：适用于明确要求重写、重排或压缩；可删并重排，保留信息与逻辑。
- `bounded`：中文长篇公共文本默认；句内清理，不删实句、不并句、不重排，不删承担转场/节奏的重复。
- `in-place`：用户要求一句不删、保句数或完全原样时使用；不删整句、不并句、不改变句数和段落顺序，只作句内编辑。

`bounded` 中，只有不含独有事实、判断、动作、指令且不承担过渡/节奏的整句空话才可删。用户已经授权删冗余、压缩或去除空句时，直接执行并简述；未给这项授权时，保留原句并在正文外列待确认项，先交付其他已完成编辑。不要把待确认项提前从稿中删掉。一般“自然一点”不等于大幅压缩。

## 核心编辑判断

- 删不传递信息的开场、空总结、谄媚、身份认证式夸奖和表演性旁白。
- 把黑话还原成原文已有的动作或判断。保留真实技术术语和系统主语。
- 对照句两端都承重时保留；三项分类、被动句、破折号和标题按用途判断。
- 保留必要限定、概率、否定、因果方向、比较对象和作者责任。不把“可能”删成确定，不把“多数”改成全部。
- 不新增事实、来源、个人经历或作者态度；不能从更具体的示例中借来数据。
- 数字、日期、单位、姓名、引文、链接目标、代码、命令、字段、路径、错误和状态受保护；完整边界见 [protected-spans.md](references/protected-spans.md)。
- SRT 的 canonical、claim、书稿和发布边界按根 AGENTS.md。

无源引用按证据依赖处理：只有原文已有独立支撑时才可删权威铺垫（`rewrite-safe`）；否则保留原文并标缺来源（`audit-only`）。用户要求编辑占位时可用 `rewrite-with-placeholder`，把待补来源显式留在编辑稿里。语气变弱不等于证据补齐。

## 回读与停止条件

先对照原文检查保护项、信息点、术语、责任和衔接；`bounded / in-place` 还要核对句数、段落顺序与关键重复。有明显模板残留再做轻量修正，仍服从原 scope。无需为了主观评分重复润色；需要新增材料或超出授权才能改善的部分留作建议。

默认只给一个版本和必要的取舍说明。标注模式给问题、位置和建议，不附完整重写稿。内容本来合适时可以不改。

## 按需 references

- 事实/引用/代码保护：[protected-spans.md](references/protected-spans.md)。
- 声纹与语域：[positive-style.md](references/positive-style.md)、[scene-guardrails.md](references/scene-guardrails.md)。
- 实际结构病灶：[operation-manual.md](references/operation-manual.md)、[structures.md](references/structures.md)。
- 短语判断：[phrases-zh.md](references/phrases-zh.md)、[phrases-en.md](references/phrases-en.md)；词表是线索，不是禁词过滤器。
- README/release note/社区帖/issue 回复需要进一步校准时：[scene-packs.md](references/scene-packs.md)。
- 示例与边界复核：[examples.md](references/examples.md)、[boundary-cases.md](references/boundary-cases.md)。
- 维护技能或做行为回归时：[evals/real-samples.md](evals/real-samples.md)；不是每次编辑的必读输入。
