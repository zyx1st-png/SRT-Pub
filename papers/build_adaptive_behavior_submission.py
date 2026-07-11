"""Export CostlySelectiveClosure_v16.md into Adaptive Behavior (SAGE) formats:
a sagej LaTeX file (for Overleaf) and a pandoc-generated .docx.

Deterministic transformation of the canonical Markdown source; run from a clean
checkout to regenerate the committed derivatives. Requires `pandoc` on PATH.

    python papers/build_adaptive_behavior_submission.py
"""
import re
import subprocess
from pathlib import Path

PAPERS = Path(__file__).resolve().parent
SRC = PAPERS / "CostlySelectiveClosure_v16.md"
text = SRC.read_text(encoding="utf-8")

# ---------- backtick -> math / plain / italic ----------
MATH = {
 'V':'V','d':'d','N':'N','q':'q',
 'Ψ_f':r'\Psi_f','η':r'\eta','κ_i':r'\kappa_i',
 'P_sel':r'P_{\mathrm{sel}}','d_cog':r'd_{\mathrm{cog}}','d_eff':r'd_{\mathrm{eff}}',
 'E_0':'E_0','x_t':'x_t','Omega_t':r'\Omega_t',
 'G_hat_theta':r'\hat{G}_\theta', r'\hat{G}_theta':r'\hat{G}_\theta',
 'lambda_i':r'\lambda_i','tau_temporal':r'\tau_{\mathrm{temporal}}','V_concern':r'V_{\mathrm{concern}}',
 'A(sigma)':r'A(\sigma)','w_A':'w_A','w_V':'w_V','w_tau':r'w_\tau',
 'Ψ_f ~ 0':r'\Psi_f \sim 0','V > 0':'V > 0','η = 0':r'\eta = 0','η > 0':r'\eta > 0','η ∈ [0,1]':r'\eta \in [0,1]',
 'd ~ 0':r'd \sim 0','d ~ 1-3':r'd \sim 1\text{--}3','d ~ 5-20':r'd \sim 5\text{--}20','d ~ 10^2-10^4':r'd \sim 10^{2}\text{--}10^{4}',
 '10^2-10^4':r'10^{2}\text{--}10^{4}',  # Table 1 cell (bare, tilde is plain text beside it)
 'E_0 = 6':'E_0 = 6','E_max = 10':r'E_{\max} = 10','T = 50':'T = 50','γ = 0.97':r'\gamma = 0.97',
 'd_eff = (Σλ_i)² / Σλ_i²':r'd_{\mathrm{eff}} = (\sum_i \lambda_i)^2 / \sum_i \lambda_i^2',
 'p < 0.0001':'p < 0.0001',
 '{0.85, 0.55}':r'\{0.85, 0.55\}','{1.2, 1.4, 1.6}':r'\{1.2, 1.4, 1.6\}',
 'P(CC | s) = P₁(C | s₁) · P₂(C | s₂)':r'P(CC \mid s) = P_1(C \mid s_1)\, P_2(C \mid s_2)',
}
NUMBERS = {'1.0','0.0','0.04','0.6','1.4','1.5','+1.0','-0.15','-0.3','-0.44','-0.45',
           '0.03','0.05','0.07','0.16','0.50','0.54','0.55','1.8','2.0',
           '2,292','0.485','0.030','0.454','0.546','0.043','+0.503','+0.454',
           '[0.346, 0.557]','[0.385, 0.612]'}
WORDS = {'cooperate','solo','rest'}


def bt(m):
    s = m.group(1)
    if s in MATH:    return f"${MATH[s]}$"
    if s in NUMBERS: return s
    if s in WORDS:   return f"*{s}*"
    return f"${s}$"


def convert(t):
    blocks = []
    t = re.sub(r"\$\$.*?\$\$", lambda mm: blocks.append(mm.group(0)) or f"@@B{len(blocks)-1}@@", t, flags=re.S)
    t = re.sub(r"`([^`]+)`", bt, t)
    for i, b in enumerate(blocks):
        t = t.replace(f"@@B{i}@@", b)
    return t


