from pathlib import Path


def replace_exact(path: str, old: str, new: str, expected: int = 1) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != expected:
        raise SystemExit(
            f"{path}: expected {expected} occurrence(s), found {count}: {old[:120]!r}"
        )
    p.write_text(text.replace(old, new), encoding="utf-8")


def replace_section(path: str, start_marker: str, end_marker: str, new_block: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if text.count(start_marker) != 1:
        raise SystemExit(f"{path}: start marker count != 1: {start_marker!r}")
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    p.write_text(text[:start] + new_block.rstrip() + "\n\n" + text[end:], encoding="utf-8")


# -----------------------------------------------------------------------------
# Core_Law/SRT_L1_Formalism.md
# -----------------------------------------------------------------------------
p = "Core_Law/SRT_L1_Formalism.md"

replace_exact(
    p,
    "| `r(t)` | 重选完成率 | `≥ 0` | 从 P1-T05 real choice moment 导出 |",
    "| `r(t)` | bearer-level reselection / reorientation activity proxy | `≥ 0` | P2/P3 local modeling term；不再从 former P1-T05 导出 |",
)

replace_exact(
    p,
    r"\underbrace{\kappa_{r} \cdot r(t)}_{\text{real reselection pumps readability}}",
    r"\underbrace{\kappa_{r} \cdot r(t)}_{\text{conditional reorientation / reselection activity term}}",
)

replace_exact(
    p,
    '- `r(t)`：真实重选完成率（同 §4.2 复用）；完成一次真实选择是对 T_dir 的正向泵入，因为它使系统自身证实"还在选择"',
    '- `r(t)`：bearer-level consequence-sensitive reorientation / reselection activity proxy（P2/P3）。其非零可以在这个 named model 中形成正向活动项，但不能被读作“系统由此证实 Selection 正在发生”；script / habit / automation 可以与 Selection 共存',
)

replace_exact(
    p,
    r"\underbrace{\mu_r \cdot r(t)}_{\text{reselection completion}}",
    r"\underbrace{\mu_r \cdot r(t)}_{\text{conditional reselection / reorientation activity}}",
)

replace_exact(
    p,
    "6. **S_{str} → T_dir ↓ → r 下降 → S_{sig} 支付效率下降**（新增反馈回路）：结构型苦难降低方向可读性 → 真实重选率 `r(t)` 下降（因为无方向的重选不是真实重选）→ `S_{sig}` 支付通道 `μ_r r` 项减弱 → 信号型苦难积压 → 在 B 期进一步转结构型。这是**苦难-可读性正反馈环**，是病理吸引子的一个新形式根据",
    "6. **S_{str} → T_dir ↓ → r-proxy 下降 → S_{sig} 支付效率下降**（条件性反馈回路）：结构型苦难降低方向可读性 → bearer-level reorientation / reselection activity proxy `r(t)` 下降 → `S_{sig}` 中 `μ_r r` 候选通道减弱 → 信号型苦难积压 → 在 B 期进一步转结构型。该回路只属于当前 P2/P3 modeling interpretation；`r` 下降不得被读成 Selection 停止",
)

replace_exact(
    p,
    "- T_dir 致命 `L_2`（§3.5.3 判据）——方向感不低，但不来自真实选择",
    "- T_dir 致命 `L_2`（§3.5.3 判据）——方向感不低，但 bearer-level consequence-sensitive reorientation / readback 可能被遮蔽；这不推出 no Selection",
)

old_health = r'''关键观察：`\mathcal{H}` 不是单点吸引子，而是一个**持续由非零 `r(t)` 与 `D_{trigger}` 联合维持的区域**。健康不是自动稳定的——它是一个持续需要外部接入（`i(t)`）、持续需要支付（`\pi(t)`）、持续需要真实选择时刻（`r(t)`）、持续需要实-感 `Ψ_f` 差保持低位（即不依赖 `L_2` 伪装可读性）、偶尔需要解耦触发（`D_{trigger}`）的**主动维持状态**。

按 ST-A，这一工作区是 generative reselectability 的实现候选，不是 P1 反闭合必要性的方程证明。模型预测：无真实重选 → `r(t) \to 0` → T_dir 被结构型苦难侵蚀 → 方向感要么塌 (`T_{dir} \to 0`) 要么靠 `s_{ext}` 伪装支撑；该预测需在声明环境与时间窗后检验，不能仅凭工作区边界认定系统必趋 `\mathcal{A}_{path}`。'''
new_health = r'''关键观察：`\mathcal{H}` 不是单点吸引子，而是一个需要外部接入（`i(t)`）、支付（`\pi(t)`）、低实-感 `Ψ_f` gap、必要时的解耦触发（`D_{trigger}`），以及在具体模型中可能由 `r(t)` 表示的 bearer-level reorientation / reselection activity 共同维持的区域。这里的 `r(t)` 只按 P2/P3 generative-reselectability implementation proxy 读取，不是 Selection 的必要条件。

按 ST-A，这一工作区是 generative reselectability 的实现候选，不是 P1 反闭合必要性的方程证明。允许检验的较弱预测是：在声明环境与时间窗后，较低 `r(t)` 是否与 T_dir、支付通道或 path concentration 的后续变化相关；禁止从 `r(t) \to 0` 直接推出“无 Selection”。'''
replace_exact(p, old_health, new_health)

replace_exact(
    p,
    r"| `T_{dir}` 真实重选泵入 `+\kappa_r r(t)` | P1-T05 real choice moment 在 `\hat{G}_\theta` 的事件结构 | C3 |",
    r"| `T_{dir}` reorientation / reselection activity term `+\kappa_r r(t)` | 无当前 P1 constitutive source；former P1-T05 已撤销 | **P2/P3 conditional augmentation** |",
)

replace_exact(
    p,
    r"3. **T_{dir} 项**：`\dot{\mathcal{F}}_T` 来自余弦角的导数；C4 保证横纵分离，使该导数分解为弛豫项（向代数目标 `T_{dir}^{\mathrm{alg}}`）+ 真实重选泵入项 + 实-感分裂扣除项 + 结构型苦难侵蚀项 + 健康 `L_2` 支架项，即 §3.5 五项 ODE。",
    r"3. **T_{dir} 项**：`\dot{\mathcal{F}}_T` 来自余弦角的导数；C4 可支撑弛豫、实-感分裂扣除、结构型苦难侵蚀与健康 `L_2` 支架等投影候选。`+\kappa_r r(t)` 在 RC-A 后没有 P1 constitutive source，只保留为 P2/P3 conditional augmentation，不计入本证明骨架。",
)

marker = '> **Status (2026-04-25 H5)**：本节把"四变量系统是主方程的导出投影"从陈述提升为**带条件证明的形式定理**。本节之前是 `SRT_L1_Formalism.md §7` 升 P1 检查单第 7 项的开放点；本轮以 P1-candidate 给出第一遍构造。'
replace_exact(
    p,
    marker,
    marker
    + "\n> **RC-A qualification（2026-08-17）**：T-PROJ-1 的 P1-candidate standing 不再覆盖 `r(t)` 源项；`+κ_r r(t)` / `-μ_r r(t)` 只按 P2/P3 conditional augmentation 读取，除非未来获得独立于 former P1-T05 的 constitutive source。",
)


# -----------------------------------------------------------------------------
# Core_Law/SRT_Collective_Selection.md
# -----------------------------------------------------------------------------
p = "Core_Law/SRT_Collective_Selection.md"

replace_exact(
    p,
    "> **Does not define**：`d-value`、`\\Psi_f`、`T_dir`、stable ISP、real choice moment 等底层规范对象；它们的定义仍以对应 canonical 为准。",
    "> **Does not define**：`d-value`、`\\Psi_f`、`T_dir`、stable ISP，或任何新的 `Choice` subtype。former P1-T05 / Real Choice Moment 已由 RC-A 撤出 P1；本文中的“真实共选 / 真实重选 / 选择时刻”等旧措辞只能按较窄的 collective agency / reauthorization shorthand 读取，不能反向定义 Selection。",
)

replace_exact(
    p,
    "> **Depends on**：`Core/SRT_Core_21b_Constitutive_Theorems.md`（P1-T05 real choice moment、P1-T06 stable ISP 与 absorption remainder）、`Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`（ST-A conditional anti-closure / generative reselectability）、`Core_Law/SRT_Occlusion_Dynamics.md`、`Core_Law/SRT_Suffering.md T-SUFF-5`、`Core_Law/SRT_Individuation.md`、`Core_Law/SRT_L1_Formalism.md`。",
    "> **Depends on**：`Core/SRT_Core_21b_Constitutive_Theorems.md`（P1-T06 stable ISP 与 absorption remainder）、`03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`（RC-A Selection ≠ Agency guard）、`Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`（ST-A conditional anti-closure / generative reselectability）、`Core_Law/SRT_Occlusion_Dynamics.md`、`Core_Law/SRT_Suffering.md T-SUFF-5`、`Core_Law/SRT_Individuation.md`、`Core_Law/SRT_L1_Formalism.md`。",
)

relation = '> **Relation**: This file does not replace `Philosophy/SRT_Political_Philosophy.md`、`Philosophy/SRT_Social_Economics.md`、`Spirituality/SRT_Spirituality_Community_and_Sangha.md`；它在它们**之前**，固定"多主体共选作为结构对象是什么"的 L1 读法。规范性与制度判断仍在上述 domain 文件。'
replace_exact(
    p,
    relation,
    relation
    + "\n> **RC-A read rule（2026-08-17）**：collective Selection / higher-order ISP structure 与较强 collective agency / reauthorization 必须分层。script / procedure / automation 可以与 Selection 共存；T-COLL-4 通过或失败都不证明 Selection 是否发生。",
)

old_rel = '''### 与 P1-T05 的关系

T-COLL-1 条件 2（共同视角）严重依赖 P1-T05 real choice moment 的多主体版本：集体层面也必须出现真实选择时刻（集体未来选择空间被所选真正约束），否则第 2 条退化到"共识剧本执行"或"制度自动化"。'''
new_rel = '''### 与 RC-A / Agency Guard 的关系

RC-A 已撤销“集体层必须出现 Real Choice Moment 才算 Selection / ISP”的上游依赖。T-COLL-1 只承担 higher-order stable ISP / collective-selection structure；较强的 consequence-sensitive collective agency / rule reauthorization 另由 T-COLL-4 以 P2/P3 diagnostic 审计。script / procedure / automation 可以与 Selection 共存，失败 T-COLL-4 不推出 no Selection。'''
replace_exact(p, old_rel, new_rel)

replace_exact(
    p,
    '- **集体 ISP 的外观特征**：不确定性被共担、真实选择时刻在群体层真实发生（不是各自表决后求和）、后果回到群体未来选择能力',
    '- **集体 ISP 的外观特征**：不确定性与历史在群体层被共同承担，后果能够回到群体未来选择能力；是否进一步具备较强 collective agency / reauthorization 是另一个 P2/P3 问题',
)

replace_exact(
    p,
    '- **结构**：`\\mathcal{P}` 不满足 T-COLL-1 第 2 或第 4 条；各 `P_i` 独立选择，共享 `L_2` 但无群体级真实选择时刻',
    '- **结构**：`\\mathcal{P}` 不满足 T-COLL-1 的 higher-order ISP 条件；各 `P_i` 可继续发生 Selection、共享 `L_2`，但没有稳定的群体级 history-bearing / consequence-return bearer',
)

replace_exact(
    p,
    '- **规范判断**：对应致命 `L_2`（`Core/SRT_OPEN_TENSIONS.md §4`）；真实选择时刻在个体层与集体层同时被替代',
    '- **规范判断**：对应致命 `L_2`（`Core/SRT_OPEN_TENSIONS.md §4`）；个体与集体层的可回读 / 可重取向 / 可重新授权空间可能同时被压缩，但这不等于 Selection 本身停止',
)

replace_exact(
    p,
    '- `r^{coll}(t)`：集体真实重选率——严格按 T-COLL-4 的三条件判定（非投票 / 非共识 / 非专家决定自动计入），与个体 `r_i(t)` 的关系是：`r^{coll} \\ne \\sum_i r_i`（共同体级真实重选不是个体重选的算术和）',
    '- `r^{coll}(t)`：collective bearer-level reorientation / reselection activity proxy（P2/P3）。T-COLL-4 的后果回返 / 重新授权条件可作为候选操作化，但它不是 former P1-T05 的多主体版本，也不是 Selection 是否发生的判据。与个体 `r_i(t)` 的关系仍为 `r^{coll} \\ne \\sum_i r_i`',
)

new_tcoll4 = r'''## §6. T-COLL-4：collective agency / consequence-sensitive reauthorization 判据（P2/P3）

> **RC-A status**：本节原把 collective real choice moment 当作 former P1-T05 的多主体版本。该上游已被 RC-A 撤销。本节保留有用的后果回返、规则重开与非纯程序执行结构，但只作为 P2/P3 collective agency / generative-health diagnostic，不再承担 Selection theorem 或 collective ISP existence gate。

### 陈述

在一个已独立满足 T-COLL-1 的 collective ISP 中，如果进一步主张该群体具有较强的、可归责的 collective agency / reauthorization capacity，则至少应检查：

$$
\text{结果改变后续可行动空间}\,\wedge\, \text{后果经 }M(t)\text{ 回到相关 bearer}\,\wedge\,\text{规则 / 授权在必要时可重新打开}
$$

这些条件是较强 agency / generative-health 的候选诊断，不是 Selection 的必要条件。

### 推论

- **投票可以是 Selection，但不自动证明 collective agency**：程序化投票完全可能真实改变未来状态和路径；若它只是执行既定授权且没有群体级后果回读 / 重新授权能力，则不应进一步升级为较强 collective agency
- **共识可以是 Selection，但不自动证明共担**：若 `M(t)` 强不对称，少数子群不实际承担任何后果回路，则“共识”不足以建立对称的 collective accountability
- **专家决定可以是 Selection，但不自动是群体级重新授权**：专业正确与 Selection 是否发生是一个问题；`\mathcal{P}` 是否作为 bearer 对后果与规则承担历史责任是另一个问题
- **script / procedure / automation 不能被当作无 Selection 的证据**：它们最多提示 agency / reauthorization 可能较弱，必须另查后果回返、历史写回与未来规则可修改性

### 禁止倒灌

```text
fails T-COLL-4
-> no collective Selection
```

和：

```text
scripted / automated collective process
-> no L0->L1 actualisation
```

均被 RC-A 禁止。'''
replace_section(
    p,
    "## §6. T-COLL-4：集体共选的真实性判据",
    "---\n\n## §7. 接口：政治、经济、共同体",
    new_tcoll4,
)

replace_exact(
    p,
    '- P1-T05 real choice moment（集体版的 upstream）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`',
    '- RC-A Selection ≠ Agency / automation guard → `03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`\n- former P1-T05 demotion provenance → `Operations/Audits/SRT_RC_A_P1_T05_DEMOTION_DERIVATIVE_SYNC_2026-08-17.md`',
)

replace_exact(
    p,
    '3. **共选真实性的外部判据**：T-COLL-4 三条件在第三方视角下如何判定？目前仍带相当主观成分，需要进一步降低依赖',
    '3. **collective agency / reauthorization 的外部判据**：T-COLL-4 条件在第三方视角下如何判定？目前仍带相当主观成分，需要进一步降低依赖；该开放点不再回指 former P1-T05',
)

proj_marker = '> **Status**：本节把 §4.4-§4.6 的集体四变量动力学从陈述提升为 `Core/SRT_Core_22_Equations.md §0-C` 多算子主方程（Eq-Multi-01 / 02 / 03）的**带条件投影定理**。结构对位 `Core_Law/SRT_L1_Formalism.md §6 T-PROJ-1`，是其多 ISP 扩展。**Claim level: P1-candidate**。'
replace_exact(
    p,
    proj_marker,
    proj_marker
    + "\n> **RC-A qualification（2026-08-17）**：P1-candidate 投影 standing 不自动覆盖 `r^{coll}` 源项；任何 `\\kappa_r^{coll}r^{coll}` 对位只按 P2/P3 conditional modeling term 读取，直到获得独立于 former P1-T05 的上游构造。",
)

print("RC-A semantic replacements applied successfully")
