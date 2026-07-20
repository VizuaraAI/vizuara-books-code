"""
Build a Diffusion Language Model from Scratch
Chapter 12: Tokenization and Embeddings
Section: The Autoregressive Baseline

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/tokenization-and-embeddings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
vocab = {
    "the": 262, "cat": 3797, "sat": 3332,
    "on":  319, "mat": 6759, "[MASK]": 50257,
}

def tokenize(text):
    return [vocab[word] for word in text.split()]

tokenize("the cat sat")   # -> [262, 3797, 3332]

# --- block 2 ---
import numpy as np

d = 8
vocab_size = 50258                 # 50257 real tokens + 1 for [MASK]
E = np.random.randn(vocab_size, d) # the learnable embedding matrix

ids = [262, 3797, 3332]            # "the cat sat"
X = E[ids]                         # fancy-index the three rows
X.shape                            # (3, 8)  -> 3 tokens, 8 numbers each

# --- block 3 ---
P = np.random.randn(512, d)        # a learnable position table, one row per slot
X = E[ids] + P[:len(ids)]          # token identity + position, element-wise add
