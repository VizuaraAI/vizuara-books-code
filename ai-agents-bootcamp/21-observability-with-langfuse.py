"""
AI Agents Bootcamp
Chapter 21: Seeing Inside Your Agent with Langfuse
Section: Frameworks I: LangChain and Smolagents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/observability-with-langfuse

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import get_weather   # the tool defined in Chapter 12

call_llm = None  # TODO: your one-call-to-the-model helper - Chapter 9 builds one.
# --- end fixups ---

# --- block 1 ---
from langfuse.decorators import observe

@observe()                     # this function becomes the ROOT span (the trace)
def weather_agent(question: str) -> str:
    plan = call_llm(question)      # emitted as a child generation span
    data = get_weather(plan.city)  # emitted as a child tool span
    return call_llm(question, data)  # a second child generation span

weather_agent("What's the 3-day forecast for Paris?")
