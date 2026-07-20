"""
RAG in Production
Chapter 6: Ingestion Is the Hard Part
Section: Data Ingestion

Read this chapter: https://books.vizuara.ai/read/rag-in-production/ingestion-is-the-hard-part

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def sanity_check_page(text: str, page_num: int) -> list[str]:
    """Flag pages whose extracted text looks corrupt, before indexing."""
    warnings = []
    n_chars = len(text.strip())

    # Near-empty page → almost certainly a scanned image needing OCR.
    if n_chars < 50:
        warnings.append(f"page {page_num}: {n_chars} chars — likely scanned image, route to OCR")

    # Very high non-alphanumeric ratio → flattened table or decode garbage.
    if n_chars > 0:
        symbols = sum(1 for c in text if not (c.isalnum() or c.isspace()))
        if symbols / n_chars > 0.30:
            warnings.append(f"page {page_num}: {symbols/n_chars:.0%} symbols — possible table/decode garbage")

    # Broken words per line hint at column interleaving (very short 'words').
    tokens = text.split()
    if tokens:
        tiny = sum(1 for t in tokens if len(t) <= 2)
        if tiny / len(tokens) > 0.40:
            warnings.append(f"page {page_num}: {tiny/len(tokens):.0%} tiny tokens — possible column scramble")

    return warnings
