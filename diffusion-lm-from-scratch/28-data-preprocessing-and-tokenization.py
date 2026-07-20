"""
Build a Diffusion Language Model from Scratch
Chapter 28: Data Preprocessing and Tokenization
Section: Build It: Code the Diffusion LM

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/data-preprocessing-and-tokenization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def chunk(stream, block_size):
    return [stream[i : i + block_size]
            for i in range(0, len(stream), block_size)]

chunk(stream, 8)
# -> [[72, 1842, 481, 1492, 262, 3797, 3332, 319],   # full: 8 tokens
#     [262, 6759]]                                     # short: 2 tokens, the tail

# --- block 2 ---
PAD_ID = 50256

def pad(ch, block_size, pad_id=PAD_ID):
    return ch + [pad_id] * (block_size - len(ch))

pad([262, 6759], 8)
# -> [262, 6759, 50256, 50256, 50256, 50256, 50256, 50256]

# --- block 3 ---
import torch

chunks = [
    [72, 1842, 481, 1492, 262, 3797, 3332, 319],          # chunk 0
    [262, 6759, 50256, 50256, 50256, 50256, 50256, 50256] # chunk 1, padded
]
masks = [
    [1, 1, 1, 1, 1, 1, 1, 1],                              # all real
    [1, 1, 0, 0, 0, 0, 0, 0]                               # two real, six pad
]

x     = torch.tensor(chunks)   # shape (2, 8)
m     = torch.tensor(masks)    # shape (2, 8)
x.shape, m.shape               # (torch.Size([2, 8]), torch.Size([2, 8]))

# --- block 4 ---
def build_batches(docs, tokenize, block_size, batch_size, pad_id=PAD_ID):
    # 1. tokenize every doc and concatenate into one stream
    stream = [tid for doc in docs for tid in tokenize(doc)]

    # 2. chunk into block_size pieces
    chunks = [stream[i:i + block_size]
              for i in range(0, len(stream), block_size)]

    # 3. pad the ragged tail and build parallel attention masks
    ids, masks = [], []
    for ch in chunks:
        real = len(ch)
        ids.append(ch + [pad_id] * (block_size - real))
        masks.append([1] * real + [0] * (block_size - real))

    # 4. stack into (n_chunks, block_size), then batch
    x = torch.tensor(ids)
    m = torch.tensor(masks)
    return x.split(batch_size), m.split(batch_size)
