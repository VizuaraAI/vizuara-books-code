"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 17: Tokenization and the Dataset
Section: Implementation & Code Walkthrough

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/tokenization-and-the-dataset

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(len(text))          # e.g. 1_115_394 characters
print(text[:80])          # "First Citizen:\nBefore we proceed any further, hear me speak.\n"

# --- block 2 ---
import tiktoken

enc = tiktoken.get_encoding("gpt2")     # the exact GPT-2 byte-level BPE

ids = enc.encode("the cats are unhappy")
print(ids)                               # [1169, 11875, 389, 19527]
print(len(ids))                          # 4 tokens for 4 words here

print(enc.decode(ids))                   # 'the cats are unhappy'  (round-trips exactly)
print([enc.decode([i]) for i in ids])    # ['the', ' cats', ' are', ' unhappy']
