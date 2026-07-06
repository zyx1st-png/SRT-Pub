"""
Figure 4: Clinical Differential Radar Chart
Four conditions × proxy axes
"""
import matplotlib.pyplot as plt
import numpy as np

categories = [
    'Task-switch\ncost',
    'Perseverative\nerrors',
    'Temporal\ndiscounting',
    'HRV recovery\n(inverted)',
    'Cortisol\nflattening',
    'SCR\namplitude',
    'ROS\nbiomarkers',
    'PCI\n(inverted)',
    'θ-γ coupling\n(inverted)',
    'μ_sem\n(modal ratio)',
]

# Predicted values (0-1 scale, higher = more impaired / higher Ψ_f)
healthy  = [0.2, 0.15, 0.3, 0.2, 0.1, 0.3, 0.15, 0.15, 0.15, 0.2]
mdd      = [0.6, 0.5,  0.8, 0.8, 0.85, 0.25, 0.75, 0.65, 0.7, 0.65]
ocd      = [0.8, 0.85, 0.4, 0.4, 0.2, 0.85, 0.25, 0.25, 0.2, 0.9]
pd       = [0.7, 0.35, 0.3, 0.4, 0.2, 0.7, 0.45, 0.55, 0.25, 0.5]

N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

fig, ax = plt.subplots(figsize=(11, 11), subplot_kw=dict(polar=True))

conditions = [
    ('Healthy Controls', healthy, '#4CAF50', 'o'),
    ('MDD', mdd, '#F44336', 's'),
    ('OCD', ocd, '#9C27B0', '^'),
    ("Parkinson's Disease", pd, '#FF9800', 'D'),
]

for label, values, color, marker in conditions:
    values_plot = values + values[:1]
    ax.plot(angles, values_plot, '-', color=color, linewidth=2, markersize=6, marker=marker, label=label)
    ax.fill(angles, values_plot, alpha=0.08, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=9)
ax.set_ylim(0, 1.0)
ax.set_yticks([0.2, 0.4, 0.6, 0.8])
ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8'], fontsize=7, color='#1a1a1a')
ax.set_rlabel_position(30)

ax.set_title('Schematic Predicted $\\Psi_f$ Proxy Signatures Across Clinical Conditions',
             fontsize=13, fontweight='bold', pad=25)

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10, framealpha=0.9)

# Note
fig.text(0.5, 0.02, 'Higher values indicate greater impairment / higher executive friction.\n'
         'Values are schematic relative predictions, not empirical estimates.',
         ha='center', fontsize=9, fontstyle='italic', color='#1a1a1a')

plt.savefig('fig4_clinical_radar.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 4 saved.")
