from __future__ import annotations

import html
import re
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "ALIFE2026_SelectiveRealityConstruction_v15_anonymous_submission.md"
HTML_OUT = ROOT / "ALIFE2026_SelectiveRealityConstruction_v15_anonymous_submission.html"


def extract_title(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    title = ""
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            body_start = i + 1
            break
    if not title:
        raise ValueError("Could not find title line.")
    body_lines = lines[body_start:]
    filtered = [
        line
        for line in body_lines
        if line.strip() not in {
            "[Anonymous Submission for Review]",
            "[Author details withheld]",
            "Special Session: Artificial Life as Experimental Philosophy",
        }
    ]
    return title, "\n".join(filtered).strip()


def preprocess_inline_notation(text: str) -> str:
    replacements = {
        "`Ψ_f`": '<span class="var">Ψ<sub>f</sub></span>',
        "`Psi_f`": '<span class="var">Ψ<sub>f</sub></span>',
        "`η`": '<span class="var">η</span>',
        "`eta`": '<span class="var">η</span>',
        "`d_cog`": '<span class="var">d<sub>cog</sub></span>',
        "`L0`": '<span class="var">L<sub>0</sub></span>',
        "`L1`": '<span class="var">L<sub>1</sub></span>',
        "`L2`": '<span class="var">L<sub>2</sub></span>',
        "`V_proxy = 1 - P(restore | failure)`": '<span class="var">V<sub>proxy</sub> = 1 - P(restore | failure)</span>',
        "`P_sel`": '<span class="var">P<sub>sel</sub></span>',
        "`V_concern`": '<span class="var">V<sub>concern</sub></span>',
        "`tau_temporal`": '<span class="var">τ<sub>temporal</sub></span>',
        "`Omega_t`": '<span class="var">Ω<sub>t</sub></span>',
        "`x_t`": '<span class="var">x<sub>t</sub></span>',
        "`d_eff`": '<span class="var">d<sub>eff</sub></span>',
        "`D_eff`": '<span class="var">D<sub>eff</sub></span>',
        "`G_hat_theta`": '<span class="var">Ĝ<sub>θ</sub></span>',
        r"`\hat{G}_theta`": '<span class="var">Ĝ<sub>θ</sub></span>',
        r"`\hat{G}_{\theta}`": '<span class="var">Ĝ<sub>θ</sub></span>',
        "`eta in [0,1]`": '<span class="var">η ∈ [0,1]</span>',
        "`eta = 0`": '<span class="var">η = 0</span>',
        "`eta > 0`": '<span class="var">η &gt; 0</span>',
        "`lambda_i`": '<span class="var">λ<sub>i</sub></span>',
        "`A(sigma)`": '<span class="var">A(σ)</span>',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def render_equation(expr: str) -> str:
    expr = " ".join(expr.split())
    known = {
        r"x_{t+1} = (1 - \eta)\,\hat{G}_{\theta}[\Omega_t] + \eta x_t":
            "x<sub>t+1</sub> = (1 − η) Ĝ<sub>θ</sub>[Ω<sub>t</sub>] + ηx<sub>t</sub>",
        r"d = D_{eff}(\hat{G}) = \frac{(\sum_i \lambda_i)^2}{\sum_i \lambda_i^2}":
            "d = D<sub>eff</sub>(Ĝ) = (Σ<sub>i</sub> λ<sub>i</sub>)² / Σ<sub>i</sub> λ<sub>i</sub><sup>2</sup>",
        r"d_{cog} \approx w_A A(\sigma) + w_V \log V_{concern} + w_\tau \tau_{temporal}":
            "d<sub>cog</sub> ≈ w<sub>A</sub>A(σ) + w<sub>V</sub> log V<sub>concern</sub> + w<sub>τ</sub>τ<sub>temporal</sub>",
        r"\frac{dq}{dt} \le \kappa_1 P_{sel} - \kappa_2 \Psi_f - \kappa_3 N":
            "(dq/dt) ≤ κ<sub>1</sub>P<sub>sel</sub> − κ<sub>2</sub>Ψ<sub>f</sub> − κ<sub>3</sub>N",
    }
    rendered = known.get(expr, html.escape(expr))
    return f'\n<div class="equation">{rendered}</div>\n'


def replace_display_math(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        return render_equation(match.group(1).strip())

    return re.sub(r"\$\$(.*?)\$\$", repl, text, flags=re.S)


def split_frontmatter(body: str) -> tuple[str, str]:
    marker = "**Keywords**:"
    if marker not in body:
        raise ValueError("Could not find keywords marker.")
    before, after = body.split(marker, 1)
    keywords_line, remainder = after.split("\n", 1)
    front = before + marker + keywords_line
    return front.strip(), remainder.strip()


def md_to_html(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=[
            "extra",
            "toc",
            "sane_lists",
            "smarty",
        ],
        output_format="html5",
    )


def wrap_tables(html_text: str) -> str:
    return re.sub(
        r"(<table>.*?</table>)",
        r'<div class="fullwidth-table">\1</div>',
        html_text,
        flags=re.S,
    )


def main() -> None:
    raw = SRC.read_text(encoding="utf-8")
    title, body = extract_title(raw)
    body = preprocess_inline_notation(body)
    body = replace_display_math(body)
    front, remainder = split_frontmatter(body)

    front_html = md_to_html(front)
    body_html = md_to_html(remainder)
    body_html = wrap_tables(body_html)

    css = """
    @page {
      size: Letter;
      margin: 0.55in 0.55in 0.65in 0.55in;
    }
    body {
      font-family: "Times New Roman", Times, serif;
      color: #111;
      margin: 0;
      padding: 0;
      background: white;
      font-size: 10pt;
      line-height: 1.18;
    }
    .page {
      padding: 0;
      margin: 0;
    }
    h1.title {
      font-size: 18pt;
      line-height: 1.1;
      text-align: center;
      margin: 0 0 6pt 0;
      font-weight: 700;
    }
    .meta {
      text-align: center;
      font-size: 9.2pt;
      margin-bottom: 10pt;
    }
    .frontmatter {
      font-size: 9.4pt;
      margin-bottom: 8pt;
    }
    .frontmatter h2 {
      font-size: 10pt;
      margin: 8pt 0 4pt 0;
      border: none;
      page-break-after: avoid;
    }
    .frontmatter p {
      margin: 0 0 4pt 0;
      text-align: justify;
    }
    .twocol {
      column-count: 2;
      column-gap: 0.32in;
      column-fill: auto;
      font-size: 9.2pt;
    }
    .twocol h2,
    .twocol h3,
    .twocol .equation,
    .twocol .MathJax_Display,
    .fullwidth-table {
      break-inside: avoid;
    }
    .twocol h2 {
      column-span: all;
      font-size: 11pt;
      margin: 10pt 0 5pt 0;
      page-break-after: avoid;
      border-top: 0.5pt solid #999;
      padding-top: 4pt;
    }
    .twocol h3 {
      font-size: 9.7pt;
      margin: 7pt 0 3pt 0;
      page-break-after: avoid;
    }
    .twocol p,
    .twocol li {
      text-align: justify;
      margin: 0 0 4pt 0;
    }
    .twocol ol,
    .twocol ul {
      margin: 0 0 6pt 16pt;
      padding: 0;
    }
    .twocol table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.2pt;
      margin: 5pt 0 7pt 0;
    }
    .twocol th,
    .twocol td {
      border: 0.5pt solid #888;
      padding: 3pt 4pt;
      vertical-align: top;
    }
    .twocol code {
      font-family: inherit;
      font-size: inherit;
      background: transparent;
      padding: 0;
    }
    .equation {
      font-family: "Times New Roman", Times, serif;
      font-size: 8.5pt;
      text-align: center;
      margin: 5pt 0 7pt 0;
      border: 0.5pt solid #ddd;
      padding: 3pt 5pt;
    }
    .twocol hr {
      display: none;
    }
    .var {
      font-style: italic;
      white-space: nowrap;
    }
    .fullwidth-table {
      column-span: all;
      margin: 6pt 0 8pt 0;
      break-inside: avoid-page;
      page-break-inside: avoid;
    }
    .fullwidth-table table {
      width: 100%;
      table-layout: fixed;
      font-size: 7.7pt;
      margin: 0;
    }
    .fullwidth-table th,
    .fullwidth-table td {
      overflow-wrap: anywhere;
      word-break: normal;
      hyphens: auto;
      padding: 3pt 4pt;
    }
    .fullwidth-table tr {
      break-inside: avoid;
      page-break-inside: avoid;
    }
    .fullwidth-table th:nth-child(1),
    .fullwidth-table td:nth-child(1) {
      width: 28%;
    }
    .fullwidth-table th:nth-child(2),
    .fullwidth-table td:nth-child(2) {
      width: 10%;
    }
    .fullwidth-table th:nth-child(3),
    .fullwidth-table td:nth-child(3) {
      width: 18%;
    }
    .fullwidth-table th:nth-child(4),
    .fullwidth-table td:nth-child(4) {
      width: 11%;
    }
    .fullwidth-table th:nth-child(5),
    .fullwidth-table td:nth-child(5) {
      width: 11%;
    }
    .fullwidth-table th:nth-child(6),
    .fullwidth-table td:nth-child(6) {
      width: 22%;
    }
    h2#4-canonical-cases {
      break-before: page;
      page-break-before: always;
    }
    """

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{html.escape(title)}</title>
  <style>{css}</style>
</head>
<body>
  <div class="page">
    <h1 class="title">{html.escape(title)}</h1>
    <div class="meta">Anonymous Submission for Review<br>Special Session: Artificial Life as Experimental Philosophy</div>
    <div class="frontmatter">{front_html}</div>
    <div class="twocol">{body_html}</div>
  </div>
</body>
</html>
"""
    HTML_OUT.write_text(html_doc, encoding="utf-8")
    print(f"Wrote {HTML_OUT}")


if __name__ == "__main__":
    main()
