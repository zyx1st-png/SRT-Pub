from pathlib import Path


def replace_exact(path: str, old: str, new: str, expected: int = 1) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != expected:
        raise SystemExit(
            f"{path}: expected {expected} occurrence(s), found {count}: {old[:160]!r}"
        )
    p.write_text(text.replace(old, new), encoding="utf-8")


# L1 formalism: keep r as a model proxy, never as the constitutive definition of d_c.
p = "Core_Law/SRT_L1_Formalism.md"
replace_exact(
    p,
    "`d_c` 定义为：低于此 `d` 值，当前主体的重选容量显著坍塌的 d 边界。操作化为：",
    "`d_c` 的概念定义仍由 `SRT_Occlusion_Dynamics.md` 承担：它是低于某个 `d` 区域时 bearer-level 可重取向 / 可重选能力显著坍塌的边界。本文件**不以 `r` 反向重定义 `d_c`**；下面只给出一个 P2/P3 local operationalization candidate：",
)
replace_exact(
    p,
    "其中 `r(d, P, t)` 是在当前 d 值下可完成的重选率，`r_{min}` 是\"非 B 期锁死\"所需的最小重选率。",
    "其中 `r(d, P, t)` 只是在当前 d 值下 bearer-level reorientation / reselection activity 的 P2/P3 proxy，`r_{min}` 是这个 named model 的操作阈值。该式可以用于拟合 / 判别，但不得把 `r` 升格为 `d_c` 的构成性定义，也不得从 `r=0` 推出 no Selection。",
)
replace_exact(
    p,
    "| 健康窄化 | `d > d_{narrow}` | `r > r_{min}`，信号型苦难可消化 |\n| A 期 | `d_c < d < d_{narrow}` | `r > 0` 但显著低于健康；结构型苦难开始积累 |\n| B 期 | `d ≤ d_c` | `r → 0`；B 期锁死 |",
    "| 健康窄化 | `d > d_{narrow}` | 本模型中 `r > r_{min}`；信号型苦难可消化 |\n| A 期 | `d_c < d < d_{narrow}` | 本模型中 `r > 0` 但显著低于健康 proxy 区；结构型苦难开始积累 |\n| B 期 | `d ≤ d_c` | 本模型中 `r → 0`；B 期锁死候选；不等于 no Selection |",
)
replace_exact(
    p,
    "即当三个恢复通道（支付、干预、重选）同时塌向零而 d_c 持续被推高，则进入 B 期锁死。",
    "即当本模型中的恢复通道（支付、干预、`r` 所代理的 bearer-level reorientation / reselection）同时塌向零而 d_c 持续被推高，则进入 B 期锁死候选。这是 generative-health / occlusion 诊断，不是 Selection ontology 的停止条件。",
)

# Collective selection: remove remaining agency-loaded wording from the ISP existence gate.
p = "Core_Law/SRT_Collective_Selection.md"
replace_exact(
    p,
    '- "集体选择"有时按多数决理解、有时按真实共选理解、有时按博弈均衡理解；',
    p and '- "集体选择"有时按多数决理解、有时按共同承担 / 共同修订理解、有时按博弈均衡理解；',
)
replace_exact(
    p,
    '- 集体层面的 d / Ψ_f / σ / S 用法分散，没有结构判据说什么算真正的**集体选择主体**。',
    '- 集体层面的 d / Ψ_f / σ / S 用法分散，没有结构判据说什么算一个 higher-order **collective ISP / consequence-bearing bearer**。',
)
replace_exact(
    p,
    "2. **共同视角**：`\\mathcal{P}` 整体对其自身作为选择主体有结构性的迭代登记（而不是仅每个 `P_i` 独立登记）",
    "2. **共同视角 / 承担位置**：`\\mathcal{P}` 整体对其自身作为 history- and consequence-bearing position 有结构性的迭代登记（而不是仅每个 `P_i` 独立登记）",
)
replace_exact(
    p,
    "4. **共同重选**：`\\mathcal{P}` 能作为整体跨步骤继续选择（不是仅各 `P_i` 独立跨步）",
    "4. **跨步持续**：`\\mathcal{P}` 能作为整体跨步骤保持 continued selectability（不是仅各 `P_i` 独立跨步）",
)
replace_exact(
    p,
    '- **"共识"不是集体 ISP 的充分条件**。所有 `P_i` 的独立选择碰巧一致，不意味着 `\\mathcal{P}` 作为主体在选择',
    '- **"共识"不是集体 ISP 的充分条件**。所有 `P_i` 的独立选择碰巧一致，不意味着 `\\mathcal{P}` 已形成 higher-order history / consequence-bearing ISP',
)
replace_exact(
    p,
    '- `Philosophy/SRT_Political_Rights.md`：投票作为 d 倾向后验验证→在本文件下翻译为"通过 T-COLL-4 共选真实性判据验证集体 d"；三层制度（公检法/监督/授权）→维护 `M(t)` 对称与 `σ_{sr}^{coll}` 限幅的结构性器官',
    '- `Philosophy/SRT_Political_Rights.md`：投票作为 d 倾向后验验证→在本文件下可用 T-COLL-4 审计较强的 collective accountability / reauthorization，而不是把投票本身判成“真/假 Selection”；三层制度（公检法/监督/授权）→维护 `M(t)` 对称与 `σ_{sr}^{coll}` 限幅的结构性器官',
)
replace_exact(
    p,
    '- P1-T06 stable ISP（集体 ISP 条件的 upstream）→ 同上\n- former P1-T07 demotion / absorption remainder → 同上',
    '- P1-T06 stable ISP（集体 ISP 条件的 upstream）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`\n- former P1-T07 demotion / absorption remainder → `Core/SRT_Core_21b_Constitutive_Theorems.md`',
)
replace_exact(
    p,
    '- **本文件做**：固定多 ISP 共享 `L_2` 场、集体 ISP 存在条件（T-COLL-1）、三类退化（T-COLL-2）、ST-A 条件性集体反闭合候选（T-COLL-3）、共选真实性判据（T-COLL-4）、**集体四变量最小耦合动力学 §4.4-§4.6**（2026-04-25 H3 新增，与 `SRT_L1_Formalism.md` 单 P 四变量系统形成上下层对应）',
    '- **本文件做**：固定多 ISP 共享 `L_2` 场、集体 ISP 存在条件（T-COLL-1）、三类退化（T-COLL-2）、ST-A 条件性集体反闭合候选（T-COLL-3）、P2/P3 collective agency / consequence-sensitive reauthorization diagnostic（T-COLL-4）、**集体四变量最小耦合动力学 §4.4-§4.6**（2026-04-25 H3 新增，与 `SRT_L1_Formalism.md` 单 P 四变量系统形成上下层对应）',
)
replace_exact(
    p,
    '- **引用规则**：涉及"集体选择作为结构对象是什么"的**结构层**陈述时，优先回链本文件；涉及具体政治、经济、共同体、制度判断时，回链相应 Philosophy / Spirituality 文件',
    '- **引用规则**：涉及"集体选择作为结构对象是什么"的**结构层**陈述时，优先回链本文件；涉及具体政治、经济、共同体、制度判断时，回链相应 Philosophy / Spirituality 文件；涉及 Selection ≠ Agency 边界时回链 RC-A Agency Guard',
)

print("RC-A final owner cleanup replacements applied successfully")
