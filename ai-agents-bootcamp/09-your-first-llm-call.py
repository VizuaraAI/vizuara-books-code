"""
AI Agents Bootcamp
Chapter 9: Your First LLM Call in Code
Section: The Engine: Large Language Models

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/your-first-llm-call

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from openai import OpenAI
client = OpenAI()  # reads OPENAI_API_KEY from the environment

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a terse assistant."},
        {"role": "user",   "content": "Name the capital of France."},
    ],
)

# --- block 2 ---
import time, random
from openai import RateLimitError

def call_with_backoff(client, **kwargs):
    delay = 1.0
    for attempt in range(6):                     # up to 6 tries
        try:
            return client.chat.completions.create(**kwargs)
        except RateLimitError:
            wait = delay + random.uniform(0, 0.5)  # jitter avoids thundering herd
            time.sleep(wait)
            delay *= 2                             # 1s → 2s → 4s → 8s ...
    raise RuntimeError("still rate-limited after 6 attempts")
