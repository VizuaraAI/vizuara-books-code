"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 10: Approaching Positional Encoding
Section: Positional Encoding

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/approaching-positional-encoding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def positional_encoding(seq_len, d_model):
    PE = np.zeros((seq_len, d_model))
    position = np.arange(seq_len)[:, None]          # shape (seq_len, 1)
    # one frequency per dimension-pair; wavelengths grow geometrically
    div = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
    PE[:, 0::2] = np.sin(position * div)            # even dims → sine
    PE[:, 1::2] = np.cos(position * div)            # odd dims  → cosine
    return PE                                       # shape (seq_len, d_model)
