"""
LLM Finetuning
Chapter 37: Setting Up a RAFT Project
Section: Research Projects

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/raft-project-setup

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import random

# --- block 1 ---
def make_raft_example(golden_chunk, corpus, k=4, p_drop_golden=0.4, llm=generate):
    # 1. Ask a strong model to invent a question answerable from the golden chunk.
    q = llm(f"Write one question answered ONLY by this text:\n{golden_chunk.text}")

    # 2. Write a cited answer that quotes the golden chunk.
    a = llm(f"Answer using this text, quoting it with ##begin_quote##/##end_quote##:\n"
            f"Q: {q}\nText: {golden_chunk.text}")

    # 3. Sample k-1 distractors: topically-near but NON-answering chunks.
    distractors = sample_hard_distractors(golden_chunk, corpus, n=k-1)

    # 4. With probability p, DROP the golden doc entirely (train retrieval-failure robustness).
    if random.random() < p_drop_golden:
        context = shuffle(distractors)                 # golden removed
    else:
        context = shuffle([golden_chunk] + distractors)

    return format_as_finetune_example(q, context, a)
