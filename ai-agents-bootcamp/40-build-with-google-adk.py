"""
AI Agents Bootcamp
Chapter 40: Building an Agent with Google ADK
Section: Frameworks III: Google ADK and n8n Automation

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/build-with-google-adk

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from google.adk.agents import Agent

weather_agent = Agent(
    name="weather_assistant",
    model="gemini-2.0-flash",
    instruction="You are a concise weather assistant. Answer in one sentence.",
    description="Answers questions about the current weather in a city.",
)

# --- block 2 ---
def get_weather(city: str) -> dict:
    """Return the current weather for a given city.

    Args:
        city: The name of the city, e.g. "London".

    Returns:
        A dict with a 'status' key ("success" or "error") and,
        on success, a 'report' string describing the weather.
    """
    fake_db = {
        "london": "16°C and drizzling",
        "delhi":  "34°C and hazy",
        "tokyo":  "22°C and clear",
    }
    key = city.strip().lower()
    if key in fake_db:
        return {"status": "success", "report": f"The weather in {city} is {fake_db[key]}."}
    return {"status": "error", "error_message": f"No weather data for '{city}'."}

# --- block 3 ---
weather_agent = Agent(
    name="weather_assistant",
    model="gemini-2.0-flash",
    instruction="You are a concise weather assistant. Use the get_weather tool to answer.",
    description="Answers questions about the current weather in a city.",
    tools=[get_weather],
)

# --- block 4 ---
import asyncio
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

APP_NAME = "weather_app"
USER_ID  = "user_1"
SESSION  = "session_1"

session_service = InMemorySessionService()

runner = Runner(
    agent=weather_agent,            # the agent + its tools from above
    app_name=APP_NAME,
    session_service=session_service,
)

async def ask(text: str):
    message = types.Content(role="user", parts=[types.Part(text=text)])
    async for event in runner.run_async(
        user_id=USER_ID, session_id=SESSION, new_message=message
    ):
        if event.is_final_response():
            print("AGENT:", event.content.parts[0].text)

async def main():
    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION
    )
    await ask("What's the weather in Tokyo?")   # turn 1
    await ask("And London?")                     # turn 2 — no city repeated

asyncio.run(main())

# --- block 5 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# async for event in runner.run_async(user_id=USER_ID, session_id=SESSION, new_message=message):
#     for part in (event.content.parts if event.content else []):
#         if part.function_call:
#             print("→ TOOL CALL:", part.function_call.name, part.function_call.args)
#         if part.function_response:
#             print("← TOOL RESULT:", part.function_response.response)
#         if part.text:
#             print("AGENT:", part.text)
