"""English redraw of slides/03-ml-classification-vs-regression.html, Fig 1 (1st inline image):
output type -- discrete boxes (classification) vs. a continuous number line (regression).

Drawn in pixel coordinates of the original (1779 x 708 px at 150 dpi).
The original placed the points on a 0..100 scale spanning the whole panel while the 0 and 100
end ticks sat inset; here the points are placed proportionally between the labelled ticks.
Output: en/IDL_115/Ch01-introduction-history/slides/03-ml-classification-vs-regression/assets/img00.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/03-ml-classification-vs-regression/assets/img00.png"

W, H, DPI = 1779, 708, 150
BG, PANEL, EDGE, INNER = "#0f172a", "#1e293b", "#2f3c50", "#0f172a"
TEXT, MUTED, LINE = "#f1f5f9", "#94a3b8", "#e2e8f0"
GREEN, PURPLE, SKY, ORANGE = "#10b981", "#a78bfa", "#38bdf8", "#f59e0b"
BLUE, RED = "#60a5fa", "#ef4444"
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["mathtext.fontset"] = "dejavusans"

fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")

fig.text(0.5, 1 - 27 / H, "Output Type: Discrete Boxes (Classification) vs Continuous Number Line (Regression)",
         ha="center", va="center", color=TEXT, fontsize=11.5)

# panels
for x0, x1, title in [(15, 878, r"Classification: Finite Discrete Labels  $\{\ell_1, \ell_2, \ldots, \ell_k\}$"),
                      (903, 1765, r"Regression: Continuous Real Value  $y \in \mathbb{R}$")]:
    ax.add_patch(Rectangle((x0, 137), x1 - x0, 556, facecolor=PANEL, edgecolor=EDGE, lw=1))
    ax.text((x0 + x1) / 2, 117, title, ha="center", va="center", color=TEXT, fontsize=11)

# classification boxes
boxes = [(100, 230, GREEN, "Apple"), (488, 230, PURPLE, "Cucumber"),
         (100, 434, SKY, "Ramen"), (488, 434, ORANGE, "Braised pork")]
for x, y, c, name in boxes:
    ax.add_patch(Rectangle((x, y), 278, 149, facecolor=INNER, edgecolor=c, lw=2.2))
    ax.text(x + 139, y + 76, name, ha="center", va="center", color=c, fontsize=10.5)
    ax.plot(x + 139, y + 120, "o", ms=8, mfc=c, mec="white", mew=1.2)
ax.text(446, 653, "Every input lands in one box", ha="center", va="center", color=MUTED, fontsize=8.5)

# number line
X0, X1, YL = 945, 1721, 414
ax.plot([X0, X1], [YL, YL], color=LINE, lw=3.5, solid_capstyle="butt", zorder=2)
for xe in (X0, X1):
    ax.plot([xe, xe], [384, 445], color=LINE, lw=3.5, zorder=2)
ax.text(X0, 483, "0", ha="center", va="center", color=MUTED, fontsize=9)
ax.text(X1, 483, "100", ha="center", va="center", color=MUTED, fontsize=9)
for v, c in [(15, BLUE), (42, SKY), (78.5, ORANGE), (88, RED)]:
    x = X0 + (X1 - X0) * v / 100
    ax.plot([x, x], [305, YL], color=c, lw=1.8, zorder=3)
    ax.plot(x, YL, "o", ms=12, mfc=c, mec="white", mew=1.8, zorder=4)
    ax.text(x, 269, f"{v:g}", ha="center", va="center", color=c, fontsize=9.5,
            bbox=dict(boxstyle="square,pad=0.15", fc=INNER, ec=c, lw=0.8))
ax.text(1333, 585, "Any real number — infinite possibilities", ha="center", va="center", color=SKY,
        fontsize=9.5, bbox=dict(boxstyle="round,pad=0.3", fc=INNER, ec=SKY, lw=1.2))
ax.text(1333, 653, "Every input maps to a point on the line", ha="center", va="center", color=MUTED, fontsize=8.5)

fig.savefig(OUT, dpi=DPI, facecolor=BG)
print(OUT)
