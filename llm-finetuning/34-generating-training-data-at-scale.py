"""
LLM Finetuning
Chapter 34: Generating Training Data at Scale
Section: Research Projects

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/generating-training-data-at-scale

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()
sem = asyncio.Semaphore(50)          # at most 50 calls in flight

async def generate_one(prompt: str) -> str:
    async with sem:                  # wait here if 50 are already running
        resp = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.0,         # HIGH temp = diverse examples
        )
        return resp.choices[0].message.content

async def generate_all(prompts: list[str]) -> list[str]:
    tasks = [generate_one(p) for p in prompts]
    return await asyncio.gather(*tasks)   # launch all, collect in order

# --- block 2 ---
import random

def build_prompt() -> str:
    lo = random.randint(0, 900)
    length = random.choice([5, 7, 10])
    return (f"Continue this sequence with {length} more numbers, "
            f"comma-separated, starting near {lo}. Numbers only.")

# --- block 3 ---
async def generate_one(prompt: str, max_retries: int = 5) -> str | None:
    for attempt in range(max_retries):
        try:
            async with sem:
                resp = await client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=1.0,
                )
            return resp.choices[0].message.content
        except Exception:
            wait = 2 ** attempt + random.uniform(0, 1)   # 1s, 2s, 4s, 8s...
            await asyncio.sleep(wait)
    return None    # gave up after max_retries — caller filters these out
