"""
Figure 2: Four-Proxy Operationalization Map
Central Ψ_f node with four radiating branches
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(-6.2, 6.2)
ax.set_ylim(-6, 6)
ax.axis('off')
ax.set_title('Operationalization Map: Four Proxy Classes for $\\Psi_f$',
             fontsize=16, fontweight='bold', pad=20)

# Central node
circle = plt.Circle((0, 0), 1.2, facecolor='#FFF3E0', edgecolor='#E65100', linewidth=3)
ax.add_patch(circle)
ax.text(0, 0.15, '$\\Psi_f$', ha='center', va='center', fontsize=24, fontweight='bold', color='#BF360C')
ax.text(0, -0.5, 'Executive\nFriction', ha='center', va='center', fontsize=11, color='#BF360C')

# Branch definitions
branches = [
    {
        'angle': 45, 'color': '#1565C0', 'bg': '#E3F2FD', 'label': 'BEHAVIORAL',
        'items': [
            'Task-switch cost (RT/error)',
            'WCST perseverative errors',
            'Stroop interference ratio',
            'Temporal discounting rate',
        ],
        'direction': '(+)'
    },
    {
        'angle': 135, 'color': '#2E7D32', 'bg': '#E8F5E9', 'label': 'PHYSIOLOGICAL',
        'items': [
            'HRV recovery slope (inv)',
            'Cortisol curve flattening',
            'SCR peak amplitude',
            'ROS biomarkers (GSH/GSSG)',
        ],
        'direction': '(+/−)'
    },
    {
        'angle': 225, 'color': '#6A1B9A', 'bg': '#F3E5F5', 'label': 'NEURAL',
        'items': [
            'PCI complexity (inv)',
            'Fisher info κ(ĝ_F)',
            'θ-γ coupling index (inv)',
            'BG gating integrity (inv)',
        ],
        'direction': '(+/−)'
    },
    {
        'angle': 315, 'color': '#C62828', 'bg': '#FFEBEE', 'label': 'LINGUISTIC',
        'items': [
            'μ_sem (modal verb ratio)',
            'Constraint modal freq',
            'Possibility modal freq (inv)',
            'Automated NLP extraction',
        ],
        'direction': '(+)'
    },
]

for branch in branches:
    angle_rad = np.radians(branch['angle'])
    # Branch box center
    cx = 3.8 * np.cos(angle_rad)
    cy = 3.8 * np.sin(angle_rad)

    # Draw connection line
    lx1 = 1.3 * np.cos(angle_rad)
    ly1 = 1.3 * np.sin(angle_rad)
    lx2 = 1.75 * np.cos(angle_rad)
    ly2 = 1.75 * np.sin(angle_rad)
    ax.annotate('', xy=(lx2, ly2), xytext=(lx1, ly1),
                arrowprops=dict(arrowstyle='->', color=branch['color'], lw=2.5, mutation_scale=15))

    # Branch box
    box_w, box_h = 3.8, 2.8
    box = FancyBboxPatch((cx - box_w/2, cy - box_h/2), box_w, box_h,
                          boxstyle="round,pad=0.2", facecolor=branch['bg'],
                          edgecolor=branch['color'], linewidth=2)
    ax.add_patch(box)

    # Title
    ax.text(cx, cy + box_h/2 - 0.4, branch['label'],
            ha='center', va='center', fontsize=12, fontweight='bold', color=branch['color'])

    # Items
    for j, item in enumerate(branch['items']):
        ax.text(cx, cy + 0.3 - j * 0.5, item,
                ha='center', va='center', fontsize=10, color='#333333')

# SEM note at bottom
ax.text(0, -5.5, 'Expected convergent validity: between-domain $r$ = 0.3–0.6\n'
        'Single-factor CFA with four indicator classes',
        ha='center', va='center', fontsize=10, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F5F5', edgecolor='#999999'))

plt.savefig('fig2_proxy_map.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 2 saved.")
