"""
Memory in AI Systems
Chapter 2: What Is Memory in an LLM?
Section: Why Memory Matters

Read this chapter: https://books.vizuara.ai/read/memory-workshop/what-is-memory-in-llms

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
model = None  # TODO: your chat model. The book builds a real one in ch.25: https://books.vizuara.ai/read/memory-workshop/project-setup
# --- end resolved names ---

# --- block 1 ---
# What the app actually sends on turn 2 — the FULL running transcript,
# not just the newest message. This replay IS the memory.
messages = [
    {"role": "user",      "content": "My name is Ravi and I'm allergic to peanuts."},
    {"role": "assistant", "content": "Nice to meet you, Ravi. I'll keep that in mind."},
    {"role": "user",      "content": "Can I eat this pad thai?"},   # the new turn
]
response = model(messages)   # now the model CAN see the allergy
