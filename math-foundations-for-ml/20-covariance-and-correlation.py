"""
Mathematical Foundations for Machine Learning
Chapter 20: Covariance and Correlation
Section: Probability and Statistics Foundations

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/covariance-and-correlation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
height = [150, 160, 170, 180, 190]   # cm
weight = [ 50,  65,  62,  80,  88]   # kg

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# The covariance matrix written in maths notation: Cov and Var are the
# mathematical operators, not Python functions, and x and y are symbols in a
# formula rather than variables any earlier block defines.
# C = [[ Cov(x, x),  Cov(x, y) ],
#      [ Cov(y, x),  Cov(y, y) ]]
#
# # which is exactly, using Cov(a,a) = Var(a):
# C = [[ Var(x),    Cov(x, y) ],
#      [ Cov(x, y), Var(y)    ]]
