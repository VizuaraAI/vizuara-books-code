"""
Memory in AI Systems
Chapter 4: Memory vs. Parameters: Where Knowledge Lives
Section: Why Memory Matters

Read this chapter: https://books.vizuara.ai/read/memory-workshop/memory-vs-parameters

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
memory = None   # TODO: a mem0 Memory(). Introduced in ch.31: https://books.vizuara.ai/read/memory-workshop/introducing-mem0
mem_id = None   # TODO: the id of a stored memory, as returned by the store
# --- end resolved names ---

# --- block 1 ---
memory.add("Priya is allergic to peanuts", user_id="priya")

# --- block 2 ---
memory.update(mem_id, "Priya is allergic to peanuts AND shellfish")
memory.delete(mem_id)   # or forgotten entirely
