# Glossary 路径修复计划（10条）

更新时间：2026-03-01
目标：处理 `GLOSSARY_AUDIT_v1.md` 发现的 10 条失效路径。

## 处理策略
1. **可映射**：若存在语义等价的新文件，直接替换为新路径。
2. **不可映射**：标记为“历史路径（待迁移）”，避免伪造引用。
3. **最小改动**：仅改路径字段，不重写术语正文。

## 逐条计划

1. `Neuroscience/SRT_Neural_Mechanisms.md`
   - 计划：历史路径标记（当前仓库无 Neuroscience 目录）。

2. `Neuroscience/SRT_Consciousness_Mechanisms.md`
   - 计划：历史路径标记。

3. `AI/SRT_AI_Foundations.md`
   - 计划：映射到 `AI/SRT_AI_00_Crisis.md`（同为 AI Foundations 起点语义）。

4. `Philosophy/SRT_Social_Systems.md`
   - 计划：映射到 `Philosophy/SRT_Soc_01_Construction.md`。

5. `Neuroscience/SRT_Neuro_10_Advanced_Models.md`
   - 计划：历史路径标记。

6. `Neuroscience/SRT_Clin_01_Pathology.md`
   - 计划：历史路径标记。

7. `Neuroscience/SRT_Neuro_06_Field_Effects.md`
   - 计划：历史路径标记。

8. `Neuroscience/SRT_Consciousness_Clinical.md`
   - 计划：历史路径标记。

9. `Core/SRT_Internal_Derivations.md`
   - 计划：映射到 `Core/SRT_Experimental_Core.md`（实验推导主文件）。

10. `AI/SRT_AI_Computation.md`
   - 计划：映射到 `AI/SRT_AI_Architecture.md`（计算与架构语义最近）。

## 验收
- 路径不可达条目从 10 降到 ≤ 6。
- 所有无法映射项均明确标记“历史路径（待迁移）”。
