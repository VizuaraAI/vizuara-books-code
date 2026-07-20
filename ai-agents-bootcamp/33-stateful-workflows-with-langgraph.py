"""
AI Agents Bootcamp
Chapter 33: LangGraph: Agents as State Machines
Section: Frameworks II: LangGraph and CrewAI

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/stateful-workflows-with-langgraph

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import llm   # the chat model defined in Chapter 17

execute = None  # TODO: the runtime that actually runs a tool call.
# --- end fixups ---

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# messages = [system_prompt, user_question]
# while True:
#     reply = llm(messages)              # think
#     if reply.tool_call:               # act?
#         result = run_tool(reply.tool_call)
#         messages.append(result)       # observe
#         continue                      # loop again
#     else:
#         return reply                  # done

# --- block 2 ---
from typing import TypedDict, Annotated
from operator import add

class State(TypedDict):
    messages: Annotated[list, add]   # new messages are APPENDED, not overwritten
    needs_lookup: bool
    steps: int

# --- block 3 ---
def call_model(state: State) -> dict:
    reply = llm(state["messages"])
    needs = reply.tool_call is not None
    return {"messages": [reply], "needs_lookup": needs, "steps": state["steps"] + 1}

def run_tool(state: State) -> dict:
    result = execute(state["messages"][-1].tool_call)
    return {"messages": [result], "needs_lookup": False}

# --- block 4 ---
from langgraph.graph import StateGraph, END

g = StateGraph(State)
g.add_node("call_model", call_model)
g.add_node("run_tool", run_tool)
g.set_entry_point("call_model")
g.add_conditional_edges(
    "call_model",
    lambda s: "run_tool" if s["needs_lookup"] and s["steps"] < 5 else END,
)
g.add_edge("run_tool", "call_model")   # tool result loops back to the model
agent = g.compile()
