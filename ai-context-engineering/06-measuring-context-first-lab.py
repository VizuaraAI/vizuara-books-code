"""
AI Context Engineering
Chapter 6: Your First Context Lab: Measuring Tokens and Effects
Section: Context Foundations

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/measuring-context-first-lab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# what the tokenizer actually returns for "Context is the program."
["Context", " is", " the", " program", "."]      # 5 tokens
# and note the leading spaces are PART of the token, not stripped

# --- block 2 ---
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o-mini")

def count_tokens(text: str) -> int:
    return len(enc.encode(text))

count_tokens("Context is the program.")   # -> 5
