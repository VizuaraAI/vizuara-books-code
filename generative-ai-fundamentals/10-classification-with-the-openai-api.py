"""
Generative AI Fundamentals
Chapter 10: Classification with the OpenAI API
Section: Your First Hands-On LLM Projects

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/classification-with-the-openai-api

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from your environment

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",
         "content": "Classify the movie review as positive or negative. "
                    "Reply with exactly one word: positive or negative."},
        {"role": "user",
         "content": "A tedious, overlong slog. I checked my watch twice."},
    ],
    temperature=0,
)
label = resp.choices[0].message.content.strip().lower()
print(label)   # -> negative

# --- block 2 ---
messages = [
    {"role": "system",
     "content": "Classify the movie review as positive or negative. "
                "Reply with exactly one word: positive or negative."},
    # two few-shot examples that pin the format:
    {"role": "user", "content": "A masterpiece. I'll watch it again tonight."},
    {"role": "assistant", "content": "positive"},
    {"role": "user", "content": "Boring and forgettable. Wasted my evening."},
    {"role": "assistant", "content": "negative"},
    # the real review:
    {"role": "user", "content": review_text},
]

# --- block 3 ---
import time

VALID = {"positive", "negative"}

def classify(review_text, retries=3):
    for attempt in range(retries):
        try:
            resp = client.chat.completions.create(
                model="gpt-4o-mini", messages=build_messages(review_text),
                temperature=0,
            )
            out = resp.choices[0].message.content.strip().lower()
            return out if out in VALID else "unknown"   # never trust the raw text
        except Exception:
            time.sleep(2 ** attempt)                     # 1s, 2s, 4s backoff
    return "error"

labels = []
for i, review in enumerate(reviews):
    labels.append(classify(review))
    if i % 50 == 0:
        save_progress(labels)   # checkpoint so a crash costs at most 50 rows
