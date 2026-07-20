"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 10: Building the Embedding Block
Section: Images as Tokens

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/building-the-embedding-block

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class PatchEmbed(nn.Module):
    def __init__(self, img_size=224, patch_size=16, in_chans=3, embed_dim=384):
        super().__init__()
        self.num_patches = (img_size // patch_size) ** 2   # 14*14 = 196

        # 1) patch projection: a strided conv IS the linear patch embedding
        self.proj = nn.Conv2d(in_chans, embed_dim,
                              kernel_size=patch_size, stride=patch_size)

        # 2) the two special tokens, one learnable vector each
        self.cls_token  = nn.Parameter(torch.zeros(1, 1, embed_dim))
        self.dist_token = nn.Parameter(torch.zeros(1, 1, embed_dim))

        # 3) one learnable position vector per token, CLS+DIST included
        num_tokens = self.num_patches + 2                  # 198
        self.pos_embed = nn.Parameter(torch.zeros(1, num_tokens, embed_dim))

# --- block 2 ---
    def forward(self, x):
        B = x.shape[0]                      # (B, 3, 224, 224)

        x = self.proj(x)                    # (B, 384, 14, 14)
        x = x.flatten(2)                    # (B, 384, 196)
        x = x.transpose(1, 2)               # (B, 196, 384)  <- tokens as rows

        cls  = self.cls_token.expand(B, -1, -1)    # (B, 1, 384)
        dist = self.dist_token.expand(B, -1, -1)   # (B, 1, 384)
        x = torch.cat((cls, dist, x), dim=1)       # (B, 198, 384)

        x = x + self.pos_embed              # (B, 198, 384) + (1, 198, 384)
        return x                            # (B, 198, 384)

# --- block 3 ---
block = PatchEmbed(img_size=224, patch_size=16, in_chans=3, embed_dim=384)
x = torch.randn(8, 3, 224, 224)
out = block(x)
print(out.shape)          # torch.Size([8, 198, 384])
