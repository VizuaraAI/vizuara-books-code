"""
AI Agents Bootcamp
Chapter 15: Generative Agents and the Idea of Memory
Section: Reasoning, Tools, and the Agent Loop

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/generative-agents-and-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
memory_stream = [
  {"text": "Isabella is setting up the Valentine's party at Hobbs Cafe",
   "created": "2023-02-13 16:00", "last_accessed": "2023-02-13 16:00",
   "importance": 8},
  {"text": "The desk in Isabella's room is idle",
   "created": "2023-02-13 16:02", "last_accessed": "2023-02-13 16:02",
   "importance": 1},
  # ... thousands more, append-only
]

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# It is the retrieval-scoring formula from the Generative Agents paper, written
# out as maths (the trailing "(1) (1) (1)" line labels the paper's weights).
# None of the six names are values the chapter ever creates.
# score = w_recency * recency + w_importance * importance + w_relevance * relevance
# #         (1)                   (1)                          (1)   in the paper
