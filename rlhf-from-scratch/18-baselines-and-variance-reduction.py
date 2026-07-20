"""
RLHF from Scratch
Chapter 18: Baselines and Variance Reduction
Section: Policy Gradients and Advantage

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/baselines-and-variance-reduction

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

# logp_chosen: (T,) log-probs of the tokens the policy sampled, log π_θ(a_t|s_t)
# reward:      scalar R(τ) from the reward model on the finished response
# baseline:    b(s) — a scalar that must NOT depend on the sampled tokens
def reinforce_with_baseline(logp_chosen, reward, baseline):
    advantage = reward - baseline          # (R − b): centered signal, can be negative
    return -(advantage * logp_chosen.sum())  # same loss shape, just centered

# cheapest legal baseline: the mean reward across the current batch of rollouts
baseline = rewards.mean()                  # detached — no gradient flows through it
loss = reinforce_with_baseline(logp_chosen, reward, baseline)
loss.backward()
