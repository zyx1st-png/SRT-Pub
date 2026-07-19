---
id: SRT-OPS-PHYSICS-P1B-FRONTMATTER-CANONICAL-CLAIMMODE-HANDOFF-2026-04-29
type: handoff_record
tags: [Operations, Physics, Frontmatter, Canonical-Flag, Claim-Mode, Codex-Handoff]
status: active_handoff_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/Archive_Records/Physics_P0b_Exact_Inventory_Report.md
  - Operations/Archive_Records/Physics_P1a_Minimal_Frontmatter_Record.md
  - Physics/README.md
  - Physics/SRT_Physics_Claim_Status.md
machine_summary: >
  Handoff for PR-P1B Physics frontmatter-only normalization. Adds explicit canonical flags
  and adjudicates invalid claim_mode: canonical usage using a local script. No body text or formulas should be touched.
---

# PR-P1B Physics Frontmatter Canonical / Claim-Mode Handoff

**Date**: 2026-04-29  
**Mode**: frontmatter-only handoff  
**Canonical impact**: none

---

## 0. Why this handoff exists

`Operations/Archive_Records/Physics_P0b_Exact_Inventory_Report.md` found:

- 25 total Physics markdown files.
- 4 files had no frontmatter; fixed in PR-P1A.
- 21 files had frontmatter but no explicit `canonical:` flag.
- Many files used `claim_mode: canonical`, even though `canonical` should be a separate boolean-like field, not a claim_mode value.

This PR-P1B should be done with a local/Codex script to avoid full-file manual rewrites through the connector.

---

## 1. Safety Record

This handoff does **not** modify Physics source files.

Allowed future PR-P1B changes:

- Edit only YAML frontmatter blocks in `Physics/*.md`.
- Add missing `canonical:` flags.
- Replace invalid `claim_mode: canonical` with a safer frontmatter value.
- Add an Operations record.

Forbidden:

- Do not edit body text outside YAML frontmatter.
- Do not move sections.
- Do not change formulas.
- Do not create `Physics_Annex/`.
- Do not promote collapse / MWI / gravity / discrete-time / constants / QBox / cosmology claims.
- Do not edit Core / Core_Law / AI / Neuroscience / Philosophy / Public / Papers / graphify-out.

---

## 2. File classification for PR-P1B

### A. Registry / navigation surfaces

Set:

```yaml
canonical: false
claim_mode: navigation
```

Files:

- `Physics/PHYSICS_COMPACT_REGISTRY.md`

### B. External review / audit-like material

Set:

```yaml
canonical: false
claim_mode: audit
```

Files:

- `Physics/SRT_AT_Physics_of_Causation_Processing_2026-03-02.md`

### C. Main physics bridge

Set:

```yaml
canonical: false
claim_mode: translation
```

Files:

- `Physics/_SRT_Phys_Bridge.md`

### D. CompactCore files

Set:

```yaml
canonical: false
claim_mode: translation
```

Files:

- `Physics/SRT_Quant_00_Intro_CompactCore.md`
- `Physics/SRT_Quant_01_Selection_CompactCore.md`
- `Physics/SRT_Quant_02_Cosmology_CompactCore.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md`
- `Physics/SRT_Phys_10_Integration_CompactCore.md`
- `Physics/SRT_Phys_07_Complex_Systems_CompactCore.md`
- `Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md`

### E. Longform physics files

Set:

```yaml
canonical: false
claim_mode: translation
```

Files:

- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/SRT_Quant_02_Cosmology.md`
- `Physics/SRT_Physics_Cosmology.md`
- `Physics/SRT_Phys_09_Formalism_Ext.md`
- `Physics/SRT_Phys_10_Integration.md`
- `Physics/SRT_Phys_07_Complex_Systems.md`
- `Physics/SRT_Phys_08_Ontology_Ext.md`

### F. Already normalized / do not alter unless verification says needed

- `Physics/README.md` already has `claim_mode: navigation`, `canonical: false`.
- `Physics/SRT_Physics_Claim_Status.md` already has `claim_mode: audit`, `canonical: false`.
- Four PR-P1A files already have `canonical: false` and safe claim_mode values.

---

## 3. Required local/Codex script

Run from repo root. This script edits **only the YAML frontmatter block**.

```bash
python3 - <<'PY'
from pathlib import Path
import re

repo = Path('.')

classification = {}

# A. registry/navigation
for p in [
    'Physics/PHYSICS_COMPACT_REGISTRY.md',
]:
    classification[p] = {'claim_mode': 'navigation', 'canonical': 'false'}

# B. audit-like / external review
for p in [
    'Physics/SRT_AT_Physics_of_Causation_Processing_2026-03-02.md',
]:
    classification[p] = {'claim_mode': 'audit', 'canonical': 'false'}

