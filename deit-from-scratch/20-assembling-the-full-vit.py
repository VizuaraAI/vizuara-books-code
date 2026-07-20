"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 20: Assembling the Full ViT
Section: The ViT Backbone

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/assembling-the-full-vit

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class VisionTransformer(nn.Module):
    def __init__(self, img_size=224, patch_size=16, in_chans=3,
                 embed_dim=384, depth=12, num_heads=6,
                 mlp_ratio=4, num_classes=1000):
        super().__init__()

        # 1) pixels -> (B, 198, 384) token matrix  (CLS + DIST + 196 patches + positions)
        self.patch_embed = PatchEmbed(img_size, patch_size, in_chans, embed_dim)

        # 2) twelve identical encoder blocks, shape-preserving
        self.blocks = nn.ModuleList([
            EncoderBlock(embed_dim, num_heads, mlp_ratio)
            for _ in range(depth)
        ])

        # 3) final norm + a linear head that reads the CLS token
        self.norm = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, num_classes)

    def forward(self, x):
        x = self.patch_embed(x)             # (B, 198, 384)
        for blk in self.blocks:
            x = blk(x)                      # (B, 198, 384)  — unchanged each pass
        x = self.norm(x)                    # (B, 198, 384)
        cls = x[:, 0]                       # (B, 384)  — token 0 is CLS
        return self.head(cls)               # (B, 1000)

# --- block 2 ---
model = VisionTransformer(embed_dim=384, depth=12, num_heads=6, num_classes=1000)
x = torch.randn(8, 3, 224, 224)
logits = model(x)
print(logits.shape)                 # torch.Size([8, 1000])
assert logits.shape == (8, 1000)
