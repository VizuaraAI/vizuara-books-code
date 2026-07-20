"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 6: Word Embeddings
Section: Introduction to Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/word-embeddings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

vocab_size, d_model = 50000, 512
E = np.random.randn(vocab_size, d_model) * 0.02   # the learnable table

token_ids = [1996, 4937, 2938]                    # "the cat sat"

# Way 1 — the lookup we actually use: index the rows
embedded = E[token_ids]            # shape (3, 512)

# Way 2 — the equivalent one-hot matmul (wasteful, but proves the point)
onehot = np.zeros((3, vocab_size))
onehot[np.arange(3), token_ids] = 1.0
embedded_matmul = onehot @ E       # shape (3, 512)

assert np.allclose(embedded, embedded_matmul)     # identical
