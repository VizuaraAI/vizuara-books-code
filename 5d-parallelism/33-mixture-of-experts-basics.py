"""
5D Parallelism for Large Model Training
Chapter 33: Mixture-of-Experts Basics
Section: Expert Parallelism and MoE

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/mixture-of-experts-basics

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

x        = np.array([0.9, -0.2, 0.1, 0.7, -0.5, 0.3, 0.0, 0.4])  # one token, d_model = 8
W_router = np.random.randn(8, 4)          # (d_model, E) = (8, 4)

logits   = x @ W_router                   # shape (4,): one raw score per expert
gates    = softmax(logits)                # turn scores into a distribution over experts
top      = gates.argmax()                 # top-1: the winning expert index
