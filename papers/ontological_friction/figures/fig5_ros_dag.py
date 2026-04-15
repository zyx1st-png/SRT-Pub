"""
Figure 5: ROS-Ψ_f Coupling Directed Acyclic Graph
Causal chain from sustained Ψ_f → ROS → chronic stress → symptoms
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(18.0, 11.0))
fig.patch.set_facecolor("white")
ax.set_xlim(0, 15.2)
ax.set_ylim(0, 9.2)
ax.axis('off')
ax.set_title('ROS–$\\Psi_f$ Coupling Mechanism: From Ontological Friction to Clinical Expression',
             fontsize=20, fontweight='bold', pad=18)

# Node definitions: (x, y, label, sublabel, color, edgecolor)
nodes = [
    (2.2, 6.35, 'Sustained High\n$\\Psi_f$', 'Chronic deviation from\n$L_0^{\\mathrm{natural}}$', '#FFF3E0', '#E65100'),
    (5.7, 6.35, 'Elevated\nMetabolic\nDemand', 'Mitochondrial\noveractivation', '#FFECB3', '#FF8F00'),
    (9.2, 6.35, 'Increased\nROS\nProduction', '$\\alpha \\cdot \\Psi_f(\\hat{G}_\\theta)$', '#FFCDD2', '#C62828'),
    (12.45, 6.35, 'Oxidative\nDamage', 'DNA, lipid,\nprotein damage', '#F8BBD0', '#AD1457'),
    (12.45, 3.75, 'Inflammatory\nSignaling', 'IL-6, TNF-α,\nNF-κB pathway', '#E1BEE7', '#6A1B9A'),
    (9.2, 3.75, 'Reduced\n$P_{\\mathrm{sel}}$', 'Neuromodulatory\nimpairment', '#BBDEFB', '#1565C0'),
    (5.7, 3.75, 'Deepened\nKnowing–Doing\nGap', 'Executive\nbreakdown', '#C8E6C9', '#2E7D32'),
    (2.2, 3.75, 'Clinical\nExpression', 'MDD, cognitive\ndecline', '#D7CCC8', '#5D4037'),
]

# Draw nodes
for x, y, label, sublabel, color, ec in nodes:
    box = FancyBboxPatch((x-1.35, y-0.95), 2.7, 1.9,
                          boxstyle="round,pad=0.15", facecolor=color,
                          edgecolor=ec, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y+0.2, label, ha='center', va='center', fontsize=20, fontweight='bold')
    ax.text(x, y-0.6, sublabel, ha='center', va='center', fontsize=13, color='#666', fontstyle='italic')

# Forward arrows (main causal chain)
arrow_pairs = [
    ((3.55, 6.35), (4.35, 6.35)),   # Ψ_f → Metabolic
    ((7.05, 6.35), (7.85, 6.35)),   # Metabolic → ROS
    ((10.55, 6.35), (11.1, 6.35)),  # ROS → Damage
    ((12.45, 5.4), (12.45, 4.7)),   # Damage → Inflammatory
    ((11.1, 3.75), (10.55, 3.75)),  # Inflammatory → Reduced P_sel
    ((7.85, 3.75), (7.05, 3.75)),   # Reduced P_sel → Gap
    ((4.35, 3.75), (3.55, 3.75)),   # Gap → Clinical
]

for (x1, y1), (x2, y2) in arrow_pairs:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#333', lw=2.6, mutation_scale=18))

# Positive feedback loop arrow (back to top)
ax.annotate('', xy=(2.2, 5.4), xytext=(2.2, 4.7),
            arrowprops=dict(arrowstyle='->', color='#C62828', lw=2.6,
                          connectionstyle='arc3,rad=0', linestyle='--'))
ax.text(1.1, 4.9, 'Positive\nfeedback\nloop', ha='center', va='center',
        fontsize=16, fontweight='bold', color='#C62828')

# Intervention targets
interventions = [
    (9.2, 1.6, 'Antioxidant\nIntervention', '↑ β · Clearance(θ_body)', '#E8F5E9', '#2E7D32'),
    (5.7, 1.6, 'Behavioral\nIntervention', '↑ P_sel via training', '#E3F2FD', '#1565C0'),
    (2.2, 1.6, 'Pharmacological\nIntervention', '↓ Ψ_f via neuromod.', '#FFF3E0', '#E65100'),
]

for x, y, label, sublabel, color, ec in interventions:
    box = FancyBboxPatch((x-1.25, y-0.65), 2.5, 1.3,
                          boxstyle="round,pad=0.1", facecolor=color,
                          edgecolor=ec, linewidth=1.5, linestyle='--')
    ax.add_patch(box)
    ax.text(x, y+0.15, label, ha='center', va='center', fontsize=15, fontweight='bold', color=ec)
    ax.text(x, y-0.35, sublabel, ha='center', va='center', fontsize=12, color='#666')

# Intervention arrows (dashed, pointing up)
for x in [9.2, 5.7, 2.2]:
    ax.annotate('', xy=(x, 2.85), xytext=(x, 2.3),
                arrowprops=dict(arrowstyle='->', color='#4CAF50', lw=2.0,
                              linestyle='--', mutation_scale=14))

# Equation box
ax.text(7.6, 0.55, '$d[\\mathrm{ROS}]/dt = \\alpha \\cdot \\Psi_f(\\hat{G}_\\theta) - \\beta \\cdot \\mathrm{Clearance}(\\theta_{\\mathrm{body}})$',
        ha='center', va='center', fontsize=18,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#333', linewidth=1.5))

plt.subplots_adjust(left=0.04, right=0.99, top=0.9, bottom=0.08)
plt.savefig('/Users/zhangyuxin/.openclaw/workspace/SRT/papers/ontological_friction/figures/fig5_ros_dag.png',
            dpi=300, bbox_inches='tight', pad_inches=0.16, facecolor='white')
plt.close()
print("Figure 5 saved.")
