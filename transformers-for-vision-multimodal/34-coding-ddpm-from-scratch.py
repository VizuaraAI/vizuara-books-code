"""
Transformers for Vision & Multimodal LLMs
Chapter 34: Coding DDPM From Scratch
Section: Generative Vision — Autoencoders to Diffusion

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-ddpm-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch.nn.functional as F

# --- block 1 ---
betas = [0.1, 0.2, 0.3, 0.4]          # β_t
alphas = [0.9, 0.8, 0.7, 0.6]         # α_t = 1 − β_t
# ᾱ_t = cumulative product of α up to t:
alpha_bars = [0.9, 0.72, 0.504, 0.3024]

# --- block 2 ---
import torch, math

def timestep_embedding(t, dim):
    # t: (batch,) integer timesteps  ->  (batch, dim) float embedding
    half = dim // 2
    freqs = torch.exp(-math.log(10000) * torch.arange(half) / half)
    args = t[:, None].float() * freqs[None]          # (batch, half)
    return torch.cat([torch.sin(args), torch.cos(args)], dim=-1)

# --- block 3 ---
for x0 in dataloader:                                 # a batch of clean images
    t   = torch.randint(0, T, (x0.size(0),))          # random timestep per image
    eps = torch.randn_like(x0)                        # the noise we will hide

    ab  = alpha_bars[t].view(-1, 1, 1, 1)             # ᾱ_t, broadcast over image
    xt  = ab.sqrt() * x0 + (1 - ab).sqrt() * eps      # the closed form — one line!

    eps_pred = model(xt, t)                           # U-Net predicts the noise
    loss = F.mse_loss(eps_pred, eps)                  # simplified DDPM objective

    optimizer.zero_grad(); loss.backward(); optimizer.step()

# --- block 4 ---
x = torch.randn(1, 1, 28, 28)                         # start from pure static
for t in reversed(range(T)):                          # T, T−1, …, 1, 0
    eps_pred = model(x, torch.tensor([t]))
    a, ab = alphas[t], alpha_bars[t]
    x = (1/ a**0.5) * (x - (1 - a)/(1 - ab)**0.5 * eps_pred)
    if t > 0:
        x = x + betas[t]**0.5 * torch.randn_like(x)   # inject stochasticity
