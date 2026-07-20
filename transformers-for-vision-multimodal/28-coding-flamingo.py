"""
Transformers for Vision & Multimodal LLMs
Chapter 28: Building Flamingo-Style Cross-Attention
Section: Video & Multimodal Models

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-flamingo

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class GatedCrossAttentionBlock(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        # standard multi-head projections
        self.w_q = nn.Linear(d_model, d_model, bias=False)  # from text
        self.w_k = nn.Linear(d_model, d_model, bias=False)  # from image
        self.w_v = nn.Linear(d_model, d_model, bias=False)  # from image
        self.w_o = nn.Linear(d_model, d_model, bias=False)
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        self.norm = nn.LayerNorm(d_model)
        self.ffn  = nn.Sequential(                          # position-wise FFN
            nn.Linear(d_model, 4 * d_model), nn.GELU(),
            nn.Linear(4 * d_model, d_model),
        )
        # the two gates — ONE scalar each, initialized to 0 → tanh(0) = 0
        self.attn_gate = nn.Parameter(torch.zeros(1))
        self.ffn_gate  = nn.Parameter(torch.zeros(1))

    def cross_attn(self, text, image):
        B, T, _ = text.shape                     # text: (B, T_text, d_model)
        _, N, _ = image.shape                    # image: (B, N_img,  d_model)
        # Q from text; K, V from image
        q = self.w_q(text).view(B, T, self.num_heads, self.d_k).transpose(1, 2)
        k = self.w_k(image).view(B, N, self.num_heads, self.d_k).transpose(1, 2)
        v = self.w_v(image).view(B, N, self.num_heads, self.d_k).transpose(1, 2)
        scores = (q @ k.transpose(-2, -1)) / (self.d_k ** 0.5)   # (B, h, T, N)
        weights = scores.softmax(dim=-1)                        # over image keys
        ctx = (weights @ v).transpose(1, 2).reshape(B, T, -1)   # (B, T, d_model)
        return self.w_o(ctx)

    def forward(self, text, image):
        # gated cross-attention, then gated FFN — both no-ops at init
        text = text + self.attn_gate.tanh() * self.cross_attn(self.norm(text), image)
        text = text + self.ffn_gate.tanh()  * self.ffn(self.norm(text))
        return text

# --- block 2 ---
block = GatedCrossAttentionBlock(d_model=8, num_heads=2)
text  = torch.randn(1, 3, 8)     # 3 text tokens
image = torch.randn(1, 4, 8)     # 4 visual tokens
out   = block(text, image)
print(torch.allclose(out, text))   # -> True  (gates are 0 at init)
