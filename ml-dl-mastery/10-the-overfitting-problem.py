"""
Machine Learning & Deep Learning Mastery
Chapter 10: The Overfitting Problem
Section: Overfitting, Features & Generalization

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/the-overfitting-problem

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# The ordinary-least-squares objective written in maths notation; y, X and
# beta are symbols in a formula, not variables any earlier block defines.
# loss = ((y - X @ beta) ** 2).sum()          # fit the data, nothing else

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# The same objective with the ridge penalty added, still maths notation.
# loss = ((y - X @ beta) ** 2).sum() + lam * (beta ** 2).sum()   # fit + penalty
