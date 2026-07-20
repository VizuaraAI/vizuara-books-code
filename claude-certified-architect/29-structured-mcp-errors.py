"""
Claude Certified Architect (CCAF)
Chapter 29: Structured MCP Errors
Section: Tool Design and MCP Integration (Domain 2)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/structured-mcp-errors

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def handle_tool_error(err, attempt, max_attempts=3):
    if not err["isError"]:
        return "continue"                     # not a failure at all
    if err["errorCategory"] == "transient" and err["isRetryable"]:
        if attempt < max_attempts:
            backoff = 2 ** attempt             # 1s, 2s, 4s
            return f"retry after {backoff}s"
        return "escalate: transient but out of retries"
    if err["errorCategory"] == "business":
        return "stop: report the business rule to the user"
    if err["errorCategory"] == "permission":
        return "stop + escalate: never retry an auth wall"
