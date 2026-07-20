"""
Build a Diffusion Language Model from Scratch
Chapter 16: Build an Autoregressive LLM from Scratch
Section: The Autoregressive Baseline

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/build-autoregressive-llm-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
config = dict(
    vocab_size = 50258,   # 50257 real tokens + 1 reserved [MASK] id
    d_model    = 8,       # embedding width (toy; real ≈ 768)
    n_head     = 2,       # attention heads per block
    n_layer    = 3,       # how many transformer blocks we stack
    context    = 16,      # max sequence length
)

# --- block 2 ---
import torch, torch.nn as nn

class AutoregressiveLM(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["d_model"])  # token lookup
        self.pos_emb = nn.Embedding(cfg["context"],    cfg["d_model"])  # position lookup
        self.blocks  = nn.ModuleList(
            TransformerBlock(cfg) for _ in range(cfg["n_layer"])        # the stack
        )
        self.ln_f    = nn.LayerNorm(cfg["d_model"])                     # final norm
        self.head    = nn.Linear(cfg["d_model"], cfg["vocab_size"], bias=False)
        self.head.weight = self.tok_emb.weight   # weight tying: read view == write view

    def forward(self, ids):                       # ids: (batch, seq_len)
        B, T = ids.shape
        pos  = torch.arange(T, device=ids.device)
        x    = self.tok_emb(ids) + self.pos_emb(pos)   # (B, T, d_model)
        for block in self.blocks:                      # the causal mask lives inside
            x = block(x)
        x = self.ln_f(x)
        return self.head(x)                            # (B, T, vocab_size) = logits

# --- block 3 ---
import torch.nn.functional as F

def loss_fn(model, ids):
    x, y   = ids[:, :-1], ids[:, 1:]           # y is x shifted left by one
    logits = model(x)                          # (B, T-1, vocab_size)
    B, T, V = logits.shape
    return F.cross_entropy(logits.reshape(B*T, V), y.reshape(B*T))

# --- block 4 ---
@torch.no_grad()
def generate(model, ids, n_new):
    for _ in range(n_new):                          # <- N sequential passes
        logits = model(ids[:, -config["context"]:]) # full forward pass
        probs  = F.softmax(logits[:, -1], dim=-1)   # distribution for the LAST position only
        nxt    = torch.multinomial(probs, 1)        # sample one token
        ids    = torch.cat([ids, nxt], dim=1)       # append, then loop again
    return ids
