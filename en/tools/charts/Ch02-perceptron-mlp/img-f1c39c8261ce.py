"""English redraw of the inline chart f1c39c8261ce (Ch02 main page + slides 01 and 14):
single-layer perceptron geometry, AND (one line suffices) vs XOR (no single line).

Original: 3590 x 1457 px. Geometry measured from it: both panels span [-0.32, 1.32];
AND boundary 0.6*x1 + 0.8*x2 - 0.9 = 0; XOR dashed x1+x2=1, dash-dot x1+x2=1.35, dotted x2=0.5.
Output: scratch/c2-redraw/f1c39c8261ce.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
import logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "scratch/c2-redraw/f1c39c8261ce.png"

W, H, DPI = 3590, 1457, 300
LIGHT = "/usr/share/fonts/truetype/noto/NotoSans-Light.ttf"
try:
    font_manager.fontManager.addfont(LIGHT)
    FAM = font_manager.FontProperties(fname=LIGHT).get_name()
except Exception:
    FAM = "DejaVu Sans"
plt.rcParams.update({"font.family": FAM, "font.weight": "light",
                     "mathtext.fontset": "dejavusans"})

DARK, FRAME, GRID = "#2d3436", "#ccd6e1", "#c4cad6"
BLUE, BLUE_E, MAG, MAG_E = "#0984e3", "#075985", "#e84393", "#9b1b63"
PINK_BG, BLUE_BG = "#ffeaea", "#e5effe"
GREEN = "#00b894"
LIM = (-0.32, 1.32)

fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor="white")


def panel(x0px):
    ax = fig.add_axes([x0px / W, 1 - 1279.5 / H, (1770 - 161) / W, (1279.5 - 440) / H])
    ax.set_xlim(*LIM); ax.set_ylim(*LIM)
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.tick_params(labelsize=8, colors=FRAME, labelcolor="#333333", length=3)
    for s in ax.spines.values():
        s.set_color(FRAME); s.set_linewidth(0.75)
    ax.grid(True, ls=":", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    ax.set_xlabel(r"Input feature $x_1$", fontsize=12.5, color=DARK, labelpad=9, fontweight="light")
    ax.set_ylabel(r"Input feature $x_2$", fontsize=12.5, color=DARK, labelpad=8, fontweight="light")
    return ax


def pts(ax, data):
    for x, y, lab in data:
        if lab:
            ax.plot(x, y, "o", ms=19, mfc=MAG, mec=MAG_E, mew=2, zorder=5)
            ax.text(x + 0.055, y + 0.07, "y=1", color=MAG, fontsize=11, zorder=6)
        else:
            ax.plot(x, y, "s", ms=17.5, mfc=BLUE, mec=BLUE_E, mew=2, zorder=5)
            ax.text(x + 0.055, y + 0.07, "y=0", color="#2f7fb5", fontsize=11, zorder=6)


fig.text(0.5, 1 - 72 / H, "Geometric power of a single-layer perceptron: AND vs XOR",
         ha="center", va="center", fontsize=17, color=DARK, fontweight="light")

# AND
ax = panel(161)
xs = np.linspace(*LIM, 200)
line = (0.9 - 0.6 * xs) / 0.8
ax.fill_between(xs, LIM[0], line, color=BLUE_BG, zorder=0)
ax.fill_between(xs, line, LIM[1], color=PINK_BG, zorder=0)
ax.plot(xs, line, color=GREEN, lw=3, zorder=3)
ax.set_title("AND: one straight line is enough", fontsize=14, color=DARK, pad=14, fontweight="light")
ax.text(0.08, 1.2, r"active: $z \geq 0$", fontsize=12.5, color=MAG_E, va="center")
ax.text(0.94, -0.19, r"inactive: $z < 0$", fontsize=12.5, color=BLUE_E, va="center", ha="center")
pts(ax, [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)])

# XOR
ax = panel(1956)
ax.plot(xs, 1 - xs, ls=(0, (5, 3)), color="#64748b", lw=2.2, zorder=3)
ax.plot(xs, 1.35 - xs, ls=(0, (7, 3, 1.5, 3)), color="#475569", lw=2.2, zorder=3)
ax.axhline(0.5, ls=":", color="#94a3b8", lw=2.2, zorder=3)
ax.set_title("XOR: classes interleaved along the diagonals", fontsize=14, color=DARK, pad=14, fontweight="light")
ax.text(0.5, 0.5, "One straight\nline cannot\nseparate XOR", ha="center", va="center",
        fontsize=13, color="#b42318", linespacing=1.0, zorder=7,
        bbox=dict(boxstyle="round,pad=0.45", fc="#fff1f2", ec="#e17055", lw=1.5))
pts(ax, [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)])

fig.savefig(OUT, dpi=DPI, facecolor="white")
print(OUT)
