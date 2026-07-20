"""
RLHF from Scratch
Chapter 26: The Actor-Critic Value Model
Section: Proximal Policy Optimization

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/the-actor-critic-value-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
def value_loss(v_pred, v_old, returns, clip=0.2):
    # v_pred: critic's CURRENT prediction ; v_old: its prediction at rollout time
    v_clipped = v_old + (v_pred - v_old).clamp(-clip, clip)
    loss_unclipped = (v_pred - returns) ** 2
    loss_clipped   = (v_clipped - returns) ** 2
    return torch.max(loss_unclipped, loss_clipped).mean()   # pessimistic: take the worse
