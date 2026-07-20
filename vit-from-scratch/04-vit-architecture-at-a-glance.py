"""
Build a Vision Transformer (ViT) from Scratch
Chapter 4: The ViT Architecture at a Glance
Section: Why Vision Transformers

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/vit-architecture-at-a-glance

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# one ViT encoder block — pre-norm, residual-wrapped
x = x + MultiHeadAttention(LayerNorm(x))   # tokens mix across positions
x = x + MLP(LayerNorm(x))                   # each token processed on its own
