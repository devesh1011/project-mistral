from llm.config import get_mistral_api_key
from llm.query_decomposition import generate_sub_queries
from llm.doc_retrieval import retrieve_all_documents
from llm.prompt_gen import construct_prompt
from llm.llm_handler import generate_answer
from langchain_mistralai import ChatMistralAI


def main(query):
    llm = ChatMistralAI(
        model_name="mistral-large-latest", api_key=get_mistral_api_key()
    )

    # getting sub queries from the main query
    sub_queries = generate_sub_queries(query, llm)

    # docs retrieval
    docs = retrieve_all_documents(sub_queries)
    context = "\n".join(docs)

    # prompt construction
    prompt = construct_prompt(context, query)

    # generating answer
    answer = generate_answer(prompt)

    return answer
