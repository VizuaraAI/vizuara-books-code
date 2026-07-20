"""
Generative AI Fundamentals
Chapter 22: LangChain and Chains
Section: Agents & LangChain

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/langchain-and-chains

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
title = "Interstellar"
text = f"What is the single-word genre of the movie '{title}'? Answer with one word."
response = model.invoke(text)      # returns a message object
genre = response.content.strip().lower()   # dig out the string, clean it

# --- block 2 ---
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "What is the single-word genre of the movie '{title}'? "
    "Answer with one lowercase word."
)
model  = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

chain = prompt | model | parser        # a Runnable, built but not yet run
chain.invoke({"title": "Interstellar"})  # -> "sci-fi"

# --- block 3 ---
from langchain_core.runnables import RunnableParallel

analyze = RunnableParallel(
    genre=prompt_genre | model | parser,
    summary=prompt_summary | model | parser,
)
analyze.invoke({"title": "Interstellar"})
# -> {"genre": "sci-fi", "summary": "A father crosses a wormhole to save humanity."}

# --- block 4 ---
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()
prompt = ChatPromptTemplate.from_template(
    "Classify the movie '{title}'. {format_instructions}"
).partial(format_instructions=parser.get_format_instructions())

chain = prompt | model | parser
chain.invoke({"title": "Interstellar"})
# -> {"genre": "sci-fi", "confidence": 0.9}
