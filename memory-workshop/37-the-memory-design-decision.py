"""
Memory in AI Systems
Chapter 37: The Memory Design Decision
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/memory-workshop/the-memory-design-decision

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
system_prompt = None  # TODO: returns the instruction layer - see ch.8: https://books.vizuara.ai/read/memory-workshop/prompts-as-context
tool_schemas = None   # TODO: returns tool schemas for this turn - see ch.10: https://books.vizuara.ai/read/memory-workshop/tools-as-context
memory = None         # TODO: a mem0 Memory(). Introduced in ch.31: https://books.vizuara.ai/read/memory-workshop/introducing-mem0
render = None         # TODO: format retrieved memories into context messages
knowledge = None      # TODO: a document store - see ch.9: https://books.vizuara.ai/read/memory-workshop/knowledge-as-context
buffer = None         # TODO: a BufferMemory instance from ch.26: https://books.vizuara.ai/read/memory-workshop/coding-buffer-memory
trim_to = None        # TODO: drop oldest-first until ctx fits - see ch.11: https://books.vizuara.ai/read/memory-workshop/the-context-budget-problem
# --- end resolved names ---

# --- block 1 ---
def build_context(user_msg, user_id, budget=8000):
    reserve = 1500                          # keep room for the reply
    ctx = []
    ctx += system_prompt()                  # 1. the frame — always
    ctx += tool_schemas(relevant_to=user_msg)  # 2. only tools this turn needs
    memories = memory.search(user_msg, user_id=user_id, limit=5)  # 3. READ long-term
    ctx += render(memories)                 #    retrieved, per-user, on-target
    ctx += knowledge.retrieve(user_msg, k=2)   # 4. grounding docs
    ctx += buffer.last(n=6)                 # 5. recent turns, verbatim
    ctx += user_msg                         # 6. the thing we're answering
    return trim_to(ctx, budget - reserve)   # 7. enforce the budget, oldest-first
