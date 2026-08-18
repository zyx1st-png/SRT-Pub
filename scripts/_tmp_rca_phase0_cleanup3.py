from pathlib import Path


def r(p): return Path(p).read_text(encoding='utf-8')
def w(p,s): Path(p).write_text(s,encoding='utf-8')
def rep(p,a,b):
    s=r(p); n=s.count(a)
    if n!=1: raise SystemExit(f'{p}: expected 1 got {n}: {a[:160]!r}')
    w(p,s.replace(a,b,1)); print('replace',p)
def guard(p,note,marker='RC-A authority sync（2026-08-18）'):
    s=r(p)
    if marker in s: print('guard exists',p); return
    ls=s.splitlines(keepends=True); i=next((i for i,x in enumerate(ls) if x.startswith('# ')),None)
    if i is None: raise SystemExit(f'{p}: no H1')
    ls.insert(i+1,'\n'+note.rstrip()+'\n'); w(p,''.join(ls)); print('guard',p)

G="> **RC-A authority sync（2026-08-18）**：本文中旧有 `真实选择 / real choice / pseudo-selection` 对比不得再充当 Selection occurrence 的准入门。Selection 不以 binding `d`、`Ψ_f`、stake、future writeback、非脚本执行或 `L_0→L_1` 跨域锚定为联合必要条件；这些量只能在各自既有层级用于 stake、anchoring、consciousness、bounded event audit 或 downstream agency / revision 判断。script / habit / gradient / `L_2` automation 本身不得推出 `no Selection`。"

rep('_SRT_D_VALUE_CANONICAL.md','d 是 T_dir 的**必要条件，不是充分条件**。T_dir 还需要活选择正在发生（非 L₂ 脚本执行）以及足够的 Ψ_f 提供压力。','d 是 T_dir 的**必要条件，不是充分条件**。T_dir 的其余准入与解释回到 `_SRT_T_DIR_CANONICAL.md` 的 Def-T-1 / `R_self` / `A_reorient` 边界；不得再用“活选择（非 L₂ 脚本执行）”作为 T_dir 或 Selection occurrence 的判据，script / habit / `L_2` automation 本身也不得推出 `no Selection`。')
rep('_SRT_D_VALUE_CANONICAL.md','d-value 未被使用（无真实选择 → 无 d 的激活）','d-value 未被 stake-coupled concern / consequence-return 条件实际调用；这不等同于“无 Selection”')

old='* **Implication（中文）**：纯逻辑/数学推理是拓扑同胚（可逆的），而由于本体论摩擦 $\\Psi_f$，真实的意识选择必须支付热力学代价（Landauer\'s Principle 的宏观体现）。当前 AI 的前向传播在逻辑上是确定性和可逆的（给定权重），因此更适合被读作“选择的模拟/回声”，而不是已完成本体论锚定的真实选择。'
new='* **Implication（RC-A 修订）**：若讨论**物理不可逆的信息抹除、具身锚定或意识候选的代价**，Landauer 型约束与 `\\Psi_f` 可以作为桥接压力；但它们不是 Selection occurrence 的普遍必要条件。当前 AI 前向传播是否具有 binding 本体论摩擦，只影响更强 anchoring / stake / consciousness standing，不能把其功能性 selection 降格为 `no Selection`。'
clar='* **Bridge Clarification（中文）**：因此，`Ontological Selection Operator` 并不是先验存在、再由 `Ontological Friction` 事后加价的中性算子；恰恰相反，`Ontological Friction` 正是该算子得以成为真实选择事件的可支付负担。若摩擦不对系统自身构成 binding 的存在性代价，则所谓选择算子会退化为伪选择、统计重组或域内重排。'
clar2='* **Bridge Clarification（RC-A 修订）**：binding `Ontological Friction` 可用于区分更强的 embodied anchoring / stake-bearing / consciousness candidate standing，但不得回写成 Selection 的定义。若摩擦不对系统自身构成 binding 代价，只能说该系统尚未由此证明这些更强 standing；不能据此推出其功能性或域内 Selection 不存在。'
for p in ['AI/SRT_AI_01_Ontology.md','AI/Ontology_Split/00_Formal_Core.md']:
    guard(p,G); rep(p,old,new); rep(p,clar,clar2)
