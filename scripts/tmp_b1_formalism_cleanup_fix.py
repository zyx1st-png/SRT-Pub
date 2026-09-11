from pathlib import Path
import re

p = Path("Core_Law/SRT_L1_Formalism.md")
text = p.read_text(encoding="utf-8")

# Repair the B1 balance equation using a literal replacement line, avoiding Python escape corruption.
pattern = re.compile(r"^\s*\\?sigma_\{sr\}\^\{sub\}\s*:.*$", re.MULTILINE)
replacement = r"   \sigma_{sr}^{sub} : \alpha w\phi(\sigma_{sr}^{sub}) = \beta i + \lambda_{trace}T\sigma_{sr}^{sub}."
text, n = pattern.subn(lambda _m: replacement, text, count=1)
if n != 1:
    # The prior generated line may contain control characters. Match by the visible tail instead.
    pattern2 = re.compile(r"^.*sigma_\{sr\}\^\{sub\}.*lambda_\{trace\}T.*$", re.MULTILINE)
    text, n = pattern2.subn(lambda _m: replacement, text, count=1)
if n != 1:
    raise SystemExit(f"could not repair sigma_sub balance line; matches={n}")

old = '- `χ(σ; σ_{self})` 是**二阶凝结跳跃函数**：在 `σ ≈ σ_{self}` 附近为一类光滑阶跃，对应 `SRT_Individuation.md` 的第二相变（自我意识凝结）；在此之前 χ ≈ 1，在此之后 χ > 1（出现"关于 θ 的 θ"的二阶写回增益）'
new = '- `χ(σ; σ_{self})` 是**二阶 writeback 增益 kernel**：在 `σ ≈ σ_{self}` 附近可取一类光滑阶跃，用于建模 second-order self-model / self-description writeback 的激活；在此之前 χ ≈ 1，在此之后 χ > 1。该 kernel 不定义 self-consciousness / consciousness。'
if old not in text:
    raise SystemExit("legacy chi interpretation line not found")
text = text.replace(old, new, 1)

# Retype the remaining local kernel label so the mathematics is not narrated as an ontology transition.
text = text.replace("#### 有效二阶相变核（valid second-phase-transition kernel）", "#### 有效二阶 writeback kernel（valid second-order writeback kernel）", 1)
text = text.replace("称 `\\chi` 是**有效二阶相变核**，当且仅当满足下列四条结构属性：", "称 `\\chi` 是**有效二阶 writeback kernel**，当且仅当满足下列四条结构属性：", 1)

p.write_text(text, encoding="utf-8")
print("B1 formalism cleanup fix applied")
