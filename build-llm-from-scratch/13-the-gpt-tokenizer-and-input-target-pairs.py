"""
Build Large Language Models (LLMs) from Scratch
Chapter 13: The GPT Tokenizer: Byte Pair Encoding and Input-Target Pairs
Section: LLM Data Pre-processing

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/the-gpt-tokenizer-and-input-target-pairs

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")
ids = tokenizer.encode("Akwirw ier")   # a made-up nonsense string
print(ids)                              # [33901, 86, 343, 86, 220, 959]
print(tokenizer.decode(ids))            # 'Akwirw ier'

# --- block 2 ---
import torch
from torch.utils.data import Dataset, DataLoader

class GPTDataset(Dataset):
    def __init__(self, token_ids, max_length, stride):
        self.inputs, self.targets = [], []
        for i in range(0, len(token_ids) - max_length, stride):
            x = token_ids[i : i + max_length]
            y = token_ids[i + 1 : i + max_length + 1]   # shifted by one
            self.inputs.append(torch.tensor(x))
            self.targets.append(torch.tensor(y))

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        return self.inputs[idx], self.targets[idx]
