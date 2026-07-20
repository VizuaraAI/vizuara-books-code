"""
Generative AI Fundamentals
Chapter 8: Movie Review Sentiment Analysis
Section: Your First Hands-On LLM Projects

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/movie-review-sentiment-analysis

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
prompt = f"""Classify the sentiment of this movie review as
positive or negative. Answer with one word only.

Review: {review}
Sentiment:"""

# --- block 2 ---
correct = 0
for review, true_label in test_set:          # e.g. 200 held-out reviews
    prompt = build_prompt(review)
    raw = llm(prompt).strip().lower()          # e.g. "negative." or "Positive"
    pred = parse_label(raw)                     # map messy text -> "positive"/"negative"
    correct += (pred == true_label)

accuracy = correct / len(test_set)

# --- block 3 ---
def parse_label(raw):
    t = raw.lower()
    if "negative" in t: return "negative"
    if "positive" in t: return "positive"
    return "unparseable"      # count these separately, don't guess
