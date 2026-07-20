"""
RAG in Production
Chapter 14: Choosing Chunk Size and Overlap
Section: Chunking

Read this chapter: https://books.vizuara.ai/read/rag-in-production/choosing-chunk-size-and-overlap

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/choosing-chunk-size-and-overlap
chunk_corpus = None  # TODO: chunks a corpus at a given size/overlap - see chapters 11-13
build_index = None   # TODO: builds a searchable index over chunk vectors - see chapter 20
overlaps = None      # TODO: true if two character spans overlap
corpus = None        # TODO: your own corpus of documents
eval_set = None      # TODO: your own labelled questions with gold spans - see chapter 36
embed = None         # TODO: your embedding function - see chapters 15-16

# --- block 1 ---
candidates = [
    {"size": 128, "overlap": 0},    # fine, no insurance
    {"size": 256, "overlap": 25},   # ~10% overlap
    {"size": 512, "overlap": 50},   # ~10% overlap  <- the usual default
    {"size": 512, "overlap": 100},  # ~20% overlap
    {"size": 1024, "overlap": 100}, # coarse, ~10% overlap
]

# --- block 2 ---
def evaluate(candidate, corpus, eval_set, embed, top_k=5):
    chunks = chunk_corpus(corpus, candidate["size"], candidate["overlap"])
    index  = build_index([embed(c.text) for c in chunks])   # same model every time
    hits = 0
    for q in eval_set:
        retrieved = index.search(embed(q.text), top_k)
        if any(overlaps(r.span, q.gold_span) for r in retrieved):
            hits += 1
    return hits / len(eval_set)      # Recall@k for this chunking

scores = {str(c): evaluate(c, corpus, eval_set, embed) for c in candidates}
