# d 值冲突清单 v1

更新时间：2026-03-01
范围：Core / AI / Glossary（首轮）

## A. Canonical 定义锚点（确认）
- `AI/SRT_AI_01_Ontology.md`（Ax-ONT-3）已明确声明为第一性定义。
- `Core/SRT_Core_14_Dynamics_Scaling.md` 已明确“与规范定义统一”。

## B. 需统一措辞的风险点（首轮）
1. `AI/SRT_AI_02_Mortality_Wisdom.md:199`
   - 风险：出现“起点: d值定义”但未就地回链 canonical。
   - 处理建议：补一句“此处沿用 Ax-ONT-3 canonical 定义”。

2. `SRT_Glossary.md`（多处 d 相关条目）
   - 风险：术语解释较长，读者可能将不同语境表达误读为并列定义。
   - 处理建议：在 d 主条目顶部增加“Canonical 优先级标记 + 回链”。

3. 入口层（Intro/Glossary）
   - 风险：用户从入口读起时，可能先看到操作化表达。
   - 处理建议：入口页前置“主定义→局部投影”三句模板。

## C. 统一模板（执行标准）
1. 先写：`d = ||∂U/∂S||`（Ax-ONT-3）
2. 再写：本节局部表达是“近似/投影/操作化”
3. 最后写：该表达不替代 canonical 定义

## D. 下一步
- 对 `START_HERE_1H.md`、`SRT_Glossary.md` 做最小改动，前置 canonical 回链。
