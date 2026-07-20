"""
Modern Robot Learning
Chapter 42: Implementing PPO in PyTorch
Section: Simulation and Policy Gradients

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/implementing-ppo-in-pytorch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.nn as nn
from torch.distributions import Normal

class Policy(nn.Module):
    def __init__(self, obs_dim=4, act_dim=2, hidden=64):
        super().__init__()
        self.body = nn.Sequential(
            nn.Linear(obs_dim, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
        )
        self.mean = nn.Linear(hidden, act_dim)        # μ depends on obs
        self.log_std = nn.Parameter(torch.zeros(act_dim))  # σ learned, obs-independent

    def distribution(self, obs):
        h = self.body(obs)
        return Normal(self.mean(h), self.log_std.exp())

# --- block 2 ---
dist = policy.distribution(obs)     # a Normal over 2 action dims
action = dist.sample()              # e.g. tensor([ 0.31, -0.88])
logp   = dist.log_prob(action).sum(-1)   # sum across act dims → one scalar per step

# --- block 3 ---
obs = env.reset()
for t in range(rollout_len):            # e.g. 2048 steps
    with torch.no_grad():
        dist = policy.distribution(obs)
        action = dist.sample()
        buf.logp[t]  = dist.log_prob(action).sum(-1)
        buf.value[t] = value_net(obs)   # a critic estimates expected return
    obs, reward, done, _ = env.step(action)
    buf.obs[t], buf.act[t], buf.rew[t] = obs, action, reward

# --- block 4 ---
for _ in range(update_epochs):          # e.g. 10 passes over the rollout
    dist = policy.distribution(buf.obs)
    logp_new = dist.log_prob(buf.act).sum(-1)
    ratio = torch.exp(logp_new - buf.logp)          # r = π_new / π_old

    unclipped = ratio * buf.adv
    clipped   = torch.clamp(ratio, 1 - 0.2, 1 + 0.2) * buf.adv
    policy_loss = -torch.min(unclipped, clipped).mean()   # minus → we ASCEND

    value_loss = ((value_net(buf.obs) - buf.ret) ** 2).mean()
    loss = policy_loss + 0.5 * value_loss - 0.01 * dist.entropy().mean()

    optim.zero_grad()
    loss.backward()
    optim.step()
