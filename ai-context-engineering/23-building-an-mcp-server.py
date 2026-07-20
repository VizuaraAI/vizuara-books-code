"""
AI Context Engineering
Chapter 23: Building a Useful MCP Server and Client
Section: Tools and MCP

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/building-an-mcp-server

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# server.py
from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi

mcp = FastMCP("youtube-transcript")   # the server's name

@mcp.tool()
def get_transcript(video_id: str) -> str:
    """Fetch the transcript of a YouTube video.

    Args:
        video_id: the 11-character YouTube id, e.g. 'dQw4w9WgXcQ'
    """
    chunks = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join(chunk["text"] for chunk in chunks)

if __name__ == "__main__":
    mcp.run(transport="stdio")

# --- block 2 ---
# client.py
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

params = StdioServerParameters(command="python", args=["server.py"])

async def main():
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()                     # 1. handshake
            tools = await session.list_tools()             # 2. discover
            print([t.name for t in tools.tools])           #    -> ['get_transcript']
            result = await session.call_tool(              # 3. invoke
                "get_transcript", {"video_id": "dQw4w9WgXcQ"}
            )
            print(result.content[0].text[:200])            # first 200 chars
