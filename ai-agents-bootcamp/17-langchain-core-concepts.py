"""
AI Agents Bootcamp
Chapter 17: LangChain: Models, Prompts, and Chains
Section: Frameworks I: LangChain and Smolagents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/langchain-core-concepts

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

response = llm.invoke([
    SystemMessage(content="You are a terse assistant. Answer in one sentence."),
    HumanMessage(content="Why is the sky blue?"),
])

print(response.content)   # -> "Sunlight scatters off air molecules, and blue scatters most."
print(type(response))     # -> <class 'langchain_core.messages.ai.AIMessage'>

# --- block 2 ---
question = "France"
prompt = "You are a geography tutor. What is the capital of " + question + "?"

# --- block 3 ---
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a geography tutor. Answer in one word."),
    ("human", "What is the capital of {country}?"),
])

filled = template.invoke({"country": "France"})
# filled is now a list of two messages, with {country} replaced by "France"

# --- block 4 ---
messages = template.invoke({"country": "France"})
reply = llm.invoke(messages)
answer = reply.content

# --- block 5 ---
from langchain_core.output_parsers import StrOutputParser

chain = template | llm | StrOutputParser()

answer = chain.invoke({"country": "France"})   # -> "Paris"
