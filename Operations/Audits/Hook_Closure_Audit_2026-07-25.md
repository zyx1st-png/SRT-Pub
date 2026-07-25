---
id: SRT-OPS-AUDIT-HOOK-CLOSURE-2026-07-25
type: audit
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
date: 2026-07-25
dependency:
  - SRT-MATERIAL-PIPELINE
  - SRT-EDIT-PROTOCOL
tags: [Governance, Pipeline1, IntegrationHook, Closure, Audit]
---

# IntegrationHook 闭环审计（2026-07-25）

> **性质**：运行层审计 + B 类编辑记录。本轮**不改任何 canonical 定义、公理、方程或理论正文**；只给 Pipeline 1 §5.6 的最后一段（hook → 正文）装上可机检的闭环账。

## 1. 为什么做这一轮

`Operations/_SRT_MATERIAL_PIPELINE.md` 把材料管线定义为
`SourceCard → PatchNote → Material Log → Index → Registry → IntegrationHook → 正文`。
前五段都有台账或索引，唯独最后一段没有任何检查能回答一个问题：

> 这张 hook 到底有没有落到正文？

审计前的实际状态：

- hook 的 `status` 字段有**三套并存写法**（`integrated` / `pending` / `active_v0_1`），互相不可比；
- Material Log 的「融入状态」列写的是**写卡当时的自述**，此后不随实际变化更新；
- 没有任何检查验证 hook 的 target 文件是否存在，或声称已融入的内容是否真的在 target 里。

结果是两类静默失效同时存在：**声称 pending 实际已落地**，和**声称有 target 实际目标不存在**。

## 2. 逐张体检结果（18 张 `*/hooks/` hook）

判定方法：对每个 target 取一条**字面锚串**，在 target 文件里实证 grep，而不是采信 hook 自己的 status。

| Hook | 审计前 status | 实证结果 | 审计后 `integration_status` |
|---|---|---|---|
| `COLL08_NTIC_Situated_Individuation` | integrated | 两个 target 均已落地 | landed |
| `CONSC14_Propofol_Traveling_Wave_Reorganization` | integrated | 已落地 | landed |
| `NEURAL15_Creative_Experience_Brain_Clock` | integrated | 已落地（专节） | landed |
| `NEURAL16_BOLD_CMRO2_Uncertainty_Gate` | integrated | 两个 target 均已落地 | landed |
| `NEURAL17_HGA_Spike_Dissociation_Gate` | integrated | 两个 target 均已落地 | landed |
| `PH_CONSC01_Depsychologization_Trap` | integrated | 已落地 | landed |
| `PH_CONSC02_Perspectival_Gap_Gate` | integrated | 已落地（§3.1a 外部视角陷阱） | landed |
| `PH_METH01_Emergence_Hygiene` | integrated | 已落地（P3-B12） | landed |
| `SOC_COG01_ZBS_Discriminatory_Cognition` | integrated | 已落地（T-Cog-6） | landed |
| `SOC_COG02_Developmental_Coordination_Scaffold` | integrated | 已落地（T-Cog-7） | landed |
| `PH_AG01_Agency_Ladder` | **pending** | **实际已落地**（状态陈旧） | landed |
| `PH_AG04_Sensorimotor_Time_Agency` | active_v0_1 | 四个真实 target 全部已落地 | landed |
| `PH_AG02_Reasoning_Bias` | active_v0_1 | agency 主文已落地；`T_dir` canonical **未落地** | **partial** |
| `PH_AG03_Constitutive_Commitment` | active_v0_1 | agency 主文已落地；`T_dir` canonical **未落地** | **partial** |
| `PH_SEM01_Bilateral_Incompatibility` | active_v0_1 | agency 主文已落地；`Occlusion_Dynamics` **未落地** | **partial** |
| `P03_Cosmological_Principle` | pending | target 文档**从未创建** | pending（planned target） |
| `P04_Spontaneous_Collapse_Classicality` | pending | target 文档**从未创建** | pending（planned target） |
| `P05_Quantum_Proper_Time_Optical_Clocks` | pending | target 文档**从未创建** | pending（planned target） |

统计：18 张中 **12 张 landed / 3 张 partial / 3 张 pending**。其中 1 张（PH-AG01）此前被低报，4 张此前状态不可判读。

## 3. 三类未落地残余的处置

### 3.1 `T_dir` canonical 落点（PH-AG02、PH-AG03）

两张 hook 都提议往 `_SRT_T_DIR_CANONICAL.md` 加一条方向效力 / 方向透明度的区分注。实证 0 命中——**未执行**。

