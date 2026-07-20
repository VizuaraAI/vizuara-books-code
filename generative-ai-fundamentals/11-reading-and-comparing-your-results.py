"""
Generative AI Fundamentals
Chapter 11: Reading and Comparing Your Results
Section: Your First Hands-On LLM Projects

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/reading-and-comparing-your-results

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def score(y_true, y_pred, positive="positive"):
    acc = accuracy_score(y_true, y_pred)
    p, r, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=[positive], average="binary",
        pos_label=positive, zero_division=0,
    )
    return {"accuracy": acc, "precision": p, "recall": r, "f1": f1}
