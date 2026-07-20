"""
Reinforcement Learning
Chapter 16: Project: Build a DQN from Scratch
Section: Deep Q-Networks

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/project-build-a-dqn-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import random

# --- block 1 ---
import torch, torch.nn as nn

class QNet(nn.Module):
    def __init__(self, n_obs=4, n_act=2, hidden=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_obs, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU(),
            nn.Linear(hidden, n_act),        # NO activation on the output
        )
    def forward(self, x):
        return self.net(x)                   # shape (batch, 2) = Q-values

# --- block 2 ---
def act(state, epsilon):
    if random.random() < epsilon:
        return env.action_space.sample()            # explore
    with torch.no_grad():
        return online(torch.tensor(state)).argmax().item()   # exploit

def learn():
    if len(buffer) < 64:            # wait until we can fill one batch
        return
    s, a, r, s2, done = sample(buffer, 64)          # random minibatch
    q      = online(s).gather(1, a)                 # Q(S,A) predicted
    with torch.no_grad():
        target = r + 0.99 * online_target(s2).max(1).values * (1 - done)
    loss = ((target - q.squeeze()) ** 2).mean()     # MSE regression
    opt.zero_grad(); loss.backward(); opt.step()    # update ONLINE only
