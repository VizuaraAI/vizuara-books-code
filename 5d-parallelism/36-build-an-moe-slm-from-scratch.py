"""
5D Parallelism for Large Model Training
Chapter 36: Build an MoE SLM from Scratch
Section: Expert Parallelism and MoE

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/build-an-moe-slm-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from dataclasses import dataclass

@dataclass
class Config:
    vocab_size: int = 256     # byte-level: every character is a token
    d_model:    int = 8       # embedding / residual width
    n_heads:    int = 2       # attention heads (d_head = 4)
    n_layers:   int = 4       # transformer blocks
    n_experts:  int = 4       # E — experts per MoE layer
    top_k:      int = 1       # k — experts each token visits
    d_ff:       int = 32      # expert hidden width (4 × d_model)
    seq_len:    int = 16      # context length

# --- block 2 ---
import torch, torch.nn as nn, torch.nn.functional as F

class Expert(nn.Module):                       # a plain FFN, one per expert
    def __init__(self, cfg):
        super().__init__()
        self.up   = nn.Linear(cfg.d_model, cfg.d_ff)
        self.down = nn.Linear(cfg.d_ff, cfg.d_model)
    def forward(self, x):
        return self.down(F.gelu(self.up(x)))

class MoE(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg     = cfg
        self.router  = nn.Linear(cfg.d_model, cfg.n_experts, bias=False)
        self.experts = nn.ModuleList([Expert(cfg) for _ in range(cfg.n_experts)])

    def forward(self, x):                        # x: (B, T, d_model)
        B, T, D = x.shape
        x = x.reshape(B * T, D)                   # flatten to one big list of tokens
        logits = self.router(x)                   # (B*T, E)
        gates, idx = logits.softmax(-1).topk(self.cfg.top_k, dim=-1)  # top-k gate + expert id

        out = torch.zeros_like(x)
        for e in range(self.cfg.n_experts):       # loop experts, not tokens
            mask = (idx == e).any(-1)             # which tokens picked expert e?
            if mask.any():
                out[mask] += self.experts[e](x[mask]) * gates[idx == e].unsqueeze(-1)
        return out.reshape(B, T, D)

# --- block 3 ---
class Block(nn.Module):
    def __init__(self, cfg, use_moe):
        super().__init__()
        self.ln1, self.ln2 = nn.LayerNorm(cfg.d_model), nn.LayerNorm(cfg.d_model)
        self.attn = CausalSelfAttention(cfg)
        self.ff   = MoE(cfg) if use_moe else DenseFFN(cfg)   # <-- the only swap
    def forward(self, x):
        x = x + self.attn(self.ln1(x))      # mix tokens
        x = x + self.ff(self.ln2(x))        # process each token (dense OR sparse)
        return x

# --- block 4 ---
for step in range(3000):
    x, y = get_batch()                          # (B, T) input & shifted target
    logits, aux = model(x)                      # model also returns the balance loss
    loss = F.cross_entropy(logits.reshape(-1, cfg.vocab_size), y.reshape(-1))
    loss = loss + 0.01 * aux                    # aux keeps experts evenly fed
    opt.zero_grad(); loss.backward(); opt.step()
