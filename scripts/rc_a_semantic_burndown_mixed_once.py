from pathlib import Path


def replace_exact(path: str, old: str, new: str, expected: int = 1) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != expected:
        raise SystemExit(
            f"{path}: expected {expected} occurrence(s), found {count}: {old[:140]!r}"
        )
    p.write_text(text.replace(old, new), encoding="utf-8")


# -----------------------------------------------------------------------------
# Core_Law/SRT_Irreversibility.md
# Preserve all ST-A / former-P1-T07 provenance; touch only RC-A derivative reading.
# -----------------------------------------------------------------------------
p = "Core_Law/SRT_Irreversibility.md"

replace_exact(
    p,
    "3. **真实选择偏置**：`r(t)` 有足够频率（P1-T05 real choice moment 不被脚本替代）",
    "3. **重取向 / 重选活动偏置（P2/P3 proxy）**：`r(t)` 在命名模型中保持非零，用于追踪 bearer-level consequence-sensitive reorientation / reselection activity；它不再从 former P1-T05 导出，也不是 Selection 是否发生的判据",
)

replace_exact(
    p,
    "- 把 `r(t)` 替换为 `L_2` 脚本（程序化决策、共识剧本）",
    "- 压低 `r(t)` 所代理的 bearer-level 后果回读 / 重取向 / 规则重开通道；程序化决策、共识剧本或其他 `L_2` automation 本身仍可包含 Selection",
)

formula = r'''$$
\varepsilon_{pg}^{\text{visible}}(P, t) \;:=\; \varepsilon_{pg}(P, t) \cdot \mathbb{1}[\sigma_{sr} < \sigma_{sr}^{path}] \cdot \mathbb{1}[\pi(t) > 0] \cdot \mathbb{1}[r(t) > 0]
$$'''
replace_exact(
    p,
    formula,
    formula
    + "\n\n> **RC-A qualification（2026-08-17）**：这里的 `\\mathbb{1}[r(t)>0]` 只是一项 **P2/P3 local visibility / reorientation proxy gate**。它表示相关 bearer 是否仍有可登记的 consequence-sensitive readback / reorientation channel；它不是 Selection gate，`r(t)=0` 不能推出 `no Selection`，script / automation 也不能由此被排除出 Selection。",
)

replace_exact(
    p,
    "致命 L_2 同时压灭后两个指示函数（`π → 0` 与 `r → 0`）并把 `σ_{sr}` 推入 `σ_{sr}^{path}`，使 `\\varepsilon_{pg}^{\\text{visible}} → 0`，即使 `\\varepsilon_{pg}` 本身仍 > 0。本地观测下 `ν_{block}` 表现为 0（误判为\"§4.3 项消失\"），但全局 `\\dot{\\Delta}_{avail}` 仍由 L_0 不可逆性决定，新失配进入暗通道（§4.3 之外的、未被登记的 `S_{str}` 累积）——这是 §5 T-IRR-4 现象的算子级源头。",
    "在这个 local visibility model 中，若 `π → 0`、`r` 所代理的 readback / reorientation channel → 0，并且 `σ_{sr}` 被推入 `σ_{sr}^{path}`，则 `\\varepsilon_{pg}^{\\text{visible}} → 0`，即使 `\\varepsilon_{pg}` 本身仍 > 0。这里描述的是**局部可见 / 可重取向通道的关闭**，不是 Selection 本体的停止。本地观测下 `ν_{block}` 可表现为 0（误判为\"§4.3 项消失\"），但全局 `\\dot{\\Delta}_{avail}` 仍由 L_0 不可逆性决定，新失配进入暗通道（§4.3 之外的、未被登记的 `S_{str}` 累积）——这是 §5 T-IRR-4 现象的算子级候选来源。",
)


# -----------------------------------------------------------------------------
# _SRT_T_DIR_CANONICAL.md
# Part I: remove direct Selection=Agency inversion.
# Part II: add supersession/read rule; do not rewrite historical bridge prose wholesale.
# -----------------------------------------------------------------------------
p = "_SRT_T_DIR_CANONICAL.md"

header_note = "> **Canonical status note（2026-04-23）**：本文件名中的 canonical 表示 governance-canonical working object 与引用锚点，不表示 `T_dir` 已具备 theory-canonical 完整奠基。价值动力学扩展段落按 bridge / theory-clarifying 读。"
replace_exact(
    p,
    header_note,
    header_note
    + "\n> **RC-A active-use override（2026-08-17）**：former `P1-T05: Real Choice Moment` 已撤出 P1。本文遗留的 `活选择 / 真实选择 / 选择时刻 / L₂替代选择` 不得再充当 Selection ontology distinction；当前只可按较窄的 bearer-level direction-readability / consequence-sensitive reorientation / agency shorthand 读取。明确禁止 `script / habit / L₂ automation -> no Selection` 与 `low T_dir -> no Selection`。",
)

replace_exact(
    p,
    "| semantic coherence | 记录叙事或概念一致性 | 可能是 L₂ 后设解释，不保证活选择方向可读 |",
    "| semantic coherence | 记录叙事或概念一致性 | 可能是 L₂ 后设解释，不保证相关 bearer 能回读选择方向或据此重取向 |",
)

replace_exact(
    p,
    "**理由**：d 是有效维度（系统能关切多大范围），T_dir 是方向可读性（系统能否读出自己选择的方向）。高 d 不自动保证方向可读——还需要活选择正在发生，且 Ψ_f 提供了足够的压力。",
    "**理由**：d 是有效维度（系统能关切多大范围），T_dir 是方向可读性（系统能否读出自己选择的方向）。高 d 不自动保证方向可读——还需要当前选择方向在相关 bearer 层形成可访问、可回读并可用于重取向的信号，且 Ψ_f 提供了足够的压力。这里不以“非脚本化”作为 Selection 的必要条件。",
)

