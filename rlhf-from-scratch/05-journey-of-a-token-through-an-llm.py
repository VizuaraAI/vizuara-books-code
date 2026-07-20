"""
RLHF from Scratch
Chapter 5: The Journey of a Token Through an LLM
Section: The LLM as an RL Agent

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/journey-of-a-token-through-an-llm

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# toy numbers, d = 8
emb["France"] = [0.21, -0.90,  0.44,  0.05, -0.33,  0.77,  0.12, -0.61]

# --- block 2 ---
import numpy as np

def softmax(logits):
    e = np.exp(logits - logits.max())   # subtract max for numerical stability
    return e / e.sum()                  # now non-negative and sums to 1

# --- block 3 ---
logits = { "Paris": 3.2, "France": 1.0, "the": 0.5, "banana": -2.0, "London": 1.8 }

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# P("Paris")  ≈ 24.5 / 35.1 ≈ 0.70
# P("London") ≈ 6.05 / 35.1 ≈ 0.17
# P("France") ≈ 2.72 / 35.1 ≈ 0.08
# P("the")    ≈ 1.65 / 35.1 ≈ 0.05
# P("banana") ≈ 0.14 / 35.1 ≈ 0.004
