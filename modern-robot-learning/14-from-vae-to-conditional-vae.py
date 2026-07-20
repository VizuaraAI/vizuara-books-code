"""
Modern Robot Learning
Chapter 14: From VAE to Conditional VAE
Section: Conditional VAEs

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/from-vae-to-conditional-vae

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

def cvae_encode(x, c, enc):
    # x: (batch, 784)   c: (batch,) integer labels 0..9
    c_onehot = F.one_hot(c, num_classes=10).float()   # (batch, 10)
    xc = torch.cat([x, c_onehot], dim=1)              # (batch, 794)  <-- the whole trick
    h = F.relu(enc.fc1(xc))                           # fc1: 794 -> hidden
    mu = enc.fc_mu(h)                                 # (batch, 8)
    logvar = enc.fc_logvar(h)                         # (batch, 8)
    return mu, logvar

def reparameterize(mu, logvar):
    std = torch.exp(0.5 * logvar)                     # sigma from log-variance
    eps = torch.randn_like(std)                       # epsilon ~ N(0, I)
    return mu + std * eps                             # z = mu + sigma * epsilon

# --- block 2 ---
def generate(decoder, digit, n=8):
    c = torch.full((n,), digit)                       # ask for the same digit n times
    c_onehot = F.one_hot(c, num_classes=10).float()
    z = torch.randn(n, 8)                             # n different styles
    return decoder(torch.cat([z, c_onehot], dim=1))   # n distinct-looking 7s
