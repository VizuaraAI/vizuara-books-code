"""
Memory in AI Systems
Chapter 16: Hybrid Memory
Section: The Memory Taxonomy

Read this chapter: https://books.vizuara.ai/read/memory-workshop/hybrid-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
VectorStore = None     # TODO: a vector store class. Coded in ch.28 as VectorMemory: https://books.vizuara.ai/read/memory-workshop/coding-a-vector-memory-store
now = None             # TODO: a clock, e.g. datetime.now(timezone.utc) - see ch.15: https://books.vizuara.ai/read/memory-workshop/episodic-memory
llm_resummarize = None # TODO: fold old turns into the running summary - see ch.14: https://books.vizuara.ai/read/memory-workshop/summary-memory
# --- end resolved names ---

# --- block 1 ---
class HybridMemory:
    def __init__(self, buffer_turns=8, top_k=4):
        self.buffer = []            # recent turns, verbatim
        self.summary = ""           # rolling compressed history
        self.episodic = VectorStore()  # timestamped events, searchable
        self.buffer_turns = buffer_turns
        self.top_k = top_k

    def assemble_context(self, user_msg):        # READ path
        recalled = self.episodic.search(user_msg, k=self.top_k)
        return {
            "summary":  self.summary,            # older history, compressed
            "recalled": recalled,                # relevant distant events
            "buffer":   self.buffer,             # recent turns, verbatim
            "user":     user_msg,
        }

    def update(self, user_msg, reply):           # WRITE path
        self.buffer.append((user_msg, reply))
        self.episodic.add(event=(user_msg, reply), ts=now())
        if len(self.buffer) > self.buffer_turns:     # overflow → summarize
            oldest = self.buffer.pop(0)
            self.summary = llm_resummarize(self.summary, oldest)
