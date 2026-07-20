"""
Claude Certified Architect (CCAF)
Chapter 10: Guaranteed JSON With tool_use
Section: Guaranteed Structured Output (Domain 4)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/structured-output-with-tool-use

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import anthropic

client = anthropic.Anthropic()

extract_tool = {
    "name": "record_ticket",
    "description": "Record the structured fields extracted from a support ticket.",
    "input_schema": {
        "type": "object",
        "properties": {
            "customer_name": {"type": "string"},
            "product": {"type": "string"},
            "urgency": {
                "type": "string",
                "enum": ["low", "medium", "high"],
            },
        },
        "required": ["customer_name", "product", "urgency"],
    },
}

resp = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=512,
    tools=[extract_tool],
    tool_choice={"type": "tool", "name": "record_ticket"},  # force this exact tool
    messages=[{"role": "user", "content": TICKET_TEXT}],
)

# --- block 2 ---
block = next(b for b in resp.content if b.type == "tool_use")
data = block.input   # already a parsed dict — no json.loads, no fence-stripping
# -> {"customer_name": "Maria Chen", "product": "Pro", "urgency": "high"}

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# "urgency": {"type": ["string", "null"], "enum": ["low", "medium", "high", None]},
# "category": {"type": "string", "enum": ["billing", "outage", "feature", "other"]},
# "category_other_detail": {"type": ["string", "null"]},
