"""
The Modern Software Developer
Chapter 12: Tools and Parameterized Function Calls
Section: MCP Servers: Reusable Integrations

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/mcp-tools-and-function-calls

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_forecast(city: str, days: int = 0) -> str:
    """Get the weather forecast for a city on a given day."""
    ...  # call a real weather API here
    return f"{city}, +{days} days: 31°C, light rain."
