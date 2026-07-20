"""
Build Large Language Models (LLMs) from Scratch
Chapter 8: Simplified Attention Mechanism - Code from Scratch
Section: LLM Attention Mechanism

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/simplified-attention-mechanism-code-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

# 4 tokens, each a 3-dim embedding.  Shape: (4, 3)
inputs = torch.tensor([
    [0.43, 0.15, 0.89],  # your      (x^1)
    [0.55, 0.87, 0.66],  # journey   (x^2)
    [0.57, 0.85, 0.64],  # starts    (x^3)
    [0.22, 0.58, 0.33],  # here       (x^4)
])

# --- block 2 ---
query = inputs[1]              # x^2 = journey, shape (3,)

scores = torch.empty(inputs.shape[0])   # one score per token, shape (4,)
for i, x_i in enumerate(inputs):
    scores[i] = torch.dot(x_i, query)

# scores -> tensor([0.9544, 1.4950, 1.4754, 0.8434])

# --- block 3 ---
attn_weights = torch.softmax(scores, dim=0)
# -> tensor([0.2098, 0.2461, 0.2417, 0.1414])
print(attn_weights.sum())   # tensor(1.0000)

# --- block 4 ---
context_vec_2 = torch.zeros(query.shape)   # shape (3,)
for i, x_i in enumerate(inputs):
    context_vec_2 += attn_weights[i] * x_i

# context_vec_2 -> tensor([0.4419, 0.6515, 0.5683])

# --- block 5 ---
attn_scores = inputs @ inputs.T          # (4,3) @ (3,4) -> (4,4)
attn_weights = torch.softmax(attn_scores, dim=-1)   # softmax over each ROW
all_context_vecs = attn_weights @ inputs # (4,4) @ (4,3) -> (4,3)
