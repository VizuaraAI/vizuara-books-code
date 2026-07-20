"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 13: Scaled Dot-Product Attention, Coded
Section: Attention from Scratch

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/scaled-dot-product-attention-coded

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V):
    # Q, K, V each have shape (num_tokens, d_k)
    d_k = Q.shape[-1]                          # 8 in our toy, 64 in DeiT
    scores  = Q @ K.transpose(-2, -1)          # (T, T): every query · every key
    scores  = scores / (d_k ** 0.5)            # scale by 1/√d_k
    weights = F.softmax(scores, dim=-1)        # row-wise → each row sums to 1
    output  = weights @ V                      # (T, d_k): blend the values
    return output, weights

# --- block 2 ---
torch.manual_seed(0)
T, d_k = 4, 8
Q, K, V = torch.randn(T, d_k), torch.randn(T, d_k), torch.randn(T, d_k)

out, attn = scaled_dot_product_attention(Q, K, V)
print(out.shape)          # torch.Size([4, 8])   -> same tokens, same width as V
print(attn.shape)         # torch.Size([4, 4])   -> the token-by-token weights
print(attn.sum(dim=-1))   # tensor([1., 1., 1., 1.]) -> every row sums to 1