old_diagram = '''L₂ 过度依赖
    │
    ├──→ 活选择被替代（L₂ 脚本执行，非 L₀→L₁ 导航）
    │         → T_dir 无来源 → 意义感消失
    │
    └──→ d↓（系统不需要感知方向来运作）
              → Ψ_f_felt↓
              → 系统感觉"无摩擦"
              → 偏好更多 L₂（正反馈回路）

同时：Ψ_f_actual 持续累积 → 隐性债务增长'''
new_diagram = '''L₂ 过度依赖
    │
    ├──→ bearer-level consequence-sensitive readback / reorientation 被预占或压缩
    │         （L₂ 脚本 / automation 仍可包含 Selection）
    │         → T_dir 缺少当前可回读 / 可重取向来源 → 意义感可能下降
    │
    └──→ d↓（系统不需要感知方向来运作）
              → Ψ_f_felt↓
              → 系统感觉"无摩擦"
              → 偏好更多 L₂（正反馈回路）

同时：Ψ_f_actual 持续累积 → 隐性债务增长'''
replace_exact(p, old_diagram, new_diagram)

replace_exact(
    p,
    "| **功能** | 为活选择释放资源 | 替代活选择 |",
    "| **功能** | 为未决问题的方向回读 / 重取向释放资源 | 预占或压缩 bearer-level readback / reorientation；不等于停止 Selection |",
)

replace_exact(
    p,
    "- L₂ 执行感觉比活选择更\"流畅\"",
    "- L₂ 自动执行往往比 consequence-sensitive readback / reorientation 更\"流畅\"",
)

replace_exact(
    p,
    "| 冥想/修行 | 系统性悬置 L₂ 脚本，迫使活选择发生 | `Spirituality/SRT_Spirit_07_Meditation_Neuro.md` |",
    "| 冥想/修行 | 系统性悬置部分 L₂ 脚本，使当前方向、后果与重取向机会更可回读 | `Spirituality/SRT_Spirit_07_Meditation_Neuro.md` |",
)

replace_exact(
    p,
    "| 创作 | 在 L₂ 没有答案的域中强制活选择 | `Spirituality/SRT_Spirit_08_Music.md` |",
    "| 创作 | 在 L₂ 没有现成答案的域中提高当前方向回读与重取向压力 | `Spirituality/SRT_Spirit_08_Music.md` |",
)

replace_exact(
    p,
    "**共同结构**：这些实践的共同机制是——**在 L₂ 不再能完全确定结果的域中，迫使活选择发生，从而重新激活 T_dir 的上升通道。**",
    "**共同结构（P2/P3 bridge reading）**：这些实践的共同候选机制是——**在 L₂ 不再能完全预占 bearer-level response 的域中，增加对当前方向、后果与可重取向性的回读，从而重新打开 T_dir 的上升通道。**这不意味着只有这些非脚本情境才发生 Selection。",
)

replace_exact(
    p,
    "| `Core_Law/SRT_L1_Formalism.md §3.4-§3.5` | T_dir 的 L1 动力学层面：§3.4 代数目标值 `T_{dir}^{\\mathrm{alg}}(\\sigma, d, d_c)`；§3.5 把 T_dir 升为独立动力学变量，ODE 含弛豫、真实重选泵入、`\\Delta\\Psi_f^{\\mathrm{gap}}` 扣除、`S_{str}` 结构侵蚀、`s_{ext}` 支架五项。§3.5.3 给出\"致命 `L_2`\"的方程化判据 `\\kappa_{\\mathrm{mask}} < \\kappa_{\\mathrm{relax}}`。本文件 §5-§6 的现象学定义在 L1 Formalism 侧对应方程级机制。 |",
    "| `Core_Law/SRT_L1_Formalism.md §3.4-§3.5` | T_dir 的 L1 动力学层面：§3.4 代数目标值 `T_{dir}^{\\mathrm{alg}}(\\sigma, d, d_c)`；§3.5 把 T_dir 升为独立动力学变量。RC-A 后 `+\\kappa_r r(t)` 只按 P2/P3 reorientation / reselection activity augmentation 读取，不再从 former P1-T05 获得 P1 权威；其余 gap、`S_{str}`、`s_{ext}` 等项按各自现有边界读取。 |",
)

part2_intro = "> 以下 §11–§16 是 2026-04-02 理论对话的高密度推进，记录了从价值遮蔽到价值结构、感知机制、吸引子动力学的完整理论链。它们共享本文件的引用锚点地位，但不因此升级为 theory-canonical 完成态；除非局部另有标注，均按 bridge / theory-clarifying 读。"
replace_exact(
    p,
    part2_intro,
    part2_intro
    + "\n> **RC-A supersession note（2026-08-17）**：Part II 是 pre-RC-A 历史桥接文本。其中 `活选择 / 真实选择 / 选择时刻 / 假选择 / L₂替代选择` 等字面语保留为 provenance 时，只能按 bearer-level agency / direction-readability / consequence-sensitive reorientation 的旧 shorthand 读取；不得据此推出 script / automation 无 Selection、没有 L₀→L₁ actualisation，或没有 `Ψ_f` 支付。若 Part II 与 Part I 的 RC-A active-use override 冲突，以 Part I override 为准。",
)

print("RC-A mixed-owner semantic replacements applied successfully")
