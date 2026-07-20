"""
Build a NanoVLM from Scratch
Chapter 30: Assembling the Full Forward Pass
Section: Building the NanoVLM

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/assembling-the-full-forward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
# Built earlier in the book: the two towers (Chapters 26-27) and the loss
# (Chapter 24).
from context import ImageEncoder, TextEncoder, clip_loss

dataloader = None  # TODO: a DataLoader over Chapter 29's ShapesDataset


# --- block 1 ---
import torch
import torch.nn as nn
import torch.nn.functional as F

class NanoVLM(nn.Module):
    def __init__(self, d=128, img_feat=768, txt_feat=512):
        super().__init__()
        self.image_encoder = ImageEncoder()          # -> (N, img_feat)
        self.text_encoder  = TextEncoder()           # -> (N, txt_feat)
        self.image_proj = nn.Linear(img_feat, d)
        self.text_proj  = nn.Linear(txt_feat, d)
        self.logit_scale = nn.Parameter(torch.tensor(2.6592))  # log-space, exp ~ 14.29

    def encode(self, images, tokens):
        I = self.image_proj(self.image_encoder(images))   # (N, d)
        T = self.text_proj(self.text_encoder(tokens))     # (N, d)
        I = F.normalize(I, dim=-1)                         # L2 -> unit sphere
        T = F.normalize(T, dim=-1)
        return I, T

    def forward(self, images, tokens):
        I, T = self.encode(images, tokens)                # (N, d), (N, d)
        scale = self.logit_scale.exp().clamp(max=100)     # ~14.29, clamped
        loss = clip_loss(I, T, scale)                     # scalar
        return loss

# --- block 2 ---
model = NanoVLM(d=128)
images, tokens = next(iter(dataloader))   # (N,3,32,32), (N,16)

loss = model(images, tokens)              # forward: encode -> normalize -> S -> loss
print(loss.item())                        # ~ log(N) on the very first step
loss.backward()                           # gradients flow into BOTH towers + logit_scale
