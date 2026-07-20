"""
AI Context Engineering
Chapter 2: Software 1.0, 2.0, and 3.0
Section: Context Foundations

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/software-1-2-3

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def sentiment(text):
    neg = {"hate", "broken", "refund", "worst", "terrible"}
    pos = {"love", "great", "perfect", "amazing"}
    score = sum(w in text.lower() for w in pos) - sum(w in text.lower() for w in neg)
    return "positive" if score >= 0 else "negative"
