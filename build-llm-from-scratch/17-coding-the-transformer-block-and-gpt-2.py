"""
Build Large Language Models (LLMs) from Scratch
Chapter 17: Coding the Transformer Block and the 124M GPT-2
Section: LLM Architecture

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/coding-the-transformer-block-and-gpt-2

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch
import torch.nn as nn

# --- shared context (added to make this file runnable) ---
# These three are defined in earlier chapters (MultiHeadAttention in ch. 12,
# LayerNorm and FeedForward in ch. 16) and are reused here without repeating.
from context import MultiHeadAttention, FeedForward, LayerNorm

# --- block 1 ---
GPT_CONFIG_124M = {
    "vocab_size": 50257,   # BPE tokenizer vocabulary
    "context_length": 1024, # max tokens the model can see at once
    "emb_dim": 768,        # width of every token vector (d_model)
    "n_heads": 12,         # attention heads per block
    "n_layers": 12,        # number of transformer blocks
    "drop_rate": 0.1,      # dropout probability
    "qkv_bias": False      # no bias on the Q/K/V projections
}

# --- block 2 ---
class TransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.att = MultiHeadAttention(
            d_in=cfg["emb_dim"], d_out=cfg["emb_dim"],
            context_length=cfg["context_length"],
            num_heads=cfg["n_heads"], dropout=cfg["drop_rate"],
            qkv_bias=cfg["qkv_bias"])
        self.ff = FeedForward(cfg)
        self.norm1 = LayerNorm(cfg["emb_dim"])
        self.norm2 = LayerNorm(cfg["emb_dim"])
        self.drop = nn.Dropout(cfg["drop_rate"])

    def forward(self, x):
        shortcut = x                      # (1) save residual
        x = self.norm1(x)                 # (2) normalize
        x = self.att(x)                   # (2) attention sublayer
        x = self.drop(x)
        x = x + shortcut                  # (3) add shortcut back

        shortcut = x                      # repeat for feed-forward
        x = self.norm2(x)
        x = self.ff(x)
        x = self.drop(x)
        x = x + shortcut
        return x

# --- block 3 ---
class GPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])   # 50257 x 768
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"]) # 1024 x 768
        self.drop_emb = nn.Dropout(cfg["drop_rate"])
        self.trf_blocks = nn.Sequential(
            *[TransformerBlock(cfg) for _ in range(cfg["n_layers"])])     # 12 blocks
        self.final_norm = LayerNorm(cfg["emb_dim"])
        self.out_head = nn.Linear(cfg["emb_dim"], cfg["vocab_size"], bias=False) # 768 -> 50257

    def forward(self, in_idx):
        batch, seq_len = in_idx.shape
        tok = self.tok_emb(in_idx)                                   # (b, seq, 768)
        pos = self.pos_emb(torch.arange(seq_len, device=in_idx.device))
        x = self.drop_emb(tok + pos)                                 # add position signal
        x = self.trf_blocks(x)                                       # 12 blocks refine x
        x = self.final_norm(x)
        logits = self.out_head(x)                                    # (b, seq, 50257)
        return logits

# --- block 4 ---
def generate_text_simple(model, idx, max_new_tokens, context_size):
    for _ in range(max_new_tokens):
        idx_cond = idx[:, -context_size:]          # crop to the context window
        with torch.no_grad():
            logits = model(idx_cond)               # (b, seq, 50257)
        logits = logits[:, -1, :]                   # keep only the last position
        probs = torch.softmax(logits, dim=-1)       # -> probabilities
        idx_next = torch.argmax(probs, dim=-1, keepdim=True)  # greedy pick
        idx = torch.cat((idx, idx_next), dim=1)     # append and loop
    return idx
