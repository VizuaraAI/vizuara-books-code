"""
Memory in AI Systems
Chapter 26: Coding Buffer Memory from Scratch
Section: Coding Memory Layers from Scratch

Read this chapter: https://books.vizuara.ai/read/memory-workshop/coding-buffer-memory

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
class BufferMemory:
    def __init__(self, max_turns=6):
        self.max_turns = max_turns      # how many (user+assistant) turns to keep
        self.messages = []              # list of {"role", "content"} dicts

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        self._trim()                    # slide the window after every add

    def _trim(self):
        # one turn = 2 messages (a user msg + an assistant reply)
        max_messages = self.max_turns * 2
        if len(self.messages) > max_messages:
            # drop from the FRONT (oldest) until we fit
            self.messages = self.messages[-max_messages:]

    def get(self):
        return self.messages            # the current window, oldest → newest

# --- block 2 ---
SYSTEM = {"role": "system", "content": "You are a friendly assistant."}
memory = BufferMemory(max_turns=6)

while True:
    user_text = input("you > ")
    if user_text.strip() == "/quit":
        break

    memory.add("user", user_text)                 # WRITE the user turn
    messages = [SYSTEM] + memory.get()            # ASSEMBLE: prompt + window
    reply = llm(messages)                         # GENERATE
    memory.add("assistant", reply)                # WRITE the reply back
    print("bot >", reply)

# --- block 3 ---
def _trim(self):
    def est_tokens(msgs):
        return sum(len(m["content"]) for m in msgs) // 4   # ≈ 4 chars/token

    while len(self.messages) > 2 and est_tokens(self.messages) > self.token_budget:
        self.messages = self.messages[2:]   # drop the oldest full turn
