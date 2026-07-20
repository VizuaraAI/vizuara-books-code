"""
Machine Learning & Deep Learning Mastery
Chapter 35: AdaGrad, RMSProp, and Adam
Section: Optimizers & Training

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/adagrad-rmsprop-adam

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# NOTE: every block in this chapter is prose in the book, not runnable code.
# They are the AdaGrad / RMSProp / Adam update rules in maths notation: the
# names are symbols in formulas, and even `sqrt` is written as the maths
# function rather than np.sqrt or math.sqrt. Chapter 36 (Optimizers in Code)
# is the runnable version of all three.

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# G = G + g**2                       # accumulate squared gradients (per parameter)
# theta = theta - (eta / (sqrt(G) + eps)) * g

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# v = beta * v + (1 - beta) * g**2       # EWMA of squared gradients, beta ≈ 0.9
# theta = theta - (eta / (sqrt(v) + eps)) * g

# --- block 3 ---
# NOTE: this block is prose in the book, not runnable code.
# m = beta1 * m + (1 - beta1) * g          # 1st moment: momentum
# v = beta2 * v + (1 - beta2) * g**2       # 2nd moment: RMSProp scale
# m_hat = m / (1 - beta1**t)               # bias-corrected (t = step number, 1-indexed)
# v_hat = v / (1 - beta2**t)
# theta = theta - eta * m_hat / (sqrt(v_hat) + eps)
