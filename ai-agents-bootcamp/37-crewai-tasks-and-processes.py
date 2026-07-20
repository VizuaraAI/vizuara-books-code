"""
AI Agents Bootcamp
Chapter 37: CrewAI: Tasks, Tools, and Sequential vs Hierarchical Processes
Section: Frameworks II: LangGraph and CrewAI

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/crewai-tasks-and-processes

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import researcher   # "defined last chapter" (Chapter 36)

writer = None  # TODO: the crew's writer Agent, built like `researcher`.
# --- end fixups ---

# --- block 1 ---
from crewai import Task

research_task = Task(
    description=(
        "Research the state of open-source LLMs in 2025. Find the most "
        "important models, who released them, and one benchmark number each."
    ),
    expected_output=(
        "A bullet list of 4-5 models, each with: name, the lab/company, "
        "release year, and one concrete benchmark figure."
    ),
    agent=researcher,          # defined last chapter: role/goal/backstory
)

write_task = Task(
    description=(
        "Using the research findings, write a 200-word blog intro that a "
        "developer would actually want to read. No fluff."
    ),
    expected_output="A single ~200-word paragraph in a confident, plain voice.",
    agent=writer,
)

# --- block 2 ---
from crewai_tools import SerperDevTool

search = SerperDevTool()               # a web-search tool

researcher.tools = [search]            # this agent can now search the web

# --- block 3 ---
from crewai import Crew, Process

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],     # order matters!
    process=Process.sequential,            # the default
)

result = crew.kickoff()

# --- block 4 ---
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.hierarchical,
    manager_llm="gpt-4o",              # CrewAI builds a manager agent for you
)
