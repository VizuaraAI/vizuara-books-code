"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 11: Why Do We Need Positional Encoding?
Section: Positional Encoding

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/why-do-we-need-positional-encoding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
dog   = [1.0, 0.0]
bites = [0.0, 1.0]
man   = [1.0, 1.0]

# --- block 2 ---
import numpy as np

def sinusoidal_pe(seq_len, d_model, base=10000.0):
    pos  = np.arange(seq_len)[:, None]              # (seq_len, 1)
    i    = np.arange(d_model // 2)[None, :]         # pair index
    freq = 1.0 / base ** (2 * i / d_model)          # (1, d_model/2)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(pos * freq)                # even dims
    pe[:, 1::2] = np.cos(pos * freq)                # odd dims
    return pe

print(np.round(sinusoidal_pe(4, 8), 3))
# [[ 0.     1.     0.     1.     0.     1.     0.     1.   ]
#  [ 0.841  0.54   0.1    0.995  0.01   1.     0.001  1.   ]
#  [ 0.909 -0.416  0.199  0.98   0.02   1.     0.002  1.   ]
#  [ 0.141 -0.99   0.296  0.955  0.03   1.     0.003  1.   ]]