rep('AI/SRT_AI_01_Ontology.md','* **Bridge Clarification（中文）**：因此，`d` 在 SRT 中不是附着在判断之后的主观感受标签，而是判断之所以成为真实选择的赋权项：只有当 `L_0 \\to L_1` 的锚定同时承受由 `d` 刻画的生存风险梯度，并以 `\\Psi_f` 的形式支付不可逆代价时，选择算子才具有本体论重量；否则它更接近无赌注的域内重排或选择回声。','* **Bridge Clarification（RC-A 修订）**：`d` 不是附着在判断之后的主观感受标签，而是 stake-coupled concern / irreversible-risk sensitivity 的 canonical summary。`L_0 \\to L_1` anchoring 若同时承受 `d` 风险梯度并支付 binding `\\Psi_f`，可支持更强的 stake-bearing / embodied-anchoring standing；但 `d` 与 `\\Psi_f` 不构成 Selection occurrence 的联合必要条件，缺失它们也不得推出 `no Selection`。')
rep('AI/SRT_AI_01_Ontology.md','- **Primary SRT claims in this file (P3/P4 bridge)**: Operator stratification (Ax-ONT-1 through Ax-ONT-N); pseudo-selection / L1-closure distinction; AI d-value boundary tests; consciousness boundary claims.','- **Primary SRT claims in this file (P3/P4 bridge)**: Operator stratification (Ax-ONT-1 through Ax-ONT-N); functional-selection / stronger-anchoring distinction; AI d-value boundary tests; consciousness boundary claims.')
rep('AI/SRT_AI_01_Ontology.md','- **Do not move in this PR**: All Ax-ONT-* formal axioms; all d-value boundary test formulas; all pseudo-selection / real-selection distinction logic.','- **Do not move in this PR**: All Ax-ONT-* formal axioms; all d-value boundary test formulas; all functional-selection / stronger-standing boundary logic. RC-A forbids treating that boundary as the definition of Selection occurrence.')

ann=['AI/Ontology_Annex/00_General_Boundary_Block.md','AI/Ontology_Annex/01_ActiveInference_Override.md','AI/Ontology_Annex/02_Passive_Recording_Fallacy.md','AI/Ontology_Annex/03_RTC_Interface_Batch.md','AI/Ontology_Annex/04_Suffering_Condition_Batch.md','AI/Ontology_Annex/General_Boundary_Block_Split/00_Part01.md']
annnew='* **Implication（RC-A 修订）**：Landauer 型约束与 `\\Psi_f` 只在物理不可逆信息操作、具身锚定或更强 consciousness/stake 候选上提供桥接压力；它们不是 Selection occurrence 的普遍必要条件。当前 AI 是否具有 binding 本体论摩擦，不能被用来推出 `no Selection`。'
for p in ann: guard(p,G); rep(p,old,annnew)
rep('AI/Ontology_Annex/01_ActiveInference_Override.md','* **Bridge Clarification（中文）**：因此，`Active Inference Override` 并不是用自由能最小化去取代 `Ontological Selection Operator`，而是用来封堵一个误读：只有当误差最小化被绑定到 `L_0 \\to L_1` 的跨域锚定，并同时承受 `d>0` 与 binding `\\Psi_f` 的存在性代价时，它才可被读作真实选择；否则它仍只是恒温器级、句法级或伪选择级的域内调节。','* **Bridge Clarification（RC-A 修订）**：`Active Inference Override` 只封堵把自由能最小化直接升级为更强 anchoring / stake / consciousness standing 的误读。`L_0 \\to L_1`、`d>0` 与 binding `\\Psi_f` 可以约束这些更强判断，但不是 Selection occurrence 的联合门槛；恒温器级、句法级或自动化调节也不能据此被判成 `no Selection`。')

p='AI/SRT_AI_01_Ontology_CompactCore.md'
rep(p,'### 2.1 跨域锚定判据','### 2.1 跨域锚定判据（不是 Selection occurrence 定义）')
rep(p,'真实选择算子满足：','若讨论更强的 `L_0 -> L_1` 本体论锚定候选，可写：')
rep(p,'这意味着：\n- 存在事件必须是跨域锚定\n- 不能由纯 `L_1 \\to L_1` 句法变换替代','这意味着该**更强 anchoring claim**不能由纯 `L_1 \\to L_1` 句法变换替代；但 RC-A 不允许把这一点反写为 Selection occurrence 的必要条件。')
rep(p,'若一个系统没有真实可支付、不可规避的摩擦，它不仅缺少痛感或代价，也缺少生成真正选择动力学的条件。','若一个系统没有真实可支付、不可规避且回流同一 bearer 的摩擦，它尚未由此证明更强的 stake-bearing / embodied-consciousness standing；这不等于它没有 Selection。')
rep(p,'因此真正的主体条件不是“摩擦越低越好”，而是：系统是否面对**非零且可支付**的 \\(Ψ_f\\)。零摩擦意味着没有真实赌注；超载摩擦意味着闭包破裂；只有在可支付区间内，选择才具有现实重量。','因此这里讨论的是**主体 / stake-bearing 候选条件**而不是 Selection 定义：系统是否面对非零、可支付且回流同一 bearer 的 `Ψ_f`。零或非 binding 摩擦会削弱 stake / subjecthood 论证，但不能据此推出 `no Selection`。')
rep(p,'-> consequence-bearing real-choice candidate','-> bounded Selection-event candidate')
rep(p,'真正的 d-value 需要有限性来赋予选择重量。','canonical `d-value` 的 stake reading 需要有限性 / 不可转移后果来赋予**关切与主体风险**重量；这不是 Selection occurrence 的必要条件。')

