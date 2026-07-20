"""
AI Agents Bootcamp
Chapter 34: Nodes, Edges, and Conditional Routing
Section: Frameworks II: LangGraph and CrewAI

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/nodes-edges-and-conditional-routing

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
answer_node = None    # TODO: the node that writes the final answer.
calc_node = None      # TODO: the node that does the arithmetic.
generate_node = None  # TODO: the node that drafts an answer.
check_node = None     # TODO: the node that checks the draft and sets `passed`.
#                       The chapter shows the wiring; these four node functions
#                       are yours to write - see the chapter link above.
# --- end fixups ---

# --- block 1 ---
from typing import TypedDict

class State(TypedDict):
    question: str
    answer: str
    category: str    # set by the classifier: "math" or "chat"
    passed: bool     # set by the checker: did the answer pass?
    attempts: int

# --- block 2 ---
def classify(state: State) -> dict:
    q = state["question"].lower()
    kind = "math" if any(c.isdigit() for c in q) else "chat"
    return {"category": kind}     # a partial update, nothing more

# --- block 3 ---
from langgraph.graph import StateGraph, START, END

g = StateGraph(State)
g.add_node("classify", classify)
g.add_node("answer", answer_node)

g.add_edge(START, "classify")      # entry point
g.add_edge("classify", "answer")   # plain, unconditional edge
g.add_edge("answer", END)          # exit point

# --- block 4 ---
def route(state: State) -> str:
    if state["category"] == "math":
        return "calculator"
    return "answer"

g.add_conditional_edges("classify", route, ["calculator", "answer"])

# --- block 5 ---
def should_retry(state: State) -> str:
    if state["passed"] or state["attempts"] >= 3:
        return "END"
    return "generate"        # <-- points back to an earlier node

g.add_conditional_edges("check", should_retry, {"generate": "generate", "END": END})

# --- block 6 ---
g = StateGraph(State)
g.add_node("classify",   classify)
g.add_node("calculator", calc_node)
g.add_node("generate",   generate_node)
g.add_node("check",      check_node)

g.add_edge(START, "classify")
g.add_conditional_edges("classify", route, ["calculator", "generate"])
g.add_edge("calculator", "check")
g.add_edge("generate",   "check")
g.add_conditional_edges("check", should_retry, {"generate": "generate", "END": END})

app = g.compile()
