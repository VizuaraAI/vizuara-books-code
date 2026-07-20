"""
Build a NanoVLM from Scratch
Chapter 26: The Image Encoder Module
Section: Building the NanoVLM

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-image-encoder-module

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# patchify (Chapter 14) and the transformer block (Chapter 27's tower) are
# described in the book but never given as standalone definitions.
from context import TransformerBlock, patchify

# The two interchangeable backbones the second version selects between. The
# book covers both routes but does not package either as a class:
# https://books.vizuara.ai/read/nanovlm-from-scratch/patch-embeddings-and-positions
# https://books.vizuara.ai/read/nanovlm-from-scratch/the-cnn-route-to-an-image-vector
PatchBackbone = None  # TODO: patch+transformer route -> (B, D_backbone)
CNNBackbone = None    # TODO: convolutional route -> (B, D_backbone)


# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
import torch.nn as nn

class ImageEncoder(nn.Module):
    def __init__(self, patch_dim, d_model, num_patches, d, n_blocks):
        super().__init__()
        self.patch_embed = nn.Linear(patch_dim, d_model)        # (patch_dim -> d_model)
        self.pos_emb     = nn.Parameter(torch.zeros(num_patches, d_model))
        self.blocks      = nn.Sequential(*[
            TransformerBlock(d_model) for _ in range(n_blocks)  # same block as the text tower
        ])
        self.head        = nn.Linear(d_model, d)                # backbone width -> shared d

    def forward(self, images):                # images: (B, C, H, W)
        x = patchify(images)                  # (B, num_patches, patch_dim)
        x = self.patch_embed(x)               # (B, num_patches, d_model)
        x = x + self.pos_emb                  # broadcast-add positions -> (B, num_patches, d_model)
        x = self.blocks(x)                    # (B, num_patches, d_model)
        x = x.mean(dim=1)                     # mean-pool over tokens -> (B, d_model)
        return self.head(x)                   # (B, d)

# --- block 2 ---
class ImageEncoder(nn.Module):
    def __init__(self, d, backbone="patch", **cfg):
        super().__init__()
        if backbone == "patch":
            self.backbone = PatchBackbone(**cfg)   # -> (B, D_backbone)
        elif backbone == "cnn":
            self.backbone = CNNBackbone(**cfg)      # -> (B, D_backbone), same contract
        self.head = nn.Linear(self.backbone.out_dim, d)   # each backbone reports its native width

    def forward(self, images):
        feats = self.backbone(images)   # (B, D_backbone) — route-agnostic
        return self.head(feats)         # (B, d)
