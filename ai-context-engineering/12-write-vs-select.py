"""
AI Context Engineering
Chapter 12: Write vs Select: Two Halves of Knowledge Injection
Section: Write and Select: RAG

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/write-vs-select

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
store = MemoryStore()                      # the durable place, outside the window

# ---- WRITE: earlier call(s), context leaves the window ----
store.write("son: Arjun, birthday March 3")   # persist a fact; costs 0 window tokens now
store.write("allergic to penicillin")

# ---- SELECT: this call, only the relevant slice comes back ----
query   = "what should I get my kid, and when?"
facts   = store.select(query, k=3)         # semantic match → the k most relevant items
window  = system_prompt + facts + query    # assemble the context for THIS call
answer  = model(window)                     # the model sees Arjun as if it always knew
