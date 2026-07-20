"""
AI Agents Bootcamp
Chapter 36: CrewAI: Role-Based Agent Teams
Section: Frameworks II: LangGraph and CrewAI

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/crewai-role-based-teams

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
writer = None  # TODO: the crew's second Agent. The chapter builds `researcher`
#                below and leaves the writer for you - see the chapter link above.
# --- end fixups ---

# --- block 1 ---
from crewai import Agent

researcher = Agent(
    role="Senior EV Market Analyst",
    goal="Uncover accurate, up-to-date specs and honest "
         "trade-offs for the leading electric cars of 2026",
    backstory=(
        "You have spent a decade reviewing cars for a consumer "
        "magazine. You distrust marketing numbers and always "
        "cross-check range claims against real-world tests. You "
        "never recommend a car you wouldn't drive yourself."
    ),
    verbose=True,      # print the agent's reasoning as it works
)

# --- block 2 ---
from crewai import Agent, Task, Crew, Process

research_task = Task(
    description="Research the top 3 electric cars of 2026: range, "
                "price, charging speed, and one honest drawback each.",
    expected_output="A bulleted fact sheet, one block per car.",
    agent=researcher,
)

write_task = Task(
    description="Using the research, write a 300-word buyer's guide "
                "for a first-time EV shopper.",
    expected_output="A short guide with a one-line verdict per car.",
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,   # run tasks in order, pass output forward
)

result = crew.kickoff()
