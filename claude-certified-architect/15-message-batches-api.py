"""
Claude Certified Architect (CCAF)
Chapter 15: The Message Batches API
Section: Batching and the Extraction Pipeline Lab

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/message-batches-api

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from anthropic import Anthropic

client = Anthropic()

# 1. Build one request per document, each tagged with a custom_id.
requests = [
    {
        "custom_id": f"doc-{i}",
        "params": {
            "model": "claude-sonnet-4-5",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": doc_text}],
        },
    }
    for i, doc_text in enumerate(documents)
]

# 2. Submit the whole bundle in ONE call. Returns immediately with a batch id.
batch = client.messages.batches.create(requests=requests)

# 3. Later — poll until it's done (this is the asynchronous part).
status = client.messages.batches.retrieve(batch.id)
# status.processing_status moves: "in_progress" -> "ended"

# 4. When ended, stream the results and re-pair them by custom_id.
for result in client.messages.batches.results(batch.id):
    doc_id = result.custom_id            # match back to the input
    if result.result.type == "succeeded":
        handle(doc_id, result.result.message)
    else:
        record_failure(doc_id, result.result)   # partial results are fine
