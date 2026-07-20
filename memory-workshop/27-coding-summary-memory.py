"""
Memory in AI Systems
Chapter 27: Coding Summary Memory from Scratch
Section: Coding Memory Layers from Scratch

Read this chapter: https://books.vizuara.ai/read/memory-workshop/coding-summary-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
from context import llm  # ch.25: https://books.vizuara.ai/read/memory-workshop/project-setup
# --- end resolved names ---

# --- block 1 ---
from collections import deque

class SummaryMemory:
    def __init__(self, llm, keep_recent=4):
        self.llm = llm                      # our stateless llm(messages) primitive
        self.summary = ""                   # the running summary (compressed past)
        self.recent = deque(maxlen=None)    # raw turns awaiting summarization
        self.keep_recent = keep_recent      # summarize once recent exceeds this

    def add_turn(self, user_msg, assistant_msg):
        self.recent.append({"role": "user", "content": user_msg})
        self.recent.append({"role": "assistant", "content": assistant_msg})
        if len(self.recent) > self.keep_recent * 2:   # *2: each turn = 2 messages
            self._compress()

# --- block 2 ---
    def _compress(self):
        new_lines = "\n".join(f"{m['role']}: {m['content']}" for m in self.recent)
        prompt = f"""You maintain a running summary of a conversation.
Given the CURRENT SUMMARY and the NEW LINES, produce an UPDATED SUMMARY
that folds in the new information. Keep durable facts about the user
(name, preferences, goals, decisions). Drop small talk. Stay under 80 words.

CURRENT SUMMARY:
{self.summary or "(none yet)"}

NEW LINES:
{new_lines}

UPDATED SUMMARY:"""
        self.summary = self.llm(
            [{"role": "user", "content": prompt}]
        ).strip()
        self.recent.clear()                 # raw turns are now folded in — drop them

# --- block 3 ---
    def assemble(self, system, user_msg):
        summary_note = (
            f"\n\nContext from earlier in this conversation:\n{self.summary}"
            if self.summary else ""
        )
        messages = [{"role": "system", "content": system + summary_note}]
        messages.extend(self.recent)                       # verbatim tail
        messages.append({"role": "user", "content": user_msg})
        return messages

# --- block 4 ---
mem = SummaryMemory(llm, keep_recent=4)
SYSTEM = "You are a friendly, concise tutor."

def chat(user_msg):
    messages = mem.assemble(SYSTEM, user_msg)
    reply = llm(messages)
    mem.add_turn(user_msg, reply)
    return reply
