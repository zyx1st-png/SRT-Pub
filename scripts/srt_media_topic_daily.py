#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1] / "SRT"
QUEUE = ROOT / "_SRT_MEDIA_QUEUE.md"


def append_topic_block(topic: str, direction: str, why: str, core_docs: str, anchors: str, hooks: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    block = f"""

- Topic: {topic}
- Direction (大众向/学术向): {direction}
- Why Now (选题原因): {why}
- Internal Mapping:
  - Core Docs: {core_docs}
  - Equation/Axiom Anchors: {anchors}
  - Experiment/Falsification Hooks: {hooks}
- Platforms (recommended):
  - Zhihu: medium
  - WeChat: medium
  - Toutiao: medium
  - Twitter/X: medium
  - Substack: medium
  - Medium: medium
- Risk Notes: 需明确边界声明，避免过度外推。
- Publish Window: next 7 days
- Generated At: {now} (Asia/Shanghai)
"""
    text = QUEUE.read_text()
    QUEUE.write_text(text.rstrip() + block + "\n")


def main():
    # baseline auto topic (can be replaced by scheduler payload)
    append_topic_block(
        topic="从‘控制性幻觉’到SRT：如何把感知差异变成可检验命题",
        direction="双向（先大众后学术）",
        why="近期信号材料集中于主动推断与感知分歧，具高时效与方法学价值。",
        core_docs="Neuroscience/SRT_Neuro_Experiments.md; Core/SRT_Core_22_Equations.md",
        anchors="\\hat{G}_\\theta 映射；L_0→L_1 选择路径；\\Psi_f 维护成本",
        hooks="固定输入下参数校准模型解释增益；z-score/CUSUM 变点检测"
    )
    print(QUEUE)


if __name__ == "__main__":
    main()
