from __future__ import annotations

import re
from pathlib import Path

PAPERS = Path(__file__).resolve().parent
SRC = PAPERS / "CostlySelectiveClosure_v17_ArtificialLife_candidate.md"
OUT = PAPERS / "CostlySelectiveClosure_v17_ArtificialLife_submission.md"

AI_DISCLOSURE = """## AI Assistance Disclosure\n\nOpenAI ChatGPT was used as an editorial and research-assistance tool during manuscript development, including literature discovery, structural critique, language revision, and consistency checking across manuscript, code descriptions, and reported results. The tool did not serve as an author. The author independently checked the cited sources, version-controlled experimental code, analyses, and manuscript claims and takes full responsibility for the content. The reported numerical results come from the committed experimental runs described in the reproduction package rather than from generative-model output.\n\n"""


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


def inject_ai_disclosure(text: str) -> str:
    marker = "## Data and Code Availability\n"
    if marker not in text:
        raise RuntimeError("Data and Code Availability marker missing")
    if "## AI Assistance Disclosure" in text:
        raise RuntimeError("AI disclosure already present")
    return text.replace(marker, AI_DISCLOSURE + marker, 1)


def word_count(text: str) -> int:
    # Submission-guidance check only: count ordinary word-like tokens and numbers,
    # ignoring Markdown punctuation. This is not a publisher-defined metric.
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def validate(text: str) -> None:
    required = [
        "## AI Assistance Disclosure",
        "## Abstract",
        "## References",
        "## Appendix: Experimental Details",
        "**Keywords**:",
    ]
    for item in required:
        if item not in text:
            raise RuntimeError(f"missing required submission element: {item}")

    forbidden = [
        "Repository note.",
        "d_cog",
        "\\hat{G}",
        "Ψ_f",
        "CostlySelectiveClosure_v16.md",
        "Adaptive Behavior v16",
    ]
    for item in forbidden:
        if item in text:
            raise RuntimeError(f"submission artifact contains internal/historical residue: {item}")

    keyword_line = next(
        (line for line in text.splitlines() if line.startswith("**Keywords**:")), None
    )
    if keyword_line is None:
        raise RuntimeError("keywords line missing")
    keywords = [x.strip() for x in keyword_line.split(":", 1)[1].split(",")]
    if len(keywords) != 6:
        raise RuntimeError(f"Artificial Life expects 5–6 keywords; found {len(keywords)}")


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    text = strip_repository_note(text)
    text = inject_ai_disclosure(text)
    text = text.lstrip()
    validate(text)
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(PAPERS.parent)}")
    print(f"submission-word-count (approx): {word_count(text)}")


if __name__ == "__main__":
    main()
