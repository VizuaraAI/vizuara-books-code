"""
AI Context Engineering
Chapter 34: Memory Architectures Lab
Section: Memory Architectures

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/memory-architectures-lab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import json

# --- block 1 ---
messages = []

def chat(user_text):
    messages.append({"role": "user", "content": user_text})
    reply = llm(messages)                      # whole list resent every call
    messages.append({"role": "assistant", "content": reply})
    return reply

chat("I'm Priya. I use pytest and I hate mocked tests.")
chat("What testing library do I use?")   # -> "You use pytest." looks like memory!

# --- block 2 ---
EXTRACT = """From the exchange below, extract 0-3 durable facts about the
USER worth remembering across sessions (preferences, identity, project
details). Ignore small talk. Return a JSON list of short strings, or []."""

def write_memories(user_text, reply):
    facts = llm(EXTRACT + f"\nUSER: {user_text}\nASSISTANT: {reply}")
    for fact in json.loads(facts):
        store.add(fact)          # persisted to disk, not RAM

# --- block 3 ---
def recall(query, k=3):
    q = embed(query)
    scored = [(cosine(q, m.vec), m.text) for m in store.all()]
    scored.sort(reverse=True)
    return [text for _, text in scored[:k]]

# --- block 4 ---
def assemble(user_text):
    memories = recall(user_text)                       # top-k from disk
    system = "You are a helpful assistant.\n\nWhat you know about the user:\n"
    system += "\n".join(f"- {m}" for m in memories) if memories else "(nothing yet)"
    return [{"role": "system", "content": system}] + short_term + \
           [{"role": "user", "content": user_text}]

# --- block 5 ---
# ---- Runtime A ----
reply = chat("I'm Priya. I use pytest and I hate mocked tests.")
# write_memories() fired: 3 facts now on disk in memory_store.json

# ====== Runtime→Restart: RAM wiped, short_term = [] ======

# ---- Runtime B (cold boot) ----
store = MemoryStore.load("memory_store.json")     # facts reloaded from DISK
chat("Hi, how should I write tests for my project?")
# -> "Hi Priya! Since you use pytest and dislike mocked tests, here's a
#     real-fixture example..."

# --- block 6 ---
store.add("User's project is in Django")   # extracted in error, turn 3

# ...20 runs later, user has moved to FastAPI, but every recall still surfaces:
recall("how do I add an endpoint?")   # -> [..., "User's project is in Django"]
