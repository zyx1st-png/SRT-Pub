from __future__ import annotations

import re
from pathlib import Path

PAPERS = Path(__file__).resolve().parent
SRC = PAPERS / "CostlySelectiveClosure_v19_ArtificialLife_candidate.md"
OUT = PAPERS / "CostlySelectiveClosure_v19_ArtificialLife_submission.md"
TITLE = "# Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents"
NOVELTY_AUDIT = PAPERS / "CostlySelectiveClosure_v19_STRONGEST_NEIGHBOR_AUDIT.md"

E2_PREREG = "5852e60d82efc14748ae3478ee2400b4d3600839"
E3_PREREG = "0c599c14ea24196c6e2d411ecd0e4e17124f18f1"
E4_PREREG = "66cb46c45e99c5535c1f63b9c200ff9dbe911506"


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
        TITLE,
        "## Abstract",
        "## 1. Introduction",
        "## 2. Related Work",
        "## 3. Conceptual Motivation: Describing Failure Consequences",
        "## 4. Experimental Programme",
        "### 4.2 Experiment 1: terminal failure versus restoration",
        "### 4.3 Experiment 2: persistent non-terminal metabolic impairment",
        "### 4.4 Experiment 3: individual-scoped recovery latency",
        "### 4.5 Experiment 4: individual versus shared consequence scope",
        "## 5. Results",
        "### 5.4 Experiment 4: shared consequence scope has a small, preregistered positive effect",
        "## 6. Discussion",
        "## 7. Conclusion",
        "## Data and Code Availability",
        "## AI Assistance Disclosure",
        "## References",
        "## Appendix D. Experiment 4 Confirmatory Guard",
        "**Experiment 1 was not preregistered.**",
        "timestamped repository preregistrations",
        "decision-count-dependent",
        "mean(shared - individual) = +0.02998",
        "29/30",
        "strong-support threshold",
        "who bears failure-triggered future opportunity loss",
        "terminality still contains additional causal structure",
        "E5 is not required",
        # Strongest-neighbor / novelty boundary guards.
        "Tampuu et al. (2017)",
        "Scott and Pitt (2023)",
        "shared consequence",
        "not new",
        # Repository preregistration provenance must be reviewer-visible.
        E2_PREREG,
        E3_PREREG,
        E4_PREREG,
    ]
    for item in required:
        if item not in text:
            raise RuntimeError(f"missing required v19 submission element: {item}")

    forbidden = [
        "# Failure Is Not One-Dimensional:",
        "CONSEQUENCE SCOPE = PLAUSIBLE MECHANISM HYPOTHESIS / NOT ESTABLISHED",
        "E4 result = UNKNOWN",
        "E4 CONFIRMATORY RUN = NOT AUTHORIZED",
        "Failure is now represented as **structured consequence architecture**",
        "V = irreversible vulnerability",
        "cheap restoration lowers operational V",
        "Only the final hypothesis receives direct support",
        "more difficult recovery\n=> greater effective vulnerability\n=> more stable costly cooperation",
        "first demonstration that shared consequences",
        "first demonstration of shared consequence",
        "first demonstration of cooperative survival",
    ]
    for item in forbidden:
        if item in text:
            raise RuntimeError(f"v19 submission contains superseded/internal residue: {item}")

    if not NOVELTY_AUDIT.is_file():
        raise RuntimeError("v19 strongest-neighbor audit is missing")

    keyword_line = next(
        (line for line in text.splitlines() if line.startswith("**Keywords**:")), None
    )
    if keyword_line is None:
        raise RuntimeError("keywords line missing")
    keywords = [x.strip() for x in keyword_line.split(":", 1)[1].split(",")]
    if not (5 <= len(keywords) <= 6):
        raise RuntimeError(f"Artificial Life expects 5-6 keywords; found {len(keywords)}")

    if "Experiment 2 is most informative when its construct boundary is respected" not in text:
        raise RuntimeError("v19 must retain the E2 construct-validity boundary")
    if "Experiment 3 has an additional interpretation boundary" not in text:
        raise RuntimeError("v19 must retain the E3 update-mechanics boundary")
    if "positive but modest H-SCOPE support" not in text:
        raise RuntimeError("v19 must retain the locked E4 Outcome-B interpretation")


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
