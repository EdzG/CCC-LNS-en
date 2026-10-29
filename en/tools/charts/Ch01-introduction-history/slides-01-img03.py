"""English redraw of the 4th inline (data: URI) image of
IDL_115/Ch01-introduction-history/slides/01-ml-theory-surrogate-bias-loop.html.

No Free Lunch: the sequence 2, 4, 6 and three equally possible next values
(8 = arithmetic, 100 = jump, "giraffe" drawn at 5 as a placeholder). 1035x585 px.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/01-ml-theory-surrogate-bias-loop/assets/img03.png"

W, H, DPI = 1035, 585, 100
plt.rcParams["font.family"] = "DejaVu Sans"

BG, PANEL, GRID = "#0f172a", "#1e293b", "#334155"
TICK, TITLE = "#94a3b8", "#e2e8f0"
BLUE, ORANGE, GREEN, PINK = "#38bdf8", "#f59e0b", "#10b981", "#e84393"

fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
# axes box in pixels of the original: x 84..1020, y 47..535 (from the top)
ax = fig.add_axes([84 / W, (H - 535) / H, (1020 - 84) / W, (535 - 47) / H])
ax.set_facecolor(PANEL)
for s in ax.spines.values():
    s.set_color(GRID)
ax.set_xlim(0.505, 5.185)
ax.set_ylim(0, 14)
ax.set_xticks([1, 2, 3, 4], ["#1", "#2", "#3", "#4 ?"])
ax.set_yticks(range(0, 15, 2))
ax.tick_params(colors=TICK, labelsize=13, length=4)
ax.set_ylabel("Sequence value", color=TICK, fontsize=12)

mk = dict(marker="o", ms=14, mec="white", mew=2, zorder=5)
ax.plot([1, 2, 3], [2, 4, 6], color=BLUE, lw=3.5, mfc=BLUE, **mk)
for x, y in [(1, 2), (2, 4), (3, 6)]:
    ax.text(x, y + 0.6, str(y), color=BLUE, fontsize=14, ha="center", va="bottom")

for y, c, lab in [(12, ORANGE, "100 (jump)"), (8, GREEN, "8 (arithmetic)"), (5, PINK, "giraffe (?)")]:
    ax.plot([3, 4], [6, y], color=c, lw=2.5, ls="--", zorder=3)
    ax.plot([4], [y], color=c, mfc=c, **mk)
    ax.text(4.15, y, lab, color=c, fontsize=11, fontweight="bold", va="center", ha="left")

ax.text(2.7, 1.0, "Inductive bias = your preconception that “it’s arithmetic”",
        color=ORANGE, fontsize=11.5, ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.3", fc=PANEL, ec="#6366f1", lw=1.5))

fig.text(0.5, 1 - 25 / H, "No Free Lunch · 2, 4, 6, what comes next? (no bias, no answer)",
         color=TITLE, fontsize=14, ha="center", va="center")

fig.savefig(OUT, dpi=DPI, facecolor=BG)
print(OUT)
