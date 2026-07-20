"""
RLHF from Scratch
Chapter 32: Training the Summarizer's Reward Model
Section: Building It From Scratch

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/training-the-summarizer-reward-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn.functional as F

def rm_loss(model, chosen_ids, rejected_ids):
    r_chosen   = model(chosen_ids)     # (B,) scalar per summary, read at last token
    r_rejected = model(rejected_ids)   # (B,)
    margin = r_chosen - r_rejected     # (B,) the Bradley-Terry difference
    loss = -F.logsigmoid(margin).mean()          # -log σ(m), batch mean
    accuracy = (margin > 0).float().mean()       # fraction ranked like the human
    return loss, accuracy
