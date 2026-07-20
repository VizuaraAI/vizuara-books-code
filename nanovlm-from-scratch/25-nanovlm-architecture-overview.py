"""
Build a NanoVLM from Scratch
Chapter 25: NanoVLM Architecture Overview
Section: Building the NanoVLM

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/nanovlm-architecture-overview

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# The two towers this overview wires together. They are built in the next two
# chapters; imported here verbatim so the blueprint checks out.
# https://books.vizuara.ai/read/nanovlm-from-scratch/the-image-encoder-module
# https://books.vizuara.ai/read/nanovlm-from-scratch/the-text-encoder-module
from context import ImageEncoder, TextEncoder

I = None  # TODO: (3, 4) image embeddings for the chapter's worked example
T = None  # TODO: (3, 4) text embeddings for the chapter's worked example


# --- block 1 ---
S = I @ T.T          # (3, 4) @ (4, 3) -> (3, 3)

# --- block 2 ---
import torch
import torch.nn as nn
import torch.nn.functional as F

class NanoVLM(nn.Module):
    def __init__(self, d=128, img_feat=768, txt_feat=512):
        super().__init__()
        self.image_encoder = ImageEncoder()          # -> (N, img_feat)
        self.text_encoder  = TextEncoder()           # -> (N, txt_feat)
        self.image_proj = nn.Linear(img_feat, d)     # projection head
        self.text_proj  = nn.Linear(txt_feat, d)     # projection head
        # learnable temperature (logit_scale), init ~ 1/0.07
        self.logit_scale = nn.Parameter(torch.tensor(2.6592))

    def forward(self, images, tokens):
        I = self.image_proj(self.image_encoder(images))   # (N, d)
        T = self.text_proj(self.text_encoder(tokens))     # (N, d)
        I = F.normalize(I, dim=-1)                         # L2, unit sphere
        T = F.normalize(T, dim=-1)
        scale = self.logit_scale.exp().clamp(max=100)     # exp() -> ~14.29
        logits = scale * (I @ T.T)                         # (N, N)
        return logits
