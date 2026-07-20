"""
Modern Robot Learning
Chapter 12: The ELBO: Reconstruction Loss Meets KL Divergence
Section: Deep Generative Modeling

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/the-elbo-and-kl-divergence

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

def vae_loss(x, x_recon, mu, logvar):
    # reconstruction: how well the decoder rebuilt x (per-pixel BCE, summed)
    recon = F.binary_cross_entropy(x_recon, x, reduction="sum")

    # KL(q(z|x) || N(0, I)), closed form, summed over latent dims:
    #   ½ Σ (μ² + σ² − log σ² − 1)  with σ² = exp(logvar)
    kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())

    return recon + kl          # the ELBO, negated → minimize this
