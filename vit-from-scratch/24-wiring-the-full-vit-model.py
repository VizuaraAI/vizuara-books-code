"""
Build a Vision Transformer (ViT) from Scratch
Chapter 24: Wiring the Full ViT Model
Section: Assembling the Full ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/wiring-the-full-vit-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class ViT(nn.Module):
    def __init__(self, img_size=224, patch_size=16, in_channels=3,
                 emb_dim=768, depth=12, heads=12, mlp_dim=3072,
                 num_classes=1000, dropout=0.0):
        super().__init__()
        num_patches = (img_size // patch_size) ** 2        # 196

        self.patch_embed = PatchEmbedding(in_channels, patch_size, emb_dim)

        # one learnable class token, shape (1, 1, D)
        self.cls_token = nn.Parameter(torch.zeros(1, 1, emb_dim))
        # position table: one row per token, INCLUDING the class token
        self.pos_embed = nn.Parameter(torch.zeros(1, num_patches + 1, emb_dim))
        self.pos_drop  = nn.Dropout(dropout)

        self.encoder = TransformerEncoder(depth, emb_dim, heads, mlp_dim, dropout)

        self.norm = nn.LayerNorm(emb_dim)                  # final pre-head norm
        self.head = nn.Linear(emb_dim, num_classes)        # the classification head

    def forward(self, x):                                  # x: (B, 3, 224, 224)
        B = x.shape[0]

        x = self.patch_embed(x)                            # (B, 196, 768)

        cls = self.cls_token.expand(B, -1, -1)             # (B, 1, 768)
        x = torch.cat((cls, x), dim=1)                     # (B, 197, 768)

        x = x + self.pos_embed                             # (B, 197, 768)
        x = self.pos_drop(x)

        x = self.encoder(x)                                # (B, 197, 768)

        cls_final = self.norm(x)[:, 0]                     # (B, 768) — row 0 only
        return self.head(cls_final)                        # (B, num_classes)
