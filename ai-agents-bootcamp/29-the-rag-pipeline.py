"""
AI Agents Bootcamp
Chapter 29: The RAG Pipeline: Chunk, Embed, Retrieve, Generate
Section: Retrieval: RAG and Agentic RAG

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/the-rag-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import llm   # the chat model defined in Chapter 17

top_k = []          # TODO: the chunks your retriever returned for this question.
user_question = ""  # TODO: the question you are answering.
# --- end fixups ---

# --- block 1 ---
context = "\n\n".join(chunk.text for chunk in top_k)   # the 3 retrieved passages

prompt = f"""Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question: {user_question}
Answer:"""

response = llm.generate(prompt)
