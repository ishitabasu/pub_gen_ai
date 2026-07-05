from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(metadata):

    texts = [item["chunk"] for item in metadata]

    vectors = model.encode(
        texts,
        convert_to_numpy=True
    )

    return vectors