"""
Reinforcement Learning
Chapter 31: How GRPO Works
Section: Build a Reasoning Model with GRPO

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/how-grpo-works

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
rewards = [1.0, 0.2, 1.0, 0.0]   # o1 correct, o2 wrong-but-formatted, o3 correct, o4 wrong

# --- block 2 ---
mean = (1.0 + 0.2 + 1.0 + 0.0) / 4          # = 0.55
std  = sqrt( mean((r - 0.55)**2 for r in rewards) )  # ≈ 0.456

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# A1 = (1.0 - 0.55) / 0.456 ≈ +0.99
# A2 = (0.2 - 0.55) / 0.456 ≈ -0.77
# A3 = (1.0 - 0.55) / 0.456 ≈ +0.99
# A4 = (0.0 - 0.55) / 0.456 ≈ -1.21

# --- block 4 ---
ratio = torch.exp(logp_new - logp_old)              # ρ_it, in log-space
surr1 = ratio * A_i                                  # A_i shared across all tokens of o_i
surr2 = torch.clamp(ratio, 1 - eps, 1 + eps) * A_i   # clipped
per_token_loss = -torch.min(surr1, surr2)            # same clip as PPO
