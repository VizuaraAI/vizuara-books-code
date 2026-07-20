"""
RAG in Production
Chapter 12: Recursive and Structure-Aware Chunking
Section: Chunking

Read this chapter: https://books.vizuara.ai/read/rag-in-production/recursive-and-structure-aware-chunking

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
document = None  # TODO: the document text to split - see https://books.vizuara.ai/read/rag-in-production/recursive-and-structure-aware-chunking

# --- block 1 ---
separators = ["\n\n", "\n", ". ", " ", ""]
#              paragraph  line  sentence word  character

# --- block 2 ---
markdown_separators = [
    "\n## ", "\n### ",     # headings first — strongest boundaries
    "\n\n", "\n",          # then paragraphs, then lines
    " ", "",               # then words, then characters
]

# --- block 3 ---
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,          # target size, in characters by default
    chunk_overlap=50,        # ~10% overlap, carried across boundaries
    separators=["\n\n", "\n", ". ", " ", ""],  # coarse → fine
)

chunks = splitter.split_text(document)
