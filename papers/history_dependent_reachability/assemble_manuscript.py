"""Assemble the eight section drafts into a single MANUSCRIPT.md.

Mechanical, auditable transformations only:
  - order: abstract, intro(1), methods(2), results(3), audit(4), discussion(5),
    limitations(6), figures (unnumbered back-matter);
  - strip the per-file draft-note blockquotes;
  - renumber headings (M#->2.#, R#->3.#, 8.x->4.x, 9.x->5.x, 10->6);
  - fix internal cross-references to the new numbering;
  - insert figure cross-citations in Results (listed explicitly below);
  - no other text changes (no language polish).
"""
from __future__ import annotations
import re
from pathlib import Path

HERE = Path(__file__).parent
MS = HERE / "manuscript"

TITLE = ("Identifying History-Dependent Reachability: "
         "A Constructive Framework for Selection-Specific Write-Back")

def load(name):
    return (MS / name).read_text(encoding="utf-8")

def strip_note(text):
    """Remove the draft-note blockquote that follows the first heading."""
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if lines[i].startswith("> ") and out and out[-1].strip() == "":
            while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
                i += 1
                if i < len(lines) and lines[i].strip() == "" and not (
                        i + 1 < len(lines) and lines[i + 1].startswith(">")):
                    i += 1
                    break
            continue
        out.append(lines[i]); i += 1
    return "\n".join(out)

def sub_all(text, pairs):
    for pat, rep in pairs:
        text = re.sub(pat, rep, text, flags=re.MULTILINE)
    return text

# ---- per-file transforms -------------------------------------------------------
abstract = strip_note(load("00_abstract.md"))
abstract = abstract.replace("# Abstract", "## Abstract")

intro = strip_note(load("01_introduction.md"))

methods = strip_note(load("02_methods.md"))
methods = sub_all(methods, [
    (r"^# Methods", "# 2. Methods"),
    (r"^## M(\d+)\.", r"## 2.\1"),
    (r"Systems S2–S4 share four separated variables:",
     "Systems S2–S4 share four separated variables (Figure 1A):"),
    (r"Future battery \(frozen parameters;",
     "Future battery (Figure 4A; frozen parameters;"),
])

results = strip_note(load("03_results.md"))
results = sub_all(results, [
    (r"^# Results", "# 3. Results"),
    (r"^## R(\d)\.", r"## 3.\1"),
    (r"two-timescale agents of R2–R4", "two-timescale agents of Sections 3.2–3.4"),
    (r"mechanism revision of R3", "mechanism revision of Section 3.3"),
    (r"carried by R4", "carried by Section 3.4"),
    (r"\(R1\)", "(3.1)"), (r"\(R2\)", "(3.2)"), (r"\(R3\)", "(3.3)"), (r"\(R4\)", "(3.4)"),
    (r"\bby R4\b", "by Section 3.4"), (r"\bin R2\b", "in Section 3.2"),
    (r"\(Methods M4\)", "(Methods 2.4)"),
    # figure cross-citations (insertions, no wording changes)
    (r"populate the P × W_sel plane \(Table 1\):",
     "populate the P × W_sel plane (Table 1; Figure 2):"),
    (r"\*\*Matched present, different future\.\*\*",
     "**Matched present, different future (Figure 1B).**"),
    (r"active 0\.239 vs yoked 0\.238 \(d = 0\.05\)",
     "active 0.239 vs yoked 0.238 (d = 0.05; Figure 3A)"),
    (r"Washout-length\ncurves", "Washout-length\ncurves (Supplementary Figure S1)"),
    (r"A cross-individual permutation confirmed",
     "A cross-individual permutation (Supplementary Figure S3) confirmed"),
    (r"was \*\*0\.570, 90% CI \[0\.559, 0\.581\]\*\*",
     "was **0.570, 90% CI [0.559, 0.581]** (Figure 3C)"),
    (r"equivalence bound: 0\.087, 90% CI \[0\.082, 0\.091\]\*\*",
     "equivalence bound: 0.087, 90% CI [0.082, 0.091]** (Figure 3B)"),
    (r"was \*\*0\.374, 95% CI \[0\.374, 0\.375\]\*\*",
     "was **0.374, 95% CI [0.374, 0.375]** (Figure 5E)"),
    (r"The difference is directional, in all three pre-registered senses:",
     "The difference is directional, in all three pre-registered senses (Figure 5A–D):"),
    (r"The external-action sham behaved as the mechanism predicts",
     "The external-action sham behaved as the mechanism predicts (Figure 4B)"),
    (r"\*\*\[pipeline validation\]\*\* memory-null = 0\.044",
     "**[pipeline validation]** (Supplementary Figure S2) memory-null = 0.044"),
])

audit = strip_note(load("05_audit.md"))
audit = sub_all(audit, [
    (r"^# 8\. Audit", "# 4. Audit"),
    (r"^## 8\.(\d)", r"## 4.\1"),
    (r"\(Section 3\)", "(Methods 2.8)"),
    (r"\(Section 10\)", "(Section 6)"),
])

discussion = strip_note(load("07_discussion.md"))
discussion = sub_all(discussion, [
    (r"^# 9\. Discussion", "# 5. Discussion"),
    (r"^## 9\.(\d)", r"## 5.\1"),
    (r"\(Sections 8 and 10\)", "(Sections 4 and 6)"),
    (r"\(Section 10\)", "(Section 6)"),
    (r"\(Section 8\.3\)", "(Section 4.3)"),
])

limitations = strip_note(load("06_limitations.md"))
limitations = sub_all(limitations, [
    (r"^# 10\. Limitations", "# 6. Limitations"),
    (r"\(Section 8\.3\)", "(Section 4.3)"),
    (r"Section 9\b", "Section 5"),
    (r"\(Sections 8 and 10\)", "(Sections 4 and 6)"),
])

references = strip_note(load("08_references.md"))

figures = strip_note(load("04_figures.md"))
figures = figures.replace("# Figures and captions", "# Figures and captions (back matter)")

parts = [
    f"# {TITLE}\n",
    "> Assembled from manuscript/00–07 by `assemble_manuscript.py` (mechanical\n"
    "> renumbering and cross-reference unification only; no language polish).\n"
    "> Numeric provenance: `RESULTS_NUMBERS.md` (read-only from frozen JSONs).\n"
    "> Governed by `PAPER_CHARTER.md` and `CLAIM_LEDGER.md`.\n",
    abstract, "\n---\n", intro, "\n---\n", methods, "\n---\n", results, "\n---\n",
    audit, "\n---\n", discussion, "\n---\n", limitations, "\n---\n", references,
    "\n---\n", figures,
]
out = "\n".join(p.strip("\n") + "\n" for p in parts)
(MS / "MANUSCRIPT.md").write_text(out, encoding="utf-8")
print(f"wrote manuscript/MANUSCRIPT.md ({len(out.splitlines())} lines, "
      f"{len(out.split())} words)")
