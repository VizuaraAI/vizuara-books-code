"""
Prompt Engineering
Chapter 3: Why the Same Model Gives Different Answers
Section: Foundations

Read this chapter: https://books.vizuara.ai/read/prompt-engineering/why-prompts-matter

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(logits):
    e = np.exp(logits - logits.max())   # subtract max for numerical safety
    return e / e.sum()

vocab = ["Paris", "France", "croissant", "banana"]
