"""
AI Context Engineering
Chapter 31: Short-Term vs Long-Term Memory
Section: Memory Architectures

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/short-term-vs-long-term-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# short-term memory = the live message list the model sees this call
window = [...]                       # volatile: discarded when the session ends

# long-term memory = a durable store recalled later by SELECT (see RAG chapters)
store = MemoryStore("ana.db")        # a file / row / vector index

def graduate(window, store):
    # policied WRITE: keep only durable, reusable facts — not the whole transcript
    for fact in extract_candidate_facts(window):
        if fact.durable and fact.reusable:
            store.upsert(fact)        # e.g. "Ana → package_manager=pnpm"

def recall(query, store, k=5):
    # SELECT: pull the few relevant memories back into the next window
    return store.search(query, top_k=k)
