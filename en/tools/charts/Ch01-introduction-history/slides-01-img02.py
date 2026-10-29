"""English redraw of the 3rd inline image (Fig 3, "Loss landscape") in
IDL_115/Ch01-introduction-history/slides/01-ml-theory-surrogate-bias-loop.html.

Left: convex bowl (a parabola) with gradient-descent steps sliding to the green minimum.
Right: a rugged non-convex curve (traced from the original; no closed form) with SGD steps
that end up in a local dip. All coordinates are output pixels (1488 x 626, y down).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/01-ml-theory-surrogate-bias-loop/assets/img02.png"

W, H = 1488, 626
plt.rcParams["font.family"] = ["Noto Sans", "DejaVu Sans"]

BG, PANEL, EDGE = "#0f172a", "#1e293b", "#334155"
BLUE, PURPLE, ORANGE, GREEN = "#38bdf8", "#a78bfa", "#f59e0b", "#10b981"
TITLE = "#e2e8f0"

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)
ax.axis("off")

for x0, x1 in ((15, 734), (755, 1473)):
    ax.add_patch(Rectangle((x0, 99), x1 - x0, 512, facecolor=PANEL, edgecolor=EDGE, lw=1.5, zorder=0))

ax.text(W / 2, 27, "Optimization Landscape · Loss Landscape and Search", color=TITLE,
        fontsize=16, ha="center", va="center")
ax.text(374.5, 80, "Smooth Convex Bowl (analytical solution)", color=BLUE, fontsize=13,
        ha="center", va="center")
ax.text(1114, 80, "Rugged Non-convex Mountains (SGD)", color=PURPLE, fontsize=13,
        ha="center", va="center")

# --- left: convex bowl y = 588 - k (x - 374.5)^2 -------------------------------
XV, YV = 374.5, 588.0
K = (YV - 121.0) / (XV - 45.0) ** 2
bowl = lambda x: YV - K * (np.asarray(x) - XV) ** 2
xl = np.linspace(45, 703, 600)
ax.plot(xl, bowl(xl), color=BLUE, lw=4, solid_capstyle="round", zorder=2)
steps = np.array([647, 570, 494, 440, 402])
ax.plot(np.r_[steps, 380], bowl(np.r_[steps, 380]), color=ORANGE, lw=3, zorder=3)
ax.scatter(steps, bowl(steps), s=150, color=ORANGE, edgecolor="white", linewidth=1.8, zorder=4)
ax.scatter([380], bowl([380]), s=380, color=GREEN, edgecolor="white", linewidth=2.2, zorder=5)
ax.annotate("start", xy=(649, 262), xytext=(663, 235), color=ORANGE, fontsize=10,
            ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.5, shrinkA=2, shrinkB=2), zorder=6)

# --- right: non-convex curve, traced from the original image --------------------
knots = np.array([
    (785, 138.5), (796, 128.1), (806, 122.3), (816, 129.9), (826, 156.0), (836, 198.3),
    (846, 251.6), (856, 305.6), (866, 350.6), (876, 380.4), (886, 393.5), (896, 394.4),
    (906, 390.4), (916, 388.3), (926, 390.9), (936, 405.2), (946, 418.3), (956, 429.8),
    (966, 434.1), (976, 430.0), (986, 420.0), (996, 411.6), (1006, 412.7), (1016, 428.4),
    (1026, 458.6), (1036, 498.9), (1046, 537.9), (1056, 573.2), (1066, 586.3), (1076, 580.6),
    (1086, 558.5), (1096, 528.1), (1106, 499.0), (1116, 473.2), (1126, 469.2), (1136, 474.5),
    (1146, 483.5), (1156, 488.4), (1166, 490.1), (1176, 488.2), (1186, 475.0), (1196, 466.9),
    (1206, 466.3), (1216, 475.5), (1226, 492.3), (1236, 510.4), (1246, 521.6), (1256, 517.1),
    (1266, 494.0), (1276, 454.5), (1286, 405.9), (1296, 357.6), (1306, 320.1), (1316, 299.1),
    (1326, 294.9), (1336, 302.5), (1346, 313.4), (1356, 319.4), (1366, 315.1), (1376, 299.8),
    (1386, 277.6), (1396, 254.1), (1406, 234.4), (1416, 220.7), (1426, 210.5), (1436, 197.9),
    (1442, 190.5)])


def catmull_rom(p, n=20):
    p = np.vstack([p[0], p, p[-1]])
    out = []
    t = np.linspace(0, 1, n, endpoint=False)[:, None]
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t ** 2
                          + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    out.append(p[-2][None])
    return np.vstack(out)


curve = catmull_rom(knots)
ax.plot(curve[:, 0], curve[:, 1], color=PURPLE, lw=4, solid_capstyle="round", zorder=2)
sgd = np.array([(831, 160), (907, 382), (983, 432), (1055, 562), (1130, 472), (1174, 481)])
ax.plot(sgd[:, 0], sgd[:, 1], color=ORANGE, lw=2.5, zorder=3)
ax.scatter(sgd[:, 0], sgd[:, 1], s=70, color=ORANGE, edgecolor="white", linewidth=1.5, zorder=4)
ax.text(1104, 503, "gradient descent\nwalking downhill blind", color=ORANGE, fontsize=9,
        ha="center", va="center", linespacing=1.0, zorder=6,
        bbox=dict(boxstyle="round,pad=0.25", facecolor=PANEL, edgecolor=ORANGE, lw=1.8))

fig.savefig(OUT, dpi=100, facecolor=BG)
print(OUT)
