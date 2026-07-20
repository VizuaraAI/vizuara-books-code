"""
Build a Vision Transformer (ViT) from Scratch
Chapter 9: Coding the PatchEmbedding Class
Section: Turning Images into Tokens

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/coding-the-patchembedding-class

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = self.proj(images)     # (B, D, H/P, W/P) = (8, 768, 14, 14)
x = x.flatten(2)          # (B, D, N)        = (8, 768, 196)
x = x.transpose(1, 2)     # (B, N, D)        = (8, 196, 768)

# --- block 2 ---
import torch
import torch.nn as nn

class PatchEmbedding(nn.Module):
    def __init__(self, in_channels=3, patch_size=16, emb_dim=768):
        super().__init__()
        self.patch_size = patch_size
        self.proj = nn.Conv2d(
            in_channels, emb_dim,
            kernel_size=patch_size, stride=patch_size,
        )

    def forward(self, x):
        # x: (B, C, H, W)
        x = self.proj(x)        # (B, D, H/P, W/P)
        x = x.flatten(2)        # (B, D, N)
        x = x.transpose(1, 2)   # (B, N, D)
        return x

# --- block 3 ---
torch.manual_seed(0)
toy = PatchEmbedding(in_channels=1, patch_size=2, emb_dim=8)

x = torch.randn(1, 1, 4, 4)     # (B, C, H, W)
out = toy(x)

print(out.shape)                # torch.Size([1, 4, 8])
print(out.numel())              # 32

# --- block 4 ---
patch_embed = PatchEmbedding()          # in=3, P=16, D=768 -> ViT-Base

images = torch.randn(8, 3, 224, 224)    # (B, C, H, W)
tokens = patch_embed(images)

print(tokens.shape)                     # torch.Size([8, 196, 768])

n_params = sum(p.numel() for p in patch_embed.parameters())
print(n_params)                         # 590,592
