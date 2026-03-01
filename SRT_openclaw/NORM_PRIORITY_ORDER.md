# SRT 规范优先级秩序（Norm Priority Order）

更新时间：2026-03-01
目的：当规则冲突时，提供统一裁决顺序。

## 优先级（高 → 低）

1. **Core 公理正文**
   - `Core/SRT_Core_01_Axioms.md`

2. **变更治理与触发策略**
   - `THEORY_CHANGE_GATE.md`
   - `DIALOGUE_TRIGGER_POLICY.md`

3. **术语与参数边界规则**
   - `TERM_USAGE_GUARDRAILS.md`
   - `PARAMETER_ROLE_MATRIX.md`

4. **入口与传播文档**
   - `START_HERE_1H.md`
   - `FAQ_CRITICAL.md`

## 冲突处理规则
1. 低优先级文本与高优先级冲突时，以高优先级为准。
2. 若 1 与 2 冲突：先冻结传播层改动，启动“对话→回写→commit”流程。
3. 任何跨层修订需在 `DIALOGUE_LOG_YYYY-MM-DD.md` 留痕。
