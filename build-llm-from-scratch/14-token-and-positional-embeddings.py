"""
Build Large Language Models (LLMs) from Scratch
Chapter 14: Token and Positional Embeddings
Section: LLM Data Pre-processing

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/token-and-positional-embeddings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

vocab_size = 6
embedding_dim = 3
torch.manual_seed(123)

embedding = torch.nn.Embedding(vocab_size, embedding_dim)
token_ids = torch.tensor([3, 3797 % vocab_size, 464 % vocab_size])  # e.g. [3, 5, 4]
print(embedding(token_ids).shape)   # torch.Size([3, 3])

# --- block 2 ---
context_length = 4
tok_emb_layer = torch.nn.Embedding(vocab_size, embedding_dim)
pos_emb_layer = torch.nn.Embedding(context_length, embedding_dim)

token_ids = torch.tensor([[3, 5, 4, 1]])          # shape (1, 4)
positions = torch.arange(4)                        # tensor([0, 1, 2, 3])

tok_emb = tok_emb_layer(token_ids)                 # (1, 4, 768)
pos_emb = pos_emb_layer(positions)                 # (4, 768), broadcasts over batch
input_emb = tok_emb + pos_emb                      # (1, 4, 768)  the model's input

# --- block 3 ---
# the standard GPT-2-small shapes
vocab_size     = 50257
embedding_dim  = 768
context_length = 1024
batch_size     = 8

tok_emb = torch.nn.Embedding(vocab_size, embedding_dim)      # (50257, 768)
pos_emb = torch.nn.Embedding(context_length, embedding_dim)  # (1024, 768)

batch = torch.randint(0, vocab_size, (batch_size, context_length))  # fake token IDs
x = tok_emb(batch) + pos_emb(torch.arange(context_length))          # (8, 1024, 768)
