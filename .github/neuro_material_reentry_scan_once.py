from pathlib import Path
import re

ROOT = Path('.')


def fm(text: str) -> str:
    if not text.startswith('---\n'):
        return ''
    end = text.find('\n---\n', 4)
    return text[4:end] if end != -1 else ''


def scalar(front: str, key: str) -> str:
    m = re.search(rf'(?m)^{re.escape(key)}:\s*["\']?([^\n"\']+)', front)
    return m.group(1).strip() if m else ''


def list_block(front: str, key: str) -> list[str]:
    m = re.search(rf'(?ms)^{re.escape(key)}:\s*\n((?:\s+-[^\n]*\n?)*)', front)
    if not m:
        return []
    return [re.sub(r'^\s+-\s*', '', x).strip().strip('"\'') for x in m.group(1).splitlines() if x.strip().startswith('-')]


def relevant_material(path: Path, text: str) -> bool:
    front = fm(text)
    domain = scalar(front, 'domain').lower()
    sid = scalar(front, 'source_id').lower()
    tags = front.lower()
    name = path.name.lower()
    direct = any(k in domain for k in ['neuro', 'brain', 'astrocy', 'glia', 'memory', 'attention', 'interocept', 'vagal', 'sleep', 'psyched'])
    named = any(k in name or k in sid for k in ['neuro', 'brain', 'astrocy', 'memory', 'attention', 'interocept', 'vagal', 'sleep', 'psyched'])
    tagged = any(k in tags for k in ['neuroscience', 'neural_', 'astrocyte', 'hippocamp', 'ripple', 'engram'])
    return direct or named or tagged

print('=== ACTIVE DIRECT NEUROSCIENCE SOURCECARDS ===')
rows = []
for path in sorted((ROOT / 'Materials' / '2026').glob('*.md')):
    text = path.read_text(encoding='utf-8', errors='replace')
    front = fm(text)
    if scalar(front, 'status') != 'active':
        continue
    if not relevant_material(path, text):
        continue
    rel = scalar(front, 'srt_relevance')
    pri = scalar(front, 'integration_priority')
    rows.append((str(path), scalar(front, 'source_id'), scalar(front, 'domain'), rel, pri))
for r in rows:
    print('\t'.join(r))
print('COUNT', len(rows))

print('\n=== ACTIVE HIGH/VERY_HIGH DIRECT NEUROSCIENCE SOURCECARDS ===')
hi = [r for r in rows if r[3] in {'high','very_high'} or r[4] in {'high','very_high'}]
for r in hi:
    print('\t'.join(r))
print('COUNT', len(hi))

print('\n=== ACTIVE NEUROSCIENCE PATCHES ===')
patch_source_ids = set()
for path in sorted((ROOT / 'Neuroscience' / 'patches').glob('*.md')):
    text = path.read_text(encoding='utf-8', errors='replace')
    front = fm(text)
    if scalar(front, 'status') != 'active':
        continue
    sids = list_block(front, 'source_ids')
    patch_source_ids.update(sids)
    print(str(path), '|', scalar(front, 'patch_id') or scalar(front,'id'), '|', ','.join(sids), '| targets=', ','.join(list_block(front,'target_documents')))

print('\n=== PATCH SOURCE IDS NOT IN DIRECT CARD SCAN ===')
direct_ids = {r[1] for r in rows}
for sid in sorted(patch_source_ids - direct_ids):
    print(sid)

print('\n=== ACTIVE NEUROSCIENCE HOOKS ===')
for path in sorted((ROOT / 'Neuroscience' / 'hooks').glob('*.md')):
    text = path.read_text(encoding='utf-8', errors='replace')
    front = fm(text)
    if scalar(front, 'status') != 'active':
        continue
    print(str(path), '|', scalar(front,'id'), '| integration=', scalar(front,'integration_status'), '| patch=', scalar(front,'patch_id'))

print('\n=== DOMAIN OWNER / GUARD / PROTOCOL SURFACES ===')
patterns = [
    'Neuroscience/README.md',
    'Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md',
    'Neuroscience/SRT_Neuroscience_Claim_Status.md',
    'Neuroscience/SRT_Neuro_Axioms_Claim_Status.md',
    'Neuroscience/SRT_Neural_Mechanisms.md',
    'Neuroscience/SRT_Neural_Mechanisms_CompactCore.md',
    'Neuroscience/_SRT_Neuro_Axioms.md',
    'Neuroscience/_SRT_Neuroscience_Hardening_Index.md',
    'Neuroscience/SRT_Neuro_Experiments.md',
    'Neuroscience/SRT_Neuro_Predictions_Table.md',
    'Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md',
    'Neuroscience/SRT_NEURAL33_EXPERIMENT_PROTOCOL_v0_1.md',
    'Neuroscience/SRT_NEURAL34_MATCHED_STATE_RELATIONAL_HISTORY_PROTOCOL_v0_1.md',
]
for p in patterns:
    if Path(p).exists():
        print(p)

print('\n=== EXPERIMENT PATHS WITH DIRECT NEURO / MEMORY / HISTORY SIGNAL ===')
for path in sorted((ROOT / 'Experiments').rglob('*')):
    if not path.is_file():
        continue
    low = str(path).lower()
    if any(k in low for k in ['neuro', 'neural', 'memory', 'engram', 'history', 'ripple', 'brain']):
        print(path)

print('\n=== SOURCE INTUITION / BOOK FILES WITH NEURO-HISTORY-BEARER SIGNAL COUNTS ===')
for path in sorted((ROOT / '01_Source_Intuition').rglob('*.md')):
    text = path.read_text(encoding='utf-8', errors='replace').lower()
    counts = {k: text.count(k) for k in ['brain','neural','neuron','memory','history','bearer','subject','identity']}
    score = counts['brain'] + counts['neural'] + counts['neuron'] + counts['memory']
    structural = counts['history'] + counts['bearer'] + counts['identity']
    if score >= 5 and structural >= 3:
        print(path, counts)

print('\n=== MANUSCRIPT / PUBLISHED ASSETS MATCHING FRONTIERS DOI ===')
doi = '10.3389/fnins.2026.1837760'
for path in ROOT.rglob('*.md'):
    if any(part in {'.git','Operations/Context_Bundles'} for part in path.parts):
        continue
    try:
        text = path.read_text(encoding='utf-8', errors='replace')
    except Exception:
        continue
    if doi in text:
        print(path)

print('\n=== FIRST-WELL / SEQUENCE RECORDS ===')
for path in sorted((ROOT / 'Operations').rglob('*.md')):
    n = path.name
    if ('NEUROSCIENCE' in n and any(x in n for x in ['PHASE8','PHASE9'])) or n == 'SRT_CONSTITUTION_DOMAIN_SEQUENCE_AUTHOR_DECISION_2026-09-03.md':
        print(path)
