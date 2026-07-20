"""
Memory in AI Systems
Chapter 19: Why Retrieval? The Recall Problem
Section: Retrieval and Knowledge

Read this chapter: https://books.vizuara.ai/read/memory-workshop/why-retrieval

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
system_prompt = ""  # TODO: the instruction layer for this agent - see ch.8: https://books.vizuara.ai/read/memory-workshop/prompts-as-context
# --- end resolved names ---

# --- block 1 ---
def answer_turn(query, memory_store, model, k=5):
    # 1. SEARCH the external store for the k most relevant memories
    relevant = memory_store.search(query, top_k=k)      # e.g. 5 short notes

    # 2. AUGMENT: assemble a small context from only what we retrieved
    context = system_prompt + "\n".join(relevant) + query

    # 3. GENERATE from that small, focused context
    return model(context)
