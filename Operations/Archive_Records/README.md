---
id: SRT-OPS-ARCHIVE-RECORDS
type: index
status: archived
claim_mode: navigation
updated: 2026-07-20
---

# Operations Archive Records

本目录存放**已完成的一次性运行层记录**：结构治理轮的 pre-audit、adjudication、extraction record、closure report、同步记录与历史审计。

判定标准：记录对应的工作已关闭，文件不再被任何活跃 pipeline 写入。

使用原则：

- 这些文件是历史留痕（provenance），不是活跃流程入口，也不产生任何维护义务。
- 引用时应说明其历史批次边界；结论若与当前 canonical 锚点或活跃台账冲突，以后者为准。
- 文内相对链接已在 2026-07-20 迁移时按新位置改写；如个别链接指向后来又移动的文件，以当前仓库结构为准。

主要批次族：

- `PR_A* / PR_B* / PR_C* / PR_D*` — Neuroscience / AI 接口抽取与 annex 治理轮（2026-04 至 2026-05）
- `Physics_P0* / P1* / P2*` — Physics 盘点、frontmatter 规范化与接口抽取轮
- `*_Closure_Report / Closure_Index / Structural_Governance_Rollup` — 各治理轮关账记录
- 其余为单次审计、导航一致性检查与同步记录

迁移记录：2026-07-20 治理减负轮，自 `Operations/` 顶层移入，见 `Governance/Governance_Load_Reduction_2026-07-20.md`。
