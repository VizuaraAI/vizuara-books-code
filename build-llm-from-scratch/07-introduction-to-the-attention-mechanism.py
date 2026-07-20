"""
Build Large Language Models (LLMs) from Scratch
Chapter 7: Introduction to the Attention Mechanism
Section: LLM Attention Mechanism

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/introduction-to-the-attention-mechanism

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# three words, each a 4-dim vector
the = np.array([1.0, 0.0, 0.0, 0.0])
cat = np.array([0.0, 1.0, 0.0, 0.0])
sat = np.array([0.0, 0.0, 1.0, 0.0])
words = np.stack([the, cat, sat])          # shape (3, 4)

# suppose attention decided: focus mostly on "cat"
weights = np.array([0.1, 0.7, 0.2])        # they sum to 1.0

context = weights @ words                    # weighted sum → shape (4,)
print(context)   # [0.1, 0.7, 0.2, 0.0]
