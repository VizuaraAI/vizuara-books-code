"""
Claude Certified Architect (CCAF)
Chapter 11: tool_choice: auto, any, and forced
Section: Guaranteed Structured Output (Domain 4)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/tool-choice-auto-any-forced

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
tools = [{
    "name": "record_invoice",
    "description": "Save the structured fields of an invoice.",
    "input_schema": {
        "type": "object",
        "properties": {
            "vendor": {"type": "string"},
            "amount": {"type": "number"},
            "date":   {"type": "string", "description": "ISO 8601"}
        },
        "required": ["vendor", "amount", "date"]
    }
}]

# --- block 2 ---
resp = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto"},          # RUN 1
    # tool_choice={"type": "any"},          # RUN 2
    # tool_choice={"type": "tool", "name": "record_invoice"},  # RUN 3
    messages=[{"role": "user",
               "content": "Invoice from Acme Corp, $4,200, dated 2026-03-03."}]
)

# --- block 3 ---
block = resp.content[0]              # the tool_use block
block.input == {"vendor": "Acme Corp",
                "amount": 4200,
                "date": "2026-03-03"}   # your schema, filled in — parsed, not string-scraped
