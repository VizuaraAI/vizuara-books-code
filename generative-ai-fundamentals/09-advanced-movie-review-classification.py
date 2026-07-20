"""
Generative AI Fundamentals
Chapter 9: Advanced Movie Review Classification
Section: Your First Hands-On LLM Projects

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/advanced-movie-review-classification

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Before: open-ended, invites chatter
prompt = f"Is this movie review positive or negative?\n\n{review}"

# After: closed label set + format contract
prompt = (
    "Classify the sentiment of the movie review below.\n"
    "Answer with exactly one word, lowercase, no punctuation: "
    "positive or negative.\n\n"
    f"Review: {review}\n"
    "Sentiment:"
)

# --- block 2 ---
prompt = (
    "Classify each movie review as positive or negative.\n\n"
    "Review: A dazzling, heartfelt film I'd watch again.\n"
    "Sentiment: positive\n\n"
    "Review: Two hours I will never get back. Painfully dull.\n"
    "Sentiment: negative\n\n"
    f"Review: {review}\n"
    "Sentiment:"
)

# --- block 3 ---
import numpy as np

def cosine(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))

review_vec = embed(review)                 # one embedding call
anchors = {lbl: embed(desc) for lbl, desc in label_prototypes.items()}
label = max(anchors, key=lambda l: cosine(review_vec, anchors[l]))
