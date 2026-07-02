"""
Figure 1: Hierarchical control architecture
Panel A: candidate policy space -> resource-bounded selection/gating -> active state -> slow constraints
Panel B: budget diagram showing the "know but can't do" zone
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.5, 14.0))
fig.patch.set_facecolor("white")

# ── Panel A: Hierarchical Control Architecture ──
ax1.set_xlim(0, 10.8)
ax1.set_ylim(0, 8.4)
ax1.axis('off')
ax1.set_title('A. Hierarchical Control Architecture', fontsize=18, fontweight='bold', pad=16)

# Domain boxes
domains = [
    (1.1, 4.0, 'Candidate\nPolicies', '#E8D5F5', '(available options)'),
    (4.3, 4.0, 'Active\nState', '#D5E8F5', '(executed policy)'),
    (7.5, 4.0, 'Slow\nConstraints', '#D5F5E0', '(habits and priors)'),
]

for x, y, label, color, sub in domains:
    box = FancyBboxPatch((x-0.9, y-1.2), 2.4, 2.4,
                          boxstyle="round,pad=0.15", facecolor=color,
                          edgecolor='#333333', linewidth=1.5)
    ax1.add_patch(box)
    ax1.text(x+0.3, y+0.2, label, ha='center', va='center', fontsize=15, fontweight='bold')
    ax1.text(x+0.3, y-0.8, sub, ha='center', va='center', fontsize=13, fontstyle='italic', color='#1a1a1a')

# Arrows
arrow_style = dict(arrowstyle='->', color='#333333', lw=2.6, mutation_scale=18)
ax1.annotate('', xy=(3.4, 4.0), xytext=(2.6, 4.0), arrowprops=arrow_style)
ax1.annotate('', xy=(6.6, 4.0), xytext=(5.8, 4.0), arrowprops=arrow_style)

# Operator label
ax1.text(3.0, 5.05, 'Selection /\ngating', ha='center', va='center', fontsize=15, fontweight='bold', color='#8B0000')
ax1.text(3.0, 5.75, 'resource-bounded', ha='center', va='center', fontsize=11, color='#8B0000')

ax1.text(6.2, 4.8, 'Stabilize', ha='center', va='center', fontsize=13, color='#006400')

# Feedback arrow L2 → L0
ax1.annotate('', xy=(1.1, 2.2), xytext=(7.8, 2.2),
             arrowprops=dict(arrowstyle='->', color='#999999', lw=2.0,
                           connectionstyle='arc3,rad=0.0', linestyle='--'))
ax1.text(4.45, 1.7, 'Shapes future selection', ha='center', va='center',
         fontsize=13, fontstyle='italic', color='#1a1a1a')

# Friction annotation
ax1.text(4.7, 7.2, '$\\Psi_f^{\\mathrm{ctrl}} \\approx \\int u^\\top R u\\,dt$',
         ha='center', va='center', fontsize=16, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF3E0', edgecolor='#E65100', linewidth=1.5))

# ── Panel B: Thermodynamic Budget Diagram ──
ax2.set_xlim(0, 11.4)
ax2.set_ylim(0, 8.4)
ax2.axis('off')
ax2.set_title('B. Selection Power Budget and the Knowing–Doing Gap', fontsize=18, fontweight='bold', pad=16)

# Bar chart concept
bar_x = [2.2, 5.2, 8.2]
bar_labels = ['Healthy\nAgent', 'Stressed\nAgent', 'Clinical\nBreakdown']

# Selection power bars (full height)
p_sel_heights = [6.0, 6.0, 6.0]
# Friction costs
friction_heights = [2.0, 4.5, 7.0]
# Noise costs
noise_heights = [0.8, 1.0, 1.2]

for i, (x, label) in enumerate(zip(bar_x, bar_labels)):
    # P_sel bar (background)
    bar_bg = FancyBboxPatch((x-0.7, 1.0), 1.4, p_sel_heights[i],
                             boxstyle="round,pad=0.05", facecolor='#C8E6C9',
                             edgecolor='#2E7D32', linewidth=1.0, alpha=0.5)
    ax2.add_patch(bar_bg)

    # Friction bar (foreground)
    bar_fr = FancyBboxPatch((x-0.6, 1.0), 0.6, friction_heights[i],
                             boxstyle="round,pad=0.03", facecolor='#FFCDD2',
                             edgecolor='#C62828', linewidth=1.0)
    ax2.add_patch(bar_fr)

    # Noise bar
    bar_no = FancyBboxPatch((x, 1.0), 0.6, noise_heights[i],
                             boxstyle="round,pad=0.03", facecolor='#FFE0B2',
                             edgecolor='#E65100', linewidth=1.0)
    ax2.add_patch(bar_no)

    ax2.text(x, 0.5, label, ha='center', va='center', fontsize=16)

# Threshold line
ax2.axhline(y=6.95, xmin=0.08, xmax=0.87, color='#333333', linestyle='--', linewidth=1.3)
ax2.text(9.65, 6.95, '$\\alpha \\cdot P_{\\mathrm{sel}}$', ha='left', va='center', fontsize=17, fontweight='bold')

# "Know but can't do" zone
zone = FancyBboxPatch((6.25, 6.65), 2.95, 1.3,
                       boxstyle="round,pad=0.1", facecolor='#FFEBEE',
                       edgecolor='#C62828', linewidth=1.5, linestyle='--', alpha=0.7)
ax2.add_patch(zone)
ax2.text(7.72, 7.35, '"Know but\ncan\'t do"', ha='center', va='center',
         fontsize=16, fontweight='bold', color='#C62828')

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#C8E6C9', edgecolor='#2E7D32', label='$\\alpha \\cdot P_{\\mathrm{sel}}$ (Selection Power)'),
    mpatches.Patch(facecolor='#FFCDD2', edgecolor='#C62828', label='$\\beta \\cdot \\Psi_f$ (Friction Cost)'),
    mpatches.Patch(facecolor='#FFE0B2', edgecolor='#E65100', label='$\\gamma \\cdot S_{\\mathrm{noise}}$ (Noise)'),
]
ax2.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0.02, 0.98),
           fontsize=15, framealpha=0.9)

# Equation
ax2.text(5.4, 0.15, '$dq/dt \\leq \\alpha \\cdot P_{\\mathrm{sel}} - \\beta \\cdot \\Psi_f - \\gamma \\cdot S_{\\mathrm{noise}}$',
         ha='center', va='center', fontsize=16,
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#333333'))

plt.subplots_adjust(left=0.06, right=0.97, top=0.95, bottom=0.06, hspace=0.18)
plt.savefig('fig1_srt_architecture.png',
            dpi=300, bbox_inches='tight', pad_inches=0.16, facecolor='white')
plt.close()
print("Figure 1 saved.")
