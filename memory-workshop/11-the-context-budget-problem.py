"""
Memory in AI Systems
Chapter 11: The Context Budget Problem
Section: Context Engineering

Read this chapter: https://books.vizuara.ai/read/memory-workshop/the-context-budget-problem

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
B = 8000                     # the fixed context window, in tokens

# fixed overhead you almost always pay
system_prompt   = 1000       # persona + rules
tool_schemas    = 800        # what the model is allowed to call

# what's left to split between knowledge, memory, and the current turn
remaining = B - system_prompt - tool_schemas      # 8000 - 1800 = 6200

current_turn    = 200        # the user's actual question, always kept
budget_for_context = remaining - current_turn      # 6000 tokens to ALLOCATE

# spend the 6000 deliberately — not "everything", but the best few things
recent_buffer   = 1500       # last few turns, verbatim   (short-term memory)
recalled_facts  = 1500       # top-k long-term memories about THIS user
retrieved_docs  = 1500       # top-k knowledge chunks for THIS query
#                 ~1500 held in reserve as safety margin, NOT spent
