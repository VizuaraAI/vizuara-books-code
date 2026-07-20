"""
LLM Production & Deployment
Chapter 37: Finetuning Research: Subliminal Learning & RAFT
Section: Finetuning LLMs

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/finetuning-research-subliminal-and-raft

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
# The golden documents (D*) and their distractors are the reader's own corpus.
D_star_1 = D_star_2 = D_star_3 = None       # TODO: the golden document per row.
distractor_a = distractor_b = None          # TODO: distractor documents.
distractor_c = distractor_d = None
distractor_e = distractor_f = None
distractor_g = distractor_h = distractor_i = None
# --- end fixups ---

# --- block 1 ---
# Toy RAFT dataset construction (k=3 docs per row, p=0.75 golden-present)
raft_rows = [
    # golden PRESENT: model must CITE D* and reason to the answer
    {"q": "When did the dam open?",   "docs": [D_star_1, distractor_a, distractor_b],
     "answer": "##begin_quote## opened in 1936 ##end_quote## → The dam opened in 1936."},
    {"q": "Who wrote the report?",    "docs": [distractor_c, D_star_2, distractor_d],
     "answer": "##begin_quote## authored by R. Mehta ##end_quote## → R. Mehta wrote it."},
    {"q": "What is the capacity?",    "docs": [distractor_e, distractor_f, D_star_3],
     "answer": "##begin_quote## rated at 40 MW ##end_quote## → The capacity is 40 MW."},
    # golden ABSENT: only distractors, model must still answer from memory
    {"q": "Which river feeds it?",    "docs": [distractor_g, distractor_h, distractor_i],
     "answer": "The reservoir is fed by the Koyna river."},
]
# 3 of 4 rows include D* → p = 0.75. Every target reasons first, then answers.
