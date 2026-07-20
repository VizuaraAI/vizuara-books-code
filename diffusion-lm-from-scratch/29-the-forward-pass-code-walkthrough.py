"""
Build a Diffusion Language Model from Scratch
Chapter 29: The Forward Pass: Code Walkthrough
Section: Build It: Code the Diffusion LM

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/the-forward-pass-code-walkthrough

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class DiffusionLM(nn.Module):
    def __init__(self, vocab_size, d_model, n_layers, n_heads, max_len):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, d_model)   # (9, 8) table
        self.pos_emb = nn.Embedding(max_len, d_model)      # one vector per position
        self.blocks  = nn.ModuleList(
            [TransformerBlock(d_model, n_heads) for _ in range(n_layers)]
        )
        self.norm    = nn.LayerNorm(d_model)
        self.lm_head = nn.Linear(d_model, vocab_size, bias=False)  # (8 -> 9)

    def forward(self, x):                       # x: (B, T) integer token IDs
        B, T = x.shape
        pos  = torch.arange(T, device=x.device) # (T,)  positions 0..T-1
        h    = self.tok_emb(x) + self.pos_emb(pos)   # (B, T, d_model)
        for block in self.blocks:
            h = block(h)                        # (B, T, d_model) -> same shape
        h      = self.norm(h)                   # (B, T, d_model)
        logits = self.lm_head(h)                # (B, T, vocab_size)
        return logits

# --- block 2 ---
# vocab:  0=[MASK] 1=the 2=cat 3=sat 4=on 5=mat 6=dog 7=ran 8=<pad>
x = torch.tensor([
    [1, 2, 0, 5],    # the  cat  [MASK]  mat     <- position 2 masked
    [1, 6, 7, 0],    # the  dog  ran     [MASK]  <- position 3 masked
])
print(x.shape)       # torch.Size([2, 4])

# --- block 3 ---
model = DiffusionLM(vocab_size=9, d_model=8, n_layers=2, n_heads=2, max_len=4)
logits = model(x)
print(logits.shape)  # torch.Size([2, 4, 9])

# --- block 4 ---
tok = self.tok_emb(x)     # (2, 4)  ->  (2, 4, 8)

# --- block 5 ---
pos_vec = self.pos_emb(pos)   # (4,) -> (4, 8)
h = tok + pos_vec             # (2, 4, 8) + (4, 8) -> (2, 4, 8)  [broadcast]

# --- block 6 ---
for block in self.blocks:
    h = block(h)     # (2, 4, 8) -> (2, 4, 8),  every iteration

# --- block 7 ---
h      = self.norm(h)       # (2, 4, 8)  final LayerNorm
logits = self.lm_head(h)    # (2, 4, 8) @ (8, 9) -> (2, 4, 9)
