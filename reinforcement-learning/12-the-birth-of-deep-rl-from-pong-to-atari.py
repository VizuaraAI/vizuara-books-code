"""
Reinforcement Learning
Chapter 12: The Birth of Deep RL: From Pong to Atari
Section: Deep Q-Networks

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/the-birth-of-deep-rl-from-pong-to-atari

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# One DQN gradient step (schematically)
# batch of transitions sampled from the replay buffer
target = R + gamma * Q_frozen(S_next).max(dim=1).values   # uses theta-minus
pred   = Q_online(S).gather(1, A)                          # value of the action taken
loss   = ((target - pred) ** 2).mean()                     # squared TD error
loss.backward()                                            # nudge theta to shrink it
