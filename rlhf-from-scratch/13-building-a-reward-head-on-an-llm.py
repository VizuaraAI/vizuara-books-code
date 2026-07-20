"""
RLHF from Scratch
Chapter 13: Building a Reward Head on an LLM
Section: Reward Models

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/building-a-reward-head-on-an-llm

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
import numpy as np

# hidden states H: (seq_len=4, d_model=8), one row per token
H = np.array([
    [ 0.1, -0.3,  0.2,  0.0,  0.5, -0.1,  0.4, -0.2],  # "The"  (pos 0)
    [-0.2,  0.1,  0.3, -0.4,  0.0,  0.2, -0.1,  0.3],  # "cat"  (pos 1)
    [ 0.4,  0.0, -0.1,  0.2, -0.3,  0.1,  0.2,  0.0],  # "sat"  (pos 2)
    [ 0.3, -0.2,  0.5, -0.1,  0.1,  0.0, -0.3,  0.4],  # "."    (pos 3)  ← LAST
])

# --- block 2 ---
w = np.array([0.5, -0.2, 0.3, 0.1, -0.4, 0.6, -0.1, 0.2])  # reward head, (8,)

h_last = H[-1]                 # the "." token's hidden vector, shape (8,)
r = h_last @ w                 # one scalar

# --- block 3 ---
import torch.nn as nn
from transformers import AutoModel

class RewardModel(nn.Module):
    def __init__(self, base_name):
        super().__init__()
        self.backbone = AutoModel.from_pretrained(base_name)   # pretrained, reused
        d_model = self.backbone.config.hidden_size             # e.g. 768
        self.reward_head = nn.Linear(d_model, 1, bias=False)   # the ONLY new layer

    def forward(self, input_ids, attention_mask):
        hidden = self.backbone(input_ids, attention_mask).last_hidden_state
        # hidden: (batch, seq_len, d_model) — a scalar-able vector at every position
        last_idx = attention_mask.sum(dim=1) - 1               # index of the final REAL token
        h_last = hidden[torch.arange(hidden.size(0)), last_idx]  # (batch, d_model)
        return self.reward_head(h_last).squeeze(-1)            # (batch,) — one r per example