def longtable_to_twocolumn(t):
    """The sagej class (Afour) sets a two-column body, where pandoc's default
    `longtable` is illegal ("longtable not in 1-column mode"). Convert each
    longtable into a full-width `table*` float wrapping a plain `tabular`. The
    column spec and body rows are preserved verbatim; a pandoc table caption and
    label (from `: caption {#tab:id}` in the Markdown) are hoisted above the
    tabular so the float is numbered, and all longtable header/footer scaffolding
    — including the `\\endfirsthead` duplicate header pandoc emits for captioned
    tables — is dropped."""
    def convert_block(m):
        block = m.group(0)
        cap = ""
        cm = re.search(r"\\caption\{.*?\}\\label\{[^}]*\}\\tabularnewline\n", block, re.S)
        if cm:                                   # hoist caption+label above the tabular
            cap = cm.group(0).replace("\\tabularnewline\n", "\n")
            block = block.replace(cm.group(0), "", 1)
        block = re.sub(r"\\endfirsthead\n.*?\\endhead\n", "", block, flags=re.S)  # drop dup header
        block = block.replace("\\toprule\\noalign{}", "\\toprule")
        block = block.replace("\\midrule\\noalign{}", "\\midrule")
        block = block.replace("\\endhead\n", "")                                 # uncaptioned case
        block = re.sub(r"\\bottomrule\\noalign\{\}\n\\endlastfoot\n", "", block)
        block = block.replace(r"\begin{longtable}[]{",
                              "\\begin{table*}[t]\n\\centering\n" + cap + "\\begin{tabular}{", 1)
        block = block.replace(r"\end{longtable}",
                              "\\bottomrule\n\\end{tabular}\n\\end{table*}")
        return block
    return re.sub(r"\\begin\{longtable\}.*?\\end\{longtable\}", convert_block, t, flags=re.S)


def crossref_tables(t):
    """Replace the hard-coded prose "Table 1"/"Table 2" with LaTeX cross-refs to
    the captioned floats (the Markdown keeps the readable literals). Only the two
    canonical-case and borderline-case tables are cited by number in the text."""
    t = t.replace("Table 1", "Table~\\ref{tab:canonical-cases}")
    t = t.replace("Table 2", "Table~\\ref{tab:borderline-cases}")
    return t


def fullwidth_figures(t):
    """Figures 2, 3 and 4 are designed at full text width; in the two-column
    sagej layout a single-column `figure` renders them too small. Promote them to
    full-width `figure*` floats spanning both columns, and size them to the full
    `\\linewidth` (not 0.9) with no fixed height cap so they are not needlessly
    shrunk. Figure 1 is a single-panel schematic and stays one column."""
    targets = ("figure2_design", "figure3_results", "figure4_common_state_probe")
    def star(m):
        block = m.group(0)
        if any(name in block for name in targets):
            block = block.replace(r"\begin{figure}", r"\begin{figure*}", 1)
            block = block.replace(r"\end{figure}", r"\end{figure*}", 1)
            block = block.replace(
                "width=0.9\\linewidth,height=\\textheight,keepaspectratio",
                "width=\\linewidth,keepaspectratio")
        return block
    return re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", star, t, flags=re.S)


# ---------- split ----------
title = next(l[2:].strip() for l in text.splitlines() if l.startswith("# "))
abstract = re.search(r"## Abstract\n\n(.+?)\n\n\*\*Keywords\*\*", text, re.S).group(1).strip()
keywords = re.search(r"\*\*Keywords\*\*:\s*(.+)", text).group(1).strip()
ref_i, app_i = text.index("## References"), text.index("## Appendix")
body = text[text.index("## 1. Introduction"):ref_i].strip()
refs = text[ref_i:app_i].strip()
appendix = text[app_i:].strip()

abstract_c = convert(abstract)
body_c = convert(body)
appendix_c = convert(appendix)

# merge "image + **Figure N.** caption" into a single captioned image (with width)
body_c = re.sub(r"!\[[^\]]*\]\(([^)]+)\)\n\n\*\*Figure \d+\.\*\*\s*(.+)",
                lambda m: f"![{m.group(2).strip()}]({m.group(1)}){{width=90%}}", body_c)

# references as plain paragraphs (drop "- " bullets, drop heading)
refs_paras = "\n\n".join(l[2:].strip() for l in refs.splitlines()
                         if l.strip().startswith("- "))
