"""
Generative AI Fundamentals
Chapter 5: How an LLM Generates Text
Section: Foundations of Generative AI

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/how-an-llm-generates-text

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def next_token(logits, temperature=1.0, top_k=None):
    logits = logits / temperature                 # 1. temperature scaling
    if top_k is not None:                          # 2. optional truncation
        cutoff = np.sort(logits)[-top_k]
        logits = np.where(logits < cutoff, -np.inf, logits)
    z = logits - logits.max()                      # 3. softmax (max-shifted)
    probs = np.exp(z) / np.exp(z).sum()
    return np.random.choice(len(probs), p=probs)   # 4. roll the weighted die
