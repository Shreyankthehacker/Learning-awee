from llms import llm
from state import State

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompts import another_example_prompt,similar_question


template = ChatPromptTemplate.from_template(another_example_prompt)

example_chain = template | llm | StrOutputParser()

template = ChatPromptTemplate.from_template(similar_question)

simq_chain = template | llm | StrOutputParser()

