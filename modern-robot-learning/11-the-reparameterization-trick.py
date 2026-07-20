"""
Modern Robot Learning
Chapter 11: Sampling and the Reparameterization Trick
Section: Deep Generative Modeling

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/the-reparameterization-trick

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
def reparameterize(self, mu, logvar):
    # logvar = log(sigma^2), emitted by the encoder
    std = torch.exp(0.5 * logvar)      # sigma = sqrt(exp(logvar))
    eps = torch.randn_like(std)        # epsilon ~ N(0, I), no gradient
    return mu + std * eps              # z: differentiable in mu and std

# --- block 2 ---
# DON'T: sampling as a node inside the graph — gradient to mu, std is None
z = torch.normal(mu, std)
