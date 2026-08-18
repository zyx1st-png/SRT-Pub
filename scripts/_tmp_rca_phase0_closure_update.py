from pathlib import Path
import re

p=Path('Operations/Audits/SRT_RC_A_SEMANTIC_SYNC_CLOSURE_2026-08-17.md')
s=p.read_text(encoding='utf-8')

def sub(pattern,repl,count=1):
    global s
    s2,n=re.subn(pattern,repl,s,count=count,flags=re.S)
    if n!=count: raise SystemExit(f'expected {count} replacement(s), got {n}: {pattern[:120]!r}')
    s=s2

sub(r'Therefore:\n\n- \*\*theory / author blockers: 0\*\*\n- \*\*engineering / environment blockers remain: 3\*\*\n  1\. exhaustive repo-wide literal inventory cannot be certified;\n  2\. bounded retrieval Q1-Q6 cannot be run as independent fresh sessions;\n  3\. Context Bundle freshness remains red and requires repository-generator regeneration\.',
'''Therefore:\n\n- **theory / author blockers: 0**\n- **engineering / environment blockers remain: 1**\n  1. bounded retrieval Q1-Q6 cannot yet be run as the protocol-required independent fresh sessions.\n\nThe previously open engineering gates are now closed:\n\n- exhaustive tracked-file inventory: **PASS**;\n- Context Bundle freshness: **PASS**;\n- full Governance Preflight on the final working tree: **PASS**.''')

sub(r'- theory-resolution head before closure writeback: `[^`]+`\n- governance-tested pre-report head: `[^`]+`\n- governance run: `[^`]+` / run number `[^`]+`',
'''- final semantic-sync head before closure writeback: `0aaa72be66272226247297f4b81ecaca811e1eef`\n- exhaustive-inventory snapshot commit: `0aaa72be66272226247297f4b81ecaca811e1eef`\n- final full-governance execution run before closure writeback: `32096756837` / run number `927`''')

sub(r'## 3\. Search / inventory status\n.*?\n---\n\n## 4\.',
'''## 3. Search / inventory status\n\nThe Phase-0 search families were rerun against the **actual PR-head tracked-file tree** inside a GitHub Actions full checkout, bypassing the GitHub code-search index entirely.\n\nFinal inventory snapshot that became commit `0aaa72be66272226247297f4b81ecaca811e1eef`:\n\n- tracked paths: **2086**;\n- regular text files scanned: **2020**;\n- read errors: **0**;\n- nonregular / symlink paths skipped: **4**;\n- binary files were identified separately rather than decoded as text.\n\nThe original seven Phase-0 families were covered (`P1-T05`; `Real Choice Moment`; real/live/active choice; Chinese real/live-choice shorthand; script/habit/automation/gradient + Selection; CG + P1-T05; T_dir + real/live choice). Two bounded hardening diagnostics were also added during execution for the deleted global `r(t)` and legacy `pseudo-selection` terminology.\n\n### Adjudication discipline\n\nLiteral zero was **not** used as the exit criterion. Residual hits were classified by current function:\n\n- **A — active contradiction**: current authority / active derivative that still implied the superseded relation;\n- **B — historical provenance**: demotion history, source intuition, changelog or audit record;\n- **C — current guarded legacy/downstream shorthand**: retained only with explicit RC-A active-use boundary;\n- **D — generated / mirrored / irrelevant-to-authority occurrence**.\n\nAll Class-A surfaces exposed by the exhaustive run were repaired, including canonical / governance / AI-owner / split / annex / glossary / OOD-regression residues. The final strengthened `pseudo-selection` diagnostic has only provenance, explicit legacy/forbidden-use text, practice-layer labels, or generated-bundle mirrors; it no longer exposes an active Selection-occurrence definition.\n\nThe final inventory therefore supports:\n\n- **repo-wide tracked-file inventory: EXECUTED / PASS**;\n- **known active RC-A contradiction in the searched families: none**;\n- prior GitHub indexed-search `0 hits` is retained only as evidence that the index was unreliable, not as repository evidence.\n\n---\n\n## 4.''')

sub(r'This is a bounded verification of the edited owner neighborhood, not an exhaustive repository-wide claim\.',
'''These owner checks are now supplemented by the exhaustive tracked-file inventory in §3; they are no longer the sole basis for the repository-wide exit judgment.''')

sub(r'`Operations/Context_Bundles/` remains generated output and must not be hand-edited\. The repository requires `scripts/build_srt_context_bundles\.py` regeneration after relevant source / guard changes\.',
'''`Operations/Context_Bundles/` remains generated output and was **not hand-edited**. During this closure round the repository generator was run on a full Actions checkout, the generated bundles were committed, and subsequent source changes were followed by `scripts/build_srt_context_bundles.py --check`. Final bundle freshness is **PASS**.''')

sub(r'## 10\. Governance / CI\n.*?\n---\n\n## 11\.',
'''## 10. Governance / CI\n\nThe final OOD-sync execution run `32096756837` (run number `927`) used the PR's actual head checkout, restored the canonical workflow before the functional commit, and validated the exact final working tree that became commit `0aaa72be66272226247297f4b81ecaca811e1eef`.\n\n### Passing gates\n\n- split metadata freshness: **PASS**;\n- Context Bundle freshness: **PASS**;\n- full `governance_preflight.py --skip-write-report --strict-split-metadata`: **PASS**;\n- final tracked-file search-family inventory: **PASS**, `read_errors=0`;\n- `git diff --cached --check`: **PASS** before each final functional commit;\n- temporary workflow / helper machinery: **removed before functional commit**.\n\nThe ordinary workflow file at the branch head is restored to the repository's canonical `contents: read` version; no temporary CI permission escalation or helper script is part of the functional PR diff.\n\nThe earlier Context Bundle freshness failure is therefore **closed**, not waived.\n\n---\n\n## 11.''')

sub(r'### Engineering / environment blockers\n\n1\. \*\*Exhaustive search remains UNVERIFIED\.\*\*.*?3\. \*\*Context Bundle freshness remains red\.\*\* Repository-generator regeneration is required; generated artifacts must not be hand-edited\.',
'''### Engineering / environment blockers\n\n1. **Bounded retrieval Q1-Q6 remain UNTESTED — environment limitation.** The protocol requires independent fresh bounded sessions; the current conversation is already primed by the target conclusions and cannot be counted as an independent run. No result is being faked as PASS.\n\nClosed engineering gates:\n\n- exhaustive tracked-file search: **PASS**;\n- Context Bundle freshness: **PASS**;\n- full Governance Preflight: **PASS**.''')

p.write_text(s,encoding='utf-8')
