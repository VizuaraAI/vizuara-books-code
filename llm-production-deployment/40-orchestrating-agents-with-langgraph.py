"""
LLM Production & Deployment
Chapter 40: Orchestrating Agents with LangGraph
Section: Agents & Memory

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/orchestrating-agents-with-langgraph

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import get_weather   # Chapter 39 defines this tool verbatim

model = None     # TODO: the chat model this chapter binds tools to. It needs a
#                  LangChain-style .bind_tools(), which Chapter 39's smolagents
#                  model does not provide, so the book leaves it to you.
subtract = None  # TODO: the second tool bound alongside get_weather.
# --- end fixups ---

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# for _ in range(max_steps):
#     out = model(context)
#     if out.is_final_answer:
#         return out.answer
#     result = tools[out.tool_name](**out.args)
#     context.append(out); context.append(observation(result))

# --- block 2 ---
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]   # reducer: new msgs are appended, not overwritten

# --- block 3 ---
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import ToolNode

llm_with_tools = model.bind_tools([get_weather, subtract])

def assistant(state: AgentState):
    sys = SystemMessage("You are a helpful weather assistant.")
    reply = llm_with_tools.invoke([sys] + state["messages"])
    return {"messages": [reply]}     # Thought + Action land in state

tool_node = ToolNode([get_weather, subtract])   # runs the tools, returns Observations

# --- block 4 ---
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

builder = StateGraph(AgentState)
builder.add_node("assistant", assistant)
builder.add_node("tools", tool_node)

builder.add_edge(START, "assistant")                 # entry: always start at the assistant
builder.add_conditional_edges("assistant", tools_condition)  # asked for tools? → "tools", else → END
builder.add_edge("tools", "assistant")               # after running tools, always think again

graph = builder.compile()
