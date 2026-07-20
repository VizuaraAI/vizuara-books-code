"""
LLM Production & Deployment
Chapter 39: Building a Multi-Agent Framework
Section: Agents & Memory

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/building-a-multi-agent-framework

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
search_web = None  # TODO: a web-search tool for the researcher agent.
visit_page = None  # TODO: a page-fetching tool for the researcher agent.
# --- end fixups ---

# --- block 1 (COMMENTED OUT - not standalone code) ---
# NOTE: this block is prose in the book, not runnable code. It shows the Python
# a CodeAgent WRITES and runs inside the smolagents sandbox, where `get_weather`
# and `final_answer` are injected at runtime. As a module-level script it uses
# `get_weather` before the book defines it (block 2) and `final_answer` never.
# Kept verbatim; nothing is guessed at.
# mumbai = get_weather(city="Mumbai")["temp_c"]   # 31
# delhi  = get_weather(city="Delhi")["temp_c"]     # 27
# diff = mumbai - delhi
# final_answer(f"Mumbai is warmer, by {diff} degrees C.")

# --- block 2 ---
from smolagents import CodeAgent, tool, InferenceClientModel

@tool
def get_weather(city: str) -> dict:
    """Return the current temperature in a city.
    Args:
        city: the city name, e.g. "Mumbai".
    """
    return {"temp_c": 31 if city == "Mumbai" else 27}

model = InferenceClientModel()                      # any chat model backend
agent = CodeAgent(tools=[get_weather], model=model)
agent.run("Is it warmer in Mumbai or Delhi, and by how much?")

# --- block 3 ---
web_agent = CodeAgent(
    tools=[search_web, visit_page], model=model,
    name="web_researcher",
    description="Searches the web and reads pages. Give it a research question.",
)

manager = CodeAgent(
    tools=[], model=model,
    managed_agents=[web_agent],          # the worker is now callable
)
manager.run("Find the population of Pune and multiply it by 3.")

# --- block 4 ---
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
# LangFuse OTel endpoint + keys configured via environment variables
SmolagentsInstrumentor().instrument()               # ONE call, at startup

manager.run("Find the population of Pune and multiply it by 3.")
# → every agent, step, model call, and tool call now appears in LangFuse
