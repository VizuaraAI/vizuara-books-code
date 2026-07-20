"""
Claude Certified Architect (CCAF)
Chapter 17: Lab: Structured Data Extraction Pipeline
Section: Batching and the Extraction Pipeline Lab

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/lab-structured-extraction-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
extract_ticket = {
    "name": "extract_ticket",
    "description": "Extract a structured record from one support email.",
    "input_schema": {
        "type": "object",
        "properties": {
            "category": {
                "type": "string",
                "enum": ["billing", "bug", "feature_request", "account", "other"]
            },
            "category_detail": {
                "type": ["string", "null"],
                "description": "Free text ONLY when category == 'other'; else null."
            },
            "severity": {"type": "string", "enum": ["low", "medium", "high", "urgent"]},
            "product":  {"type": ["string", "null"]},
            "order_id": {"type": ["string", "null"],
                         "description": "The order number if explicitly present, else null."}
        },
        "required": ["category", "severity", "product", "order_id"]
    }
}

# --- block 2 ---
import jsonschema

def extract_one(client, email, max_retries=2):
    messages = [{"role": "user", "content": email}]
    for attempt in range(max_retries + 1):
        resp = client.messages.create(
            model="claude-sonnet-4-5", max_tokens=1024,
            tools=[extract_ticket],
            tool_choice={"type": "tool", "name": "extract_ticket"},  # forced
            messages=messages,
        )
        block = next(b for b in resp.content if b.type == "tool_use")
        try:
            jsonschema.validate(block.input, extract_ticket["input_schema"])
            return block.input                       # clean record
        except jsonschema.ValidationError as e:
            messages += [
                {"role": "assistant", "content": resp.content},
                {"role": "user", "content": [{
                    "type": "tool_result", "tool_use_id": block.id,
                    "content": f"Validation failed: {e.message}. Fix and call again.",
                    "is_error": True,
                }]},
            ]
    return None                                       # exhausted → escalate

# --- block 3 ---
live, backlog = partition(emails, key=lambda e: human_is_waiting(e))

results = [extract_one(client, e) for e in live]          # fast path

batch = client.messages.batches.create(requests=[         # cheap path
    {"custom_id": e.id,
     "params": {"model": "claude-sonnet-4-5", "max_tokens": 1024,
                "tools": [extract_ticket],
                "tool_choice": {"type": "tool", "name": "extract_ticket"},
                "messages": [{"role": "user", "content": e.body}]}}
    for e in backlog
])
# poll batch.id until ended; validate each result with the SAME loop; None → human queue
