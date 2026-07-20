"""
Memory in AI Systems - shared definitions from earlier chapters

Some chapters use a name that an EARLIER chapter defined and did not repeat.
Those definitions are collected here so the per-chapter files can import them
instead of failing a static check.

Every definition below is COPIED VERBATIM from the chapter named above it.
Nothing in this file is invented.

Book: https://books.vizuara.ai/read/memory-workshop
"""

# --- Chapter 25: Project Setup: A Bare LLM Loop, block 1 ---
# https://books.vizuara.ai/read/memory-workshop/project-setup
from openai import OpenAI
client = OpenAI()

def llm(messages):
    # messages: a list of {"role", "content"} dicts
    # returns: one assistant message (a string)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    return resp.choices[0].message.content

# --- Chapter 25: Project Setup: A Bare LLM Loop, block 2 ---
# https://books.vizuara.ai/read/memory-workshop/project-setup
SYSTEM = {"role": "system", "content": "You are a friendly assistant."}

# --- Chapter 27: Coding Summary Memory from Scratch, block 4 ---
# https://books.vizuara.ai/read/memory-workshop/coding-summary-memory
# Chapter 27 names this SYSTEM too, but as a plain string rather than chapter
# 25's message dict. Both spellings are used by later chapters, so both are
# kept here under distinct names.
SYSTEM_TUTOR = "You are a friendly, concise tutor."

# --- Chapter 21: Retrieval-Augmented Generation (RAG), block 1 ---
# https://books.vizuara.ai/read/memory-workshop/retrieval-augmented-generation
def build_prompt(query, retrieved_chunks):
    context = "\n".join(f"- {c}" for c in retrieved_chunks)
    return (
        "Answer using ONLY the context below. "
        "If the answer isn't there, say you don't know.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}"
    )
