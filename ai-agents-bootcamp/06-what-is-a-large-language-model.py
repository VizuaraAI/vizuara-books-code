"""
AI Agents Bootcamp
Chapter 6: What Is a Large Language Model?
Section: The Engine: Large Language Models

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/what-is-a-large-language-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from numpy import argmax

END = None  # TODO: your tokenizer's end-of-sequence token id.
# --- end fixups ---

# --- block 1 ---
def generate(prompt_tokens, model, max_new=50):
    tokens = list(prompt_tokens)
    for _ in range(max_new):
        probs = model(tokens)        # (vocab_size,) — one prob per possible next token
        next_token = argmax(probs)   # greedy: take the most likely
        tokens.append(next_token)    # glue it on and go around again
        if next_token == END:
            break
    return tokens
