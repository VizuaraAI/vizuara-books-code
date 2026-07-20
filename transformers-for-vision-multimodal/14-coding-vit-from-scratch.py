"""
Transformers for Vision & Multimodal LLMs
Chapter 14: Coding the Vision Transformer From Scratch
Section: The Vision Transformer

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-vit-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class EncoderBlock(nn.Module):
    def __init__(self, D=768, n_heads=12, mlp_ratio=4, drop=0.0):
        super().__init__()
        self.norm1 = nn.LayerNorm(D)
        self.attn  = nn.MultiheadAttention(D, n_heads, dropout=drop,
                                           batch_first=True)
        self.norm2 = nn.LayerNorm(D)
        self.mlp   = nn.Sequential(
            nn.Linear(D, mlp_ratio * D),   # 768 -> 3072
            nn.GELU(),
            nn.Linear(mlp_ratio * D, D),   # 3072 -> 768
        )

    def forward(self, x):                          # x: (B, N+1, D)
        x = x + self.attn(self.norm1(x), self.norm1(x),
                          self.norm1(x))[0]         # pre-LN attention + residual
        x = x + self.mlp(self.norm2(x))            # pre-LN MLP + residual
        return x

# --- block 2 ---
class ViT(nn.Module):
    def __init__(self, img=224, P=16, C=3, D=768, L=12,
                 n_heads=12, num_classes=1000):
        super().__init__()
        N = (img // P) ** 2                              # 196 patches
        self.patch = nn.Conv2d(C, D, kernel_size=P, stride=P)  # front door
        self.cls   = nn.Parameter(torch.zeros(1, 1, D))       # [CLS] token
        self.pos   = nn.Parameter(torch.zeros(1, N + 1, D))   # position table
        self.blocks = nn.ModuleList([
            EncoderBlock(D, n_heads) for _ in range(L)        # L identical blocks
        ])
        self.norm = nn.LayerNorm(D)
        self.head = nn.Linear(D, num_classes)                 # the only new part

    def forward(self, x):                    # x: (B, 3, 224, 224)
        B = x.shape[0]
        x = self.patch(x)                    # (B, 768, 14, 14)
        x = x.flatten(2).transpose(1, 2)     # (B, 196, 768)  -> tokens
        cls = self.cls.expand(B, -1, -1)     # (B, 1, 768)
        x = torch.cat([cls, x], dim=1)       # (B, 197, 768)  prepend CLS
        x = x + self.pos                     # add position (broadcast over B)
        for blk in self.blocks:
            x = blk(x)                       # (B, 197, 768) throughout
        x = self.norm(x)
        return self.head(x[:, 0])            # take CLS row -> (B, num_classes)
