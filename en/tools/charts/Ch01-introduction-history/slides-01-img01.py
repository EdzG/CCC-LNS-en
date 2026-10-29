"""English redraw of the 2nd inline (data: URI) image of
IDL_115/Ch01-introduction-history/slides/01-ml-theory-surrogate-bias-loop.html:
the MSE worked example (squared errors 4, 16, 25; mean 15). 罪孽值 = "sin score" in this deck.
Original: 1035x614 px, dark theme.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "en/IDL_115/Ch01-introduction-history/slides/01-ml-theory-surrogate-bias-loop/assets/img01.png"

W, H, DPI = 1035, 614, 100
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["mathtext.fontset"] = "dejavusans"

BG, PANEL, GRID, TEXT, MUTED = "#0f172a", "#1e293b", "#334155", "#e2e8f0", "#94a3b8"
COLORS = ["#38bdf8", "#a78bfa", "#f59e0b"]
GREEN = "#10b981"

students = [("Stu A", 80, 82), ("Stu B", 90, 86), ("Stu C", 70, 75)]
sq = [(y - yh) ** 2 for _, y, yh in students]
mse = sum(sq) / len(sq)

fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
fig.patch.set_facecolor(BG)
ax = fig.add_axes([85 / W, (H - 540) / H, (1020 - 85) / W, (540 - 47) / H])
ax.set_facecolor(PANEL)
for s in ax.spines.values():
    s.set_color(GRID)

x = range(3)
ax.bar(x, sq, width=0.55, color=COLORS, edgecolor="white", linewidth=1.5, zorder=2)
for xi, v in zip(x, sq):
    ax.text(xi, v + 0.6, f"{v}", ha="center", va="bottom", color="white",
            fontsize=17, fontweight="bold", zorder=3)
ax.axhline(mse, color=GREEN, linestyle="--", linewidth=2.5, zorder=4)
ax.text(1.0, mse + 1.2, f"MSE = {mse:g} (mean)", ha="center", va="center", color=GREEN,
        fontsize=15, zorder=5,
        bbox=dict(boxstyle="round,pad=0.3", facecolor=PANEL, edgecolor=GREEN, linewidth=1.2))

ax.set_xlim(-0.405, 2.40)
ax.set_ylim(0, 26.28)
ax.set_xticks(list(x))
ax.set_xticklabels([f"{n}\n$y={y}, \\hat{{y}}={yh}$" for n, y, yh in students])
ax.set_yticks([0, 5, 10, 15, 20, 25])
ax.tick_params(colors=MUTED, labelsize=14.5)
ax.set_ylabel("Squared Error", color=MUTED, fontsize=15)
ax.set_title(f"MSE = (4+16+25)/3 = {mse:g}  ·  Computing the sin score", color=TEXT,
             fontsize=16, pad=12)

fig.savefig(OUT, dpi=DPI, facecolor=BG)
print(OUT)
