"""
Build a NanoVLM from Scratch
Chapter 6: What We Will Build: The NanoVLM Blueprint
Section: Vision-Language Foundations

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/what-we-will-build-nanovlm-blueprint

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
from torch import arange
from torch.nn.functional import cross_entropy

# Blueprint sketch: these stand for the tensors the finished model produces.
# Chapter 30 assembles the real forward pass:
# https://books.vizuara.ai/read/nanovlm-from-scratch/assembling-the-full-forward-pass
I = None       # TODO: (N, d) L2-normalized image embeddings
T = None       # TODO: (N, d) L2-normalized text embeddings
N = 0          # TODO: the batch size
logits = None  # TODO: (N, N) scaled similarities


# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# cos(a, b) = (a · b) / (||a|| * ||b||)

# --- block 2 ---
S = I @ T.T          # shape (N, N): S[i][j] = cosine(image_i, text_j)

# --- block 3 ---
labels = arange(N)                     # [0, 1, ..., N-1]
loss_i2t = cross_entropy(logits,   labels)   # each row: pick the right caption
loss_t2i = cross_entropy(logits.T, labels)   # each column: pick the right image
loss     = (loss_i2t + loss_t2i) / 2

# --- block 4 ---
S = [[0.90, 0.10],     # image 0 vs [its caption, the wrong one]
     [0.15, 0.85]]     # image 1 vs [the wrong one, its caption]
