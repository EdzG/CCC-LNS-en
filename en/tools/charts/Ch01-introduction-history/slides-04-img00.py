"""English redraw of slides/04-ml-unsupervised-clustering-dr.html, 1st inline image:
clustering granularity, same 10 check-in points with m=2 (coarse) vs m=5 (fine).

Points and centroid positions were read off the original's gridlines.
Output: en/IDL_115/Ch01-introduction-history/slides/04-ml-unsupervised-clustering-dr/assets/img00.png
(1468 x 713 px, same as the original).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/04-ml-unsupervised-clustering-dr/assets/img00.png"

BG, PANEL, SPINE, TICK = "#0f172a", "#1e293b", "#334155", "#94a3b8"
BLUE, ORANGE, GREEN, RED, PURPLE = "#38bdf8", "#f59e0b", "#10b981", "#ef4444", "#a78bfa"

BOOK = [(1, 4), (2, 3.5), (1.5, 2), (2.5, 2.5), (3.5, 3)]
GAME = [(7, 6.5), (8, 8), (8, 7.5), (9, 7), (7.5, 5.5)]

# m=5 assignment and centroids as drawn in the original.
FINE = [
    (GREEN, [(1, 4), (3.5, 3)], (2.75, 3.25)),
    (BLUE, [(2, 3.5), (1.5, 2), (2.5, 2.5)], (2.0, 2.25)),
    (ORANGE, [(7, 6.5), (8, 7.5)], (7.5, 7.0)),
    (RED, [(9, 7), (7.5, 5.5)], (8.25, 6.25)),
    (PURPLE, [(8, 8)], (8.0, 8.0)),
]

plt.rcParams["font.family"] = "DejaVu Sans"
W, H, DPI = 1468, 713, 150
fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
axL = fig.add_axes([72 / W, 1 - 643 / H, 515 / W, 515 / H])
axR = fig.add_axes([928 / W, 1 - 643 / H, 515 / W, 515 / H])


def style(ax, title):
    ax.set_facecolor(PANEL)
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_xticks(range(0, 11, 2))
    ax.set_yticks(range(0, 11, 2))
    ax.tick_params(colors=TICK, labelsize=7, length=3)
    for s in ax.spines.values():
        s.set_color(SPINE)
    ax.grid(True, color="#334155", ls=":", lw=0.6, alpha=0.6)
    ax.set_axisbelow(True)
    ax.set_title(title, color="#f1f5f9", fontsize=9.5, pad=7)
    ax.set_xlabel("x1: Library hours", color="#cbd5e1", fontsize=8)


def pts(ax, xy, color):
    x, y = zip(*xy)
    ax.scatter(x, y, s=150, color=color, edgecolors="white", linewidths=1.4, zorder=3)


def centre(ax, xy, color):
    ax.scatter(*xy, s=260, marker="X", color=color, edgecolors="white", linewidths=1.3, zorder=4)


fig.text(0.5, 1 - 28 / H, "Clustering Granularity: Same Data, Different m (Coarse vs Fine)",
         color="white", fontsize=10.5, fontweight="bold", ha="center", va="center")

# Left: m=2
style(axL, "m=2 Coarse (Bookworms / Gamers)")
axL.set_ylabel("x2: Arcade hours", color="#cbd5e1", fontsize=8)
axL.add_patch(Ellipse((2.1, 3.0), 4.5, 3.5, facecolor=BLUE, alpha=0.2, edgecolor=BLUE,
                      ls="--", lw=1.2, zorder=1))
axL.add_patch(Ellipse((7.9, 6.9), 4.5, 3.5, facecolor=ORANGE, alpha=0.2, edgecolor=ORANGE,
                      ls="--", lw=1.2, zorder=1))
pts(axL, BOOK, BLUE)
pts(axL, GAME, ORANGE)
centre(axL, (2.1, 3.0), BLUE)
centre(axL, (7.9, 6.9), ORANGE)
for x, lab, c in [(2.2, "ℓ1 Bookworms", BLUE), (8.0, "ℓ2 Gamers", ORANGE)]:
    axL.text(x, 8.9, lab, color=c, fontsize=8.5, ha="center", va="center", zorder=5,
             bbox=dict(boxstyle="round,pad=0.3", facecolor=BG, edgecolor=c, lw=1.2))

# Right: m=5
style(axR, "m=5 Fine (FPS/RPG split etc.)")
for c, xy, ctr in FINE:
    pts(axR, xy, c)
for c, xy, ctr in FINE:
    centre(axR, ctr, c)
axR.text(5, 0.5, "Large splits, small merges — answer not unique", color="#cbd5e1",
         fontsize=6.5, ha="center", va="center", zorder=5,
         bbox=dict(boxstyle="round,pad=0.3", facecolor=BG, edgecolor="#475569", lw=1))

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=DPI, facecolor=BG)
print(OUT)
