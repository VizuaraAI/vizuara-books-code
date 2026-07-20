"""
LLM Finetuning
Chapter 21: Adding a Custom Classification Head
Section: Finetuning with Hugging Face & Unsloth

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/adding-a-classification-head

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

# body outputs vectors of width d = 768; we want 2 classes
classification_head = nn.Linear(in_features=768, out_features=2)

# --- block 2 ---
outputs = model.transformer(input_ids)          # body only, no lm_head
hidden = outputs.last_hidden_state               # (batch, seq_len, 768)
last_token = hidden[:, -1, :]                     # (batch, 768) — the summary
logits = classification_head(last_token)          # (batch, 2)

# --- block 3 ---
import torch
import torch.nn as nn
from transformers import GPT2Model

class GPT2ForClassification(nn.Module):
    def __init__(self, num_classes=2):
        super().__init__()
        # 1. the reusable pretrained body (no lm_head loaded)
        self.body = GPT2Model.from_pretrained("gpt2")   # d = 768
        # 2. a brand-new, randomly-initialized head
        self.head = nn.Linear(768, num_classes)

    def forward(self, input_ids, attention_mask=None):
        hidden = self.body(input_ids, attention_mask=attention_mask).last_hidden_state
        last_token = hidden[:, -1, :]        # (batch, 768)
        return self.head(last_token)         # (batch, num_classes) logits
