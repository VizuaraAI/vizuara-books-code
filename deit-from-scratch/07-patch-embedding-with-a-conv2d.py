"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 7: Patch Embedding with a Conv2d
Section: Images as Tokens

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/patch-embedding-with-a-conv2d

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

class PatchEmbed(nn.Module):
    def __init__(self, in_chans=3, embed_dim=384, patch_size=16):
        super().__init__()
        self.proj = nn.Conv2d(in_chans, embed_dim,
                              kernel_size=patch_size, stride=patch_size)

    def forward(self, x):                 # x: (B, 3, 224, 224)
        x = self.proj(x)                  # (B, 384, 14, 14)
        x = x.flatten(2)                  # (B, 384, 196)   merge 14×14 → 196
        x = x.transpose(1, 2)             # (B, 196, 384)   tokens last-but-one
        return x

# --- block 2 ---
import torch
model = PatchEmbed(in_chans=3, embed_dim=384, patch_size=16)
x = torch.randn(1, 3, 224, 224)     # one fake image
out = model(x)
print(out.shape)                     # torch.Size([1, 196, 384])
