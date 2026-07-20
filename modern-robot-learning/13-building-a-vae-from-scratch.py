"""
Modern Robot Learning
Chapter 13: Building a VAE from Scratch
Section: Deep Generative Modeling

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/building-a-vae-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn
import torch.nn.functional as F

LATENT = 20

class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1     = nn.Linear(784, 400)
        self.fc_mu   = nn.Linear(400, LATENT)   # mean head
        self.fc_lv   = nn.Linear(400, LATENT)   # log-variance head

    def forward(self, x):          # x: (batch, 784)
        h = F.relu(self.fc1(x))    # h: (batch, 400)
        return self.fc_mu(h), self.fc_lv(h)     # each (batch, 20)

# --- block 2 ---
def reparameterize(mu, logvar):
    std = torch.exp(0.5 * logvar)     # sigma = exp(logvar/2), always > 0
    eps = torch.randn_like(std)       # eps ~ N(0, I), same shape as std
    return mu + std * eps             # z = mu + sigma * eps

# --- block 3 ---
class VAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = Encoder()
        self.fc3 = nn.Linear(LATENT, 400)
        self.fc4 = nn.Linear(400, 784)

    def decode(self, z):
        h = F.relu(self.fc3(z))
        return torch.sigmoid(self.fc4(h))       # x_hat in [0,1], shape (batch, 784)

    def forward(self, x):
        mu, logvar = self.encoder(x)
        z = reparameterize(mu, logvar)
        return self.decode(z), mu, logvar

# --- block 4 ---
def vae_loss(x_hat, x, mu, logvar):
    recon = F.binary_cross_entropy(x_hat, x, reduction='sum')
    kl    = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return recon + kl

# --- block 5 ---
model = VAE()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

for x, _ in train_loader:            # x: (batch, 1, 28, 28)
    x = x.view(-1, 784)              # flatten to (batch, 784)
    x_hat, mu, logvar = model(x)
    loss = vae_loss(x_hat, x, mu, logvar)
    opt.zero_grad(); loss.backward(); opt.step()

# --- block 6 ---
z = torch.randn(16, LATENT)          # 16 fresh latent codes from the prior
new_digits = model.decode(z)         # (16, 784) → reshape to 16 images
