"""
LLM Production & Deployment
Chapter 7: Throughput: vLLM vs HuggingFace
Section: Efficient Inference at Scale

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/throughput-vllm-vs-huggingface

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
MODEL = None     # TODO: the model handle being benchmarked (e.g. the
#                  "microsoft/phi-2" checkpoint used in Chapters 4-5).
messages = None  # TODO: the list of input texts to classify - your own data.
prompt = None    # TODO: builds the prompt string for one message.
parse = None     # TODO: turns one generation back into a label.
# --- end fixups ---

# --- block 1 ---
# Contender 1: raw HuggingFace pipeline — the naive loop
from transformers import pipeline
clf = pipeline("text-generation", model=MODEL, device=0)

labels = []
for msg in messages:                       # <-- one at a time
    out = clf(prompt(msg), max_new_tokens=1)
    labels.append(parse(out))

# --- block 2 ---
# Contender 2: vLLM — hand it the whole list at once
from vllm import LLM, SamplingParams
llm = LLM(model=MODEL)
params = SamplingParams(max_tokens=1)

prompts = [prompt(m) for m in messages]    # <-- all of them
outs = llm.generate(prompts, params)       # vLLM schedules them internally
labels = [parse(o) for o in outs]
