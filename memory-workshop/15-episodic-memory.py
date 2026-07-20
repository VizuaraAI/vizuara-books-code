"""
Memory in AI Systems
Chapter 15: Episodic Memory
Section: The Memory Taxonomy

Read this chapter: https://books.vizuara.ai/read/memory-workshop/episodic-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from datetime import datetime, timezone

def make_event(user_id, content, kind="turn"):
    return {
        "user_id": user_id,
        "kind": kind,
        "content": content,
        "ts": datetime.now(timezone.utc).isoformat(),
    }

episodes = []  # the log: just a list, oldest first
episodes.append(make_event("u_42", "learner mixes up mitosis and meiosis", "struggle"))

# --- block 2 ---
def recent(user_id, k=5):
    mine = [e for e in episodes if e["user_id"] == user_id]
    return sorted(mine, key=lambda e: e["ts"])[-k:]   # last k by time
