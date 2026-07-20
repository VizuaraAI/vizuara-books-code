"""
RLHF from Scratch
Chapter 17: REINFORCE and the Log-Derivative Trick
Section: Policy Gradients and Advantage

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/reinforce-and-the-log-derivative-trick

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

# logp_chosen: (T,) log-probs of the tokens the policy actually sampled, log π_θ(a_t|s_t)
# reward:      scalar R(τ) from the reward model on the finished response
def reinforce_loss(logp_chosen, reward):
    # maximize E[R · log π] == minimize -(R · Σ log π_θ(a_t|s_t))
    return -(reward * logp_chosen.sum())

loss = reinforce_loss(logp_chosen, reward)   # a single scalar
loss.backward()                              # autograd fills in ∇_θ for every weight
