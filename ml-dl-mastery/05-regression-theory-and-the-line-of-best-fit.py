"""
Machine Learning & Deep Learning Mastery
Chapter 5: Regression Theory and the Line of Best Fit
Section: Regression

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/regression-theory-and-the-line-of-best-fit

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# It is the equation of the line typeset as Python; w, x and b are symbols in
# a formula, not variables any earlier block defines.
# ŷ = w * x + b     # w = slope, b = intercept

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# The definition of a residual, in maths notation.
# residual_i = y_i - ŷ_i     # actual minus predicted, for point i

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# SSR = Σ (y_i - ŷ_i)²     # sum over all data points i

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# MSE = (1/n) * Σ (y_i - ŷ_i)²     # n = number of points
