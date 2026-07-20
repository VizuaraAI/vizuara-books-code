"""
RAG in Production
Chapter 8: Cleaning, Normalizing, and Metadata
Section: Data Ingestion

Read this chapter: https://books.vizuara.ai/read/rag-in-production/cleaning-normalizing-and-metadata

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
raw = None                  # TODO: raw extracted text from a loader - see chapter 7
clean_and_normalize = None  # TODO: the chapter's prose name for the cleaning step; the
                            # runnable version in this chapter is `clean` (block 1 below)

# --- block 1 ---
import ftfy, re

def clean(text: str) -> str:
    text = ftfy.fix_text(text)                    # repair mojibake, ligatures
    text = re.sub(r"[ \t]+", " ", text)           # collapse spaces/tabs
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)  # un-wrap single newlines
    text = re.sub(r"\n{3,}", "\n\n", text)        # cap blank runs at one
    return text.strip()

# --- block 2 ---
document = {
    "text": clean_and_normalize(raw),
    "metadata": {
        "source": "/docs/refund_policy.pdf",
        "title": "Customer Refund Policy",
        "section": "3.2 Refund Policy",   # nearest preceding heading
        "year": 2024,                      # typed int, for filtering
        "created_at": "2024-03-01",
        "ingested_at": "2026-07-06",
    },
}
