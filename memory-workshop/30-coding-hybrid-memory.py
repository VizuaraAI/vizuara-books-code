"""
Memory in AI Systems
Chapter 30: Assembling a Hybrid Memory Layer
Section: Coding Memory Layers from Scratch

Read this chapter: https://books.vizuara.ai/read/memory-workshop/coding-hybrid-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
from context import llm                        # ch.25: https://books.vizuara.ai/read/memory-workshop/project-setup
from context import SYSTEM_TUTOR as SYSTEM     # ch.27: https://books.vizuara.ai/read/memory-workshop/coding-summary-memory

buffer = None        # TODO: a BufferMemory instance from ch.26: https://books.vizuara.ai/read/memory-workshop/coding-buffer-memory
summarizer = None    # TODO: a SummaryMemory instance from ch.27: https://books.vizuara.ai/read/memory-workshop/coding-summary-memory
vector_store = None  # TODO: a VectorMemory instance from ch.28: https://books.vizuara.ai/read/memory-workshop/coding-a-vector-memory-store
# --- end resolved names ---

# --- block 1 ---
class HybridMemory:
    def __init__(self, buffer, summarizer, vector_store,
                 k=3, buffer_turns=2, summary_max_tokens=250):
        self.buffer = buffer            # last-N verbatim turns
        self.summary = summarizer       # running compressed gist
        self.vectors = vector_store     # embed + top-k search
        self.k = k
        self.buffer_turns = buffer_turns

    def read(self, query: str) -> str:
        """Assemble the memory block for THIS turn's query."""
        ...

    def write(self, user_msg: str, assistant_msg: str) -> None:
        """Persist this exchange across all three stores."""
        ...

# --- block 2 ---
def read(self, query: str) -> str:
    # 1. retrieve: search long-term store for facts relevant to THIS query
    hits = self.vectors.search(query, top_k=self.k)   # cosine similarity, top-k
    retrieved = "\n".join(f"- {h.text}" for h in hits)

    # 2. summary: the running gist of older turns
    gist = self.summary.text()                         # already token-capped

    # 3. buffer: the last few turns, verbatim
    recent = self.buffer.last(self.buffer_turns)       # e.g. last 2 exchanges

    return (
        f"## Relevant memories\n{retrieved}\n\n"
        f"## Conversation summary\n{gist}\n\n"
        f"## Recent turns\n{recent}"
    )

# --- block 3 ---
def write(self, user_msg: str, assistant_msg: str) -> None:
    exchange = f"User: {user_msg}\nAssistant: {assistant_msg}"

    # 1. long-term: embed and store for later semantic search
    self.vectors.add(exchange)

    # 2. short-term: push onto the buffer; capture what overflows
    overflow = self.buffer.push(exchange)              # returns evicted turns, if any

    # 3. if the buffer overflowed, compress the evicted turns INTO the summary
    if overflow:
        self.summary.update(overflow)                  # LLM folds it into the gist

# --- block 4 ---
mem = HybridMemory(buffer, summarizer, vector_store, k=3, buffer_turns=2)

def chat(user_msg: str) -> str:
    context = mem.read(user_msg)                        # READ  → assemble
    prompt  = f"{SYSTEM}\n\n{context}\n\nUser: {user_msg}"
    reply   = llm(prompt)                               # GENERATE
    mem.write(user_msg, reply)                          # WRITE → persist
    return reply
