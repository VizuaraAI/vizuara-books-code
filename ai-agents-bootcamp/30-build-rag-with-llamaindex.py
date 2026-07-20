"""
AI Agents Bootcamp
Chapter 30: Build a RAG System with LlamaIndex
Section: Retrieval: RAG and Agentic RAG

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/build-rag-with-llamaindex

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()   # 1. read the PDF
index = VectorStoreIndex.from_documents(documents)       # 2. chunk + embed + store
query_engine = index.as_query_engine()                   # 3. build the retriever+LLM
response = query_engine.query(                           # 4. retrieve + generate
    "What was the company's revenue in 2023?"
)
print(response)

# --- block 2 ---
response = query_engine.query("What was the company's revenue in 2023?")

print(response)                                  # the answer
for node in response.source_nodes:               # the receipt
    print(f"  score={node.score:.2f}  page={node.metadata.get('page_label')}")
    print(f"  {node.text[:120]}...")
