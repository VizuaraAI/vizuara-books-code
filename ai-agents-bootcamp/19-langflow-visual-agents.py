"""
AI Agents Bootcamp
Chapter 19: Langflow: Building Agents Visually
Section: Frameworks I: LangChain and Smolagents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/langflow-visual-agents

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("Explain {topic} to a 10-year-old.")
model  = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

chain = prompt | model          # the "|" is the wire between the two boxes
print(chain.invoke({"topic": "photosynthesis"}).content)
