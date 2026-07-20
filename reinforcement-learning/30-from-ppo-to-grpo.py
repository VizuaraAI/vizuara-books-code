"""
Reinforcement Learning
Chapter 30: From PPO to GRPO
Section: Build a Reasoning Model with GRPO

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/from-ppo-to-grpo

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# rewards r for G sampled responses to ONE prompt
import numpy as np
r = np.array([0.9, 0.2, 0.7, 0.1])      # G = 4 responses, scored by the reward model
adv = (r - r.mean()) / (r.std() + 1e-8)  # group-relative advantage, one number per response

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# ratio = pi_theta(tokens) / pi_theta_old(tokens)      # per token
# clipped = clip(ratio, 1 - eps, 1 + eps)
# loss = -mean( min(ratio * adv, clipped * adv) ) + beta * KL(pi_theta || pi_ref)
