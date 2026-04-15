from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pypandoc


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "paper_ontological_friction_frontiers_submission.md"
HTML_OUT = ROOT / "paper_ontological_friction_frontiers_submission.html"
DOCX_OUT = ROOT / "paper_ontological_friction_frontiers_submission.docx"
PDF_OUT = ROOT / "paper_ontological_friction_frontiers_submission.pdf"
POSTPROCESS = ROOT / "postprocess_frontiers_docx.py"
DOCX2PDF = ROOT.parent.parent / ".venv" / "bin" / "docx2pdf"

def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Could not find top-level title.")


def build_html(title: str, body_html: str) -> str:
    css = """
    body {
      font-family: Georgia, "Times New Roman", serif;
      color: #111;
      margin: 0 auto;
      max-width: 780px;
      padding: 36px 44px 48px;
      line-height: 1.45;
      background: #fff;
    }
    h1, h2, h3 {
      line-height: 1.25;
    }
    h1 {
      margin-top: 0;
      margin-bottom: 0.4em;
      font-size: 2em;
    }
    h2 {
      margin-top: 1.45em;
      border-top: 1px solid #ddd;
      padding-top: 0.55em;
      font-size: 1.35em;
    }
    h3 {
      margin-top: 1.1em;
      font-size: 1.08em;
    }
    p {
      margin: 0.8em 0;
      text-align: justify;
    }
    ul, ol {
      margin: 0.7em 0 0.9em 1.3em;
    }
    li {
      margin: 0.25em 0;
    }
    hr {
      border: none;
      border-top: 1px solid #ccc;
      margin: 1.2em 0;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1em 0 1.2em;
      font-size: 0.94em;
    }
    th, td {
      border: 1px solid #cfcfcf;
      padding: 0.45em 0.55em;
      vertical-align: top;
    }
    th {
      background: #f7f7f7;
      text-align: left;
    }
    @media print {
      body {
        max-width: none;
        padding: 0;
        font-size: 11pt;
      }
      h2, h3 {
        page-break-after: avoid;
      }
      table, pre, blockquote {
        page-break-inside: avoid;
      }
    }
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>{css}</style>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js"></script>
</head>
<body>
{body_html}
</body>
</html>
"""


def render_html(title: str) -> None:
    body_html = pypandoc.convert_file(
        str(SRC),
        "html5",
        format="md",
        extra_args=[
            "--from=markdown+tex_math_dollars+raw_tex+pipe_tables+table_captions",
            "--to=html5",
            "--mathjax",
        ],
    )
    HTML_OUT.write_text(build_html(title, body_html), encoding="utf-8")


def build_reference_doc() -> Path | None:
    return None


def render_docx(title: str) -> None:
    reference_doc = build_reference_doc()
    extra_args = [
        "--standalone",
        "--from=markdown+tex_math_dollars+raw_tex+pipe_tables+table_captions",
    ]
    if reference_doc is not None:
        extra_args.append(f"--reference-doc={reference_doc}")

    try:
        pypandoc.convert_file(
            str(SRC),
            "docx",
            format="md",
            outputfile=str(DOCX_OUT),
            extra_args=extra_args,
        )
    finally:
        if reference_doc is not None and reference_doc.exists():
            reference_doc.unlink()

    subprocess.run([sys.executable, str(POSTPROCESS), str(DOCX_OUT)], check=True)


def render_pdf() -> None:
    if not DOCX2PDF.exists():
        return
    subprocess.run([str(DOCX2PDF), str(DOCX_OUT), str(PDF_OUT)], check=True)


def render() -> None:
    raw = SRC.read_text(encoding="utf-8")
    title = extract_title(raw)
    render_html(title)
    render_docx(title)
    render_pdf()


if __name__ == "__main__":
    render()
