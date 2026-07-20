"""
AI Context Engineering
Chapter 29: Compress and Isolate Lab
Section: Compress and Isolate

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/compress-isolate-lab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
history = load_transcript("session_5_support.json")   # 10 turns

raw_tokens = count_tokens(render(history))
print(raw_tokens)        # -> 21,847

# --- block 2 ---
SUMMARIZE = "Summarize the conversation so far. Preserve every order \
number, decision, dollar amount, and open action item verbatim."

summary = llm(SUMMARIZE + render(history[:-1]))   # a cheap call
compressed = summary + render(history[-1:])       # summary + latest turn

# --- block 3 ---
comp_tokens = count_tokens(compressed)
print(comp_tokens)                       # -> 1,930
print(raw_tokens / comp_tokens)          # -> 11.3x

# --- block 4 ---
q = "What refund did we approve, and for which order?"

ans_raw  = llm(render(history) + q)     # 21,847-token context
ans_comp = llm(compressed + q)          # 1,930-token context

print(ans_raw)   # "Order #A-4471: full refund approved, minus a 10% restocking fee."
print(ans_comp)  # "Order #A-4471: full refund approved, minus a 10% restocking fee."

# --- block 5 ---
# the sub-agent works in its OWN window
sub_ctx   = policy_docs                     # ~6,000 tokens, isolated
sub_answer = sub_agent(sub_ctx + "electronics refund policy?")
print(count_tokens(sub_answer))             # -> 42 tokens

# only the 42-token digest crosses back into the orchestrator
main_ctx += sub_answer
