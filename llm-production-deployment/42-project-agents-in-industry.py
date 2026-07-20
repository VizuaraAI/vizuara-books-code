"""
LLM Production & Deployment
Chapter 42: Project: Agents in Industry
Section: Agents & Memory

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/project-agents-in-industry

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from langgraph.graph import MessagesState

get_calendar = None    # TODO: the calendar-reading tool.
lookup_project = None  # TODO: the project-lookup tool.
file_email = None      # TODO: the email-filing tool.
llm = None             # TODO: the chat model the assistant node calls.
# --- end fixups ---

# --- block 1 ---
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

tools = [get_calendar, lookup_project, file_email]
llm_with_tools = llm.bind_tools(tools)          # tell the model the schemas

def assistant(state):                            # the thinking node
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)  # tool? -> tools ; else -> END
builder.add_edge("tools", "assistant")           # the loop-back edge
graph = builder.compile()
