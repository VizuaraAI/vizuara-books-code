"""
Memory in AI Systems
Chapter 9: Knowledge: Grounding in External Facts
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/memory-workshop/knowledge-as-context

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
store = None   # TODO: a searchable chunk store. Coded in ch.28: https://books.vizuara.ai/read/memory-workshop/coding-a-vector-memory-store
query = ""     # TODO: the user's question for this turn
llm = None     # TODO: your llm(messages) primitive. Defined in ch.25: https://books.vizuara.ai/read/memory-workshop/project-setup
# --- end resolved names ---

# --- block 1 ---
system = "You answer using ONLY the policy below. If it is not covered, say so."
policy = open("refund_policy.txt").read()   # ~300 tokens
user   = "Can I return opened software?"

context = [
    {"role": "system",  "content": system + "\n\nPOLICY:\n" + policy},
    {"role": "user",    "content": user},
]

# --- block 2 ---
hits = store.search(query, top_k=1)          # [chunk A]
knowledge = "\n\n".join(h.text for h in hits)

context = [
    {"role": "system", "content": "Answer using ONLY the sources below.\n\n" + knowledge},
    {"role": "user",   "content": query},
]
answer = llm(context)
