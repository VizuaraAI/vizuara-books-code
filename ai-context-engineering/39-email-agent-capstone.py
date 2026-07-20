"""
AI Context Engineering
Chapter 39: Capstone: Building an Email Agent
Section: Capstone Builds

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/email-agent-capstone

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
tools = [
    {"name": "search_threads",
     "description": "Find email threads relevant to a query. Returns thread ids + snippets.",
     "input_schema": {"type": "object",
                      "properties": {"query": {"type": "string"}},
                      "required": ["query"]}},
    {"name": "get_calendar",
     "description": "Free/busy for a date range.",
     "input_schema": {"type": "object",
                      "properties": {"start": {"type": "string"}, "end": {"type": "string"}},
                      "required": ["start", "end"]}},
    {"name": "draft_reply",
     "description": "Compose a reply to a thread. Returns a DRAFT — never sends.",
     "input_schema": {"type": "object",
                      "properties": {"thread_id": {"type": "string"}, "body": {"type": "string"}},
                      "required": ["thread_id", "body"]}},
]
