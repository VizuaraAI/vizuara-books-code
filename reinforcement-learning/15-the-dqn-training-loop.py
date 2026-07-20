"""
Reinforcement Learning
Chapter 15: The DQN Training Loop
Section: Deep Q-Networks

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/the-dqn-training-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch
import torch.nn.functional as F

# --- block 1 ---
# one gradient step on a minibatch (s, a, r, s2, done)
q_pred   = online(s).gather(1, a)                     # Q(S,A;θ) for the taken action
with torch.no_grad():                                  # target is a constant — detach
    q_next   = target(s2).max(dim=1).values            # max_a' Q(S',a';θ⁻)
    q_target = r + gamma * q_next * (1 - done)          # Bellman target
loss = F.mse_loss(q_pred, q_target)                    # (target − prediction)²
optimizer.zero_grad(); loss.backward(); optimizer.step()

# --- block 2 ---
eps = max(eps_end, eps_start - step * (eps_start - eps_end) / decay_steps)
# eps_start=1.0, eps_end=0.05, decay_steps=10_000
