"""
Build a Vision Transformer (ViT) from Scratch
Chapter 15: Multi-Head Attention
Section: Attention Inside the ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/multi-head-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# x: (4, 8) after Q/K/V projection, here just Q for illustration
# 4 tokens, D = 8, h = 2 heads, d_k = 4
Q = Q.reshape(4, 2, 4)        # (tokens, heads, d_k) -> split 8 into 2 x 4
Q = Q.transpose(1, 0, 2)      # (heads, tokens, d_k) -> heads on the outside
# now Q[0] is a (4, 4) matrix: head-0's queries for all 4 tokens
# and Q[1] is head-1's (4, 4) queries
