"""
Build a Vision Transformer (ViT) from Scratch
Chapter 20: Residual Connections
Section: The Transformer Encoder Block

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/residual-connections

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = sublayer(x)          # plain: the input is gone, only the transform survives

# --- block 2 ---
x = x + sublayer(x)      # residual: the input passes straight through, sublayer nudges it

# --- block 3 ---
x = x + MultiHeadAttention(LayerNorm(x))   # residual around attention
x = x + MLP(LayerNorm(x))                   # residual around the MLP
