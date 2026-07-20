"""
AI Agents Bootcamp - shared context for the companion repo.

Several chapters use a name that the book defines in a DIFFERENT chapter
("the same regex parser as before", "defined last chapter", "the
VectorStoreIndex from the previous chapter"). This module collects those
definitions in one place so each chapter file can import them instead of
tripping over an undefined name.

Every definition below is COPIED VERBATIM from the chapter cited above it.
Nothing here is invented. Where the book's own code depends on something the
reader has to supply (an API endpoint), that value is left as an obvious stub.

Importing this module executes everything in it, so the third-party packages
it uses (requests, langchain-openai, llama-index, crewai) need to be
installed - see requirements.txt.
"""

# ---------------------------------------------------------------------------
# Chapter 14: Build a ReAct Agent From Scratch (block 2)
# https://books.vizuara.ai/read/ai-agents-bootcamp/build-a-react-agent-from-scratch
# Referred to by chapters 2, 11, 16, 24 ("the same regex parser as before")
# and 25.
# ---------------------------------------------------------------------------
import re

ACTION_RE = re.compile(r'Action\s*\d*:\s*(\w+)\("(.*)"\)')


def parse_action(text: str):
    """Find the last 'Action N: name("arg")' line and split it."""
    match = None
    for match in ACTION_RE.finditer(text):
        pass                        # keep the LAST match, in case of stray lines
    if match is None:
        return None, None
    return match.group(1), match.group(2)   # ('calc', '48 * 12')


# ---------------------------------------------------------------------------
# Chapter 12: What Are Tools, Really? (block 1)
# https://books.vizuara.ai/read/ai-agents-bootcamp/what-are-tools
# Referred to by chapter 21 (the tool span in the Langfuse trace).
# ---------------------------------------------------------------------------
import requests

WEATHER_API = None  # TODO: the weather service endpoint URL you sign up for -
#                     the book leaves this to the reader. See chapter 12.


def get_weather(city: str, unit: str = "C") -> float:
    """Return the current temperature for a city."""
    r = requests.get(WEATHER_API, params={"q": city, "units": unit})
    return r.json()["temp"]


# ---------------------------------------------------------------------------
# Chapter 17: LangChain: Models, Prompts, and Chains (block 1)
# https://books.vizuara.ai/read/ai-agents-bootcamp/langchain-core-concepts
# Referred to by chapters 29 and 33, which call `llm` without redefining it.
# ---------------------------------------------------------------------------
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# ---------------------------------------------------------------------------
# Chapter 30: Build a RAG System with LlamaIndex (block 1)
# https://books.vizuara.ai/read/ai-agents-bootcamp/build-rag-with-llamaindex
# Referred to by chapter 31: "`index` is the VectorStoreIndex from the
# previous chapter".
# ---------------------------------------------------------------------------
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()   # 1. read the PDF
index = VectorStoreIndex.from_documents(documents)       # 2. chunk + embed + store
query_engine = index.as_query_engine()                   # 3. build the retriever+LLM


# ---------------------------------------------------------------------------
# Chapter 33: LangGraph: Agents as State Machines (block 2)
# https://books.vizuara.ai/read/ai-agents-bootcamp/stateful-workflows-with-langgraph
# Referred to by chapter 35, whose node signatures are annotated `State`.
# ---------------------------------------------------------------------------
from typing import TypedDict, Annotated
from operator import add


class State(TypedDict):
    messages: Annotated[list, add]   # new messages are APPENDED, not overwritten
    needs_lookup: bool
    steps: int


# ---------------------------------------------------------------------------
# Chapter 36: CrewAI: Role-Based Agent Teams (block 1)
# https://books.vizuara.ai/read/ai-agents-bootcamp/crewai-role-based-teams
# Referred to by chapter 37: "defined last chapter: role/goal/backstory".
# ---------------------------------------------------------------------------
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