处置：**不代为执行**。改 `T_dir` 主定义属 `Governance/SRT_EDIT_PROTOCOL.md` C 类高风险编辑，须作者授权。ledger 记为 `pending` + `blocked_by: canonical freeze`，使这条待办从此可见而不是隐形。

### 3.2 停驻目标（PH-AG02、PH-AG03、PH-SEM01）

三张 hook 指向 `_SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md` 与 `_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md`。这两个文件在 2026-07-20 治理减负轮下沉到 `90_Backstage/Incubation/`，**hook 的路径没跟着更新**——即"下沉带回流路径"这条治理原则在 hook 层漏了一处。

处置：路径修正到现址，状态记 `pending` + `blocked_by: 目标已停驻（ChoiceMap / IRP 产品线未重启）`。停驻内容不因被 hook 指向而自动复活。

### 3.3 计划中但从未创建的 target（Physics P03/P04/P05）

三张 Physics hook 的 target 是 `Physics/SRT_Physics_Bridge_v0_2.md`。该文件**从未存在**，但它也**不是笔误**：三份 patch 的 `target_future_doc`、三张 SourceCard、`Physics/_SRT_Physics_Hardening_Index.md`、`_SRT_Recent_Material_Patches_Index.md` 与 QBox/EarthAccretion 旧 hook 包都一致引用它。它是一份**计划中的 Physics bridge 综合文**。

处置：**不静默改指** `Physics/_SRT_Phys_Bridge.md`。落点二选一——新建该综合文，或改并入现有 bridge 主文——是理论落位判断，属作者裁决。ledger 记为 `pending` + `target_status: planned` + `blocked_by`，让"目标不存在"这件事本身成为账上一条显式条目。

**待作者裁决项（本轮不代拍板）**：Physics 三张 patch 的最终落点。

## 4. 闭环机制（本轮新增）

### 4.1 ledger 结构

hook frontmatter 统一为：

```yaml
status: active                       # 文件是否在用（ratchet enum）
integration_status: landed | partial | pending | withdrawn   # hook 是否落地
landing_ledger:
  - target: "<repo 相对路径>"
    state: landed | pending | withdrawn
    anchor: "<必须在 target 中字面出现的锚串>"   # landed 专用
    blocked_by: "<阻塞原因>"                    # pending 专用
    target_status: planned                      # target 尚未创建时必填
```

关键设计：**把「文件是否在用」与「hook 是否落地」拆成两个字段**。审计前这两件事挤在同一个 `status` 里，正是三套写法并存的根因。

### 4.2 机器检查

新增 `scripts/check_hooks.py`，已接入 `scripts/governance_preflight.py`（因而进 CI）。它强制：

1. 每张 hook 必须有 `integration_status` 与非空 `landing_ledger`；
2. 每个 target 必须存在——除非显式声明 `withdrawn` + 理由，或 `pending` + `target_status: planned` + 理由；
3. 每条 `landed` 必须带 anchor，且该 anchor 字面出现在 target 中；
4. `integration_status` 必须与 ledger 自洽（全 landed → landed；无 landed → pending；混合 → partial）。

第 3 条是本轮的核心：**「已融入」从自述变成可验证**。第 2 条的两个逃逸口都要求把缺席写出来，因此死 target 无法再隐形。

## 5. 顺带清理

- 18 张 hook 的 `status` 归入 ratchet enum（`active`），清掉 frontmatter 基线 21 行已知债，**零新增**。
- Physics 三张 hook 补齐 `id` / `type` / `layer` / `epistemic_layer` / `claim_mode` / `canonical`。
- 修复 main 上 CI 已红的四条 ratchet 违规（2026-07-23/24 三个直推 commit 引入）：两份 Conversations 材料 `seed_v0 → draft`（原值保留为 `seed_stage`），`EC-PHIL-INDEX-COMPRESSION-WORLD-RESOLUTION.md` 补 `epistemic_layer` 并归入 enum。

`uv run python scripts/governance_preflight.py --skip-write-report --strict-split-metadata`：7/7 PASS。

## 6. 边界

- 本轮**不新增、不修改、不降级任何理论命题**；所有 landed 判定都是对**既有正文**的实证读取，不是新的回写。
- ledger 的 `landed` 只断言「该锚串出现在该文件中」，**不断言**回写质量、去材料化程度或 claim-level 正确性。那属于内容评审，不属于闭环检查。
- 三类未落地残余（`T_dir` canonical / 停驻目标 / Physics 计划文档）本轮只做**登记**，不做处置。
