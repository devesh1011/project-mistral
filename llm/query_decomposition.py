from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def generate_sub_queries(question, llm):
    template = """You are a helpful assistant that generates multiple sub-questions related to an input question. 
    The goal is to break down the input into a set of sub-problems / sub-questions that can be answered in isolation. 
    Only write the query, not its description.
    Generate multiple search queries related to: {question}
    Output (3 queries):"""

    decompose_query_prompt = ChatPromptTemplate.from_template(template)

    generate_queries_decomposition = (
        decompose_query_prompt | llm | StrOutputParser() | (lambda x: x.split("\n"))
    )
    return generate_queries_decomposition.invoke({"question": question})
