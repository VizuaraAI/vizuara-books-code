"""
AI Context Engineering
Chapter 33: Building Memory with Retrieval
Section: Memory Architectures

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/building-memory-with-retrieval

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
memory = VectorStore()          # the same index type you built for RAG

def remember(turn_text):
    # 1. WRITE: distill the turn into 0+ durable facts (a cheap model call)
    facts = extract_facts(turn_text)      # e.g. ["user is vegetarian"]
    for f in facts:
        memory.add(text=f, vector=embed(f))   # store fact + its embedding

def recall(query, k=3):
    # 2. SELECT: embed the query, take top-k memories by cosine
    hits = memory.search(vector=embed(query), k=k)
    return [h.text for h in hits]

def answer(user_msg):
    facts = recall(user_msg)              # e.g. ["user is vegetarian", "hates coriander"]
    context = format_memories(facts) + user_msg   # 3. RECALL: inject, then generate
    reply = model(context)
    remember(user_msg)                    # write anything new the turn revealed
    return reply
