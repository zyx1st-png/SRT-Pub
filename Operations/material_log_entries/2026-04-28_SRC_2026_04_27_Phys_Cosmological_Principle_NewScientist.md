---
log_entry_id: LOG-2026-04-28-SRC-2026-04-27-PHYS-COSMOLOGICAL-PRINCIPLE-NEWSCIENTIST
source_id: SRC-2026-04-27-PHYS-COSMOLOGICAL-PRINCIPLE-NEWSCIENTIST
patch_id: PATCH-PHYS-P03-COSMOLOGICAL-PRINCIPLE-EFFECTIVE-SYMMETRY
pipeline: Pipeline 1
status: processed_A
material_log_target: Operations/_SRT_MATERIAL_LOG.md
note: "Standalone log entry created to avoid truncating the long central material log file; should be batch-merged later if needed."
---

# Material Log Entry: Cosmological Principle / Effective Symmetry

| 日期 | 来源标题 / URL | 类型 | 审核结论 | 落点（文件 + 节位） | 融入状态 | 备注 |
|-----|--------------|------|---------|-----------------|---------|------|
| 2026-04-28 | New Scientist: *100-year-old assumption about the universe may soon be overturned* / https://www.newscientist.com/article/2524208-100-year-old-assumption-about-the-universe-may-soon-be-overturned/ | 科学新闻/二手；已用 Royal Society meeting、Aluri et al. 2023 review、Binney et al. 2025 manifesto 作更强锚点 | A | `Physics/patches/SRT_Phys_P03_Cosmological_Principle_Effective_Symmetry_v0_1.md`; future `Physics/SRT_Physics_Bridge_v0_2.md` | 已作为 Pipeline 1 v2 patch 写入；正文 hook pending | 新增接口：宇宙学原理作为 effective symmetry / L1-L2 modeling compression；反向修正：禁止把 FLRW/ΛCDM 的成功直接投射为 L0 本体均匀性；加固内容：`L0_total != L0_accessible`、physical L2、model friction；SRT反哺：把 Hubble tension / dipole / large-scale structure anomalies 解释为模型闭合摩擦探针而非即时证伪；残余压力：宇宙学原理尚未被推翻，异常可能来自系统误差、选择效应或 look-elsewhere effect |

## Pipeline 1裁决

- 结论：A，但限于 non-canonical bridge / methodology patch。
- 证据等级：New Scientist 为 secondary；承重依据放在 Royal Society 会议、Aluri et al. review、Binney et al. manifesto。
- 主落点：`Physics/patches/SRT_Phys_P03_Cosmological_Principle_Effective_Symmetry_v0_1.md`
- 未来合并：`Physics/SRT_Physics_Bridge_v0_2.md`

## 写入产物

- SourceCard: `Materials/2026/SRC_2026_04_27_Phys_Cosmological_Principle_NewScientist.md`
- PatchNote: `Physics/patches/SRT_Phys_P03_Cosmological_Principle_Effective_Symmetry_v0_1.md`
- IntegrationHook: `Physics/hooks/P03_Cosmological_Principle_Integration_Hook.md`
- Domain Index: `Physics/_SRT_Physics_Hardening_Index.md`
- Material Log Entry: current file

## 边界声明

- 不宣称宇宙学原理已经被推翻。
- 不宣称 SRT 预测了 ΛCDM 失败。
- 不以 New Scientist 单独承重。
- 不把物理模型摩擦等同于 existential d-value。
