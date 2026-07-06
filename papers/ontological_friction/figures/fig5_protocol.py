"""
Figure 5: Experimental Protocol + Predicted Nonlinear Cost Curve
Panel A: Protocol timeline for H72 + H-NEURO-EXEC-01
Panel B: Predicted nonlinear cost curve vs linear alternative
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.5, 14.5), gridspec_kw={'height_ratios': [1.05, 1]})
fig.patch.set_facecolor("white")

# ── Panel A: Protocol Timeline ──
ax1.set_xlim(0, 12)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('A. Experimental Protocol (Single Session)', fontsize=18, fontweight='bold', pad=16)

# Timeline blocks
blocks = [
    (0.5, 8.0, 2.5, 1.2, 'Semi-structured\nInterview', '#E3F2FD', '15 min', '#1565C0'),
    (3.5, 8.0, 2.5, 1.2, 'Behavioral Battery\n(Task switching, Stroop,\nWCST)', '#FFF3E0', '20 min', '#E65100'),
    (6.5, 8.0, 2.0, 1.2, 'Resting HRV\n+ SCR', '#E8F5E9', '5 min', '#2E7D32'),
    (9.0, 8.0, 2.0, 1.2, 'Cortisol\n(optional)', '#F3E5F5', '2 min', '#6A1B9A'),
]

for x, y, w, h, label, color, dur, ec in blocks:
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor=ec, linewidth=1.5)
    ax1.add_patch(box)
    label_size = 12 if label.startswith('Behavioral Battery') else 15
    ax1.text(x + w/2, y + h/2 + 0.1, label, ha='center', va='center',
             fontsize=label_size, fontweight='bold')
    ax1.text(x + w/2, y - 0.3, dur, ha='center', va='center', fontsize=12, color='#1a1a1a')

# Arrows between blocks
for x1, x2 in [(3.0, 3.5), (6.0, 6.5), (8.5, 9.0)]:
    ax1.annotate('', xy=(x2, 8.6), xytext=(x1, 8.6),
                 arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

# Analysis pipeline
ax1.text(6.0, 6.0, 'Analysis Pipeline', ha='center', va='center',
         fontsize=18, fontweight='bold', color='#333')

analysis = [
    (1.5, 4.5, 'Language-feature\nExtraction', '#E3F2FD', '#1565C0'),
    (4.0, 4.5, 'Composite\nZ-score', '#FFF3E0', '#E65100'),
    (6.5, 4.5, 'Multilevel\nCorrelation', '#E8F5E9', '#2E7D32'),
    (9.0, 4.5, 'Latent Factor\nModel', '#F3E5F5', '#6A1B9A'),
]

for x, y, label, color, ec in analysis:
    box = FancyBboxPatch((x-0.8, y-0.5), 1.8, 1.0, boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor=ec, linewidth=1.2)
    ax1.add_patch(box)
    ax1.text(x+0.1, y, label, ha='center', va='center', fontsize=13)

for x1, x2 in [(2.5, 3.2), (5.0, 5.7), (7.5, 8.2)]:
    ax1.annotate('', xy=(x2, 4.5), xytext=(x1, 4.5),
                 arrowprops=dict(arrowstyle='->', color='#999', lw=1.2))

# Output labels
outputs = ['μ_sem', 'Ψ_f^beh', 'r(μ_sem, Ψ_f)', 'λ loadings']
for i, (x, _, _, _, _) in enumerate(analysis):
    ax1.text(x+0.1, 3.4, outputs[i], ha='center', va='center', fontsize=9,
             fontstyle='italic', color='#1a1a1a')

# Study design box
design_text = ('Study Design\n'
               'N = 120 healthy adults\n'
               '3 sessions × 6 weeks\n'
               'test-retest reliability')
ax1.text(6.0, 1.5, design_text, ha='center', va='center', fontsize=13,
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#FAFAFA', edgecolor='#999'))

# ── Panel B: Nonlinear Cost Curve ──
ax2.set_title('B. Predicted Task-Switch Cost Under $\\Psi_f$ Load', fontsize=18, fontweight='bold', pad=14)

load = np.linspace(0, 1, 100)
# Linear model
linear_cost = 50 + 200 * load
# Nonlinear (bandwidth saturation) model
nonlinear_cost = 50 + 80 * load + 500 * load**3

ax2.plot(load, linear_cost, '--', color='#9E9E9E', linewidth=3.0, label='Linear model (additive resources)')
ax2.plot(load, nonlinear_cost, '-', color='#C62828', linewidth=4.0, label='Bandwidth saturation model')

# Saturation zone
ax2.axvspan(0.7, 1.0, alpha=0.1, color='#C62828')
ax2.text(0.85, 100, '"Know but\ncan\'t do"\nzone', ha='center', va='center',
         fontsize=20, fontweight='bold', color='#C62828', alpha=0.7)

# Load level markers
levels = [0.0, 0.33, 0.67, 1.0]
level_labels = ['No load', 'Low\ncognitive', 'High\ncognitive', 'Stress\ninduction']
for lv, ll in zip(levels, level_labels):
    ax2.axvline(x=lv, color='#E0E0E0', linewidth=0.8, linestyle=':')
ax2.set_xticks(levels)
ax2.set_xticklabels(level_labels, fontsize=18, color='#1a1a1a')

ax2.set_xlabel('$\\Psi_f$ Load Level (normalized)', fontsize=22, labelpad=10)
ax2.set_ylabel('Task-Switch Cost (ms)', fontsize=22)
ax2.set_xlim(-0.05, 1.1)
ax2.set_ylim(0, 700)
ax2.tick_params(axis='both', labelsize=17, width=1.5, length=6)
ax2.legend(loc='upper left', fontsize=18, framealpha=0.9)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Falsification note
ax2.text(0.73, 585, 'Falsification: $R^2_{\\mathrm{linear}} \\geq R^2_{\\mathrm{quadratic}}$',
         ha='center', va='center', fontsize=18,
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF9C4', edgecolor='#F9A825'))

plt.subplots_adjust(left=0.08, right=0.97, top=0.95, bottom=0.08, hspace=0.2)
plt.savefig('fig5_protocol.png',
            dpi=300, bbox_inches='tight', pad_inches=0.16, facecolor='white')
plt.close()
print("Figure 5 saved.")
