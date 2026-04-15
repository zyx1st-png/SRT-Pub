---
id: SRT-CORE-TEXT-ADJUDICATION-2026-04
type: governance
tags: [Governance, CoreText, Adjudication, Audit]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: evidence
dependency: [SRT-L0-METAPHYSICS, SRT-LAYER-GUARD, SRT-L1-INTERFACE-SPEC]
created: 2026-04-01
---

# SRT 主文本裁决备忘（2026-04-01）

> 用途：为中文主论证入口的裁决提供一次不改 canonical 地位的预审，并记录入口层同步后的剩余阻塞项。
> 本文件记录角色分工、Euclid 版负担标注核查结果、入口层同步进度，以及正式升格前的阻塞项。

---

## 1. 审计对象与当前角色

| 文件 | 当前事实角色 | 当前问题 |
|------|-------------|---------|
| `Core_Law/SRT_Core_Text_CN.md` | 旧版中文自足主论证文 | 已降位为历史主文 / 读者入口；当前剩余问题是不在 registry 层形成独立、稳定的角色说明 |
| `Core_Law/SRT_Core_Text_CN_Euclid.md` | 候选中文 canonical 主论证文 | `status: draft_v1`；已补齐 L1 依赖，但仍未进入 registry / canonical 入口 |
| `Core_Law/SRT_Selection_Argument.md` | L1 哲学辩护文 / 展开论证文 | 角色说明与 `status` 已收紧；当前剩余问题是 `claim_mode: canonical` 仍偏强，但受现有枚举约束 |

---

## 2. Euclid 版负担标注核查

### 2.1 已覆盖的负担链

Euclid 版当前已经把主论证链的核心负担显式写出：

- `A1`
- `O1`
- `D1-D8`
- `S1-S8`
- `C1-C3`
- `H1-H2`
- `E1-E5`

就“主链是否只标到前半段”这一点，当前结论是：**不是**。  
其主论证、条件命题、趋势命题与解释性回读已经覆盖到全文骨架，而不是只覆盖起点与前几步。

### 2.2 当前未单独挂负担标签的部分

以下部分属于元层整理，而不是新的未标注证明步骤：

- `## 4. 到这一步，本文究竟建立了什么`
- `## 6. 本文明确不主张什么`
- `## 7. 开放问题`
- `## 8. 给读者的审查清单`

因此，当前 Euclid 版的主要阻塞**不是负担标签缺失**，而是**治理流程尚未闭合**。

---

## 3. Layer Guard 预审结果

按 `Governance/SRT_Layer_Guard.md` 的五问做最小预审：

1. **是否依赖某个科学理论的正确性？**
   - 主链本身不依赖具体科学文献或外部框架。
2. **能否被实验证伪？**
   - 作为中文主论证文，其核心角色不是 L2 预测，而是 L1 自足论证。
3. **是在解释 L0，还是为 L0 提供证据？**
   - 主要是在解释、展开、整理 L0，不是在用外部证据反向证明 L0。
4. **是否加了引用 / 公式？**
   - 当前无引用、无形式符号；这有利于保持其作为自足论证文的清洁度。
5. **若其局部失败，是否会直接改写 L0？**
   - 不应直接改写。它应被理解为 L0 的一份 L1 主论证表达，而不是 L0 本身。

预审结论：**Euclid 版作为 `(L1, os)` 主论证候选是合格的。**

---

## 4. 入口层同步后的剩余阻塞项

### B1. Euclid 版尚未进入 registry / canonical 入口

当前入口层文案已经把 Euclid 版写成“中文主论证候选”，  
但它仍然保持 `draft_v1`，且尚未进入 manifest / registry / canonical 入口的正式裁决。

### B2. `Selection_Argument.md` 的 claim_mode 仍偏强

该文件的正文定位和 `status` 已收紧，  
但在现有治理枚举下，它仍保留 `claim_mode: canonical`，这与“哲学辩护文”的真实角色并不完全等价。

### B3. 当前 claim_mode 枚举没有 `argument`

仓库当前允许的 `claim_mode` 是：

- `canonical`
- `translation`
- `hypothesis`
- `evidence`

因此，对 `Selection_Argument.md` 的重定位不能直接写成 `claim_mode: argument`，除非先更新治理规范。  
这意味着它的元数据修正需要二选一：

1. 先扩展治理枚举；
2. 或在不扩枚举的前提下，用 `type: argument` + 更精确的 blockquote/状态语句完成降负担。

---

## 5. 最小裁决顺序

建议按下面顺序执行，而不是直接改 Euclid 为 canonical：

1. **先完成本文件对应的人工裁决**
   - 明确三文件的角色分工；
   - 明确旧主文的降位文案；
   - 明确 `Selection_Argument.md` 的元数据处理规则。

2. **修 Euclid 版为“可升格候选”**
   - 补齐与 L1 规范一致的 `dependency`；
   - 保持 `status: draft_v1`，直到入口裁决完成。

3. **处理旧主文**
   - 给 `Core_Text_CN.md` 补 frontmatter；
   - 去掉“默认核心文本”的唯一化表述；
   - 改成“历史版 / 原版自足论证 / 读者版”之一。

4. **处理 `Selection_Argument.md`**
   - 先决定是否扩展 `claim_mode` 枚举；
   - 若不扩枚举，至少先把正文定位写清为“哲学辩护文”，避免继续被误读成主入口。

5. **最后才改 registry / canonical 入口**
   - 决定是否将 Euclid 版正式接入 registry / manifest / canonical 入口；
   - 再决定是否升为 `canonical_v1`。

---

## 6. 当前结论

当前结论不是“Euclid 版还不够好”，而是：

- **Euclid 版已经足够像主论证文本**
- **文本角色裁决与入口层同步已经完成**
- **但它还没有完成进入 registry / canonical 入口所需的最后治理闭环**

因此，下一步最合理的动作不是继续扩写三份文本中的任何一份，  
而是完成**Euclid 是否正式入 canonical 入口**的最后裁决。
