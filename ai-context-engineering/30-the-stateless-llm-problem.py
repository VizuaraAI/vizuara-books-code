"""
AI Context Engineering
Chapter 30: The Stateless LLM Problem
Section: Memory Architectures

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/the-stateless-llm-problem

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Turn 2, WITHOUT resending history — the model has no idea:
messages = [{"role": "user", "content": "What's my name?"}]
# -> "I don't have access to your name."
