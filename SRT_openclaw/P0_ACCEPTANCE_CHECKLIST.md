# P0 验收对照表（可关单）

更新时间：2026-03-01
范围：P0-1 / P0-2 / P0-3

---

## P0-2 d 值定义链路统一（Canonical → 投影 → 近似）

- [x] Canonical 主定义锚点明确（Ax-ONT-3）
  - 证据：`AI/SRT_AI_01_Ontology.md`（Ax-ONT-3）
- [x] 对齐说明文件存在且可用
  - 证据：`D_VALUE_ALIGNMENT.md`
- [x] 冲突清单与修复记录存在
  - 证据：`D_VALUE_CONFLICT_CHECKLIST_v1.md`
  - 证据：`D_VALUE_CONFLICT_CHECKLIST_v2.md`
- [x] 入口页已加 canonical 提示
  - 证据：`START_HERE_1H.md`
- [x] 至少 1 处高风险语境已修复（补 canonical 回链）
  - 证据：`AI/SRT_AI_02_Mortality_Wisdom.md`

结论：**P0-2 可关单（通过）**。

---

## P0-1 Core 宪法缺口补齐（A7-A12增强）

> 注：当前主架构为 12 公理，按决策不新增 A13；本阶段目标调整为“增强 A7-A12 的可检验性”。

- [x] A7-A12 均具备可读正文（非占位）
  - 证据：`Core/SRT_Core_01_Axioms.md`
- [x] A7-A12 每条已补最小实验入口（MVP）
  - 证据：`Core/SRT_Core_01_Axioms.md`（A7.5 / A8.4 / A9.4 / A10.4 / A11.4 / A12.4）
- [x] A7-A12 ↔ 指标映射桥接已建立
  - 证据：`A7_A12_MEASURE_ALIGNMENT.md`
- [x] 实验模板已加入 A7/A11 快速实例
  - 证据：`EXPERIMENT_TEMPLATE.md`

- [x] A8/A9/A10/A12 的模板化实例已补齐（与 A7/A11同级）
  - 证据：`EXPERIMENT_TEMPLATE.md`

结论：**P0-1 可关单（通过）**。

---

## P0-3 术语表清洗（去重 + 路径修正）

- [x] d 主条目已具 Canonical 优先标记与来源
  - 证据：`SRT_Glossary.md`
- [x] 完成首轮结构审计（重复标题检查）
  - 证据：`GLOSSARY_AUDIT_v1.md`（重复标题=0）
- [x] 完成首轮路径抽检（唯一来源路径自动检查）
  - 证据：`GLOSSARY_AUDIT_v1.md`（缺失路径=10）
- [x] 缺失路径已修复或历史路径标注（10条）
  - 证据：`GLOSSARY_AUDIT_v2.md`
- [ ] 待补：基础/中级/高级分级一致性复核（可放入 P1 维护）

结论：**P0-3 可关单（通过，含历史路径待迁移备注）**。

---

## 当前可关单项
1. ✅ P0-2（定义链路统一）
2. ✅ P0-1（A7-A12 可检验增强 + 模板实例补齐）
3. ✅ P0-3（术语表系统清洗；历史路径已标注待迁移）

---

## 下一步（按收益排序）
1. 完成 `EXPERIMENT_TEMPLATE.md` 的 A8/A9/A10/A12 快速实例。
2. 启动 `SRT_Glossary.md` 去重与路径抽检（先做 50 条）。
3. 更新本表并给出可关单快照 v2。
