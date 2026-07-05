def compose_answer(results):

    if not results:
        return {
            "answer":
            "I could not find enough support for that answer in the provided documents.",
            "sources": []
        }

    answer = results[0]["chunk"]

    sources = list(
        set(
            item["filename"]
            for item in results
        )
    )

    return {
        "answer": answer,
        "sources": sources
    }