from __future__ import annotations

import re
from pathlib import Path

PAPERS = Path(__file__).resolve().parent
SRC = PAPERS / "CostlySelectiveClosure_v18_ArtificialLife_candidate.md"
OUT = PAPERS / "CostlySelectiveClosure_v18_ArtificialLife_submission.md"
DESIGN_FIGURE = "costly_selective_closure_supplement/figures/figure1_design_v17.svg"
EVIDENCE_FIGURE = "costly_selective_closure_supplement/figures/figure2_evidence_summary_v18.svg"
E1_SENSITIVITY_AUDIT = "costly_selective_closure_supplement/audit_e1_paired_sensitivity.py"
EVIDENCE_FIRST_TITLE = (
    "# Failure Is Not One-Dimensional: Terminality, Persistent Damage, "
    "and Recovery Architecture in Artificial Agents"
)


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        raise RuntimeError("unterminated YAML frontmatter")
    return text[end + 5 :]


def strip_repository_note(text: str) -> str:
    return re.sub(
        r"\n?> \*\*Repository note\.\*\*.*?(?=\n\n## Abstract)",
        "",
        text,
        count=1,
        flags=re.S,
    )


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def validate(text: str) -> None:
    required = [
        EVIDENCE_FIRST_TITLE,
        "## Abstract",
        "## 1. Introduction",
        "## 4. Experimental Programme",
        "## 5. Results",
        "## 6. Discussion",
        "## 7. Conclusion",
        "## Data and Code Availability",
        "## AI Assistance Disclosure",
        "## References",
        "## Appendix A. Experiment 1 Details",
        "## Appendix B. Experiment 2 Confirmatory Guard",
        "## Appendix C. Experiment 3 Confirmatory Guard",
        "**Keywords**:",
        DESIGN_FIGURE,
        EVIDENCE_FIGURE,
        E1_SENSITIVITY_AUDIT,
        "**Experiment 1 was not preregistered**",
        "timestamped repository preregistrations",
        "two-sample label-permutation test",
        "paired sign-flip sensitivity analysis",
        "This sensitivity analysis is post-hoc",
        "p = 0.0000499975",
        "24 of 30 paired differences are positive",
        "25 of 30 paired differences positive",
        "rho = +0.0548074683",
        "rho = -0.7037203560",
    ]
    for item in required:
        if item not in text:
            raise RuntimeError(f"missing required v18 submission element: {item}")

    forbidden = [
        "Repository note.",
        "CostlySelectiveClosure_v16.md",
        "Adaptive Behavior v16",
        "v17-specific supplement note",
        "NEW EXPERIMENT BEFORE SUBMISSION = NOT REQUIRED",
        "used below as the shorthand **real-stake**",
        "cheap restoration lowers operational V",
        "Only the final hypothesis receives direct support",
        "most important next experiment is also clear",
        "# Costly Selective Closure: Terminal Failure, Persistent Damage, and Recovery Architecture in Artificial Agents",
        "Terminal failure strongly stabilizes costly cooperation relative to cheap restoration",
        "two-sided paired sign-flip permutation test at the 20,000-resample resolution floor",
        "The paired difference is approximately `0.511`, with the two-sided paired sign-flip",
    ]
    for item in forbidden:
        if item in text:
            raise RuntimeError(f"v18 submission contains superseded/internal residue: {item}")

    if not (PAPERS / E1_SENSITIVITY_AUDIT).is_file():
        raise RuntimeError("v18 E1 sensitivity audit script is missing")

    keyword_line = next(
        (line for line in text.splitlines() if line.startswith("**Keywords**:")), None
    )
    if keyword_line is None:
        raise RuntimeError("keywords line missing")
    keywords = [x.strip() for x in keyword_line.split(":", 1)[1].split(",")]
    if not (5 <= len(keywords) <= 6):
        raise RuntimeError(f"Artificial Life expects 5–6 keywords; found {len(keywords)}")

    if "Experiment 2: persistent non-terminal metabolic impairment" not in text:
        raise RuntimeError("v18 submission must retain Experiment 2")
    if "Experiment 3: fully reversible recovery latency" not in text:
        raise RuntimeError("v18 submission must retain Experiment 3")


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    text = strip_repository_note(text)
    text = text.lstrip()
    validate(text)
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(PAPERS.parent)}")
    print(f"submission-word-count (approx): {word_count(text)}")


if __name__ == "__main__":
    main()
