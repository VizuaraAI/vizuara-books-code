"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 9: Sinusoidal Encoding
Section: Positional Encoding

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/sinusoidal-encoding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def sinusoidal_encoding(max_len, d_model, base=10000.0):
    pos = np.arange(max_len)[:, None]          # shape (max_len, 1)
    i   = np.arange(0, d_model, 2)[None, :]    # even indices: 0,2,4,...
    freq = 1.0 / (base ** (i / d_model))       # shape (1, d_model/2)

    PE = np.zeros((max_len, d_model))
    PE[:, 0::2] = np.sin(pos * freq)           # even dims → sin
    PE[:, 1::2] = np.cos(pos * freq)           # odd dims  → cos
    return PE

PE = sinusoidal_encoding(max_len=50, d_model=128)
print(PE.shape)   # (50, 128)
