"""
LLM Production & Deployment
Chapter 4: Loading a Model with HuggingFace
Section: Foundations of Language AI

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/loading-a-model-with-huggingface

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    device_map="auto",        # put weights on GPU if one exists
    torch_dtype="auto",       # pick FP16/BF16 automatically
)

out = pipe(
    "Write a one-line explanation of what a GPU does:",
    max_new_tokens=40,
    do_sample=False,          # greedy: same output every time
)
print(out[0]["generated_text"])

# --- block 2 ---
out = pipe(
    "Write a haiku about GPUs:",
    max_new_tokens=40,
    do_sample=True,
    temperature=0.9,   # higher = flatter distribution = more surprising
    top_p=0.95,        # nucleus sampling: only the top tokens summing to 0.95
)
