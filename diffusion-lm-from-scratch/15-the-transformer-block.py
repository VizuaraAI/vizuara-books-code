"""
Build a Diffusion Language Model from Scratch
Chapter 15: Inside the Transformer Block
Section: The Autoregressive Baseline

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/the-transformer-block

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- block 1 ---
def feed_forward(x, W1, b1, W2, b2):
    # x: (seq_len, d_model)   one row per token
    h = x @ W1 + b1           # up-project:   (seq_len, d_ff)
    h = np.maximum(h, 0)      # ReLU non-linearity (GELU in real models)
    return h @ W2 + b2        # down-project: (seq_len, d_model)

# --- block 2 ---
def transformer_block(x):
    # x: (seq_len, d_model)  — same shape returned at the end
    x = x + masked_attention(layer_norm(x))   # 1. mix across tokens (causal)
    x = x + feed_forward(layer_norm(x))        # 2. think per token
    return x                                    # (seq_len, d_model)
