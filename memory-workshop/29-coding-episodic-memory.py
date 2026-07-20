"""
Memory in AI Systems
Chapter 29: Coding Episodic Memory from Scratch
Section: Coding Memory Layers from Scratch

Read this chapter: https://books.vizuara.ai/read/memory-workshop/coding-episodic-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
from datetime import timedelta
from context import llm, SYSTEM  # ch.25: https://books.vizuara.ai/read/memory-workshop/project-setup

embed = None  # TODO: text -> unit-norm vector. Passed into VectorMemory in ch.28: https://books.vizuara.ai/read/memory-workshop/coding-a-vector-memory-store
# --- end resolved names ---

# --- block 1 ---
import numpy as np
from datetime import datetime, timezone

def make_event(user_id, content, kind="turn"):
    return {
        "user_id": user_id,                              # WHO
        "kind": kind,                                    # what type: "turn", "struggle", ...
        "content": content,                              # WHAT — plain text, verbatim
        "ts": datetime.now(timezone.utc),               # WHEN — a real datetime, sortable
        "vec": embed(content),                           # the embedding, computed ONCE, now
    }

# --- block 2 ---
class EpisodicMemory:
    def __init__(self):
        self.episodes = []                               # the log: oldest first

    def remember(self, user_id, content, kind="turn"):
        e = make_event(user_id, content, kind)
        self.episodes.append(e)                          # only ever grows
        return e

# --- block 3 ---
    def recent(self, user_id, k=5):
        mine = [e for e in self.episodes if e["user_id"] == user_id]
        mine.sort(key=lambda e: e["ts"])
        return mine[-k:]                                 # last k by time

# --- block 4 ---
    def relevant(self, user_id, query, k=3):
        q = embed(query)                                 # embed the query ONCE
        mine = [e for e in self.episodes if e["user_id"] == user_id]
        scored = [(float(np.dot(q, e["vec"])), e) for e in mine]   # cosine, normalized
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [e for _, e in scored[:k]]                # top-k by similarity

# --- block 5 ---
    def recall(self, user_id, query, k=3, within_days=None):
        mine = [e for e in self.episodes if e["user_id"] == user_id]
        if within_days is not None:
            cutoff = datetime.now(timezone.utc) - timedelta(days=within_days)
            mine = [e for e in mine if e["ts"] >= cutoff]     # time gate FIRST
        q = embed(query)
        scored = sorted(mine, key=lambda e: float(np.dot(q, e["vec"])), reverse=True)
        return scored[:k]

# --- block 6 ---
def episodic_digest(mem, user_id, query):
    hits = {id(e): e for e in mem.recent(user_id, k=2)}          # arc
    hits.update({id(e): e for e in mem.relevant(user_id, query, k=2)})  # topic
    events = sorted(hits.values(), key=lambda e: e["ts"])
    lines = [f'- {e["ts"]:%b %d}: {e["content"]}' for e in events]
    return "Relevant history:\n" + "\n".join(lines)

# --- block 7 ---
mem = EpisodicMemory()
history = [SYSTEM]

while True:
    user_text = input("you > ")
    if user_text.strip() == "/quit":
        break
    digest = episodic_digest(mem, "u_42", user_text)          # READ (recall)
    turn = [SYSTEM, {"role": "system", "content": digest},    # AUGMENT
            {"role": "user", "content": user_text}]
    reply = llm(turn)                                          # GENERATE
    mem.remember("u_42", user_text, kind="turn")              # WRITE the event back
    print("bot >", reply)
