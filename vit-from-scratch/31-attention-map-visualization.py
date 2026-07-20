"""
Build a Vision Transformer (ViT) from Scratch
Chapter 31: Visualizing Attention Maps
Section: Training, Data, and Beyond

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/attention-map-visualization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import math
import torch
import torch.nn as nn

# --- block 1 ---
scores  = Q @ K.transpose(-2, -1) / math.sqrt(d_k)   # (N+1, N+1)
weights = scores.softmax(dim=-1)                       # (N+1, N+1), each row sums to 1
out     = weights @ V                                  # (N+1, d_k)

# --- block 2 ---
class MultiHeadAttention(nn.Module):
    def forward(self, x):
        # ... project to Q, K, V, split into h heads ...
        scores  = (Q @ K.transpose(-2, -1)) / math.sqrt(self.d_k)
        weights = scores.softmax(dim=-1)      # (B, h, N+1, N+1)
        self.attn_weights = weights.detach()  # <-- stash for later
        out = weights @ V
        # ... concat heads, output projection ...
        return out

# --- block 3 ---
A = 0.5 * attn_per_layer + 0.5 * torch.eye(N + 1)   # residual: half self, half attention
A = A / A.sum(dim=-1, keepdim=True)                  # renormalize rows to sum to 1

# --- block 4 ---
rollout = A_layer1
for A in layers[1:]:
    rollout = A @ rollout        # (197, 197) chained matrix product
cls_map = rollout[0, 1:]         # class-token row, drop self -> 196 patch weights

# --- block 5 ---
import torch.nn.functional as F

heat = cls_map.reshape(1, 1, 14, 14)                       # (1,1,14,14)
heat = F.interpolate(heat, size=(224, 224), mode="bilinear",
                     align_corners=False)                   # (1,1,224,224)
heat = (heat - heat.min()) / (heat.max() - heat.min())      # normalize to [0,1] for display
# overlay `heat` on the original image with a colormap (e.g. matplotlib 'jet')
