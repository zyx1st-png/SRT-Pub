---
id: SRT-OPS-PHYSICS-P0B-EXACT-INVENTORY-HANDOFF-2026-04-29
type: handoff_record
tags: [Operations, Physics, Inventory, Frontmatter, Codex-Handoff, Guardrail]
status: active_handoff_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/Archive_Records/Physics_P0_Inventory_Frontmatter_Audit.md
  - Operations/Archive_Records/Physics_Split_Annex_PreAudit_2026-04-29.md
  - Physics/README.md
  - Physics/SRT_Physics_Claim_Status.md
  - Physics/PHYSICS_COMPACT_REGISTRY.md
machine_summary: >
  Handoff record for the PR-P0b exact Physics inventory. The connector session cannot guarantee
  exact local line counts for every Physics markdown file. This file provides a local/Codex script,
  output schema, safety constraints, and a commit/PR template for exact inventory execution.
---

# PR-P0b Physics Exact Inventory Handoff

**Date**: 2026-04-29  
**Mode**: handoff / local exact inventory  
**Canonical impact**: none

---

## 0. Why this handoff exists

`Operations/Archive_Records/Physics_P0_Inventory_Frontmatter_Audit.md` identified the need for exact line counts and frontmatter verification across `Physics/*.md`.

The current GitHub connector session can fetch individual files but does not expose a reliable local directory traversal / line-count execution context for the repository. To avoid false precision, this handoff records the exact local/Codex command that should be run from the repository root.

---

## 1. Safety Record

This handoff pass did **not** execute extraction.

- No Physics source body text moved.
- No Physics source body text rewritten.
- No formulas changed.
- No `Physics_Annex/` directory created.
- No collapse / MWI / gravity / discrete-time / constants / QBox / cosmology claims promoted.
- No Core / Core_Law / AI / Neuroscience / Philosophy / Public / Papers / graphify-out files touched.

---

## 2. Required local exact inventory script

Run from repo root:

```bash
python3 - <<'PY'
from pathlib import Path
import re

rows = []
for p in sorted(Path('Physics').glob('*.md')):
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    fm = text.startswith('---')
    claim_mode = re.search(r'^claim_mode:\s*(.*)$', text, re.M)
    epistemic = re.search(r'^epistemic_layer:\s*(.*)$', text, re.M)
    canonical = re.search(r'^canonical:\s*(.*)$', text, re.M)
    status = re.search(r'^status:\s*(.*)$', text, re.M)
    layer = re.search(r'^layer:\s*(.*)$', text, re.M)
    ftype = re.search(r'^type:\s*(.*)$', text, re.M)
    has_claim_status = 'SRT_Physics_Claim_Status.md' in text
    has_readme = 'Physics/README.md' in text or '](' in text and 'README.md' in text
    high_risk_hits = []
    patterns = {
        'collapse': r'collapse|Collapse|坍缩|测量即选择|Measurement as Selection',
        'mwi': r'MWI|Everett|Many-Worlds|多世界',
        'discrete_time': r'Discrete Time|离散时间|Planck time|普朗克',
        'gravity_psif': r'gravity|Gravity|引力|G_\{\\mu\\nu\}|Psi_f|\\Psi_f',
        'constants': r'Planck|hbar|\\hbar|Boltzmann|fine structure|常数|alpha|\\alpha',
        'qbox_post_quantum': r'QBox|hyperdecoherence|post-quantum|后量子',
        'cosmology': r'cosmology|Cosmology|宇宙|multiverse|anthropic|人择',
    }
    for name, pat in patterns.items():
        if re.search(pat, text, re.I):
            high_risk_hits.append(name)
    rows.append({
        'file': str(p),
        'lines': len(lines),
        'frontmatter': fm,
        'type': ftype.group(1).strip() if ftype else 'MISSING',
        'status': status.group(1).strip() if status else 'MISSING',
        'layer': layer.group(1).strip() if layer else 'MISSING',
        'epistemic_layer': epistemic.group(1).strip() if epistemic else 'MISSING',
        'claim_mode': claim_mode.group(1).strip() if claim_mode else 'MISSING',
        'canonical': canonical.group(1).strip() if canonical else 'MISSING',
        'claim_status_ptr': has_claim_status,
        'readme_ptr': has_readme,
        'risk_hits': ','.join(high_risk_hits) if high_risk_hits else 'none',
    })

print('| File | Lines | Frontmatter | type | status | layer | epistemic_layer | claim_mode | canonical | Claim-status ptr | README ptr | Risk hits |')
print('|---|---:|---:|---|---|---|---|---|---|---:|---:|---|')
for r in rows:
    print(f"| `{r['file']}` | {r['lines']} | {r['frontmatter']} | {r['type']} | {r['status']} | {r['layer']} | {r['epistemic_layer']} | {r['claim_mode']} | {r['canonical']} | {r['claim_status_ptr']} | {r['readme_ptr']} | {r['risk_hits']} |")

print('\n## Missing pointer summary')
for r in rows:
    missing = []
    if not r['claim_status_ptr'] and not r['file'].endswith('SRT_Physics_Claim_Status.md'):
        missing.append('claim-status')
    if not r['readme_ptr'] and not r['file'].endswith('README.md'):
        missing.append('README')
    if r['canonical'] == 'MISSING':
        missing.append('canonical flag')
    if r['claim_mode'] == 'MISSING':
        missing.append('claim_mode')
    if missing:
        print(f"- `{r['file']}`: missing {', '.join(missing)}")
PY
```

