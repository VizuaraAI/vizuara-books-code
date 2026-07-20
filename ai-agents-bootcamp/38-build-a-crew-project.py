"""
AI Agents Bootcamp
Chapter 38: Build a Research-and-Write Crew
Section: Frameworks II: LangGraph and CrewAI

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/build-a-crew-project

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# pip install crewai crewai-tools
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

os.environ["GEMINI_API_KEY"] = "your-gemini-key"
os.environ["SERPER_API_KEY"] = "your-serper-key"

search_tool = SerperDevTool()   # a real tool: name + description + arg schema

# --- block 2 ---
researcher = Agent(
    role="Senior Research Analyst",
    goal="Find and verify the 4-5 most important, current facts about {topic}",
    backstory="You are meticulous. You never state a fact without a source, "
              "and you prefer recent, primary sources over blog summaries.",
    tools=[search_tool],
    llm="gemini/gemini-1.5-flash",
    verbose=True,
)

writer = Agent(
    role="Technical Writer",
    goal="Turn research notes into a clear, engaging 300-word brief on {topic}",
    backstory="You write for a smart non-expert. You use only the facts you are "
              "given, and you never invent numbers or claims not in the notes.",
    llm="gemini/gemini-1.5-flash",
    verbose=True,
)

# --- block 3 ---
research_task = Task(
    description="Research {topic}. Use web search to find the 4-5 most "
                "important, current facts. Note a source for each.",
    expected_output="A bullet list of 4-5 verified facts, each with its source URL.",
    agent=researcher,
)

write_task = Task(
    description="Using ONLY the research notes provided, write a 300-word "
                "brief on {topic} for a smart non-expert.",
    expected_output="A ~300-word report with a title and 2-3 short paragraphs.",
    agent=writer,
    context=[research_task],   # ← the wire that carries findings forward
)

# --- block 4 ---
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,   # run tasks in listed order
    verbose=True,
)

result = crew.kickoff(inputs={"topic": "quantum error correction in 2024"})
print(result)
