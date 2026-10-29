"""English redraw of slides/02-ml-vector-representation-mapping.html, 2nd inline image:
the data matrix X = [x_1 ... x_n] in R^{d x n} (columns = samples/students, rows = features).

Cell values are copied from the original image.
Output: en/IDL_115/Ch01-introduction-history/slides/02-ml-vector-representation-mapping/assets/img01.png
(1185 x 612 px, same as the original).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/02-ml-vector-representation-mapping/assets/img01.png"

BG, PANEL, EDGE = "#0f172a", "#1e293b", "#334155"
SKY, SKY_LT, ORANGE, DIM, SOFT = "#38bdf8", "#7dd3fc", "#f59e0b", "#64748b", "#94a3b8"
W, H, DPI = 1185, 612, 150
VALS = [["62", "143", "110", "78", "81", "179"],
        ["127", "135", "118", "107", "76", "72"],
        ["153", "167", "...", "...", "...", "..."],
        ["170", "74", "80", "113", "75", "119"]]

plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)
ax.axis("off")

ax.text(W / 2, 26, r"Data Matrix  $X=[\mathbf{x}_1\cdots\mathbf{x}_n]\in\mathbb{R}^{d\times n}$",
        color="#f1f5f9", fontsize=10.5, ha="center", va="center")

X0, Y0, CW, RH = 153, 210, 104, 75
# faded cells first, highlighted columns on top
for r in range(4):
    for c in range(6):
        hi = c < 2
        ax.add_patch(Rectangle((X0 + c * CW, Y0 + r * RH), CW, RH, fc=PANEL,
                               ec=SKY if hi else EDGE, lw=1.6 if hi else 1.0, zorder=3 if hi else 2))
        if hi:
            col = SKY if r == 0 else ("white" if r == 1 else SOFT)
        else:
            col = DIM
        ax.text(X0 + (c + 0.5) * CW, Y0 + (r + 0.5) * RH, VALS[r][c], color=col, fontsize=7.5,
                ha="center", va="center", zorder=4)

for c, lab in enumerate(["x1", "x2"]):
    cx = X0 + (c + 0.5) * CW
    ax.text(cx, 186, lab, color=SKY, fontsize=8, ha="center", va="center")
    ax.add_patch(FancyArrowPatch((cx, 532), (cx, 208), arrowstyle="<|-|>", mutation_scale=9,
                                 color=SKY, lw=1.5, ls=(0, (4, 2.5)), zorder=5))

ax.text(465, 135, "n columns = samples (students)", color=SKY_LT, fontsize=8, fontweight="bold",
        ha="center", va="center")

ax.add_patch(FancyArrowPatch((124, 507), (124, 214), arrowstyle="<|-|>", mutation_scale=9,
                             color=ORANGE, lw=1.5, ls=(0, (4, 2.5))))
ax.text(97, 360, "d rows\n= features", color=ORANGE, fontsize=8, fontweight="bold", rotation=90,
        ha="center", va="center", linespacing=0.95)

ax.text(916, 210, "Each column\nis a vector", color=SKY, fontsize=6.5, ha="center", va="center",
        linespacing=0.9, bbox=dict(boxstyle="round,pad=0.3", fc=BG, ec=SKY, lw=1.2))
ax.text(650, 487, r"Example:  4 features $\times$ 6 students  $\to$  4$\times$6 matrix", color=SOFT,
        fontsize=7, ha="center", va="center", zorder=6,
        bbox=dict(boxstyle="round,pad=0.35", fc=PANEL, ec="#475569", lw=1.0))

fig.savefig(OUT, dpi=DPI, facecolor=BG)
print(OUT)
