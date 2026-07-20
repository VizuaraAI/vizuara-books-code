"""
Foundations for AI & ML
Chapter 2: The Map: AI, ML, and Deep Learning
Section: Getting Started

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/the-map-ai-ml-deep-learning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
SPAM_WORDS = {"free", "winner", "prize", "click", "viagra"}

def is_spam(email_words):
    hits = sum(1 for w in email_words if w in SPAM_WORDS)
    return hits >= 3          # threshold picked by a human
