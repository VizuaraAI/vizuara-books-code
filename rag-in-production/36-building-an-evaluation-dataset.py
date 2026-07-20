"""
RAG in Production
Chapter 36: Building an Evaluation Dataset
Section: Evaluating RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/building-an-evaluation-dataset

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
GEN_PROMPT = """You are given ONE chunk from a company knowledge base.
Write a question that a real employee might ask, whose answer is
FULLY contained in this chunk. Then write the exact answer, using
only facts from the chunk. If the chunk is boilerplate or contains
no answerable fact, reply exactly: SKIP.

CHUNK (id={chunk_id}):
{chunk_text}

Return JSON: {{"question": "...", "answer": "...", "answerable": true}}"""

# --- block 2 ---
# golden_set.jsonl — one row per line, version-controlled, frozen
{"id": "q001", "question": "If my order arrived last Tuesday, how long do I still have to return it?",
 "reference": "You have 30 days from delivery to return an order.",
 "gold_chunk_ids": ["returns_policy#4"], "type": "factual"}
{"id": "q002", "question": "How do I export my data and delete my account in one go?",
 "reference": "Export from Settings → Data, then use Delete Account; export must finish first.",
 "gold_chunk_ids": ["data_policy#2", "account_policy#9"], "type": "multi_hop"}
{"id": "q003", "question": "What is your office's WiFi password?",
 "reference": "I don't know — that information is not in the provided documents.",
 "gold_chunk_ids": [], "type": "adversarial"}
