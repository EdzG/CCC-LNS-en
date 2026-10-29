"""English redraw of slides/02-ml-vector-representation-mapping.html, Fig (1st inline image):
Vectorization -- Xiao Ming's 4D health vector vs. a cat image as a 10,000-D vector.

Bar values are from the chart labels. The 10x10 gray grid was sampled from the original image;
the 40 mini bars are the first 40 grid values flattened row by row (as in the original).
Output: en/IDL_115/Ch01-introduction-history/slides/02-ml-vector-representation-mapping/assets/img00.png
(1319 x 587 px, same as the original).
"""
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/02-ml-vector-representation-mapping/assets/img00.png"

BG, PANEL, EDGE, TICK = "#0f172a", "#1e293b", "#334155", "#94a3b8"
GRID = np.array([
    [175, 195, 25, 246, 67, 211, 151, 103, 92, 185],
    [142, 23, 72, 89, 110, 42, 218, 136, 167, 230],
    [68, 176, 127, 135, 172, 0, 75, 55, 250, 6],
    [19, 188, 44, 191, 69, 56, 152, 183, 181, 112],
    [251, 189, 192, 34, 56, 201, 206, 38, 4, 238],
    [137, 87, 227, 195, 72, 83, 176, 1, 192, 144],
    [118, 159, 93, 172, 92, 252, 71, 23, 10, 233],
    [35, 192, 60, 135, 151, 92, 247, 224, 149, 100],
    [163, 225, 67, 123, 219, 225, 19, 155, 4, 19],
    [32, 123, 30, 185, 229, 73, 221, 209, 127, 159]])

W, H, DPI = 1319, 587, 150
plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)


def box(l, t, r, b):
    return [l / W, 1 - b / H, (r - l) / W, (b - t) / H]


fig.text(0.5, 1 - 24 / H, "Vectorization: Health 4D vs Cat Image 10,000D", color="#f1f5f9",
         fontsize=9.5, ha="center", va="center")

# Left: Xiao Ming's four health features.
ax = fig.add_axes(box(80, 97, 783, 464))
ax.set_facecolor(PANEL)
names = ["Blood pressure", "Blood sugar", "Height", "Weight"]
vals = [120, 95, 175, 70]
cols = ["#38bdf8", "#a78bfa", "#f59e0b", "#34d399"]
x = np.arange(4)
ax.bar(x, vals, width=0.63, color=cols, edgecolor="white", linewidth=1.2, zorder=3)
for xi, v in zip(x, vals):
    ax.text(xi, v + 3, str(v), color="white", fontsize=8.5, ha="center", va="bottom", zorder=4)
ax.set_xlim(-0.49, 3.49)
ax.set_ylim(0, 200)
ax.set_yticks(range(0, 201, 25))
ax.set_xticks(x)
ax.set_xticklabels([f"{n}\n{v}" for n, v in zip(names, vals)], linespacing=0.95)
ax.tick_params(colors=TICK, labelsize=6.5)
for s in ax.spines.values():
    s.set_color(EDGE)
ax.set_ylabel("value", color=TICK, fontsize=6.5)
ax.set_title(r"Xiao Ming  $\mathbf{x}=[120,95,175,70]^\top\in\mathbb{R}^4$", color="#f1f5f9",
             fontsize=8, pad=7)
fig.text(431 / W, 1 - 551 / H, "4 features → 4D point", color="#7dd3fc", fontsize=6.5,
         ha="center", va="center")

# Right: cat image as a pixel grid.
axc = fig.add_axes(box(939, 97, 1305, 463))
axc.imshow(GRID, cmap="gray", vmin=0, vmax=255, extent=(0, 10, 10, 0), interpolation="nearest")
for k in range(1, 10):
    axc.axhline(k, color="#475569", lw=0.5)
    axc.axvline(k, color="#475569", lw=0.5)
axc.set_xticks([])
axc.set_yticks([])
for s in axc.spines.values():
    s.set_color("black")
    s.set_linewidth(1.2)
axc.set_title(r"Cat  $100\times100\ \to\ \mathbb{R}^{10000}$", color="#f1f5f9", fontsize=8, pad=7)
fig.text(1122 / W, 1 - 477 / H, "10,000 pixels flattened → super-long vector", color="#f59e0b",
         fontsize=6.5, ha="center", va="center")

# Mini bar strip: first 40 values of the flattened grid.
axm = fig.add_axes(box(956, 499, 1288, 566))
axm.set_facecolor(BG)
axm.bar(np.arange(40), GRID.ravel()[:40], width=0.88, color="#64748b")
axm.set_xlim(-0.75, 40.25)
axm.set_ylim(0, 255)
axm.set_xticks([])
axm.set_yticks([0, 255])
axm.tick_params(colors="#64748b", labelsize=5, length=2)
for s in axm.spines.values():
    s.set_color(EDGE)
axm.set_title("first 40 dims of 10,000", color=TICK, fontsize=6, pad=2)

fig.savefig(OUT, dpi=DPI, facecolor=BG)
print(OUT)
