"""
The Modern Software Developer
Chapter 15: Build and Connect Your Own MCP Server
Section: MCP Servers: Reusable Integrations

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/build-an-mcp-server

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# server.py
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("notes")               # the server's name, as the agent will see it
NOTES = Path("notes.md")

@mcp.tool()
def count_words(path: str) -> int:
    """Return the exact number of words in a local text file."""
    text = Path(path).read_text(encoding="utf-8")
    return len(text.split())

@mcp.tool()
def add_note(text: str) -> int:
    """Append a note to notes.md and return the new total note count."""
    with NOTES.open("a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    return sum(1 for _ in NOTES.open())

if __name__ == "__main__":
    mcp.run()                        # start speaking MCP over stdio
