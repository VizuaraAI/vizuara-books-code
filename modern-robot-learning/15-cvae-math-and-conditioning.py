"""
Modern Robot Learning
Chapter 15: The Math of Conditioning
Section: Conditional VAEs

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/cvae-math-and-conditioning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

x = torch.tensor([0.9, 0.1, 0.2, 0.8])          # flattened 2x2 image, length 4
c = torch.tensor([0,0,0,0,0,0,0,1,0,0.])          # one-hot label "7",  length 10

enc_in = torch.cat([x, c], dim=-1)                # length 14  <- this is q(z | x, c)
print(enc_in.shape)                               # torch.Size([14])

# --- block 2 ---
import torch.nn.functional as F

def cvae_loss(x, x_recon, mu, logvar):
    # x_recon came from decoder(cat([z, c]));  mu, logvar from encoder(cat([x, c]))
    recon = F.binary_cross_entropy(x_recon, x, reduction="sum")   # rebuild x
    kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())   # SAME as VAE, prior = N(0,I)
    return recon + kl
