"""
Mathematical Foundations for Machine Learning
Chapter 22: Bernoulli and Binomial Distributions
Section: Probability Distributions

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/bernoulli-and-binomial

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# P(X = 1) = p
# P(X = 0) = 1 - p

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# P(X = k) = C(n, k) · p^k · (1 - p)^(n - k)

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# P(X=0) = C(3,0)·0.125 = 1 × 0.125 = 0.125   # TTT
# P(X=1) = C(3,1)·0.125 = 3 × 0.125 = 0.375   # HTT, THT, TTH
# P(X=2) = C(3,2)·0.125 = 3 × 0.125 = 0.375   # HHT, HTH, THH
# P(X=3) = C(3,3)·0.125 = 1 × 0.125 = 0.125   # HHH

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# P(y | p) = p^y · (1 - p)^(1 - y)

# --- block 5 ---
# NOTE: this block is prose in the book, not runnable code.
# The binary cross-entropy loss in maths notation, like the four formulas
# above it: log is the mathematical function (not math.log or np.log), and
# y and p are symbols rather than variables any earlier block defines.
# loss = -( y*log(p) + (1 - y)*log(1 - p) )
