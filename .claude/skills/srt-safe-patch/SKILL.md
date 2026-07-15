---
name: srt-safe-patch
description: 大文件安全打补丁工作流——对大到无法整文件安全替换的 SRT 文件，只做最小定向编辑（加护栏指针、局部注记、guardrail note），不重写整文件。这段指令你过去在 Operations/Codex_Prompts/ 里反复手写、还存了根级 fallback 副本，本 skill 把它固化。适用时机：要给某个长文件加 PH-SS 护栏指针/公式角色注记/claim 边界注、要在 Philosophy/Physics/AI 大文件里插入交叉链接或安全读法、或任何"改一个大文件但只想局部加东西"的任务。绝不重写整文件、绝不删除或重排既有长段、绝不把 companion 提升为 canonical、绝不改 P0/P1 定义或动数学（除了加角色/护栏注记）。新建文件、材料融入、接口抽取的主体动作不走本 skill（抽取的落地补丁可配合本 skill 的纪律）。
argument-hint: "[目标文件 | 要加的护栏/注记类型]"
---

# 大文件安全打补丁工作流（触发器）

先例与完整提示词：`Operations/Codex_Prompts/CODEX_PROMPT_Philosophy_Long_File_PH_SS_Direct_Pointers.md`
（及其根级 fallback 副本）。本 skill 把那段被反复手写的指令固化成可复用触发层；
具体要插入哪些护栏文字，按目标文件对应的 guardrails 主文档取。

## 什么时候用

文件大到"远程整文件替换不安全"，但你只想**局部**加东西：护栏指针、公式角色注记、
claim 边界注、交叉链接、安全读法块。**不是**要改它的论证或定义。

## 固定流程

### 1. 先验证 repo 与 branch（不跳过）

```bash
git remote -v
git branch --show-current
git rev-parse HEAD
```

确认在 `zyx1st-png/SRT-Pub` 且在预期分支。不符就停下报告，不硬改。

### 2. 先读上下文，再动手

读目标文件对应的 guardrails / index / execution-plan 主文档（缺哪个报告哪个，用可见的继续）。
明确：要插的护栏文字**从哪份 canonical/guardrail 文档取**，不自造措辞。

### 3. 只做最小定向编辑

- 在 frontmatter 与既有 canonical 交叉链接块**之后**插入短块（护栏指针 / 交叉链接 / 安全读法）。
- 在有风险的 claim / 公式**标题或公式正下方**加短注（不替换原 claim）。
- 若文件已有类似护栏，**合并措辞、不重复**。
- 用 append/insert 式最小编辑，逐处定位唯一锚点。

### 4. 编辑后自查

```bash
git diff -- <目标目录>
```

确认只做了定向插入/注记，没有整文件重写、没有删段、没有重排。

### 5. 按固定模板报告

```
Patched files:
- ...
Skipped files:
- ... 及原因
Key inserted guardrails:
- ...
No full-file rewrites performed: yes/no
Potential follow-up:
- ...
```

## 硬红线（安全规则）

1. **不重写整文件。**
2. **不删除既有内容**，不重排既有长段。
3. **不把 companion / annex / bridge 升格为 canonical 定义。**
4. **不改 P0/P1 定义**，不改数学——除了添加公式角色 / 护栏注记。
5. **不把 bridge claim 转成 canonical claim。**
6. 所有新增保持**短、可见、易 grep**。
7. 缺失的目标文件跳过并报告，**不为缺失目标新建替换文件**。
8. 只在真的插入了内容后，才在 TODO/状态里标记"已完成"，不谎报。
