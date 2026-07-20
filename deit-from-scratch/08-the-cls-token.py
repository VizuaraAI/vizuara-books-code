"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 8: The CLS Token
Section: Images as Tokens

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-cls-token

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

D = 384                                        # DeiT-Small embedding width
cls_token = nn.Parameter(torch.zeros(1, 1, D)) # ONE learnable vector, shape (1, 1, 384)
nn.init.trunc_normal_(cls_token, std=0.02)     # init as small noise, then it's learned

# x is the patch-embedding output: (batch, 196, D)
x = patch_embed(image)                         # e.g. (8, 196, 384)
B = x.shape[0]                                  # batch size = 8

cls = cls_token.expand(B, -1, -1)              # (8, 1, 384): same vector for every image
x = torch.cat([cls, x], dim=1)                 # PREPEND -> (8, 197, 384)

# --- block 2 ---
x = encoder(x)          # (8, 197, 384) -> (8, 197, 384)
cls_final = x[:, 0]     # (8, 384): take ONLY position 0, the CLS token
logits = head(cls_final)  # nn.Linear(384, 1000): (8, 1000) class scores
