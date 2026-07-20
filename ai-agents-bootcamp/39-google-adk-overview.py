"""
AI Agents Bootcamp
Chapter 39: Google ADK: Google's Agent Development Kit
Section: Frameworks III: Google ADK and n8n Automation

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/google-adk-overview

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """Return the current weather for a city."""
    return {"city": city, "temp_c": 21, "condition": "clear"}

weather_agent = Agent(
    name="weather_agent",
    model="gemini-2.5-flash",
    instruction="You answer weather questions. Use the get_weather tool.",
    tools=[get_weather],
)
