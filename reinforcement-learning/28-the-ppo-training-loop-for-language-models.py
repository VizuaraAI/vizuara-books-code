"""
Reinforcement Learning
Chapter 28: The PPO Training Loop for Language Models
Section: RLHF from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/the-ppo-training-loop-for-language-models

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
# per-token KL: how far policy drifted from reference at this token
kl = log_pi_theta - log_pi_ref          # elementwise, per token
reward_t = -beta * kl                    # KL leash at every token
reward_t[-1] += r_phi                    # sequence reward lands on the LAST token

# --- block 2 ---
policy_loss  = -torch.min(ratio * adv, clipped_ratio * adv).mean()
value_loss   =  0.5 * (values - returns).pow(2).mean()
entropy_loss = -entropy_coef * entropy.mean()
loss = policy_loss + vf_coef * value_loss + entropy_loss
