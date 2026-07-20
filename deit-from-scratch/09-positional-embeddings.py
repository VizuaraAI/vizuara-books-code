"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 9: Positional Embeddings
Section: Images as Tokens

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/positional-embeddings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

torch.manual_seed(0)
X = torch.randn(4, 8)                  # 4 tokens, d = 8
attn = torch.nn.MultiheadAttention(8, num_heads=1, batch_first=True)

perm = torch.tensor([2, 0, 3, 1])      # a permutation of the 4 rows
out,  _ = attn(X[None],       X[None],       X[None])
out_p, _ = attn(X[perm][None], X[perm][None], X[perm][None])

# undo the permutation on the output and compare
print(torch.allclose(out[0][perm], out_p[0], atol=1e-6))   # -> True

# --- block 2 ---
import torch.nn as nn

num_tokens = 198          # 196 patches + CLS + distillation (DeiT-Small)
d = 384
pos_embed = nn.Parameter(torch.zeros(1, num_tokens, d))
nn.init.trunc_normal_(pos_embed, std=0.02)    # small random init, learned from here

# in the forward pass, after prepending the special tokens:
x = x + pos_embed        # broadcast-add over the batch, shapes (B,198,384)+(1,198,384)
