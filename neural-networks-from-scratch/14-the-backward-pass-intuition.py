"""
Neural Networks from Scratch
Chapter 14: The Backward Pass: The Intuition
Section: How a Network Learns

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/the-backward-pass-intuition

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file runs standalone) ---
# `a` is the starting value of the chapter's three-step worked example. The
# chapter's own numbers pin it down: it quotes dL/dc = 28, and L = c**2 gives
# dL/dc = 2c, so c = 14, b = 12, a = 4.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/the-backward-pass-intuition
a = 4.0   # TODO: the input you want to differentiate with respect to

# --- block 1 ---
b = a * 3        # step 1: multiply
c = b + 2        # step 2: add
L = c ** 2       # step 3: square

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# dL/da = (dL/dc) * (dc/db) * (db/da)
#       =    28    *    1    *    3     =  84

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# # the gradient that seeds the entire backward pass
# dscores = predicted_probs - true_labels   #  p - y
#         = [0.7, 0.2, 0.1] - [1, 0, 0]
#         = [-0.3, 0.2, 0.1]
