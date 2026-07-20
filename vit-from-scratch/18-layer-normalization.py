"""
Build a Vision Transformer (ViT) from Scratch
Chapter 18: Layer Normalization
Section: The Transformer Encoder Block

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/layer-normalization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0]

# --- block 2 ---
import torch.nn as nn
norm = nn.LayerNorm(768)   # normalizes the last dim (D), learns gamma & beta of length 768

# --- block 3 ---
x = x + MultiHeadAttention(LayerNorm(x))   # sublayer 1: mix across tokens
x = x + MLP(LayerNorm(x))                   # sublayer 2: process each token
