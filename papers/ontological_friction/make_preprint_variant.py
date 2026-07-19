from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "paper_ontological_friction.md"
OUT = ROOT / "paper_ontological_friction_preprint.md"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Could not find expected {label} block in {SRC.name}")
    return text.replace(old, new, 1)


text = SRC.read_text(encoding="utf-8")

text = replace_once(
    text,
    "**Article type**: Hypothesis and Theory  \n"
    "**Target journal**: Frontiers in Neuroscience  \n",
    "**Manuscript status**: Preprint; not a peer-reviewed version of record  \n"
    "**Article type**: Theoretical Article  \n"
    "**Version**: 1.0 (19 July 2026)  \n"
    "**Author**: Yuxin Zhang  \n"
    "**Affiliation**: Independent Researcher, Kaili, Guizhou, China  \n"
    "**Correspondence**: zyx1st@gmail.com  \n"
    "**ORCID**: https://orcid.org/0009-0007-6659-8518  \n",
    "journal-specific front matter",
)

text = replace_once(
    text,
    "This is a theoretical and computational contribution aimed at empirical translation. No new data are reported. Consistent with the *Frontiers in Neuroscience* Hypothesis and Theory format, the paper advances a testable model within a specific area of investigation — the knowing-doing gap in executive dysfunction — and provides measurement strategy, falsification rules, and clinically tractable protocols for future adjudication.",
    "This is a theoretical and computational contribution aimed at empirical translation. No new data are reported. As a theoretical framework paper, the manuscript advances a testable model of the knowing-doing gap in executive dysfunction and provides measurement strategies, falsification rules, and clinically tractable protocols for future adjudication.",
    "journal-specific scope sentence",
)

if "Frontiers in Neuroscience" in text:
    raise RuntimeError("Journal-specific Frontiers wording remains in the generated preprint")
if "**Target journal**" in text:
    raise RuntimeError("Target-journal metadata remains in the generated preprint")

OUT.write_text(text, encoding="utf-8")
print(f"Wrote {OUT.name}")
