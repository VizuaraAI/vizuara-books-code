"""
Modern Robot Learning
Chapter 20: Vision Transformers: Images as Tokens
Section: Transformer Architecture from Scratch

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/vision-transformers-images-as-tokens

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class PatchEmbed(nn.Module):
    def __init__(self, img_size=224, patch=16, in_ch=3, d_model=768):
        super().__init__()
        self.n_patches = (img_size // patch) ** 2          # (224//16)**2 = 196
        # kernel == stride == patch  ->  one non-overlapping projection per patch
        self.proj = nn.Conv2d(in_ch, d_model, kernel_size=patch, stride=patch)
        self.cls = nn.Parameter(torch.zeros(1, 1, d_model))            # [CLS]
        self.pos = nn.Parameter(torch.zeros(1, self.n_patches + 1, d_model))

    def forward(self, x):                    # x: (batch, 3, 224, 224)
        x = self.proj(x)                     # (batch, 768, 14, 14)
        x = x.flatten(2).transpose(1, 2)     # (batch, 196, 768)  -> tokens!
        cls = self.cls.expand(x.shape[0], -1, -1)
        x = torch.cat([cls, x], dim=1)       # (batch, 197, 768)
        return x + self.pos                  # add positions, done
