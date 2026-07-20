"""
AI Context Engineering
Chapter 24: Tool-Context Hygiene
Section: Tools and MCP

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/tool-context-hygiene

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def clean_search(raw):
    # raw = 10 hits, ~320 tokens each. Keep 3 hits, 2 fields each.
    return [
        {"title": h["title"], "snippet": h["snippet"][:200]}
        for h in raw["results"][:3]
    ]
