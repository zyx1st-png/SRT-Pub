---
id: SRT-BOOK-STYLE-PATCH-2026-06-14-FRONTAL-REBUTTAL-PHRASE
type: style_patch
status: pending_manual_apply
created: 2026-06-14
scope:
  - 01_Source_Intuition/BOOK/Drafts_26Q/Q03_前对象场.md
  - 01_Source_Intuition/BOOK/Drafts_26Q/Q11_被选择.md
  - 01_Source_Intuition/BOOK/Drafts_26Q/Q15_关切维度.md
keep_unchanged:
  - 01_Source_Intuition/BOOK/Drafts_26Q/Q07_锚定.md
purpose: 全书反对者段落去模板化，减少“必须正面接住”句式重复
---

# 句式降重补丁：“必须正面接住”

本补丁用于后续手动替换 Drafts_26Q 正文中的重复防守句式。

原则：**Q07 保留一处“必须正面接住”**，因为 Q07 §4 是“锚定 vs 因果影响力”的正面战场；其他章节改成更贴合语境的表达，降低模板感。

---

## 替换清单

| 文件 | 原句 | 替换为 |
|---|---|---|
| `01_Source_Intuition/BOOK/Drafts_26Q/Q03_前对象场.md` | `这个追问必须正面接住。` | `这个追问不能绕开。` |
| `01_Source_Intuition/BOOK/Drafts_26Q/Q11_被选择.md` | `这个反驳必须正面接住，因为它的错法恰恰揭示了旧地板的隐藏假设。` | `这个反驳不能轻轻带过，因为它的错法恰恰揭示了旧地板的隐藏假设。` |
| `01_Source_Intuition/BOOK/Drafts_26Q/Q11_被选择.md` | `第二步必须正面接住这个无限倒退。` | `真正的难点在第二步：这个无限倒退不能靠一句“仍有选择”打发。` |
| `01_Source_Intuition/BOOK/Drafts_26Q/Q15_关切维度.md` | `这个反驳切中了一个真实的结构对应，必须正面接住。` | `这个反驳切中了一个真实的结构对应，不能否认；但也不能让它把关切多样性吞掉。` |

---

## 一键替换脚本

在 repo 根目录运行：

```python
from pathlib import Path

repls = {
    "01_Source_Intuition/BOOK/Drafts_26Q/Q03_前对象场.md": {
        "这个追问必须正面接住。": "这个追问不能绕开。",
    },
    "01_Source_Intuition/BOOK/Drafts_26Q/Q11_被选择.md": {
        "这个反驳必须正面接住，因为它的错法恰恰揭示了旧地板的隐藏假设。": "这个反驳不能轻轻带过，因为它的错法恰恰揭示了旧地板的隐藏假设。",
        "第二步必须正面接住这个无限倒退。": "真正的难点在第二步：这个无限倒退不能靠一句“仍有选择”打发。",
    },
    "01_Source_Intuition/BOOK/Drafts_26Q/Q15_关切维度.md": {
        "这个反驳切中了一个真实的结构对应，必须正面接住。": "这个反驳切中了一个真实的结构对应，不能否认；但也不能让它把关切多样性吞掉。",
    },
}

for file, mapping in repls.items():
    p = Path(file)
    text = p.read_text(encoding="utf-8")
    for old, new in mapping.items():
        if old not in text:
            raise RuntimeError(f"not found in {file}: {old}")
        text = text.replace(old, new, 1)
    p.write_text(text, encoding="utf-8")

print("done")
```

---

## 验证命令

替换后，在 repo 根目录运行：

```bash
grep -R "必须正面接住\|正面接住" 01_Source_Intuition/BOOK/Drafts_26Q --include="*.md"
```

预期：Drafts_26Q 正文中只剩 Q07 §4 的一处保留用法。

---

## 保留理由

Q07 §4 原句：

> 这个反驳必须正面接住，因为如果锚定只是因果影响力的同义词，这一章就什么都没做。

保留原因：Q07 的核心反驳就是“锚定是不是因果影响力”，这里需要一次强防守句。其他章节的同类句式改掉，可以让 Q07 的保留更有分量。
