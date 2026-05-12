---
id: SRT-BOOK-PART02-STABLE-REPLACEMENT-PATCH-0811
type: codex_ready_patch_instruction
part: 02_nature_of_selection
status: draft_v1_codex_ready
based_on:
  - 01_Source_Intuition/BOOK/Versioned_Drafts/Part_02_选择的本性/00_卷二冻结执行状态审计_v2.md
  - 01_Source_Intuition/BOOK/Versioned_Drafts/Part_02_选择的本性/08_选择算子_从可成为性到显现_v5r_terrain_embodiment_focus_pass.md
  - 01_Source_Intuition/BOOK/Versioned_Drafts/Part_02_选择的本性/09_排除_选择的阴影_v5w_shadow_return_alignment_pass.md
  - 01_Source_Intuition/BOOK/Versioned_Drafts/Part_02_选择的本性/11_本体论摩擦_为什么现实不会免费成形_v13_bridge_boundary_shadow_alignment_pass.md
purpose:
  - codex_or_human_safe_full_file_replacement
  - avoid_truncated_chat_copy_risk
  - synchronize_part02_stable_maintexts
---

# 卷二 08 / 09 / 11 稳定主稿替换补丁说明 v1

> 本文件是 Codex / 人工执行用补丁说明。请勿按片段拼接。所有替换均应执行“全文替换”：用源候选文件的完整内容覆盖目标稳定主稿路径。

---

## 0. 执行目标

将卷二中枢三章同步到最新冻结候选：

```text
08 → v5r terrain / embodiment focus pass
09 → v5w shadow-return alignment pass
11 → v13 bridge-boundary shadow alignment pass
```

这些替换完成后，卷二稳定主稿将与当前推荐冻结状态一致。

---

## 1. 替换任务一：第 8 章

### 目标稳定主稿

```text
01_Source_Intuition/BOOK/Part_02_选择的本性/08_选择算子_从可成为性到显现.md
```

### 源候选稿

```text
01_Source_Intuition/BOOK/Versioned_Drafts/Part_02_选择的本性/08_选择算子_从可成为性到显现_v5r_terrain_embodiment_focus_pass.md
```

### 执行方式

全文替换目标主稿内容为源候选稿完整内容。

不要局部合并。

不要只复制 frontmatter。

不要只复制正文。

### 替换理由

v5r 解决第 4 章与第 8 章的重影问题，将第 8 章从“选择不是挑选”的抽象定义复述，转向“选择算子如何在地形中具体成形”。

v5r 主轴：

```text
接触窗口
→ 分辨率
→ 关切耦合
→ 承载条件
→ 时间窗口
→ 候选竞争
→ 前景显现
→ 旁路受压
→ 历史写回
```

替换后第 8 章应承担卷二中枢功能：

```text
第 7 章：选项不是起点，地形进入选择之前
第 8 章：地形中，可成为性如何被压成显现
第 9 章：显现形成后，被压低者成为阴影
```

### 替换后校验

- frontmatter `status` 应为 `draft_v5r_terrain_embodiment_focus_pass`；
- 章首引文应为：

```text
第四章说明选择做什么：排除、定形、写入。第八章说明这件事如何在地形中发生：可成为性怎样穿过身体、关切、代价、时间窗口和承接条件，获得现实厚度。
```

- 章末应自然推出第 9 章阴影问题；
- 不应残留 `draft_v5q_final_compression_pass`。

---

## 2. 替换任务二：第 9 章

### 目标稳定主稿

```text
01_Source_Intuition/BOOK/Part_02_选择的本性/09_排除_选择的阴影.md
```

### 源候选稿

```text
01_Source_Intuition/BOOK/Versioned_Drafts/Part_02_选择的本性/09_排除_选择的阴影_v5w_shadow_return_alignment_pass.md
```

### 执行方式

全文替换目标主稿内容为源候选稿完整内容。

不要局部合并。

### 替换理由

