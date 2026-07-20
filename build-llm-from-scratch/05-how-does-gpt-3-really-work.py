"""
Build Large Language Models (LLMs) from Scratch
Chapter 5: How does GPT-3 really work?
Section: LLM Basics

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/how-does-gpt-3-really-work

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- shared context (added to make this file runnable) ---
# `softmax` is defined in chapter 4 and reused here without being repeated.
from context import softmax

# --- block 1 ---
import numpy as np

def generate(model, tokenizer, prompt, max_new_tokens=50, temperature=0.8):
    tokens = tokenizer.encode(prompt)          # e.g. [464, 3797, 3332, ...]
    for _ in range(max_new_tokens):
        logits = model(tokens)                 # shape (vocab_size,) = (50257,)
        logits = logits / temperature          # sharpen or flatten the odds
        probs = softmax(logits)                # turn scores into a distribution
        next_token = np.random.choice(len(probs), p=probs)   # roll the die
        tokens.append(next_token)              # <- autoregression: feed it back
        if next_token == tokenizer.eot_id:     # the model chose to stop
            break
    return tokenizer.decode(tokens)
