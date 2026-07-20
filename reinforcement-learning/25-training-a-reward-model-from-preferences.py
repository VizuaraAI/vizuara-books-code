"""
Reinforcement Learning
Chapter 25: Training a Reward Model from Preferences
Section: RLHF from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/training-a-reward-model-from-preferences

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

# reward_model(prompt, response) -> scalar reward, one shared network
r_chosen   = reward_model(x, y_chosen)     # e.g. tensor(2.0)
r_rejected = reward_model(x, y_rejected)   # e.g. tensor(1.5)

# Bradley-Terry loss = -log σ(r_w - r_l)
loss = -F.logsigmoid(r_chosen - r_rejected)

loss.backward()
optimizer.step()
