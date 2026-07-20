"""
RAG in Production
Chapter 39: Agentic RAG with Tools and Routing
Section: Agentic & Graph RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/agentic-rag-with-tools-and-routing

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/agentic-rag-with-tools-and-routing
llm = None       # TODO: tool-calling LLM; returns a reply with .tool_call / .content
run_tool = None  # TODO: dispatches a tool call to one of the `tools` above

# --- block 1 ---
tools = [
    {"name": "search_docs",
     "description": "Semantic search over product manuals and policies. "
                    "Use for how-to, features, and policy questions.",
     "parameters": {"query": "str"}},
    {"name": "query_orders",
     "description": "Run a read-only SQL query against the live orders DB. "
                    "Use for a specific order's status, dates, or items.",
     "parameters": {"sql": "str"}},
    {"name": "web_search",
     "description": "Search the public web for current events or facts "
                    "NOT in company data (e.g. carrier strikes, weather).",
     "parameters": {"query": "str"}},
]

def agentic_rag(question, max_steps=5):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        reply = llm(messages, tools=tools)          # model plans one action
        if reply.tool_call is None:                 # decided it has enough →
            return reply.content                    # final grounded answer
        result = run_tool(reply.tool_call)          # we execute the tool
        messages.append(reply)                      # record the request
        messages.append({"role": "tool", "content": result})  # feed it back
    return "Stopped: hit the step budget without a confident answer."
