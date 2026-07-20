"""
AI Agents Bootcamp
Chapter 18: LangChain Agents: Tools and Memory
Section: Frameworks I: LangChain and Smolagents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/langchain-tools-and-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The chapter uses these names without defining them. Placeholders so the file runs.
history_messages_key="chat_history", # fills the placeholder above

# --- block 1 ---
from langchain_core.tools import tool

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

@tool
def check_calendar(day: str) -> str:
    """Check whether the user is free on a given weekday, e.g. 'Thursday'."""
    busy = {"Thursday": "2pm meeting", "Friday": "free all day"}
    return busy.get(day, "free all day")

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# >>> multiply.name
# 'multiply'
# >>> multiply.description
# 'Multiply two numbers together.'
# >>> multiply.args
# {'a': {'type': 'number'}, 'b': {'type': 'number'}}

# --- block 3 ---
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [multiply, check_calendar]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use tools when they help."),
    ("placeholder", "{chat_history}"),      # <- memory slot, we fill this next
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),  # <- the ReAct loop's working notes
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# >>> executor.invoke({"input": "What is 48 times 12?", "chat_history": []})

# --- block 5 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# >>> executor.invoke({"input": "What is 48 times 12?", "chat_history": []})
# 576
# >>> executor.invoke({"input": "Now multiply that by 2.", "chat_history": []})
# "I'm sorry, multiply that by what? I don't have a previous value."

# --- block 6 ---
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

history = ChatMessageHistory()

chat_agent = RunnableWithMessageHistory(
    executor,
    lambda session_id: history,          # where to load/save the transcript
    input_messages_key="input",
)

cfg = {"configurable": {"session_id": "demo"}}
chat_agent.invoke({"input": "What is 48 times 12?"}, config=cfg)   # -> 576
chat_agent.invoke({"input": "Now multiply that by 2."}, config=cfg) # -> 1152
