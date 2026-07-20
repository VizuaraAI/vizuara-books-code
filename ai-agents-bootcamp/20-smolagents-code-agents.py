"""
AI Agents Bootcamp
Chapter 20: Smolagents: Agents That Write Code to Act
Section: Frameworks I: LangChain and Smolagents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/smolagents-code-agents

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
final_answer = None  # TODO: smolagents injects this into its sandbox at run
#                      time. Block 2 below is the code the AGENT writes and the
#                      sandbox runs, not code you call yourself.
# --- end fixups ---

# --- block 1 ---
from smolagents import CodeAgent, tool, InferenceClientModel

@tool
def convert_to_celsius(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: the temperature in degrees Fahrenheit.
    """
    return (fahrenheit - 32) * 5 / 9

agent = CodeAgent(
    tools=[convert_to_celsius],
    model=InferenceClientModel(),   # any LLM backend
)

agent.run(
    "These readings are in Fahrenheit: 98.6, 50, 68, 212. "
    "Convert them all and give me the average in Celsius."
)

# --- block 2 ---
temps_f = [98.6, 50, 68, 212]
temps_c = [convert_to_celsius(t) for t in temps_f]
average = sum(temps_c) / len(temps_c)
final_answer(average)