# C/D/E. bridge, compact cores, longforms
for p in [
    'Physics/_SRT_Phys_Bridge.md',
    'Physics/SRT_Quant_00_Intro_CompactCore.md',
    'Physics/SRT_Quant_01_Selection_CompactCore.md',
    'Physics/SRT_Quant_02_Cosmology_CompactCore.md',
    'Physics/SRT_Physics_Cosmology_CompactCore.md',
    'Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md',
    'Physics/SRT_Phys_10_Integration_CompactCore.md',
    'Physics/SRT_Phys_07_Complex_Systems_CompactCore.md',
    'Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md',
    'Physics/SRT_Quant_00_Intro.md',
    'Physics/SRT_Quant_01_Selection.md',
    'Physics/SRT_Quant_02_Cosmology.md',
    'Physics/SRT_Physics_Cosmology.md',
    'Physics/SRT_Phys_09_Formalism_Ext.md',
    'Physics/SRT_Phys_10_Integration.md',
    'Physics/SRT_Phys_07_Complex_Systems.md',
    'Physics/SRT_Phys_08_Ontology_Ext.md',
]:
    classification[p] = {'claim_mode': 'translation', 'canonical': 'false'}

changed = []
for rel, fields in classification.items():
    path = repo / rel
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        raise RuntimeError(f'{rel} has no YAML frontmatter; PR-P1A should have handled no-frontmatter files')
    end = text.find('\n---\n', 4)
    if end == -1:
        raise RuntimeError(f'{rel} has malformed YAML frontmatter')
    fm = text[:end+5]  # includes closing ---\n
    body = text[end+5:]

    # Replace or add claim_mode.
    if re.search(r'^claim_mode:\s*.*$', fm, re.M):
        fm2 = re.sub(r'^claim_mode:\s*.*$', f"claim_mode: {fields['claim_mode']}", fm, count=1, flags=re.M)
    else:
        fm2 = fm.replace('\n---\n', f"\nclaim_mode: {fields['claim_mode']}\n---\n")

    # Replace or add canonical.
    if re.search(r'^canonical:\s*.*$', fm2, re.M):
        fm2 = re.sub(r'^canonical:\s*.*$', f"canonical: {fields['canonical']}", fm2, count=1, flags=re.M)
    else:
        # Prefer placing canonical immediately after claim_mode.
        fm2 = re.sub(
            r'^(claim_mode:\s*.*)$',
            r'\1\ncanonical: ' + fields['canonical'],
            fm2,
            count=1,
            flags=re.M,
        )

    new = fm2 + body
    if new != text:
        path.write_text(new, encoding='utf-8')
        changed.append(rel)

print('changed files:')
for p in changed:
    print('-', p)
PY
```

---

## 4. Verification script

Run after the edit:

```bash
python3 - <<'PY'
from pathlib import Path
import re

bad = []
for p in sorted(Path('Physics').glob('*.md')):
    text = p.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        bad.append((str(p), 'missing frontmatter'))
        continue
    end = text.find('\n---\n', 4)
    fm = text[:end+5] if end != -1 else text
    cm = re.search(r'^claim_mode:\s*(.*)$', fm, re.M)
    cn = re.search(r'^canonical:\s*(.*)$', fm, re.M)
    if not cm:
        bad.append((str(p), 'missing claim_mode'))
    elif cm.group(1).strip() == 'canonical':
        bad.append((str(p), 'invalid claim_mode: canonical'))
    if not cn:
        bad.append((str(p), 'missing canonical'))

if bad:
    print('frontmatter issues:')
    for item in bad:
        print('-', item[0], item[1])
    raise SystemExit(1)
print('OK: all Physics/*.md have frontmatter, claim_mode, and canonical; no claim_mode: canonical remains.')
PY
```

---

## 5. Required report file

Create:

```text
Operations/Archive_Records/Physics_P1b_Frontmatter_Canonical_ClaimMode_Record.md
```

Must include:

- list of files changed;
- claim_mode assignment table;
- safety confirmation;
- verification-script result;
- note that no body text or formulas were changed.

---

## 6. Codex prompt for PR-P1B

```text
You are working in SRT-Pub. Complete PR-P1B: Physics frontmatter-only canonical flag and claim_mode normalization.

Read:
- Operations/Archive_Records/Physics_P0b_Exact_Inventory_Report.md
- Operations/Archive_Records/Physics_P1a_Minimal_Frontmatter_Record.md
- Operations/Archive_Records/Physics_P1b_Frontmatter_Canonical_ClaimMode_Handoff.md
- Physics/SRT_Physics_Claim_Status.md

Task:
1. Run the PR-P1B local script in Operations/Archive_Records/Physics_P1b_Frontmatter_Canonical_ClaimMode_Handoff.md §3.
2. Run the verification script in §4.
3. Create Operations/Archive_Records/Physics_P1b_Frontmatter_Canonical_ClaimMode_Record.md with changed files, assignment table, verification result, and safety record.

Allowed:
- Edit only YAML frontmatter blocks in Physics/*.md.
- Add canonical: false where missing.
- Replace claim_mode: canonical with one of navigation, audit, or translation according to the classification table.

Forbidden:
- Do not edit body text outside YAML frontmatter.
- Do not move sections.
- Do not change formulas.
- Do not create Physics_Annex/.
- Do not rewrite or promote physics claims.
- Do not touch Core/, Core_Law/, AI/, Neuroscience/, Philosophy/, Public/, Papers/, or graphify-out/.

Commit message:
"Normalize Physics frontmatter claim modes"
Open a draft PR. Do not merge automatically.
```

---

## 7. Bottom line

PR-P1B should be a scripted frontmatter-only normalization pass. Do not perform it manually through full-file connector rewrites unless absolutely necessary.
