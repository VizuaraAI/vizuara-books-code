"""
Reinforcement Learning
Chapter 27: The PPO Algorithm Explained
Section: RLHF from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/the-ppo-algorithm-explained

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
ratio = pi_new(a | s) / pi_old(a | s)   # 0.30 / 0.10 = 3.0

# --- block 2 ---
L_clip = min( ratio * A,  clip(ratio, 1 - eps, 1 + eps) * A )

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# reward_t = reward_model_score_t - beta * kl(pi(.|s_t), pi_ref(.|s_t))

# --- block 4 ---
# per token: the PPO-clip objective
ratio   = torch.exp(logp_new - logp_old)          # ρ_t, in log-space
surr1   = ratio * A                                # raw surrogate
surr2   = torch.clamp(ratio, 1 - eps, 1 + eps) * A # clipped surrogate
policy_loss = -torch.min(surr1, surr2).mean()      # maximize → minimize the negative
