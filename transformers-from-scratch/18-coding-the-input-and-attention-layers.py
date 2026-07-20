"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 18: Coding the Input and Attention Layers
Section: Implementation & Code Walkthrough

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/coding-the-input-and-attention-layers

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np
rng = np.random.default_rng(0)

vocab_size, d_model = 12, 4
embedding = rng.normal(0, 1, size=(vocab_size, d_model)).round(2)

token_ids = np.array([5, 2, 9])   # our sentence, seq_len = 3
X = embedding[token_ids]           # the entire "layer": fancy indexing
print(X.shape)                     # (3, 4)

# --- block 2 ---
def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]                       # (seq_len, 1)
    i   = np.arange(d_model)[None, :]                       # (1, d_model)
    angle = pos / np.power(10000, (2 * (i // 2)) / d_model) # (seq_len, d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])   # even columns: sine
    pe[:, 1::2] = np.cos(angle[:, 1::2])   # odd columns: cosine
    return pe

PE = positional_encoding(seq_len=3, d_model=4)
X = X + PE     # same shape, so we just add

# --- block 3 ---
def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)

def attention(Q, K, V):
    d_k = Q.shape[-1]
    scores  = Q @ K.T / np.sqrt(d_k)   # (seq_len, seq_len)
    weights = softmax(scores, axis=-1) # each row sums to 1
    return weights @ V                 # (seq_len, d_k)

# --- block 4 ---
def multi_head_attention(X, Wq, Wk, Wv, Wo, num_heads):
    seq_len, d_model = X.shape
    d_k = d_model // num_heads
    heads = []
    for h in range(num_heads):
        s = slice(h * d_k, (h + 1) * d_k)          # this head's columns
        Q = X @ Wq[:, s]                            # (seq_len, d_k)
        K = X @ Wk[:, s]
        V = X @ Wv[:, s]
        heads.append(attention(Q, K, V))            # (seq_len, d_k)
    concat = np.concatenate(heads, axis=-1)         # (seq_len, d_model)
    return concat @ Wo                              # (seq_len, d_model)
