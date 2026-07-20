"""
Vision-Language-Action & World Models for Robotics
Chapter 15: Training ACT in Simulation
Section: Building the Action Chunking Transformer

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/training-act-in-simulation

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
import numpy as np

a_hat = np.array([[ 0.10, 0.50],   # predicted 4×2 chunk
                  [ 0.15, 0.55],
                  [ 0.05, 0.60],
                  [-0.05, 0.62]])
a_true = np.array([[ 0.12, 0.48],   # ground-truth 4×2 chunk
                   [ 0.14, 0.60],
                   [ 0.00, 0.65],
                   [-0.10, 0.60]])

l1 = np.abs(a_hat - a_true).mean()   # mean over all 8 entries

# --- block 2 ---
# per-dimension KL from N(mu, sigma^2) to N(0,1); sum over dims
kl = -0.5 * np.sum(1 + logvar - mu**2 - np.exp(logvar))

# --- block 3 ---
loss = l1 + beta * kl

# --- block 4 ---
model.train()
for epoch in range(num_epochs):
    for obs, state, a_true in dataloader:        # sample a batch
        mu, logvar = model.cvae_encoder(a_true, state)
        z = mu + torch.exp(0.5 * logvar) * torch.randn_like(mu)  # reparam
        a_hat = model.policy(obs, state, z)       # decode images + z → chunk

        l1 = (a_hat - a_true).abs().mean()
        kl = -0.5 * (1 + logvar - mu.pow(2) - logvar.exp()).sum(-1).mean()
        loss = l1 + beta * kl

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
