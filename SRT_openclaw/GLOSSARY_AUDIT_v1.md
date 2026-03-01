# Glossary 审计 v1（P0-3）

更新时间：2026-03-01
目标：快速评估 `SRT_Glossary.md` 的可维护性风险。

## 结果摘要
- `首次出现`条目数：57
- 术语标题（`####`）数：87
- 重复标题数：0（未发现同名重复）
- 抽取到的来源路径（唯一）数：23
- 不存在路径数：10（需修复）

## 缺失路径清单（首轮）
1. `Neuroscience/SRT_Neural_Mechanisms.md`
2. `Neuroscience/SRT_Consciousness_Mechanisms.md`
3. `AI/SRT_AI_Foundations.md`
4. `Philosophy/SRT_Social_Systems.md`
5. `Neuroscience/SRT_Neuro_10_Advanced_Models.md`
6. `Neuroscience/SRT_Clin_01_Pathology.md`
7. `Neuroscience/SRT_Neuro_06_Field_Effects.md`
8. `Neuroscience/SRT_Consciousness_Clinical.md`
9. `Core/SRT_Internal_Derivations.md`
10. `AI/SRT_AI_Computation.md`

## 判断
- 结构层（是否重复）风险低。
- 引用层（路径失效）风险中高，需在 P0-3 处理中修复。

## 下一步
1. 对上述 10 条路径进行“现有等价文件”重定向或标记“历史路径”。
2. 完成 50 条来源路径抽检（当前已自动抽检 23 条唯一路径）。
3. 修复后输出 `GLOSSARY_AUDIT_v2.md`。
