def construct_prompt(context, query):
    return (
        "You are a knowledgeable and precise assistant capable of extracting relevant answers "
        "from a given context. Always ensure your responses are concise, factual, and directly "
        "address the question.\n\n"
        f"Context: {context}\n\n"
        f"Question: {query}\n\n"
        f"Answer:"
    )
