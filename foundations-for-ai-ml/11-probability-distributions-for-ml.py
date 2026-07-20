"""
Foundations for AI & ML
Chapter 11: Probability Distributions for ML
Section: Probability & Statistics

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/probability-distributions-for-ml

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from math import comb

def binomial_pmf(k, n, p):
    # comb(n, k) counts the arrangements; the rest is the per-arrangement probability
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

print(binomial_pmf(2, 4, 0.5))   # 0.375
