def retrieve_documents(query):
    pass


def retrieve_all_documents(queries):
    docs = []
    for query in queries:
        retrieved_docs = retrieve_documents(query)
        docs.extend(retrieved_docs)
    return docs
