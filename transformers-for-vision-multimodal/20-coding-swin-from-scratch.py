"""
Transformers for Vision & Multimodal LLMs
Chapter 20: Coding Swin From Scratch
Section: Hierarchical & Dense Vision Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-swin-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

def window_partition(x, M):
    # x: (B, H, W, C) -> (num_windows*B, M, M, C)
    B, H, W, C = x.shape
    x = x.view(B, H // M, M, W // M, M, C)          # split H and W into (n, M)
    windows = x.permute(0, 1, 3, 2, 4, 5).contiguous()
    return windows.view(-1, M, M, C)                 # (num_windows*B, M, M, C)

def window_reverse(windows, M, H, W):
    # inverse: (num_windows*B, M, M, C) -> (B, H, W, C)
    B = int(windows.shape[0] / (H * W / M / M))
    x = windows.view(B, H // M, W // M, M, M, -1)
    x = x.permute(0, 1, 3, 2, 4, 5).contiguous()
    return x.view(B, H, W, C)

# --- block 2 ---
shift = M // 2                                   # e.g. M=4 -> shift=2 ; M=7 -> shift=3
x = torch.roll(x, shifts=(-shift, -shift), dims=(1, 2))   # (B, H, W, C)
# ... window_partition, attention, window_reverse ...
x = torch.roll(x,  shifts=( shift,  shift), dims=(1, 2))  # undo the roll

# --- block 3 ---
def build_attn_mask(H, W, M, shift, device):
    img_mask = torch.zeros((1, H, W, 1), device=device)     # region-ID canvas
    hs = (slice(0, -M), slice(-M, -shift), slice(-shift, None))
    ws = (slice(0, -M), slice(-M, -shift), slice(-shift, None))
    cnt = 0
    for h in hs:
        for w in ws:
            img_mask[:, h, w, :] = cnt                       # 9 distinct regions
            cnt += 1
    mask_windows = window_partition(img_mask, M).view(-1, M * M)   # (nW, M*M)
    attn_mask = mask_windows.unsqueeze(1) - mask_windows.unsqueeze(2)
    attn_mask = attn_mask.masked_fill(attn_mask != 0, -100.0)
    return attn_mask.masked_fill(attn_mask == 0, 0.0)        # (nW, M*M, M*M)

# --- block 4 ---
import torch.nn as nn

class PatchMerging(nn.Module):
    def __init__(self, C):
        super().__init__()
        self.norm = nn.LayerNorm(4 * C)
        self.reduction = nn.Linear(4 * C, 2 * C, bias=False)

    def forward(self, x):               # x: (B, H, W, C)
        x0 = x[:, 0::2, 0::2, :]        # top-left    of each 2×2
        x1 = x[:, 1::2, 0::2, :]        # bottom-left
        x2 = x[:, 0::2, 1::2, :]        # top-right
        x3 = x[:, 1::2, 1::2, :]        # bottom-right
        x = torch.cat([x0, x1, x2, x3], dim=-1)   # (B, H/2, W/2, 4C)
        return self.reduction(self.norm(x))       # (B, H/2, W/2, 2C)

# --- block 5 ---
class SwinStage(nn.Module):
    def __init__(self, C, depth, n_heads, M=7, merge=True):
        super().__init__()
        # depth blocks, alternating shift = 0, M//2, 0, M//2, ...
        self.blocks = nn.ModuleList([
            SwinBlock(C, n_heads, M, shift=(0 if i % 2 == 0 else M // 2))
            for i in range(depth)
        ])
        self.merge = PatchMerging(C) if merge else None

    def forward(self, x):                # x: (B, H, W, C)
        for blk in self.blocks:
            x = blk(x)                   # W-MSA then SW-MSA, in pairs
        if self.merge is not None:
            x = self.merge(x)            # (B, H/2, W/2, 2C)
        return x
