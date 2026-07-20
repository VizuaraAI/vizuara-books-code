"""
Prompt Engineering
Chapter 13: Chat, Playground, and API
Section: The Prompting Toolbox

Read this chapter: https://books.vizuara.ai/read/prompt-engineering/chat-vs-api-vs-playground

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a terse assistant. Answer in one sentence."},
        {"role": "user",   "content": "Explain what a prompt is."},
    ],
    temperature=0.7,   # if you omit this, the API picks a default for you
    max_tokens=60,     # a HARD cap on output length — it truncates, it does not summarize
)
print(resp.choices[0].message.content)