refs_paras = convert(refs_paras)


def pandoc(md, args):
    r = subprocess.run(["pandoc", "-f", "markdown", "--wrap=preserve"] + args,
                       input=md, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr)
    return r.stdout


# ================= LaTeX (sagej) =================
body_latex_md = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)(\{[^}]*\})",
                       lambda m: f"![{m.group(1)}]({Path(m.group(2)).stem}.pdf){m.group(3)}", body_c)
frag = pandoc(body_latex_md, ["-t", "latex"])
frag = crossref_tables(frag)
abstract_tex = pandoc(abstract_c, ["-t", "latex"])
refs_tex = pandoc(refs_paras, ["-t", "latex"])
appendix_tex = pandoc(appendix_c, ["-t", "latex"])

UNI = {'ρ':r'\rho','−':'-','∞':r'\infty','×':r'\times','≈':r'\approx','≤':r'\le','≥':r'\ge',
       '∈':r'\in','Σ':r'\sum','λ':r'\lambda','η':r'\eta','Ψ':r'\Psi','κ':r'\kappa','γ':r'\gamma',
       'τ':r'\tau','σ':r'\sigma','Ω':r'\Omega','≠':r'\neq','→':r'\to','∼':r'\sim','²':r'^{2}'}
uni_lines = "\n".join(rf"\newunicodechar{{{c}}}{{\ensuremath{{{l}}}}}" for c, l in UNI.items())

preamble = rf"""\documentclass[Afour,sageh,times,doublespace]{{sagej}}

\usepackage[utf8]{{inputenc}}
\usepackage[T1]{{fontenc}}
\usepackage{{moreverb,url}}
\usepackage{{graphicx}}
\usepackage{{amsmath,amssymb}}
\usepackage{{booktabs,longtable,array,calc}}
\usepackage{{newunicodechar}}
{uni_lines}
\newunicodechar{{–}}{{--}}
% pandoc-fragment helper macros (this file is assembled without pandoc's template)
\providecommand{{\tightlist}}{{\setlength{{\itemsep}}{{0pt}}\setlength{{\parskip}}{{0pt}}}}
\providecommand{{\real}}[1]{{#1}}
\providecommand{{\pandocbounded}}[1]{{#1}}
\usepackage[colorlinks,bookmarksopen,bookmarksnumbered,citecolor=red,urlcolor=red]{{hyperref}}

\graphicspath{{{{costly_selective_closure_supplement/figures/}}}}

\begin{{document}}

\runninghead{{Zhang}}

\title{{{title}}}

\author{{Yuxin Zhang\affilnum{{1}}}}

\affiliation{{\affilnum{{1}}Independent Researcher}}

\corrauth{{Yuxin Zhang, Independent Researcher.}}

\email{{zyx1st@gmail.com}}

\begin{{abstract}}
{abstract_tex.strip()}
\end{{abstract}}

\keywords{{{keywords}}}

\maketitle

"""
tex = (preamble + frag.strip()
       + "\n\n\\section*{References}\n\n" + refs_tex.strip()
       + "\n\n" + appendix_tex.strip()
       + "\n\n\\end{document}\n")
tex = longtable_to_twocolumn(tex)
tex = fullwidth_figures(tex)
(PAPERS / "CostlySelectiveClosure_AdaptiveBehavior_submission.tex").write_text(tex, encoding="utf-8")
print("wrote .tex  (%d bytes)" % len(tex))

# ================= DOCX =================
docx_md = f"""**Yuxin Zhang**  \\
Independent Researcher  \\
zyx1st@gmail.com

## Abstract

{abstract_c}

**Keywords:** {keywords}

{body_c}

## References

{refs_paras}

{appendix_c}
"""
(PAPERS / "_docx_src.md").write_text(docx_md, encoding="utf-8")
r = subprocess.run(["pandoc", "_docx_src.md", "--wrap=preserve",
                    "--metadata", f"title={title}",
                    "-o", "CostlySelectiveClosure_AdaptiveBehavior_submission.docx"],
                   cwd=PAPERS, capture_output=True, text=True)
if r.returncode:
    raise RuntimeError(r.stderr)
(PAPERS / "_docx_src.md").unlink()
print("wrote .docx")
