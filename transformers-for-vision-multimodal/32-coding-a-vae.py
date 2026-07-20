"""
Transformers for Vision & Multimodal LLMs
Chapter 32: Coding a VAE
Section: Generative Vision — Autoencoders to Diffusion

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-a-vae

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class Encoder(nn.Module):
    def __init__(self, in_dim=784, hidden=400, latent=2):
        super().__init__()
        self.body     = nn.Sequential(nn.Linear(in_dim, hidden), nn.ReLU())
        self.fc_mu     = nn.Linear(hidden, latent)   # → μ
        self.fc_logvar = nn.Linear(hidden, latent)   # → log σ²

    def forward(self, x):              # x: (B, 784)
        h = self.body(x)              # (B, 400)
        mu     = self.fc_mu(h)        # (B, 2)
        logvar = self.fc_logvar(h)    # (B, 2)
        return mu, logvar

# --- block 2 ---
def reparameterize(mu, logvar):
    std = torch.exp(0.5 * logvar)     # σ from log σ²
    eps = torch.randn_like(std)       # ε ~ N(0, I), same shape, no grad
    return mu + std * eps             # z = μ + σ·ε

# --- block 3 ---
import torch.nn.functional as F

def vae_loss(x_hat, x, mu, logvar):
    # reconstruction: BCE summed over pixels, then over the batch
    recon = F.binary_cross_entropy(x_hat, x, reduction='sum')
    # KL( N(μ,σ²) ‖ N(0,I) ), closed form
    kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return recon + kl

# --- block 4 ---
class VAE(nn.Module):
    def __init__(self, in_dim=784, hidden=400, latent=2):
        super().__init__()
        self.encoder = Encoder(in_dim, hidden, latent)
        self.decoder = nn.Sequential(
            nn.Linear(latent, hidden), nn.ReLU(),
            nn.Linear(hidden, in_dim), nn.Sigmoid(),   # pixels in [0, 1]
        )

    def forward(self, x):
        mu, logvar = self.encoder(x)
        z = reparameterize(mu, logvar)
        return self.decoder(z), mu, logvar             # x̂, μ, log σ²

# --- block 5 ---
model = VAE()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

for x, _ in dataloader:               # x: (B, 1, 28, 28)
    x = x.view(x.size(0), -1)          # flatten → (B, 784)
    x_hat, mu, logvar = model(x)
    loss = vae_loss(x_hat, x, mu, logvar)
    opt.zero_grad()
    loss.backward()                    # gradients flow through z, thanks to the trick
    opt.step()

# --- block 6 ---
with torch.no_grad():
    z = torch.randn(16, 2)             # 16 fresh latents from the prior
    samples = model.decoder(z)         # (16, 784) → reshape to 28×28 and view
