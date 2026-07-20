"""
Build a NanoVLM from Scratch
Chapter 27: The Text Encoder Module
Section: Building the NanoVLM

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-text-encoder-module

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class TextEncoder(nn.Module):
    def __init__(self, vocab_size=50000, seq_len=4, d_model=8, d=4,
                 n_heads=2, n_layers=2):
        super().__init__()
        self.tok_embed = nn.Embedding(vocab_size, d_model)   # (50000, 8) table
        self.pos_embed = nn.Embedding(seq_len,    d_model)   # (4, 8) table

# --- block 2 ---
        block = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads,
            dim_feedforward=4 * d_model, batch_first=True)
        self.blocks = nn.TransformerEncoder(block, num_layers=n_layers)

# --- block 3 ---
    def forward(self, ids):                    # ids: (batch, seq_len) ints
        B, S = ids.shape
        positions = torch.arange(S, device=ids.device)   # [0, 1, 2, 3]
        x = self.tok_embed(ids) + self.pos_embed(positions)  # (B, S, d_model)
        x = self.blocks(x)                     # (B, S, d_model) — same shape
        pooled = x.mean(dim=1)                 # (B, d_model) — mean over tokens
        return self.proj(pooled)               # (B, d) — into the shared space

# --- block 4 (COMMENTED OUT - out-of-context fragment) ---
# NOTE: this block is prose in the book, not runnable code.
# It is a one-line fragment that belongs inside __init__ (alongside the other
# self.* assignments in block 1), shown separately so the chapter can talk
# about the projection on its own. Concatenating the chapter's blocks in
# document order drops it after `forward`'s `return` instead, where it is both
# unreachable and out of scope (d_model and d are __init__ parameters).
# Block 5 below repeats the whole class with this line in its correct place.
#         self.proj = nn.Linear(d_model, d)      # (8 -> 4): into the shared space

# --- block 5 ---
import torch
import torch.nn as nn

class TextEncoder(nn.Module):
    def __init__(self, vocab_size=50000, seq_len=4, d_model=8, d=4,
                 n_heads=2, n_layers=2):
        super().__init__()
        self.tok_embed = nn.Embedding(vocab_size, d_model)
        self.pos_embed = nn.Embedding(seq_len,    d_model)
        block = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads,
            dim_feedforward=4 * d_model, batch_first=True)
        self.blocks = nn.TransformerEncoder(block, num_layers=n_layers)
        self.proj = nn.Linear(d_model, d)

    def forward(self, ids):                     # (B, S) ints
        S = ids.shape[1]
        positions = torch.arange(S, device=ids.device)
        x = self.tok_embed(ids) + self.pos_embed(positions)  # (B, S, d_model)
        x = self.blocks(x)                      # (B, S, d_model)
        pooled = x.mean(dim=1)                   # (B, d_model)
        return self.proj(pooled)                 # (B, d)

# --- block 6 ---
enc = TextEncoder()
ids = torch.randint(0, 50000, (2, 4))   # 2 captions, 4 tokens each
out = enc(ids)
print(out.shape)                        # torch.Size([2, 4])  ✓ (batch, d)
