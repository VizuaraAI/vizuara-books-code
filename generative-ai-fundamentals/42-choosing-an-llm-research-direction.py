"""
Generative AI Fundamentals
Chapter 42: Choosing an LLM Research Direction
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/choosing-an-llm-research-direction

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# the entire experiment, on paper before any code
systems  = ["baseline: bi-encoder top-5",
            "ours:     bi-encoder top-50 -> cross-encoder -> top-5"]
metric   = "faithfulness"          # RAGAS-style: is the answer supported by context?
dataset  = "200 held-out medical Q&A pairs"
control  = "same LLM, same prompt, same k=5 fed to the generator"  # only the reranker changes
