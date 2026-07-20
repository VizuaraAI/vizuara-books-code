"""
Writing Journal & Conference Papers
Chapter 34: Tools for Making Figures
Section: Figures and Tables

Read this chapter: https://books.vizuara.ai/read/writing-research-papers/tools-for-making-figures

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import seaborn as sns
import matplotlib.pyplot as plt

# five methods, their reported accuracies from your literature review
methods  = ["Ours", "CNN", "RNN", "SVM", "Baseline"]
accuracy = [0.91, 0.86, 0.83, 0.77, 0.62]

sns.set_theme(style="whitegrid")          # clean publication defaults
ax = sns.barplot(x=methods, y=accuracy)
ax.set_ylabel("Accuracy")
ax.set_ylim(0, 1)                          # honest axis: start bars at 0
plt.savefig("fig3.pdf", bbox_inches="tight")   # vector, again
