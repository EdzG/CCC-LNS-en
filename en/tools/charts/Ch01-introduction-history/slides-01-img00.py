"""English redraw of slides/01-ml-theory-surrogate-bias-loop.html, Fig 1 (1st inline image):
Map != Territory -- messy real world vs. a clean surrogate (model).

The noisy path on the left was traced from the original image (the original used random noise);
the road on the right is y = 5 + 0.2 sin(1.2 x), fitted to the original.
Output: en/IDL_115/Ch01-introduction-history/slides/01-ml-theory-surrogate-bias-loop/assets/img00.png
(1480 x 622 px, same as the original).
"""
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/01-ml-theory-surrogate-bias-loop/assets/img00.png"

BG, PANEL, BOX = "#0f172a", "#1e293b", "#334155"
SLATE, ORANGE, SKY, SKY_LT = "#475569", "#f59e0b", "#38bdf8", "#7dd3fc"

# Noisy "reality" path, traced from the original (x, y in 0..10 axis units).
XY = [(0.021,4.86), (0.063,5.38), (0.105,5.16), (0.161,5.01), (0.218,5.14), (0.288,4.88),
      (0.344,5.45), (0.372,5.45), (0.400,5.67), (0.428,5.83), (0.484,5.85), (0.512,5.63),
      (0.554,5.69), (0.667,5.50), (0.723,5.33), (0.779,5.69), (0.835,5.91), (0.891,5.41),
      (0.947,5.51), (1.004,5.82), (1.060,5.66), (1.088,5.61), (1.116,5.85), (1.144,5.96),
      (1.200,6.02), (1.228,5.81), (1.270,6.16), (1.326,5.86), (1.593,5.74), (1.649,5.53),
      (1.705,5.45), (1.761,5.58), (1.818,5.61), (1.902,5.72), (1.958,5.29), (2.028,5.64),
      (2.070,5.28), (2.112,5.26), (2.351,5.11), (2.407,4.85), (2.463,4.72), (2.519,4.97),
      (2.604,4.50), (2.646,4.31), (2.688,4.45), (2.730,4.90), (2.772,5.00), (2.814,4.33),
      (2.870,4.98), (2.926,4.90), (2.954,4.72), (2.996,4.46), (3.053,4.27), (3.207,4.56),
      (3.263,4.84), (3.333,4.76), (3.389,4.50), (3.432,4.76), (3.460,4.45), (3.516,3.99),
      (3.572,4.15), (3.628,3.99), (3.698,3.84), (3.754,4.31), (3.796,4.21), (3.853,4.07),
      (3.993,4.15), (4.049,4.24), (4.175,4.46), (4.232,4.53), (4.288,4.58), (4.344,4.36),
      (4.386,4.23), (4.428,4.39), (4.484,4.49), (4.540,4.68), (4.596,4.58), (4.653,4.49),
      (4.723,4.78), (4.821,4.70), (4.863,4.34), (4.919,4.22), (4.975,4.77), (5.018,4.28),
      (5.060,4.47), (5.144,4.96), (5.200,4.70), (5.256,4.82), (5.298,5.16), (5.340,5.35),
      (5.396,5.26), (5.453,5.17), (5.537,5.52), (5.691,5.61), (5.789,5.49), (6.028,5.51),
      (6.182,6.39), (6.239,5.86), (6.295,5.86), (6.351,5.85), (6.407,5.54), (6.449,5.53),
      (6.618,5.69), (6.758,5.51), (6.814,5.30), (6.870,5.74), (6.926,5.54), (6.982,5.46),
      (7.109,5.60), (7.165,5.70), (7.277,5.58), (7.333,5.34), (7.418,4.92), (7.474,5.27),
      (7.642,4.98), (7.768,4.85), (7.811,4.66), (7.867,5.04), (7.937,4.91), (7.993,4.82),
      (8.035,4.67), (8.063,4.35), (8.091,4.17), (8.133,4.08), (8.189,4.15), (8.232,4.78),
      (8.274,4.37), (8.302,4.45), (8.358,4.50), (8.414,4.29), (8.456,4.72), (8.512,4.49),
      (8.540,4.39), (8.765,4.24), (8.821,4.07), (8.877,3.87), (8.961,4.21), (8.989,3.86),
      (9.046,4.23), (9.088,3.84), (9.116,4.02), (9.144,4.28), (9.186,4.53), (9.242,3.92),
      (9.298,3.92), (9.340,4.13), (9.396,4.19), (9.425,4.39), (9.481,4.31), (9.537,4.44),
      (9.621,4.40), (9.691,4.26), (9.775,4.29), (9.888,4.40), (9.944,4.56)]

plt.rcParams["font.family"] = "DejaVu Sans"
fig = plt.figure(figsize=(14.8, 6.22), dpi=100, facecolor=BG)
W, H = 1480, 622
axL = fig.add_axes([14.5 / W, 1 - 607 / H, 712.5 / W, 492.5 / H])
axR = fig.add_axes([752.5 / W, 1 - 607 / H, 712.5 / W, 492.5 / H])
for ax in (axL, axR):
    ax.set_facecolor(PANEL)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color("#020307")
        s.set_linewidth(1.5)

fig.text(0.5, 1 - 29 / H, "Map ≠ Territory", color="white", fontsize=19,
         ha="center", va="center")

# Left: the real world, full of noise.
rng = np.random.default_rng(7)
n = 75
axL.scatter(rng.uniform(0, 10, n), rng.uniform(0, 10, n), s=rng.uniform(20, 140, n),
            color=SLATE, alpha=0.3, linewidths=0)
x, y = np.array(XY).T
axL.plot(x, y, color=SLATE, lw=12, alpha=0.5, solid_capstyle="round", solid_joinstyle="round")
axL.plot(x, y, color=ORANGE, lw=3, alpha=0.9, ls=(0, (3, 2)))
axL.set_title("Real World", color="#f8fafc", fontsize=16, pad=8)
axL.text(5, 9.15, "Reality: leaves / potholes / cats", color="#94a3b8", fontsize=13,
         ha="center", va="center")
axL.text(5, 0.75, "...millions of bits of noise...", color="#64748b", fontsize=12,
         ha="center", va="center")

# Right: the surrogate keeps only the road and the blocks.
for bx, by in [(1.2, 2.2), (4.2, 5.2), (6.2, 1.2)]:
    axR.add_patch(Rectangle((bx, by), 1.6, 1.6, facecolor=BOX, edgecolor=SKY, lw=2))
xr = np.linspace(0, 10, 400)
axR.plot(xr, 5 + 0.2 * np.sin(1.2 * xr), color=SKY, lw=4)
axR.scatter([1, 5, 9], [5.0, 5.2, 4.9], s=180, color=SKY, edgecolors="white", linewidths=1.5,
            zorder=5)
axR.set_title("Surrogate (Model)", color=SKY, fontsize=16, pad=8)
axR.text(5, 9.15, "Map: only roads & blocks", color=SKY_LT, fontsize=13,
         ha="center", va="center")
axR.text(5, 0.75, "Keeps only where the road is", color=SKY, alpha=0.7, fontsize=12,
         ha="center", va="center")

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=100, facecolor=BG)
print(OUT)
