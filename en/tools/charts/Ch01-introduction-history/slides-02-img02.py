"""English redraw of slides/02-ml-vector-representation-mapping.html, Fig 3 (3rd inline image):
linear projection w=[1,1], b=0, f(x)=x1+x2 from R^2 (left) to a colored R^1 number line (right).

Points read off the original: Xiao Ai (1.5,2), Xiao Hua (2.5,2.5), x3 (2,4), x4 (5,3), x5 (6,6),
Xiao Mei (7,6.5), x7 (8,8); their f values (3.5 ... 16.0) match the deck's projChart data.
Squares are the exact orthogonal projections onto the line y = x. Colormap: coolwarm, 3.5..16.
Output: en/IDL_115/Ch01-introduction-history/slides/02-ml-vector-representation-mapping/assets/img02.png
(1364 x 807 px, same as the original).
"""
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/02-ml-vector-representation-mapping/assets/img02.png"

BG, PANEL, EDGE, TICK = "#0f172a", "#1e293b", "#334155", "#94a3b8"
SKY, ORANGE = "#38bdf8", "#f59e0b"
W, H, DPI = 1364, 807, 150

PTS = [("Xiao Ai", 1.5, 2.0), ("Xiao Hua", 2.5, 2.5), ("x3", 2.0, 4.0), ("x4", 5.0, 3.0),
       ("x5", 6.0, 6.0), ("Xiao Mei", 7.0, 6.5), ("x7", 8.0, 8.0)]
# label anchor (x, y) in data units for each point's value tag
TAGS = {"Xiao Ai": (1.05, 2.45), "Xiao Hua": (3.15, 2.15), "x3": (2.15, 4.35), "x4": (4.6, 2.65),
        "x5": (5.55, 6.35), "Xiao Mei": (7.55, 6.1), "x7": (8.1, 8.35)}
norm = Normalize(3.5, 16.0)
cmap = plt.get_cmap("coolwarm")

plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)


def box(l, t, r, b):
    return [l / W, 1 - b / H, (r - l) / W, (b - t) / H]


fig.text(630 / W, 1 - 26 / H,
         r"Linear Projection:  $\mathbf{w}=[1,1]^\top$,  $b=0$  $\cdot$  $f_\theta(\mathbf{x})=x_1+x_2$"
         r"   (d=2 $\to$ p=1)", color="#f1f5f9", fontsize=10, ha="center", va="center")

tag = dict(color="#f1f5f9", fontsize=6, ha="center", va="center", linespacing=0.95, zorder=8,
           bbox=dict(boxstyle="round,pad=0.25", fc="#0f172a", ec=EDGE, lw=0.8, alpha=0.9))

# ---- left: input space R^2 ----
ax = fig.add_axes(box(66, 91, 666, 692))
ax.set_facecolor(PANEL)
ax.set_xlim(0, 9.2)
ax.set_ylim(0, 9.2)
ax.set_xticks(range(0, 9, 2))
ax.set_yticks(range(0, 9, 2))
ax.grid(color="#334155", lw=0.5, ls=":", alpha=0.6)
ax.tick_params(colors=TICK, labelsize=7)
for s in ax.spines.values():
    s.set_color(EDGE)
ax.set_xlabel(r"x$_1$  (feature 1)", color=TICK, fontsize=8)
ax.set_ylabel(r"x$_2$  (feature 2)", color=TICK, fontsize=8)
ax.plot([0, 9], [0, 9], color=ORANGE, lw=2.5, zorder=2)
ax.annotate("", xy=(7.35, 7.35), xytext=(6.9, 6.9),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2, mutation_scale=12), zorder=3)
ax.text(8.25, 7.55, "w=[1,1]", color=ORANGE, fontsize=8, ha="left", va="center", zorder=6)
for name, x, y in PTS:
    v = x + y
    p = v / 2
    c = cmap(norm(v))
    ax.plot([x, p], [y, p], color="#64748b", lw=1.2, ls="--", zorder=3)
    ax.scatter([x], [y], s=110, color=c, edgecolors="white", linewidths=1.5, zorder=5)
    ax.scatter([p], [p], s=80, marker="s", color=c, edgecolors="white", linewidths=1.2, zorder=6)
    tx, ty = TAGS[name]
    sep = "\n" if name.startswith("Xiao") else " "
    ax.text(tx, ty, f"{name}{sep}{v:.1f}", **tag)
ax.text(0.65, 8.7, "Input space  R²", color=SKY, fontsize=8.5, ha="left", va="center",
        bbox=dict(boxstyle="round,pad=0.3", fc=BG, ec=SKY, lw=1.2))
ax.text(0.2, 0.45, "dashed = orthogonal projection", color=TICK, fontsize=6.5, ha="left",
        va="center")

# ---- right: output space R^1 ----
axr = fig.add_axes(box(892, 91, 1350, 692))
axr.set_facecolor(PANEL)
axr.set_xlim(2.0, 17.5)
axr.set_ylim(0, 1)
axr.set_xticks([4, 8, 12, 16])
axr.set_yticks([])
axr.tick_params(colors=TICK, labelsize=7)
axr.grid(axis="x", color="#334155", lw=0.5, ls=":", alpha=0.6)
for s in axr.spines.values():
    s.set_color(EDGE)
axr.set_xlabel(r"f$\theta$(x) = x$_1$+x$_2$  (projected value)", color="#e2e8f0", fontsize=8,
               labelpad=2)
axr.axhline(0.497, color="#334155", lw=3, zorder=1)
for name, x, y in PTS:
    v = x + y
    c = cmap(norm(v))
    axr.plot([v, v], [0.497, 0.637], color=c, lw=1.8, zorder=2)
    axr.scatter([v], [0.497], s=130, color=c, edgecolors="white", linewidths=1.5, zorder=4)
    axr.text(v, 0.72, f"{v:.1f}", **tag)
axr.text(9.75, 0.932, "Output space  R¹  (scalar axis)", color=SKY, fontsize=8.5, ha="center",
         va="center", bbox=dict(boxstyle="round,pad=0.3", fc=BG, ec=SKY, lw=1.2))
axr.text(3.1, 0.257, "Low end: cool blue", color="#60a5fa", fontsize=6.5, ha="left", va="center")
axr.text(17.3, 0.257, "High end: warm colors", color="#f87171", fontsize=6.5, ha="right",
         va="center")

# ---- colorbar ----
cax = fig.add_axes(box(720, 743, 1115, 763))
cb = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), cax=cax, orientation="horizontal")
cb.set_ticks([3.5, 9.75, 16.0])
cb.set_ticklabels(["3.5 (low)", "9.8", "16.0 (high)"])
cb.ax.tick_params(colors=TICK, labelsize=6)
cb.outline.set_edgecolor(EDGE)
fig.text(832 / W, 1 - 726 / H, "Color = output value: farther from origin → warmer", color=TICK,
         fontsize=5.5, ha="center", va="center")

fig.savefig(OUT, dpi=DPI, facecolor=BG)
print(OUT)
