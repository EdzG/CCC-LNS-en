"""English redraw of IDL_115/Ch01-introduction-history/assets/idl115-w1-clustering-vs-dim-reduction.png
(used in the condensed deck idl115-w1-dl-intro-history.html).

Left: the same S-shaped band of points clustered with m = 2, 3, 5 (contiguous segments along
the curve, k-means-like). Right: a 3D S-shaped manifold (an S-curve extruded along a depth axis,
projected obliquely), a "dimensionality reduction" arrow, and its 1-D wave-like embedding.
All coordinates are in output pixels (1536 x 1024, y down).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, FancyBboxPatch, Polygon

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/idl115-w1-dl-intro-history/assets/idl115-w1-clustering-vs-dim-reduction.png"

W, H = 1536, 1024
plt.rcParams["font.family"] = ["Noto Sans", "DejaVu Sans"]
plt.rcParams["mathtext.fontset"] = "dejavusans"

# palette (sampled from the original)
BLUE_HDR, BLUE_SUB, BLUE_TXT, BLUE_PILL, BLUE_EDGE = "#2862C2", "#DCE8F8", "#1D3B70", "#4A8EDD", "#B5D1F1"
GREEN_HDR, GREEN_SUB, GREEN_TXT = "#217A43", "#E2F1E4", "#1D4F30"
C_BLUE, C_ORANGE, C_GREEN, C_YELLOW, C_RED, C_PURPLE = (
    "#1F64C8", "#F5731C", "#3E9A4E", "#F6B41C", "#E0322E", "#8E3FA8")
AXIS_GRAY = "#8A9096"

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)
ax.set_aspect("equal")
ax.axis("off")
fig.patch.set_facecolor("white")
renderer = fig.canvas.get_renderer()


def rbox(x0, y0, x1, y1, face, edge="none", lw=0, r=22, z=1):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=face, ec=edge, lw=lw, zorder=z))


def fit_text(x, y, s, max_w, size, color, weight="bold", ha="center", ls=1.25, z=5):
    """Draw text, shrinking the font until its width fits max_w pixels."""
    t = ax.text(x, y, s, ha=ha, va="center", fontsize=size, color=color,
                fontweight=weight, linespacing=ls, zorder=z)
    while t.get_window_extent(renderer).width > max_w and size > 8:
        size -= 0.5
        t.set_fontsize(size)
    return t


def catmull_rom(pts, n=400):
    """Smooth curve through pts, resampled to n points equally spaced by arc length."""
    p = np.asarray(pts, float)
    p = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for t in np.linspace(0, 1, 30, endpoint=False):
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t ** 2
                              + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    out.append(p[-2])
    c = np.array(out)
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(c, axis=0).T))]
    s = np.linspace(0, d[-1], n)
    return np.c_[np.interp(s, d, c[:, 0]), np.interp(s, d, c[:, 1])]


def dots(xy, colors, r, z=4):
    ax.add_collection(PatchCollection([Circle(p, r) for p in xy], fc=colors, ec="none", zorder=z))


def arrow_line(x0, y0, x1, y1, dashed):
    ls = (0, (4, 4)) if dashed else "-"
    ax.plot([x0, x1], [y0, y1], color=AXIS_GRAY, lw=1.8, ls=ls, zorder=2)
    v = np.array([x1 - x0, y1 - y0], float); v /= np.hypot(*v)
    ax.annotate("", xy=(x1, y1), xytext=(x1 - 14 * v[0], y1 - 14 * v[1]),
                arrowprops=dict(arrowstyle="-|>,head_length=0.7,head_width=0.35",
                                color=AXIS_GRAY, lw=1.8), zorder=2)


# ---------------------------------------------------------------- divider
ax.plot([770, 770], [0, H], color="#9AA0A6", lw=2, ls=(0, (6, 6)), zorder=0)

# ---------------------------------------------------------------- left: clustering
rbox(100, 15, 686, 85, BLUE_HDR, r=26)
fit_text(393, 50, "Same points, split with different m", 570, 25, "white")
rbox(148, 96, 645, 162, BLUE_SUB, r=26)
fit_text(396, 129, "The clustering is not unique → ambiguity", 480, 20, BLUE_TXT)

# S-shaped band (centerline through the original's shape, m = 2 panel coordinates)
center = catmull_rom([(220, 357), (222, 322), (235, 290), (254, 262), (283, 239), (318, 226),
                      (352, 229), (380, 248), (396, 278), (398, 312), (412, 342), (440, 357),
                      (470, 353), (500, 337), (524, 311), (544, 281), (558, 252), (572, 236)])
tang = np.gradient(center, axis=0)
tang /= np.hypot(*tang.T)[:, None]
norm = np.c_[-tang[:, 1], tang[:, 0]]
n_pos = 19
band, frac = [], []
for i in range(n_pos):
    for side, shift in ((+1, 0.0), (-1, 0.5)):
        f = min((i + shift) / (n_pos - 0.5), 1.0)
        k = int(round(f * (len(center) - 1)))
        band.append(center[k] + side * 13 * norm[k])
        frac.append(f)
band, frac = np.array(band), np.array(frac)


def segment_colors(bounds, cols):
    return [cols[int(np.searchsorted(bounds, f, side="right"))] for f in frac]


panels = [  # (top, label, cluster boundaries along the curve, colors)
    (175, "m = 2", [0.50], [C_BLUE, C_ORANGE]),
    (413, "m = 3", [0.25, 0.51, 0.76], [C_BLUE, C_GREEN, C_YELLOW, C_ORANGE]),
    (650, "m = 5", [0.25, 0.47, 0.64, 0.80], [C_BLUE, C_GREEN, C_YELLOW, C_RED, C_PURPLE]),
]
for top, label, bounds, cols in panels:
    h = 222 if top == 175 else 220
    rbox(55, top, 720, top + h, "white", edge=BLUE_EDGE, lw=2, r=18, z=1)
    rbox(68, top + 12, 197, top + 66, BLUE_PILL, r=27, z=2)
    ax.text(132, top + 40, label, ha="center", va="center", fontsize=22,
            color="white", fontweight="bold", zorder=3)
    dots(band + [0, top - 175], segment_colors(bounds, cols), 9)

rbox(55, 887, 720, 1000, BLUE_SUB, r=22)
fit_text(388, 943, "The number of clusters m is given by the user;\n"
                   "the same points can have different clustering results.",
         630, 19, BLUE_TXT)

# ---------------------------------------------------------------- right: dimensionality reduction
rbox(842, 15, 1465, 85, GREEN_HDR, r=26)
fit_text(1153, 50, "High-dimensional data often hides\non a low-dimensional manifold",
         600, 19, "white", ls=1.1)
rbox(842, 96, 1465, 162, GREEN_SUB, r=26)
fit_text(1153, 129, "Dimensionality reduction flattens the point cloud,\n"
                    "keeping the structure and removing redundant dimensions",
         600, 17, GREEN_TXT, ls=1.15)

# label box for the 3D cloud
rbox(820, 182, 1110, 288, GREEN_SUB, r=22)
fit_text(965, 235, "High-dimensional $\\mathbf{R}^{\\mathbf{d}}$\n($d$-dimensional space)",
         270, 19, GREEN_TXT)

# 3D axes (dashed), origin at (1155, 420)
O = (1155, 420)
arrow_line(*O, 1155, 168, dashed=True)
arrow_line(*O, 940, 487, dashed=True)
arrow_line(*O, 1463, 460, dashed=True)

# S-shaped 2-D manifold in 3-D: an S-curve in the image plane extruded along a depth axis D
rng = np.random.default_rng(7)
s_curve = catmull_rom([(1098, 452), (1058, 432), (1022, 400), (1006, 362), (1016, 326),
                       (1048, 304), (1092, 296), (1136, 306), (1172, 330), (1210, 356),
                       (1250, 378), (1290, 390), (1326, 376), (1342, 344), (1328, 312),
                       (1298, 294), (1264, 286), (1240, 266), (1242, 242), (1272, 226),
                       (1314, 222), (1358, 236), (1400, 262)], n=300)
D = np.array([-16.0, 20.0])          # depth direction (towards the viewer, lower-left)
pts, shade = [], []
for k in range(0, len(s_curve), 6):
    for w in np.linspace(-1, 1, 4):
        p = s_curve[k] + w * D + rng.normal(0, 3.0, 2)
        pts.append(p)
        shade.append(w)
pts, shade = np.array(pts), np.array(shade)
dark, light = np.array([0.10, 0.45, 0.22]), np.array([0.58, 0.82, 0.52])
mix = np.clip((1 - shade) / 2 + rng.normal(0, 0.12, len(shade)), 0, 1)[:, None]
order = np.argsort(-shade)            # draw back (light) first, front (dark) on top
dots(pts[order], (dark + (light - dark) * mix)[order], 6.5)

# big down arrow + label
ax.add_patch(Polygon([(1130, 503), (1168, 503), (1168, 552), (1188, 552), (1148, 596),
                      (1108, 552), (1130, 552)], closed=True, fc=GREEN_HDR, ec="none", zorder=3))
ax.text(1205, 548, "Dimensionality\nreduction", ha="left", va="center", fontsize=24,
        color="#1B2A22", fontweight="bold", linespacing=1.1, zorder=3)

# label box for the embedding
rbox(817, 607, 1095, 710, GREEN_SUB, r=22)
fit_text(956, 658, "Low-dimensional\nmanifold embedding\n(low-dimensional space)",
         255, 18, GREEN_TXT, ls=1.15)

# 2D axes (solid), origin at (928, 848)
arrow_line(928, 848, 928, 722, dashed=False)
arrow_line(928, 848, 1463, 848, dashed=False)

# 1-D embedding: a sine wave
xw = np.linspace(950, 1452, 28)
yw = 775 - 45 * np.sin(2 * np.pi * (xw - 985) / 335)
t = (xw - xw[0]) / (xw[-1] - xw[0])
f = 0.15 + 0.85 * np.exp(-((t - 0.55) / 0.22) ** 2)
f[t < 0.12] *= t[t < 0.12] / 0.12
f[t > 0.9] *= (1 - t[t > 0.9]) / 0.1 * 0.6 + 0.4
dots(np.c_[xw, yw], dark + (light - dark) * f[:, None], 7.5)

rbox(822, 887, 1487, 1000, GREEN_SUB, r=22)
fit_text(1154, 943, "High-dimensional point clouds often lie on a\n"
                    "low-dimensional manifold; dimensionality\n"
                    "reduction can reveal this structure.",
         630, 19, GREEN_TXT, ls=1.15)

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=100, facecolor="white")
print(OUT)
