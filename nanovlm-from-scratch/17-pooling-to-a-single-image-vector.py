"""
Build a NanoVLM from Scratch
Chapter 17: Pooling to a Single Image Vector
Section: Encoding Images into Vectors

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/pooling-to-a-single-image-vector

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# The [CLS] route needs a learned CLS parameter and a stack of transformer
# blocks. The chapter describes both but does not code them here.
cls = None                 # TODO: (1, D) learned [CLS] parameter
transformer_blocks = None  # TODO: the transformer stack, (S, D) -> (S, D)


# --- block 1 ---
import numpy as np

tokens = np.array([
    [1.0, 0.0, 2.0],   # patch 0
    [3.0, 2.0, 0.0],   # patch 1
    [1.0, 4.0, 2.0],   # patch 2
    [3.0, 2.0, 0.0],   # patch 3
])                      # shape (4, 3): 4 tokens, D=3

image_vec = tokens.mean(axis=0)   # average DOWN the rows
# column 0: (1+3+1+3)/4 = 2.0
# column 1: (0+2+4+2)/4 = 2.0
# column 2: (2+0+2+0)/4 = 1.0
print(image_vec)                  # -> [2.0, 2.0, 1.0], shape (3,)

# --- block 2 ---
# tokens: (196, D) patch embeddings, cls: (1, D) learned parameter
seq = np.concatenate([cls, tokens], axis=0)   # (197, D): [CLS] + 196 patches
seq = transformer_blocks(seq)                 # (197, D): every token has mixed
image_vec = seq[0]                            # keep ONLY the [CLS] output, shape (D,)
