"""
RLHF from Scratch
Chapter 14: Training the Reward Model
Section: Reward Models

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/training-the-reward-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

def reward_model_loss(model, chosen_ids, rejected_ids):
    # chosen_ids, rejected_ids: (B, T) token-id tensors, right-padded
    r_chosen  = model(chosen_ids)     # (B,) scalar per sequence, read from last token
    r_rejected = model(rejected_ids)  # (B,)
    margin = r_chosen - r_rejected    # (B,) the Bradley-Terry difference
    # -log σ(margin), averaged over the batch = softplus(-margin).mean()
    loss = -F.logsigmoid(margin).mean()
    accuracy = (margin > 0).float().mean()   # fraction the model ranks correctly
    return loss, accuracy
