"""Draw assets/execution_accuracy.png from results/metrics.csv."""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
rows = list(csv.DictReader((root / "results" / "metrics.csv").open()))
rows.sort(key=lambda r: float(r["execution_accuracy"]))
names = [r["method"] for r in rows]
acc = [float(r["execution_accuracy"]) * 100 for r in rows]

BG, INK, MUT, BLUE, GRAY = "#fcfcfb", "#0b0b0b", "#52514e", "#2a78d6", "#b9b8b3"
colors = [GRAY if "Template" in n or "Chain" in n else BLUE for n in names]

fig, ax = plt.subplots(figsize=(9, 4.2), dpi=200, facecolor=BG)
ax.set_facecolor(BG)
bars = ax.barh(names, acc, color=colors, height=0.62)
for b, v in zip(bars, acc):
    ax.text(v + 0.8, b.get_y() + b.get_height() / 2, f"{v:.1f}%", va="center", color=INK, fontsize=9)
ax.set_xlim(0, 58)
ax.set_xlabel("Execution accuracy (% of 499 questions)", color=MUT)
ax.set_title("Natural-language-to-SQL: execution accuracy by method", loc="left",
             fontsize=11, fontweight="bold", color=INK)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(colors=MUT)
fig.tight_layout()
out = root / "assets" / "execution_accuracy.png"
fig.savefig(out, facecolor=BG)
print("wrote", out)
