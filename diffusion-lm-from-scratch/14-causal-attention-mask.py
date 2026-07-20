"""
Build a Diffusion Language Model from Scratch
Chapter 14: The Causal Attention Mask
Section: The Autoregressive Baseline

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/causal-attention-mask

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# scores[i][j] = how much query i wants key j  (shape 4x4, pre-softmax)
scores = [
  [ 2.0,  0.5,  1.0,  0.3 ],   # row 0 = "The"  querying keys 0..3
  [ 0.4,  3.0,  0.8,  1.2 ],   # row 1 = "cat"
  [ 0.9,  1.1,  2.5,  0.7 ],   # row 2 = "sat"
  [ 0.2,  0.6,  1.5,  2.2 ],   # row 3 = "on"
]

# --- block 2 ---
import numpy as np

def causal_mask(L):
    # 1 = keep (allowed), 0 = block (future)
    return np.tril(np.ones((L, L)))      # lower triangle incl. diagonal

def masked_scores(scores):
    L = scores.shape[0]
    mask = causal_mask(L)
    # where mask is 0 (the future), overwrite the score with -inf
    return np.where(mask == 1, scores, -np.inf)

# --- block 3 ---
[[ 2.0, -inf, -inf, -inf ],   # "The" may see only itself
 [ 0.4,  3.0, -inf, -inf ],   # "cat" may see The, cat
 [ 0.9,  1.1,  2.5, -inf ],   # "sat" may see The, cat, sat  (the 0.7 leak is gone)
 [ 0.2,  0.6,  1.5,  2.2 ]]   # "on"  may see everything before + itself
