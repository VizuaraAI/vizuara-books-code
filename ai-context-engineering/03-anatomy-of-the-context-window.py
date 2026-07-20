"""
AI Context Engineering
Chapter 3: Anatomy of the Context Window
Section: Context Foundations

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/anatomy-of-the-context-window

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

def n_tokens(text: str) -> int:
    return len(enc.encode(text))

system = "You are a support agent. Refuse to discuss competitors..."
print(n_tokens(system))        # -> e.g. 248
print(n_tokens("How do I get a refund?"))  # -> 6
