"""
RAG in Production
Chapter 9: Building a Robust Ingestion Pipeline
Section: Data Ingestion

Read this chapter: https://books.vizuara.ai/read/rag-in-production/building-a-robust-ingestion-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/building-a-robust-ingestion-pipeline
load = None                 # TODO: the loader router from chapter 7
EmptyExtract = None         # TODO: the pipeline's own exception type
clean_and_normalize = None  # TODO: the cleaning step from chapter 8 (`clean`)
build_metadata = None       # TODO: the metadata builder from chapter 8
sha256_of = None            # TODO: content hash of a file, for the manifest
discover = None             # TODO: walks a folder and yields source paths
chunk = None                # TODO: the chunker - "next section's job", see chapters 11-14
save_manifest = None        # TODO: persists the path -> hash manifest
build_report = None         # TODO: builds the run report shown in block 3

# --- block 1 ---
def process_one(path):
    raw = load(path)          # router from the loaders chapter
    if not raw.strip():       # empty extract = probably a scan
        raise EmptyExtract(path)
    text = clean_and_normalize(raw)
    meta = build_metadata(path)
    return {"text": text, "metadata": meta}

def ingest(paths):
    ok, dead = [], []
    for path in paths:
        try:
            ok.append(process_one(path))
        except Exception as e:                     # isolate!
            dead.append({"path": path, "error": repr(e)})
    return ok, dead

# --- block 2 ---
def plan(paths, manifest):
    now = {p: sha256_of(p) for p in paths}
    new     = [p for p in now if p not in manifest]
    changed = [p for p in now if p in manifest and now[p] != manifest[p]]
    deleted = [p for p in manifest if p not in now]
    unchanged = [p for p in now if manifest.get(p) == now[p]]
    return new, changed, deleted, unchanged, now

# --- block 3 ---
report = {
    "run_at":        "2026-07-06T02:00:00Z",
    "counts":        {"new": 20, "changed": 10, "deleted": 5,
                      "unchanged": 3965, "dead_letter": 19},
    "empty_extract_rate": 0.006,          # 6 in ~1000 — normal
    "chunks_written":     412,
    "dead_letter":  [{"path": ".../trunc.pdf", "error": "EmptyExtract"}],
}

# --- block 4 ---
def run_ingestion(folder, index, manifest):
    paths = discover(folder)
    new, changed, deleted, unchanged, hashes = plan(paths, manifest)

    for path in deleted + changed:            # delete-then-insert
        index.delete(where={"source": path})

    ok, dead = ingest(new + changed)          # isolate per file
    for doc in ok:
        chunks = chunk(doc)                   # next section's job
        index.upsert(chunks)

    save_manifest({p: hashes[p] for p in hashes
                   if p not in {d["path"] for d in dead}})   # only successes
    return build_report(new, changed, deleted, unchanged, dead)
