---
name: srt-humanization-pipeline
description: 对 SRT-Pub 中的中文或英文文章、公共内容、书稿试写和说明文执行可复用的三阶段真人化流程：先用 shuorenhua 做场景诊断与保真轻改，再用 humanizer-zh 调整结构和节奏，最后用 stop-slop 做残留模板审计，并核对数字、链接、标题、引文和理论边界。触发：三步去 AI 味、文章真人化、按三个技能优化、humanization pipeline、发布前语言清理、评价或复核 AI 写作纹理。
---

# SRT Humanization Pipeline

把三项编辑能力固定成一个有顺序、有保护项、有失败出口的流水线。目标不是骗过检测器，而是在不损伤事实、术语、主张等级和作者立场的前提下，减少可见的 AI 模板纹理。

## 依赖与读取顺序

开始前完整读取：

1. `../shuorenhua/SKILL.md`
2. `../humanizer-zh/SKILL.md`
3. `../stop-slop/SKILL.md`

按任务需要读取三项技能直接链接的 references。中文长文默认至少读取：

- `../shuorenhua/references/protected-spans.md`
- `../shuorenhua/references/positive-style.md`
- `../shuorenhua/references/operation-manual.md`
- `../shuorenhua/references/structures.md`
- `../shuorenhua/references/phrases-zh.md`
- `../shuorenhua/references/scene-guardrails.md`
- `../stop-slop/references/phrases.md`
- `../stop-slop/references/structures.md`

若目标是公开发布，再读取仓库根目录下的 `05_Public_Release/PUBLIC_GUARDRAILS.md`；涉及书稿公共内容时，同时读取 `01_Source_Intuition/BOOK/BOOK_PUBLIC_CONTENT_STRATEGY_2026-06-12.md`。这些文件只负责发布边界，不定义理论。

## 不可变规则

- 三阶段必须按顺序执行，不并行为一次泛化润色。
- 先保真，后去味；任何风格收益都不能覆盖事实、数字、日期、单位、专名、归属、引用、链接、代码、字段、路径和发布状态。
- 不新增原文没有的事实、来源、个人经历或作者态度。
- 不把 bridge、lab、public 或 open tension 语言升级为 canonical 结论。
- 不把 `stop-slop` 的英文规则机械套到中文。中文允许承担论证的对照句、少量破折号、被动结构和正式语体。
- 不承诺通过 AI 检测器。检测结果只能作为不稳定信号。
- 公共内容的语言清理不等于发布批准；保留原有 `publication_status` 与禁发提示。

## 阶段 0：建立基线

1. 判断主场景：`chat / status / docs / public-writing / book-trial`。
2. 保存或定位改写前版本。已跟踪文件优先使用 Git 基线；公共长文按仓库规则保留版本轨迹。
3. 建立 protected spans 清单：
   - 数字、日期、比例、单位；
   - 人名、机构、理论名、术语、责任与观点归属；
   - 引号、文献条目、URL、Markdown 链接目标；
   - frontmatter、发布状态、claim level 与失败条件。
4. 确定 scope：
   - 中文长篇公共写作默认 `bounded`；
   - 技术说明默认 `in-place` 或轻度 `bounded`；
   - 只有用户明确授权重写、重排或大幅压缩时才用 `structural`。
5. 对 SRT 公共文本记录材料底座与作者语料是否缺失。缺少作者语料时，只能称为编辑稿，不能称为最终作者版。

## 阶段 1：shuorenhua 初诊与轻改

目标：先处理最明显的场景错位和模板姿态，不动大结构。

1. 按 `shuorenhua` 判 Tier、档位和 scope。
2. 优先处理开场套话、总结提示腔、旁白层、商业或工程表演腔、无源权威铺垫和语域混搭。
3. 长文 `bounded` 模式不擅自删除有信息的整句，不重排段落。纯空句进入待确认清单。
4. 回读 protected spans，形成 Pass 1。

阶段出口：事实、术语或责任主体一旦漂移，回退并修复后才能进入下一阶段。

## 阶段 2：humanizer-zh 结构真人化

目标：处理 Stage 1 留下的段落级纹理，让文章从“清理过”变成“自然可读”。

1. 检查夸大的意义、宣传腔、模糊归因、机械三段式、同构段落、过度标题化、连续等长句和过密连接词。
2. 在 scope 允许范围内拆分承重过高的长段，合并同功能短段，打散连续同构结构。
3. 保留作者真正承担论证的重复、比喻和强判断；不要把专业文本口语化。
4. 不用第一人称、口头禅、错别字或伪造细节制造“人味”。
5. 再次核对主张等级、证据边界和 protected spans，形成 Pass 2。

阶段出口：如果更自然只能靠新增材料或改变论证顺序，停止并请求作者补充或授权。

## 阶段 3：stop-slop 终审

目标：只消除仍然显眼的残留模式，不再进行一轮重写。

1. 检查填充语、假戏剧二元对比、否定式铺垫、碎句表演、远距离旁白、金句式收尾、三件套强迫和机械节奏。
2. 将 `stop-slop` 作为审计器而非删除器：
   - 对照两端都承担边界时保留；
   - 技术或学术被动语态能明确归属时保留；
   - 中文破折号看密度和功能，不要求归零；
   - 三项列举若对应真实分类，不为避“三”而硬改。
3. 每次只处理高置信度残留。若改动开始削弱作者声纹，停止。
4. 形成 Pass 3，不追加新的拔高总结。

## 阶段 4：保真与差异核验

运行：

```bash
uv run python .agents/skills/srt-humanization-pipeline/scripts/audit_text.py BEFORE AFTER
```

若没有 `uv`，可用 `python3`，并在结果中说明。

脚本硬检查数字、URL 和 Markdown 链接目标；标题、代码片段和引号变化作为人工复核项。随后人工检查：

1. 专名、观点归属与责任主体；
2. 引文、参考文献和证据强度；
3. SRT 术语、claim level、open tension 与失败条件；
4. frontmatter 和发布状态；
5. 是否从“更自然”滑成“更中性、更无菌”。

硬检查失败时不得交付为完成版。人工复核项必须说明保留、回退或接受变动的理由。

## 输出合同

默认返回：

```text
场景 / scope：
protected spans：通过 / 失败 / 待人工复核
Stage 1：处理了什么
Stage 2：处理了什么
Stage 3：处理了什么
核验：数字 / URL / 链接 / 标题 / 引号 / claim 边界
剩余风险：
最终文件：
```

用户只要求审稿或评价时，不修改文件；按三阶段分别指出问题，并给出总评。用户要求直接改写时，才写回目标文件。

## 调用示例

- `$srt-humanization-pipeline 按三步优化这篇公共长文，保留所有数字、文献和理论边界。`
- `$srt-humanization-pipeline 只评价这个优化稿，不继续修改。`
- `$srt-humanization-pipeline 对比改写前后，检查有没有为了去 AI 味损伤作者声纹。`
