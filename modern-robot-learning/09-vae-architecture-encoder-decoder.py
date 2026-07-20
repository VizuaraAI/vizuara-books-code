"""
Modern Robot Learning
Chapter 9: The VAE: Encoder, Decoder, and the Bottleneck
Section: Deep Generative Modeling

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/vae-architecture-encoder-decoder

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

def encode(x, encoder):
    h = encoder(x)                       # shared trunk
    mu = h[..., :2]                      # mean vector      (2 numbers)
    logvar = h[..., 2:]                  # log-variance     (2 numbers)
    return mu, logvar

def sample_latent(mu, logvar):
    sigma = torch.exp(0.5 * logvar)      # std-dev, always positive
    eps = torch.randn_like(sigma)        # eps ~ N(0, I)
    return mu + sigma * eps              # z = mu + sigma * eps
