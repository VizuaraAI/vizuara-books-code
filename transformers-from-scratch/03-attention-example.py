"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 3: Attention Example
Section: Foundations of Attention

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/attention-example

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# rows: [the, cat, sat]
Q = np.array([[1.0, 0.0],    # the  is looking for...
              [0.0, 1.0],    # cat  is looking for...
              [1.0, 1.0]])   # sat  is looking for...

K = np.array([[1.0, 0.0],    # the  offers
              [1.0, 1.0],    # cat  offers
              [0.0, 1.0]])   # sat  offers

V = np.array([[10.0,  0.0],  # the  carries
              [ 0.0, 10.0],  # cat  carries
              [ 5.0,  5.0]]) # sat  carries

# --- block 2 ---
def softmax(s):
    s = s - np.max(s)          # subtract the max for numerical stability
    e = np.exp(s)              # exponentiate — always positive, monotonic
    return e / np.sum(e)       # normalize so the weights sum to 1

# --- block 3 ---
d_k = Q.shape[1]                          # = 2
scores  = Q @ K.T                         # (3,2)@(2,3) -> (3,3)
scores  = scores / np.sqrt(d_k)           # scale, still (3,3)
weights = softmax_rows(scores)            # softmax each ROW -> (3,3), rows sum to 1
output  = weights @ V                     # (3,3)@(3,2) -> (3,2)
