"""
AI Agents Bootcamp
Chapter 31: Agentic RAG: Retrieval as a Tool
Section: Retrieval: RAG and Agentic RAG

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/agentic-rag

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import index, query_engine   # built in Chapter 30

hr_engine = None   # TODO: a query engine over your HR corpus, built the way
#                    Chapter 30 builds `query_engine`.
eng_engine = None  # TODO: a query engine over your engineering corpus.
# --- end fixups ---

# --- block 1 ---
def search_docs(query: str) -> str:
    """Search the company handbook for a passage relevant to `query`.
    Call this when you need facts you don't already have."""
    response = query_engine.query(query)
    return str(response)

# --- block 2 ---
def search_hr_handbook(query: str) -> str:
    """Search HR policies: leave, benefits, conduct, payroll."""
    return str(hr_engine.query(query))

def search_eng_wiki(query: str) -> str:
    """Search engineering docs: architecture, APIs, deploy runbooks."""
    return str(eng_engine.query(query))

# --- block 3 ---
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

# `index` is the VectorStoreIndex from the previous chapter
search_tool = QueryEngineTool.from_defaults(
    query_engine=index.as_query_engine(similarity_top_k=3),
    name="search_docs",
    description="Search the company handbook for facts. "
                "Call this whenever you need information you don't already have.",
)

agent = ReActAgent.from_tools(
    [search_tool],
    llm=OpenAI(model="gpt-4o-mini"),
    verbose=True,          # print every Thought / Action / Observation
)

print(agent.chat("Which grew faster 2022→2023, headcount or revenue?"))
