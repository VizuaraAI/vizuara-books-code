"""
AI Agents Bootcamp
Chapter 12: What Are Tools, Really?
Section: Reasoning, Tools, and the Agent Loop

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/what-are-tools

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
import requests

WEATHER_API = None  # TODO: the weather service endpoint URL you sign up for.
# --- end fixups ---

# --- block 1 ---
def get_weather(city: str, unit: str = "C") -> float:
    """Return the current temperature for a city."""
    r = requests.get(WEATHER_API, params={"q": city, "units": unit})
    return r.json()["temp"]

# --- block 2 ---
# 1. the model emits (provider parses it into structured JSON):
{"tool_call": {"name": "get_weather",
               "arguments": {"city": "Paris", "unit": "C"}}}

# 2. the RUNTIME — not the model — runs the real function:
result = get_weather(city="Paris", unit="C")     # → 14.0

# 3. the result is appended to the conversation as an observation:
{"role": "tool", "name": "get_weather", "content": "14.0"}

# 4. the model is called AGAIN, now able to read "14.0", and answers:
#    "It's currently 14°C in Paris."
