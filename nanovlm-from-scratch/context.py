"""
Build a NanoVLM from Scratch - shared context for the companion code.

The chapter files in this folder are teaching excerpts: a later chapter often
uses a class or function that an earlier chapter built. This module collects
those shared definitions in one place so each chapter file can say

    from context import NanoVLM, clip_loss

and be checkable on its own.

Every definition below is COPIED VERBATIM from the book's own code blocks.
The only things written here that are not in the book are the two explicit
placeholders at the top (`patchify`, `TransformerBlock`), which the book
describes but never gives as a standalone definition. They are honest stubs,
not guesses at an implementation.

Read the book: https://books.vizuara.ai/read/nanovlm-from-scratch
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

# ---------------------------------------------------------------------------
# Placeholders the reader supplies.
#
# The book explains both of these in prose and shows the mechanics inline, but
# never packages either one as a named, reusable definition, so there is
# nothing to copy verbatim.
# ---------------------------------------------------------------------------

# TODO: the cut-an-image-into-flattened-patches step. Chapter 14 walks through
# the exact reshape/transpose that does this:
# https://books.vizuara.ai/read/nanovlm-from-scratch/patchify-an-image
patchify = None

# TODO: one transformer encoder block. Chapter 27 uses PyTorch's built-in
# nn.TransformerEncoderLayer for the text tower; the image tower in Chapter 26
# assumes "the same block":
# https://books.vizuara.ai/read/nanovlm-from-scratch/the-image-encoder-module
TransformerBlock = None


# ---------------------------------------------------------------------------
# Chapter 26, block 1 (verbatim) - The Image Encoder Module
# https://books.vizuara.ai/read/nanovlm-from-scratch/the-image-encoder-module
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Chapter 27, block 5 (verbatim) - The Text Encoder Module
# https://books.vizuara.ai/read/nanovlm-from-scratch/the-text-encoder-module
# ---------------------------------------------------------------------------

class TextEncoder(nn.Module):
    def __init__(self, vocab_size=50000, seq_len=4, d_model=8, d=4,
                 n_heads=2, n_layers=2):
        super().__init__()
        self.tok_embed = nn.Embedding(vocab_size, d_model)
        self.pos_embed = nn.Embedding(seq_len,    d_model)
        block = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads,
            dim_feedforward=4 * d_model, batch_first=True)
        self.blocks = nn.TransformerEncoder(block, num_layers=n_layers)
        self.proj = nn.Linear(d_model, d)

    def forward(self, ids):                     # (B, S) ints
        S = ids.shape[1]
        positions = torch.arange(S, device=ids.device)
        x = self.tok_embed(ids) + self.pos_embed(positions)  # (B, S, d_model)
        x = self.blocks(x)                      # (B, S, d_model)
        pooled = x.mean(dim=1)                   # (B, d_model)
        return self.proj(pooled)                 # (B, d)


# ---------------------------------------------------------------------------
# Chapter 24, block 1 (verbatim) - Coding the Contrastive Loss
# https://books.vizuara.ai/read/nanovlm-from-scratch/coding-the-contrastive-loss
# ---------------------------------------------------------------------------

def clip_loss(img_emb, text_emb, logit_scale):
    # img_emb, text_emb: (N, d), already L2-normalized
    N = img_emb.shape[0]

    # 1. similarity matrix, scaled into logits
    logits = logit_scale * img_emb @ text_emb.T   # (N, N)

    # 2. the labels are just the batch indices
    labels = torch.arange(N, device=img_emb.device)

    # 3. classify rows (image->text) and columns (text->image)
    loss_i2t = F.cross_entropy(logits,   labels)
    loss_t2i = F.cross_entropy(logits.T, labels)

    # 4. symmetric average
    return (loss_i2t + loss_t2i) / 2


# ---------------------------------------------------------------------------
# Chapter 30, block 1 (verbatim) - Assembling the Full Forward Pass
# https://books.vizuara.ai/read/nanovlm-from-scratch/assembling-the-full-forward-pass
# ---------------------------------------------------------------------------

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
