"""
Build a NanoVLM from Scratch
Chapter 24: Coding the Contrastive Loss
Section: Contrastive Learning

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/coding-the-contrastive-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

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
