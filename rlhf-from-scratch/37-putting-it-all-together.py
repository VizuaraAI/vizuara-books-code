"""
RLHF from Scratch
Chapter 37: Putting It All Together
Section: Beyond PPO

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/putting-it-all-together

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
ratio = torch.exp(new_logp - old_logp)          # per-token, shape (4,)
unclipped = ratio * advantages
clipped   = torch.clamp(ratio, 1 - eps, 1 + eps) * advantages   # eps ≈ 0.2
policy_loss = -torch.min(unclipped, clipped).mean()             # maximize → negate
