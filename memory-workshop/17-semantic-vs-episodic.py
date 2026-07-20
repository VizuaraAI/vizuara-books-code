"""
Memory in AI Systems
Chapter 17: Semantic vs. Episodic: Facts vs. Events
Section: The Memory Taxonomy

Read this chapter: https://books.vizuara.ai/read/memory-workshop/semantic-vs-episodic

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import time

semantic = {}          # user_id -> {fact_text: fact_text}  (a SET, deduped)
episodic = []          # list of {user_id, t, event}        (a SEQUENCE)

def remember_fact(user_id, fact):
    # overwrite on dedupe key -> facts stay a current, non-contradictory set
    semantic.setdefault(user_id, {})[fact] = fact

def remember_event(user_id, event):
    # always append, never merge -> the timeline is preserved
    episodic.append({"user_id": user_id, "t": time.time(), "event": event})

def recall_facts(user_id):
    return list(semantic.get(user_id, {}).values())      # who they are

def recall_recent(user_id, n=3):
    hist = [e for e in episodic if e["user_id"] == user_id]
    return sorted(hist, key=lambda e: e["t"])[-n:]        # what just happened
