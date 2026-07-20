"""
Generative AI Fundamentals
Chapter 6: Running an LLM on Your Own Computer
Section: Your First Hands-On LLM Projects

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/running-an-llm-on-your-own-computer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from llama_cpp import Llama

# Point at a local .gguf file — nothing here touches the network.
llm = Llama(
    model_path="./llama-3.2-3b-instruct-Q4_K_M.gguf",
    n_ctx=2048,        # context window: max tokens it can attend over
    n_threads=8,       # CPU threads to parallelize across
)

out = llm(
    "Explain gravity to a five-year-old.",
    max_tokens=128,    # how many tokens to generate before stopping
    temperature=0.7,   # sampling randomness — recall the previous chapter
    top_p=0.9,         # nucleus sampling cutoff
)

print(out["choices"][0]["text"])
