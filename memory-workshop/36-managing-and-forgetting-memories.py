"""
Memory in AI Systems
Chapter 36: Managing and Forgetting Memories
Section: Building with Mem0

Read this chapter: https://books.vizuara.ai/read/memory-workshop/managing-and-forgetting-memories

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
redundant_ids = []  # TODO: the duplicate memory ids your clustering step found
# --- end resolved names ---

# --- block 1 ---
from mem0 import Memory

m = Memory()

# find the stale fact
hits = m.search("skill level", user_id="learner_42")
# hits -> [{'id': 'a1b2', 'memory': 'user is a Python beginner', ...}]

# option A: correct it in place
m.update(memory_id="a1b2", data="user is at an intermediate Python level")

# option B: let add() reconcile it for you
m.add("I'm comfortable with intermediate stuff now",
      user_id="learner_42")   # Mem0 detects the conflict and UPDATES a1b2

# --- block 2 ---
mems = m.get_all(user_id="learner_42")
# ... cluster by cosine similarity, keep one representative per cluster ...
for dup_id in redundant_ids:
    m.delete(memory_id=dup_id)     # collapse the duplicates

# --- block 3 ---
import time

def is_live(mem, now, ttl_days):
    age_days = (now - mem["created_at"]) / 86400
    return age_days <= ttl_days

# ephemeral facts expire; durable facts don't
TTL = {"logistics": 14, "preference": None, "skill_level": None}
