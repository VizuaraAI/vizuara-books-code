"""
LLM Production & Deployment
Chapter 41: Agentic RAG
Section: Agents & Memory

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/agentic-rag

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
embed = None          # TODO: the same embedder used at indexing time (Ch. 26).
index = None          # TODO: the vector index built in Chapter 26.
system_prompt = None  # TODO: renders the tool descriptions into a system message.
user = None           # TODO: wraps the goal as a user message.
observation = None    # TODO: wraps a tool result as an observation message.
# --- end fixups ---

# --- block 1 ---
def search_handbook(query: str, k: int = 3) -> list[str]:
    """Search the employee handbook. Returns the k most
    relevant passages. Call this when the user asks about
    company policy, benefits, or rules."""
    q_vec = embed(query)                  # same embedder as indexing
    hits  = index.nearest(q_vec, k=k)     # cosine top-k, as before
    return [chunk.text for chunk in hits]

# --- block 2 ---
# the same TAO engine; only the tool set changed
def run_agentic_rag(goal, tools, model, max_steps=6):
    context = [system_prompt(tools), user(goal)]
    for _ in range(max_steps):
        out = model(context)                       # Thought + Action
        if out.is_final_answer:
            return out.answer
        result = tools[out.tool_name](**out.args)  # maybe search, maybe not
        context.append(out)
        context.append(observation(result))        # chunks (or math) fed back
    return "stopped: hit max_steps"