---

## 3. Required output file

Create:

```text
Operations/Archive_Records/Physics_P0b_Exact_Inventory_Report.md
```

The report must contain:

1. The full table produced by the script.
2. A missing-pointer summary.
3. A high-risk-hit summary by category.
4. A safety confirmation that no Physics source text was edited.
5. A recommended PR-P1 adjudication queue.

---

## 4. Allowed actions for PR-P0b

- Run the exact inventory script.
- Add `Operations/Archive_Records/Physics_P0b_Exact_Inventory_Report.md`.
- Optionally update `Operations/Archive_Records/Physics_P0_Inventory_Frontmatter_Audit.md` to point to the exact report.
- Optionally update `Physics/README.md` and `PHYSICS_COMPACT_REGISTRY.md` with one-line pointers to the exact report.

---

## 5. Forbidden actions for PR-P0b

- Do not edit Physics source body sections.
- Do not move sections between files.
- Do not change formulas.
- Do not create `Physics_Annex/`.
- Do not rewrite collapse / MWI / gravity / discrete-time / constants / QBox / cosmology claims.
- Do not edit Core / Core_Law / AI / Neuroscience / Philosophy / Public / Papers / graphify-out.
- Do not promote any physics claim status.

---

## 6. Codex prompt for PR-P0b

```text
You are working in SRT-Pub. Complete PR-P0b: exact Physics inventory and frontmatter audit.

Read:
- Operations/Archive_Records/Physics_P0_Inventory_Frontmatter_Audit.md
- Operations/Archive_Records/Physics_P0b_Exact_Inventory_Handoff.md
- Physics/README.md
- Physics/SRT_Physics_Claim_Status.md

Task:
1. Run the exact inventory Python script from Operations/Archive_Records/Physics_P0b_Exact_Inventory_Handoff.md.
2. Create Operations/Archive_Records/Physics_P0b_Exact_Inventory_Report.md with the exact table, missing-pointer summary, high-risk-hit summary, and safety record.
3. Do not edit Physics source body text.
4. Do not move sections.
5. Do not change formulas.
6. Do not create Physics_Annex/.
7. Do not touch Core/, Core_Law/, AI/, Neuroscience/, Philosophy/, Public/, Papers/, or graphify-out/.

Optional, only if simple:
- Add a one-line pointer in Operations/Archive_Records/Physics_P0_Inventory_Frontmatter_Audit.md to the exact report.
- Add a one-line pointer in Physics/README.md to the exact report.

Commit message:
"Audit Physics exact inventory and frontmatter"
Open a draft PR. Do not merge automatically.
```

---

## 7. Bottom line

This handoff intentionally avoids false precision. The next exact inventory must be run in a local/Codex environment with repository file access, then recorded in `Operations/Archive_Records/Physics_P0b_Exact_Inventory_Report.md`.
