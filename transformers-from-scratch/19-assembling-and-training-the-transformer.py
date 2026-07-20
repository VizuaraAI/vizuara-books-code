"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 19: Assembling and Training the Transformer
Section: Implementation & Code Walkthrough

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/assembling-and-training-the-transformer

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

# --- block 1 ---
class Transformer(nn.Module):
    def __init__(self, vocab_size, d_model=512, N=6, h=8, d_ff=2048):
        super().__init__()
        self.src_embed = nn.Embedding(vocab_size, d_model)
        self.tgt_embed = nn.Embedding(vocab_size, d_model)
        self.pos = PositionalEncoding(d_model)          # the sinusoidal table
        self.encoder = nn.ModuleList([EncoderBlock(d_model, h, d_ff) for _ in range(N)])
        self.decoder = nn.ModuleList([DecoderBlock(d_model, h, d_ff) for _ in range(N)])
        self.lm_head = nn.Linear(d_model, vocab_size)   # 512 -> 50000 logits

    def encode(self, src):
        x = self.pos(self.src_embed(src))               # (B, src_len, 512)
        for block in self.encoder:
            x = block(x)                                # no mask: bidirectional
        return x                                        # the memory

    def decode(self, tgt, memory, tgt_mask):
        x = self.pos(self.tgt_embed(tgt))               # (B, tgt_len, 512)
        for block in self.decoder:
            x = block(x, memory, tgt_mask)              # masked self-attn + cross-attn
        return x

    def forward(self, src, tgt, tgt_mask):
        memory = self.encode(src)
        out = self.decode(tgt, memory, tgt_mask)        # (B, tgt_len, 512)
        return self.lm_head(out)                         # (B, tgt_len, 50000)

# --- block 2 ---
opt = torch.optim.Adam(model.parameters(), lr=1e-4, betas=(0.9, 0.98))
loss_fn = nn.CrossEntropyLoss(ignore_index=PAD)   # don't score padding slots

for src, tgt in dataloader:                       # tgt: (B, tgt_len+1) incl. <s>...</s>
    dec_in  = tgt[:, :-1]                          # drop the last: [<s>, Le, chat, s'assit]
    labels  = tgt[:, 1:]                           # drop the first: [Le, chat, s'assit, </s>]
    mask    = causal_mask(dec_in.size(1))          # lower-triangular (tgt_len × tgt_len)

    logits  = model(src, dec_in, mask)             # (B, tgt_len, 50000)
    loss    = loss_fn(logits.reshape(-1, 50000), labels.reshape(-1))

    opt.zero_grad(); loss.backward(); opt.step()   # backprop + update

# --- block 3 ---
def generate(model, src, max_len=50):
    memory = model.encode(src)             # run the ENCODER ONCE
    tgt = torch.tensor([[BOS]])            # start with just <s>
    for _ in range(max_len):
        mask   = causal_mask(tgt.size(1))
        out    = model.decode(tgt, memory, mask)   # (1, cur_len, 512)
        logits = model.lm_head(out[:, -1])         # ONLY the last position
        next_id = logits.argmax(-1)                # greedy pick
        tgt = torch.cat([tgt, next_id.view(1, 1)], dim=1)
        if next_id == EOS:
            break
    return tgt
