from __future__ import annotations

import re
from pathlib import Path

PAPERS = Path(__file__).resolve().parent
SRC = PAPERS / "CostlySelectiveClosure_v19_1_ArtificialLife_candidate.md"
OUT = PAPERS / "CostlySelectiveClosure_v19_1_ArtificialLife_submission.md"
TITLE = "# Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents"
FIG1 = "costly_selective_closure_supplement/figures/figure1_experiment_architectures_v19.svg"
FIG2 = "costly_selective_closure_supplement/figures/figure2_evidence_summary_v19_1.svg"
EXPLORATORY = "costly_selective_closure_supplement/results/consequence_scope_E4_individual_latency_exploratory.json"

AI_DISCLOSURE_OLD = (
    "OpenAI ChatGPT was used during the September 2026 revision process for literature organization, "
    "manuscript restructuring, wording assistance, code-review support, experimental-governance checks, "
    "consistency review, and post-hoc analysis scripting. Reported confirmatory numerical results derive "
    "from committed experiment code and preserved result artifacts rather than from generative-model output. "
    "The author determined the hypotheses, approved the preregistrations, accepted unfavorable confirmatory "
    "outcomes, verified claims against preserved outputs, and takes responsibility for the manuscript."
)

AI_DISCLOSURE_SUBMISSION = (
    "OpenAI ChatGPT (OpenAI; including GPT-5.6 Sol; accessed September 16, 2026) was used for literature "
    "organization, manuscript restructuring, wording assistance, code-review support, experimental-governance "
    "checks, consistency review, and post-hoc analysis scripting. Anthropic Claude (Anthropic; accessed "
    "September 2026; exact model version not retained in the project record) was used as an independent "
    "manuscript-critique tool during revision. Neither system is an author. Reported confirmatory numerical "
    "results derive from committed experiment code and preserved result artifacts rather than from generative-model "
    "output. The author determined the hypotheses, approved the preregistrations, accepted unfavorable confirmatory "
    "outcomes, verified claims and citations, made the final interpretive decisions, and takes responsibility for "
    "the manuscript."
)


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end < 0:
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


def patch_ai_disclosure(text: str) -> str:
    if AI_DISCLOSURE_OLD not in text:
        raise RuntimeError("could not locate internal v19.1 AI disclosure for submission patch")
    return text.replace(AI_DISCLOSURE_OLD, AI_DISCLOSURE_SUBMISSION, 1)


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def validate(text: str) -> None:
    required = [
        TITLE,
        "## Abstract",
        "## 1. Introduction",
        "## 2. Related Work",
        "## 4. Experimental Programme",
        "## 5. Results",
        "#### Exploratory cross-check under the corrected E4 update",
        "## 6. Discussion",
        "### 6.5 Why terminality remains mechanistically live",
        "## 7. Conclusion",
        "## Data and Code Availability",
        "## AI Assistance Disclosure",
        "## References",
        "## Appendix E. Post-hoc E4 Individual-Scope Latency Cross-Check",
        "E1 and E4 differ in update semantics, evaluation endpoint and state bank, confirmatory seed set, and baseline regime",
        "post-hoc exploratory",
        "bundled shared recovery/action-opportunity architecture",
        "not a controlled decomposition",
        "does not require an immediate Experiment 5",
        "29/30",
        "+0.02998",
        "rho = -0.494",
        "OpenAI ChatGPT (OpenAI; including GPT-5.6 Sol; accessed September 16, 2026)",
        "Anthropic Claude (Anthropic; accessed September 2026; exact model version not retained in the project record)",
        "Neither system is an author.",
        EXPLORATORY,
        FIG1,
        FIG2,
    ]
    for item in required:
        if item not in text:
            raise RuntimeError(f"missing required v19.1 element: {item}")

    forbidden = [
        "than the v18 claim",
        "Outcome B",
        "adjudication record",
        "mechanism audit",
        "too small to explain the much larger terminality effect by itself",
        "scope can explain only",
        "scope explains only",
        "the current evidence supports an additive or interacting role",
        "> **Repository note.**",
    ]
    for item in forbidden:
        if item in text:
            raise RuntimeError(f"reader-facing internal/overclaim residue: {item}")

    for rel in [FIG1, FIG2, EXPLORATORY]:
        if not (PAPERS / rel).is_file():
            raise RuntimeError(f"missing v19.1 asset: {rel}")

    keyword_line = next((line for line in text.splitlines() if line.startswith("**Keywords**:")), None)
    if keyword_line is None:
        raise RuntimeError("keywords line missing")
    keywords = [x.strip() for x in keyword_line.split(":", 1)[1].split(",")]
    if not (5 <= len(keywords) <= 6):
        raise RuntimeError(f"expected 5-6 keywords, found {len(keywords)}")

    if "The first and only E4 confirmatory run" not in text:
        raise RuntimeError("must preserve first-and-only E4 run boundary")
    if "not a preregistered replication" not in text:
        raise RuntimeError("must preserve exploratory latency boundary")

    wc = word_count(text)
    if not (6000 <= wc <= 12000):
        raise RuntimeError(f"Artificial Life Article word-count guard failed: {wc}")


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    text = strip_repository_note(text)
    text = patch_ai_disclosure(text).lstrip()
    validate(text)
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(PAPERS.parent)}")
    print(f"submission-word-count (approx): {word_count(text)}")
    print("journal_submission=NOT_PERFORMED")


if __name__ == "__main__":
    main()