v5w 将“阴影”从未显现残余，推进为后续地形中的效力分布与回流压力，直接承接：

```text
第 8 章：旁路受压
第 9 章：阴影作为效力分布与回流压力
第 10 章：前景与阴影共同造成不可逆
第 11 章：阴影回流成为修复摩擦
第 13 章：代价外包成为可协调问题
```

### 替换后校验

- frontmatter `status` 应为 `draft_v5w_shadow_return_alignment_pass`；
- 章首引文应为：

```text
前景获得厚度时，未被打开的未来不会归零。它们退入后续地形，成为摩擦、阈值、残差、回流压力和修复成本的分布。
```

- 正文应包含 `从阴影到修复摩擦` 与 `从阴影到代价外包` 两节；
- 章末应自然推出第 10 章不可逆性；
- 不应残留 `draft_v5v_cross_scale_tempered_pass`。

---

## 3. 替换任务三：第 11 章

### 目标稳定主稿

```text
01_Source_Intuition/BOOK/Part_02_选择的本性/11_本体论摩擦_为什么现实不会免费成形.md
```

### 源候选稿

```text
01_Source_Intuition/BOOK/Versioned_Drafts/Part_02_选择的本性/11_本体论摩擦_为什么现实不会免费成形_v13_bridge_boundary_shadow_alignment_pass.md
```

### 执行方式

全文替换目标主稿内容为源候选稿完整内容。

不要局部合并。

### 替换理由

v13 控制科学材料的显影剂边界，防止 Landauer / Sagawa–Ueda / Crooks 公式喧宾夺主；同时将第 9 章阴影回流明确接到第 11 章修复摩擦，并自然推出第 12 章可支付性。

v13 主轴：

```text
显现获得现实厚度
→ 阴影回流要求修复
→ 零摩擦等于没有真正成形
→ 科学材料只是显影剂
→ 四种支付：形成、维持、切换、修复
→ 感受摩擦 vs 实际摩擦
→ 可支付性入口
```

### 替换后校验

- frontmatter `status` 应为 `draft_v13_bridge_boundary_shadow_alignment_pass`；
- 章首引文应为：

```text
选择算子让一个方向进入前景；阴影让未进入者继续有效；不可逆说明世界不能回到原点。本体论摩擦说明：在已经改变的地形上重新成形，必须有人、某个系统或某个层级为现实厚度承重。
```

- 正文应包含 `科学材料的边界：显影剂，不是证明`；
- 正文应包含 `从本体论摩擦到可支付性`；
- 不应残留 `draft_v12_philosophical_synthesis_pass`。

---

## 4. 执行后统一校验

替换三章后，执行以下检查：

```text
07 status = draft_v18_final_literary_philosophical_polish
08 status = draft_v5r_terrain_embodiment_focus_pass
09 status = draft_v5w_shadow_return_alignment_pass
10 status = draft_v14_review_polish_pass
11 status = draft_v13_bridge_boundary_shadow_alignment_pass
12 status = draft_v16_final_prose_pass
13 status = draft_v8_final_prose_tension_pass
```

并检查卷二机制链：

```text
07 地形进入选择之前
08 选择算子在地形中压出显现
09 显现制造阴影，阴影回流改变地形
10 前景与阴影共同造成不可逆
11 不可逆使现实不能免费成形
12 摩擦必须支付，支付沉积为路径
13 路径健康需要三判据，主体与价值被推出
```

---

## 5. 建议 commit message

```text
Freeze Part II stable chapters 08 09 11 to latest candidates
```

或分章提交：

```text
Freeze chapter 08 to terrain embodiment focus pass
Freeze chapter 09 to shadow return alignment pass
Freeze chapter 11 to bridge boundary shadow alignment pass
```

---

## 6. 注意事项

不要通过聊天截断内容复制替换。

不要使用不完整 fetch 输出覆盖主稿。

不要合并 v5q / v5r、v5v / v5w、v12 / v13。

本次替换应为全文替换，保持候选稿完整性。
