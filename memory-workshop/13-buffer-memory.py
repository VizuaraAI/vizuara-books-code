"""
Memory in AI Systems
Chapter 13: Buffer Memory
Section: The Memory Taxonomy

Read this chapter: https://books.vizuara.ai/read/memory-workshop/buffer-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
model = None         # TODO: your chat model. Built in ch.25: https://books.vizuara.ai/read/memory-workshop/project-setup
count_tokens = None  # TODO: a tokenizer-backed len() for a message list
# --- end resolved names ---

# --- block 1 ---
buffer = []  # the memory. a list of {"role", "content"} messages.

def chat(user_text, system_prompt):
    buffer.append({"role": "user", "content": user_text})
    messages = [{"role": "system", "content": system_prompt}] + buffer
    reply = model(messages)            # the stateless call
    buffer.append({"role": "assistant", "content": reply})
    return reply

# --- block 2 ---
def trim(buffer, max_tokens=6000):
    while count_tokens(buffer) > max_tokens:
        buffer.pop(0)   # drop the oldest message
    return buffer
