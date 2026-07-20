"""
Memory in AI Systems
Chapter 22: RAG as a Long-Term Memory Engine
Section: Retrieval and Knowledge

Read this chapter: https://books.vizuara.ai/read/memory-workshop/rag-as-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
from context import build_prompt  # ch.21: https://books.vizuara.ai/read/memory-workshop/retrieval-augmented-generation

embed = None          # TODO: text -> vector. Passed into VectorMemory in ch.28: https://books.vizuara.ai/read/memory-workshop/coding-a-vector-memory-store
llm = None            # TODO: your llm(prompt) primitive. Defined in ch.25: https://books.vizuara.ai/read/memory-workshop/project-setup
extract_facts = None  # TODO: pull durable facts out of a turn (Mem0 does this for you in ch.31)
# --- end resolved names ---

# --- block 1 ---
def respond(user_id, message, store, buffer):
    # 1. READ — retrieve relevant long-term memories for THIS user
    q = embed(message)
    memories = store.search(q, user_id=user_id, k=5)   # top-k by cosine

    # 2. AUGMENT — assemble the four components within budget
    prompt = build_prompt(
        system="You are a patient tutor.",
        knowledge=None,
        memory=memories,            # <-- long-term, retrieved
        buffer=buffer.recent(6),    # <-- short-term, verbatim
        user_message=message,
    )

    # 3. GENERATE
    reply = llm(prompt)

    # 4. WRITE — extract durable facts and store them, scoped to the user
    for fact in extract_facts(message, reply):
        store.upsert(embed(fact), fact, user_id=user_id)  # add-or-update

    buffer.append(message, reply)
    return reply
