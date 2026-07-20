"""
Build a Diffusion Language Model from Scratch
Chapter 18: The Forward Masking Process
Section: Diffusion Language Model Theory

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/the-forward-masking-process

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

def forward_mask(x, t, mask_id):
    # x: LongTensor of token ids, shape (L,)   t: float in [0, 1]
    coins = torch.rand(x.shape)          # one uniform draw per position
    masked = coins < t                   # True where the coin says "mask"
    return torch.where(masked, mask_id, x), masked

# --- block 2 ---
t = torch.rand(1).item()             # a new masking level per training example
x_t, masked = forward_mask(x0, t, mask_id)
