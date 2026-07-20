"""
LLM Production & Deployment
Chapter 13: Zero-Shot vs Finetuned Classification
Section: Text Classification with LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/zero-shot-vs-finetuned-classification

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
prompt = (
    "Classify the movie review as Positive or Negative.\n"
    "Review: a masterpiece of tension\n"
    "Sentiment:"
)
# the big model reads the instruction and answers "Positive" — no labels, no training
