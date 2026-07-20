"""
RLHF from Scratch
Chapter 6: Tokenization and Embeddings Refresher
Section: The LLM as an RL Agent

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/tokenization-and-embeddings-refresher

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("gpt2")

tok.encode("Once upon a time")
# -> [7454, 2402, 257, 640]

[tok.decode([i]) for i in [7454, 2402, 257, 640]]
# -> ['Once', ' upon', ' a', ' time']

# --- block 2 ---
import torch
emb = torch.nn.Embedding(num_embeddings=50257, embedding_dim=8)

ids = torch.tensor([7454, 2402, 257, 640])   # "Once upon a time"
x = emb(ids)
x.shape        # -> torch.Size([4, 8])   four tokens, each an 8-d vector
