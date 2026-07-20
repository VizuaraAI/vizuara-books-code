"""
Reinforcement Learning
Chapter 19: The REINFORCE Algorithm
Section: Policy Gradient Methods from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/the-reinforce-algorithm

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class PolicyNet(nn.Module):
    def __init__(self, obs_dim=4, n_actions=2, hidden=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, n_actions),
        )

    def forward(self, state):
        logits = self.net(state)
        return torch.distributions.Categorical(logits=logits)

# --- block 2 ---
policy = PolicyNet()
optimizer = torch.optim.Adam(policy.parameters(), lr=1e-2)
gamma = 0.99

for episode in range(1000):
    state, _ = env.reset()
    log_probs, rewards = [], []

    # --- collect one full episode (Monte Carlo) ---
    done = False
    while not done:
        state = torch.tensor(state, dtype=torch.float32)
        dist = policy(state)
        action = dist.sample()
        log_probs.append(dist.log_prob(action))
        state, reward, terminated, truncated, _ = env.step(action.item())
        rewards.append(reward)
        done = terminated or truncated

    # --- compute discounted returns G_t, backward ---
    returns, G = [], 0.0
    for r in reversed(rewards):
        G = r + gamma * G
        returns.insert(0, G)
    returns = torch.tensor(returns)
    returns = (returns - returns.mean()) / (returns.std() + 1e-8)  # normalize

    # --- one gradient step ---
    loss = -torch.stack([lp * G for lp, G in zip(log_probs, returns)]).sum()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
