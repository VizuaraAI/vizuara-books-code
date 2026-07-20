"""
Mathematical Foundations for Machine Learning
Chapter 21: Distributions as Shapes of Chance
Section: Probability Distributions

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/distributions-as-shapes-of-chance

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from scipy.stats import binom

# 10 fair coin flips: a discrete variable, so it has a PMF
print(binom.pmf(5, n=10, p=0.5))   # P(exactly 5 heads) ≈ 0.246  ← a real probability
print(binom.cdf(5, n=10, p=0.5))   # P(5 or fewer heads) ≈ 0.623  ← accumulated
print(binom.pmf(0, n=10, p=0.5) +
      binom.pmf(1, n=10, p=0.5))   # matches binom.cdf(1, ...)   ← spikes add to CDF
