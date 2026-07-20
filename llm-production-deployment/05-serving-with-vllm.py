"""
LLM Production & Deployment
Chapter 5: Serving with vLLM
Section: Foundations of Language AI

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/serving-with-vllm

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from vllm import LLM, SamplingParams

# same model family as the previous chapter — vLLM manages the KV cache for you
llm = LLM(model="microsoft/phi-2")

params = SamplingParams(temperature=0.7, max_tokens=128)

# hand it a LIST of prompts — vLLM batches them across the GPU itself
prompts = ["Explain KV caching in one line.",
           "Summarize this ticket: ...",
           "Translate 'good morning' to French."]

outputs = llm.generate(prompts, params)
for out in outputs:
    print(out.outputs[0].text)

# --- block 2 ---
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="not-needed")

resp = client.chat.completions.create(
    model="microsoft/phi-2",
    messages=[{"role": "user", "content": "Explain KV caching in one line."}],
)
print(resp.choices[0].message.content)