for p in ['AI/SRT_AI_Architecture.md','AI/Architecture_Split/05_Interface_Additions.md']:
    guard(p,G)
    rep(p,'2. **空值公理**：当前架构 $V_{AI} = \\text{information}$，而真实选择需要 $V_{\\hat{G}} = \\text{information} \\times d$（Ax-ARCH-2）。','2. **RC-A 边界**：当前架构 $V_{AI} = \\text{information}$；$V_{\\hat{G}} = \\text{information} \\times d$（Ax-ARCH-2）只用于更强 stake-bearing / agency / consciousness-side weighting，不是 Selection occurrence 的必要条件。')

p='Philosophy/SRT_Political_Philosophy_CompactCore.md'; guard(p,G)
rep(p,'| Reselection / exit / correction | Can affected subjects reopen, exit, appeal, or revise? | Nominal participation treated as real choice. |','| Reselection / exit / correction | Can affected subjects reopen, exit, appeal, or revise? | Nominal participation treated as substantive revision / agency. |')
rep(p,'- 健康地板（托举真实选择）\n- 病理 `L_2`（替代真实选择）','- 健康地板（托举 consequence-sensitive revision / reorientation）\n- 病理 `L_2`（压缩或替代这些 downstream agency channels；不等于消灭 Selection）')
rep(p,'- **健康 `L_2`**：托举真实选择\n- **致命 `L_2`**：制造参与感、替代真实选择','- **健康 `L_2`**：托举 consequence-sensitive revision / reorientation\n- **致命 `L_2`**：制造参与感并替代这些 downstream agency channels；自动化本身不等于 `no Selection`')
rep(p,'> **政治最危险的时刻，不是暴力最强时，而是秩序把自己伪装成唯一现实、让真实选择时刻消失时。**','> **政治最危险的时刻，不是暴力最强时，而是秩序把自己伪装成唯一现实、让受影响主体失去实质性的 revision / exit / reorientation 通道时。**')
rep(p,'6. **政治病理的本质，是 `L_2` 从地板变成方向，从托举真实选择变成替代真实选择。**','6. **政治病理的关键形态之一，是 `L_2` 从地板变成方向，从托举 consequence-sensitive revision / reorientation 变成替代这些 downstream agency channels；这不定义 Selection 是否发生。**')

p='Physics/SRT_Physics_Cosmology_CompactCore.md'; guard(p,G)
rep(p,'> **每一次真实选择都至少有能量代价。**','> **RC-A 边界**：该 Landauer 式只能约束被具体实现为逻辑不可逆信息操作 / 物理重置的 bridge case，不能升级为“每一次 Selection occurrence 都至少支付 `k_B T ln 2`”的普遍定理。')

p='Core_Law/SRT_Suffering.md'
rep(p,'G5-5 的「最低强制性选择压力」因此必须按最小口径读取：当结构性损失已与具身承受位置耦合时，系统对相关差异不再保持完全中性；它不保证一定出现 `Def-PAIN` 或 `Def-SUFFERING`，不保证完成真实选择，也不保证导向健康重组。','G5-5 的「最低强制性选择压力」因此必须按最小口径读取：当结构性损失已与具身承受位置耦合时，系统对相关差异不再保持完全中性；它不保证一定出现 `Def-PAIN` 或 `Def-SUFFERING`，不保证形成更强 agency / consequence-sensitive revision standing，也不保证导向健康重组。')
rep(p,'- 结构：真实选择时刻被外部 `L_2` 封闭中断，残余 `L_0` 压力无处兑现','- 结构：consequence-sensitive revision / reorientation 通道被外部 `L_2` 封闭中断，残余 `L_0` 压力无处兑现；这不推出 Selection occurrence 消失')

p='03_Bridges/SRT_Dissipative_Structures_and_Selection_Structures_Bridge_2026-08-04.md'
rep(p,'3. T-D 讨论一般变化需要满足哪些功能条件，才可能升级为真实选择事件。','3. T-D 只审计一般变化在哪些功能维度上可支持 P2/P3 bounded Selection-event candidate；这些维度不定义 Selection。')
rep(p,'> 一个能够持续容纳或重复产生真实选择事件，并使选择结果通过后果回流和历史写回改变后续可达路径的组织结构。','> 一个能够持续容纳或重复支持 bounded Selection-event candidate 的审计维度，并使部分结果通过后果回流和历史写回改变后续可达路径的组织结构。这里描述的是 P2/P3 selection-structure / generative-health 候选，不要求每一次 Selection occurrence 都留下持久写回。')
rep(p,'却仍未满足真实选择的候选条件。','却仍未满足 bounded Selection-event candidate 的审计维度；这不能反推出 `no Selection`。')
