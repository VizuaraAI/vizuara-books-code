"""
Build a Mini ClawdBot from Scratch
Chapter 17: RAG vs Memory: When to Use Which
Section: Memory and RAG

Read this chapter: https://books.vizuara.ai/read/mini-clawdbot-from-scratch/rag-vs-memory-when-to-use-which

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# both fire before the LLM call — parallel, not either/or
facts    = memory.search(user_id=user)          # semantic: "what is true about this person"
messages = rag.query(embed(user_text), k=5)     # episodic: "what was said, most similar to now"

prompt = system_prompt + facts + messages + history + user_text
reply  = llm(prompt)                            # the model sees one merged context
