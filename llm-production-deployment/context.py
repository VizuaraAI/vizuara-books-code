"""
LLM Production & Deployment - shared context for the companion repo.

A few chapters use a name that the book defines in an EARLIER chapter and then
refers back to ("the same query as before", "the weather tool from the previous
chapter"). This module collects those definitions in one place so each chapter
file can import them instead of tripping over an undefined name.

Every definition below is COPIED VERBATIM from the chapter cited above it.
Nothing here is invented.

Importing this module executes everything in it, so the third-party packages it
uses (smolagents) need to be installed.
"""

# ---------------------------------------------------------------------------
# Chapter 26: Embedding & Retrieval (block 1)
# https://books.vizuara.ai/read/llm-production-deployment/embedding-and-retrieval
# Referred to by Chapter 27, which builds a grounded prompt around the same
# question but never re-defines it.
# ---------------------------------------------------------------------------
query = "Where is the Eiffel Tower?"


# ---------------------------------------------------------------------------
# Chapter 39: Building a Multi-Agent Framework (block 2)
# https://books.vizuara.ai/read/llm-production-deployment/building-a-multi-agent-framework
# Referred to by Chapter 40, which binds the same tool to a LangGraph model.
# Note: as written in the book this is decorated with smolagents' @tool, so it
# is a smolagents Tool object, not a LangChain tool.
# ---------------------------------------------------------------------------
from smolagents import tool


@tool
def get_weather(city: str) -> dict:
    """Return the current temperature in a city.
    Args:
        city: the city name, e.g. "Mumbai".
    """
    return {"temp_c": 31 if city == "Mumbai" else 27}
