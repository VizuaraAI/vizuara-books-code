"""
AI Agents Bootcamp
Chapter 35: Cycles, Checkpoints, and Human-in-the-Loop
Section: Frameworks II: LangGraph and CrewAI

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/cycles-and-human-in-the-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import State   # the TypedDict defined in Chapter 33

graph = None       # TODO: the StateGraph you built in Chapters 33-34.
user_msg = ""      # TODO: the incoming user message.
email_tool = None  # TODO: whatever actually sends mail for you.
# --- end fixups ---

# --- block 1 ---
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()                 # dev: an in-process dict
agent = graph.compile(checkpointer=memory)

# --- block 2 ---
config = {"configurable": {"thread_id": "customer-4471"}}
agent.invoke({"messages": [user_msg]}, config)   # snapshots saved under thread "customer-4471"

# --- block 3 ---
from langgraph.types import interrupt, Command

def send_email(state: State) -> dict:
    draft = state["draft"]
    decision = interrupt({                      # ⏸ freezes here, checkpoints, returns to caller
        "question": "Send this email?",
        "draft": draft,
    })
    if decision == "approve":
        result = email_tool.send(draft)
        return {"messages": [result], "sent": True}
    else:
        return {"messages": ["human rejected the draft"], "sent": False}

# --- block 4 ---
config = {"configurable": {"thread_id": "customer-4471"}}
out = agent.invoke({"messages": [user_msg]}, config)

print(out["__interrupt__"])
# [Interrupt(value={'question': 'Send this email?', 'draft': 'Dear ...'})]

# --- block 5 ---
final = agent.invoke(Command(resume="approve"), config)   # same config / same thread_id

# --- block 6 ---
for snapshot in agent.get_state_history(config):
    print(snapshot.config["configurable"]["checkpoint_id"], snapshot.values["steps"])
