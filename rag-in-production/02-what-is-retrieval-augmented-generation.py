"""
RAG in Production
Chapter 2: What Is Retrieval-Augmented Generation?
Section: RAG Foundations

Read this chapter: https://books.vizuara.ai/read/rag-in-production/what-is-retrieval-augmented-generation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# The chapter names its retrieved chunks C1/C2/C3 in prose, but the code
# block below never defines them.
C2 = None  # TODO: the retrieved chunk text - see https://books.vizuara.ai/read/rag-in-production/what-is-retrieval-augmented-generation

# --- block 1 ---
prompt = f"""Answer the question using ONLY the context below.
If the context does not contain the answer, say "I don't know."
Cite the source chunk in brackets.

Context:
[C2] {C2}

Question: How much vacation do I get?
"""
