"""English redraw of IDL_115/Ch01-introduction-history/assets/idl115-w1-learning-frameworks-imagegen.png
(used in the condensed deck idl115-w1-dl-intro-history.html).

Three panels: supervised / unsupervised / reinforcement learning. The original is a bilingual
AI-generated infographic ("English | 中文"); this version keeps only the English labels.
Coordinates are in pixels of the original (1672x941), y pointing down.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/idl115-w1-dl-intro-history/assets/idl115-w1-learning-frameworks-imagegen.png"

W, H, DPI = 1672, 941, 100
PX = 72 / DPI  # points per pixel

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["mathtext.fontset"] = "dejavusans"

THEMES = {
    "blue":   dict(head="#286adf", edge="#1a62d8", panel="#f1f6fe", pedge="#89b7f8",
                   box="#d3e7fc", line="#0b5eda", text="#101c4f"),
    "green":  dict(head="#1a926c", edge="#1a8a66", panel="#effaf6", pedge="#8fd3bb",
                   box="#d9f1e8", line="#088460", text="#062a22"),
    "orange": dict(head="#e85d0d", edge="#e9601a", panel="#fdf3ed", pedge="#f4b38c",
                   box="#fdd9c4", line="#e65a10", text="#3a1606"),
}

fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)
ax.axis("off")
fig.patch.set_facecolor("#fdfdfd")


def rbox(x0, y0, x1, y1, fc, ec, lw=3.0, r=16, z=2):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw * PX * 1.4, zorder=z))


def label(x, y, s, color, size=28, weight="normal"):
    ax.text(x, y, s, ha="center", va="center", color=color, fontsize=size * PX,
            fontweight=weight, linespacing=1.25, zorder=5)


def node(box, s, t, size=28):
    x0, y0, x1, y1 = box
    rbox(x0, y0, x1, y1, t["box"], t["line"])
    label((x0 + x1) / 2, (y0 + y1) / 2, s, t["text"], size)


def poly(pts, t, arrow=True):
    xs, ys = zip(*pts)
    end = len(pts) - 1 if arrow else len(pts)
    ax.plot(xs[:end + (0 if arrow else 0)], ys[:end + (0 if arrow else 0)],
            color=t["line"], lw=9 * PX, solid_joinstyle="miter", solid_capstyle="butt", zorder=1)
    if arrow:
        (xa, ya), (xb, yb) = pts[-2], pts[-1]
        ax.add_patch(FancyArrowPatch((xa, ya), (xb, yb), arrowstyle="-|>,head_length=1.3,head_width=0.9",
                                     mutation_scale=12, color=t["line"], lw=9 * PX,
                                     shrinkA=0, shrinkB=0, zorder=1))


def curve(a, b, rad, t):
    ax.add_patch(FancyArrowPatch(a, b, connectionstyle=f"arc3,rad={rad}",
                                 arrowstyle="-|>,head_length=1.3,head_width=0.9", mutation_scale=12,
                                 color=t["line"], lw=9 * PX, shrinkA=0, shrinkB=0, zorder=1))


def panel(x0, x1, title, t):
    y0, y1, hh = 45, 888, 80
    rbox(x0, y0, x1, y1, t["panel"], t["pedge"], lw=2.5, r=14, z=0)
    rbox(x0, y0, x1, y0 + hh, t["head"], t["edge"], lw=2.5, r=14, z=0.5)
    # square off the bottom corners of the header
    ax.add_patch(plt.Rectangle((x0 + 1, y0 + hh - 20), x1 - x0 - 2, 20, fc=t["head"], ec="none", zorder=0.6))
    label((x0 + x1) / 2, y0 + hh / 2 + 2, title, "white", 29, "bold")


# ---------------- supervised ----------------
b = THEMES["blue"]
panel(18, 556, "SUPERVISED LEARNING", b)
poly([(162, 258), (162, 297), (424, 297), (424, 258)], b, arrow=False)
poly([(285, 297), (285, 366)], b)
poly([(285, 472), (285, 547)], b)
poly([(285, 652), (285, 726)], b)
node((43, 163, 282, 258), r"features $x$", b)
node((313, 163, 533, 258), r"label $y$", b)
node((122, 368, 449, 472), r"model $f_\theta$", b, 30)
node((125, 549, 449, 652), r"prediction $\hat{y}$", b)
node((75, 728, 497, 852), "loss: compare\n$\\hat{y}$ with $y$", b)

# ---------------- unsupervised ----------------
g = THEMES["green"]
panel(567, 1105, "UNSUPERVISED LEARNING", g)
poly([(836, 258), (836, 337)], g)
poly([(836, 457), (836, 489), (704, 489), (704, 546)], g)
poly([(836, 489), (969, 489), (969, 546)], g)
poly([(704, 658), (704, 688), (969, 688), (969, 660)], g, arrow=False)
poly([(836, 688), (836, 733)], g)
node((598, 162, 1074, 258), r"unlabeled data $x$", g)
node((616, 339, 1058, 457), "representation /\ngrouping", g)
node((589, 548, 820, 658), "clusters", g)
node((850, 548, 1083, 660), "latent features", g, 26)
node((587, 735, 1087, 855), "feedback: similarity\nor reconstruction", g)

# ---------------- reinforcement ----------------
o = THEMES["orange"]
panel(1116, 1655, "REINFORCEMENT LEARNING", o)
curve((1505, 222), (1578, 352), -0.45, o)   # agent -> action
curve((1578, 442), (1530, 582), -0.40, o)   # action -> environment
curve((1265, 612), (1188, 472), -0.45, o)   # environment -> next state + reward
curve((1185, 368), (1268, 222), -0.40, o)   # next state + reward -> agent
node((1270, 167, 1505, 272), "agent", o, 30)
node((1435, 355, 1642, 442), r"action $a_t$", o, 27)
node((1265, 562, 1527, 665), "environment", o)
node((1128, 368, 1402, 468), "next state $s_{t+1}$\n+ reward $r_t$", o, 25)
node((1143, 737, 1632, 853), "goal: maximize\ncumulative reward", o)

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=DPI, facecolor=fig.get_facecolor())
print(OUT)
