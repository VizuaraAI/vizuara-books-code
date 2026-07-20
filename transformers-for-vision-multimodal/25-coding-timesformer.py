"""
Transformers for Vision & Multimodal LLMs
Chapter 25: Running TimeSformer on Video
Section: Video & Multimodal Models

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-timesformer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

def sample_frames(video, T=8):
    # video: (num_frames, 3, H, W) decoded RGB tensor, values in [0, 1]
    num_frames = video.shape[0]
    idx = torch.linspace(0, num_frames - 1, T).long()   # T evenly-spaced indices
    return video[idx]                                    # (T, 3, H, W)

# --- block 2 ---
import torch.nn as nn

class VideoPatchEmbed(nn.Module):
    def __init__(self, P=16, D=768):
        super().__init__()
        self.proj = nn.Conv2d(3, D, kernel_size=P, stride=P)   # linear patch projection

    def forward(self, x):                    # x: (B, T, 3, H, W)
        B, T = x.shape[0], x.shape[1]
        x = x.flatten(0, 1)                  # (B*T, 3, H, W) — treat frames as a big batch
        x = self.proj(x)                     # (B*T, D, H/P, W/P)
        x = x.flatten(2).transpose(1, 2)     # (B*T, N, D), N = 196
        return x.reshape(B, T, -1, x.shape[-1])   # (B, T, N, D)

# --- block 3 ---
class DividedSpaceTimeBlock(nn.Module):
    def __init__(self, D=768, n_heads=12, mlp_ratio=4):
        super().__init__()
        self.t_norm = nn.LayerNorm(D)
        self.t_attn = nn.MultiheadAttention(D, n_heads, batch_first=True)
        self.s_norm = nn.LayerNorm(D)
        self.s_attn = nn.MultiheadAttention(D, n_heads, batch_first=True)
        self.m_norm = nn.LayerNorm(D)
        self.mlp = nn.Sequential(nn.Linear(D, mlp_ratio * D), nn.GELU(),
                                 nn.Linear(mlp_ratio * D, D))

    def forward(self, x, T, N):              # x: (B, T*N, D), CLS handled separately
        B, _, D = x.shape
        # --- temporal: each spatial spot attends across time ---
        xt = x.reshape(B, T, N, D).permute(0, 2, 1, 3).reshape(B * N, T, D)
        xt = self.t_norm(xt)
        x = x + self.t_attn(xt, xt, xt)[0].reshape(B, N, T, D) \
                  .permute(0, 2, 1, 3).reshape(B, T * N, D)
        # --- spatial: each frame attends within itself ---
        xs = x.reshape(B, T, N, D).reshape(B * T, N, D)
        xs = self.s_norm(xs)
        x = x + self.s_attn(xs, xs, xs)[0].reshape(B, T * N, D)
        # --- position-wise MLP, pre-LN, residual ---
        x = x + self.mlp(self.m_norm(x))
        return x

# --- block 4 ---
class TimeSformer(nn.Module):
    def __init__(self, T=8, P=16, D=768, L=12, num_classes=400):
        super().__init__()
        self.embed = VideoPatchEmbed(P, D)
        self.cls = nn.Parameter(torch.zeros(1, 1, D))
        self.pos = nn.Parameter(torch.zeros(1, 1 + T * (224 // P) ** 2, D))
        self.blocks = nn.ModuleList([DividedSpaceTimeBlock(D) for _ in range(L)])
        self.norm = nn.LayerNorm(D)
        self.head = nn.Linear(D, num_classes)

    def forward(self, x):                    # x: (B, T, 3, H, W)
        B, T = x.shape[0], x.shape[1]
        x = self.embed(x)                    # (B, T, N, D)
        N = x.shape[2]
        x = x.reshape(B, T * N, -1)          # (B, T*N, D)
        cls = self.cls.expand(B, -1, -1)     # (B, 1, D)
        x = torch.cat([cls, x], dim=1) + self.pos    # (B, 1 + T*N, D)
        cls_tok, patches = x[:, :1], x[:, 1:]
        for blk in self.blocks:
            patches = blk(patches, T, N)      # divided attention over patches
        x = torch.cat([cls_tok, patches], dim=1)
        return self.head(self.norm(x[:, 0]))  # (B, num_classes)
