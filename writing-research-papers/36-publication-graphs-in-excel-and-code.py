"""
Writing Journal & Conference Papers
Chapter 36: Publication Graphs in Excel and Code
Section: Figures and Tables

Read this chapter: https://books.vizuara.ai/read/writing-research-papers/publication-graphs-in-excel-and-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import seaborn as sns
import matplotlib.pyplot as plt

methods  = ["Ours", "CNN", "RNN", "SVM", "Baseline"]
accuracy = [0.91, 0.86, 0.83, 0.77, 0.62]

sns.set_theme(style="whitegrid", context="paper", font_scale=1.4)  # print-sized text

fig, ax = plt.subplots(figsize=(3.3, 2.6))          # column width in INCHES, at final size
bars = ax.bar(methods, accuracy, color="#4C72B0")
bars[0].set_color("#DD8452")                          # highlight "Ours" in one accent color

ax.set_ylim(0, 1)                                     # honest axis: bars start at zero
ax.set_ylabel("Accuracy")
ax.set_xlabel("")
sns.despine()                                         # drop the top + right spines (chartjunk)

for bar, v in zip(bars, accuracy):                    # print the exact value on each bar
    ax.text(bar.get_x() + bar.get_width()/2, v + 0.02,
            f"{v:.2f}", ha="center", fontsize=9)

fig.savefig("fig3.pdf", bbox_inches="tight")          # vector, again
