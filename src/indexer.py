import os
import faiss
import pickle


def save_index(vectors, metadata):

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    os.makedirs("index", exist_ok=True)

    faiss.write_index(
        index,
        "index/faiss.index"
    )

    with open("index/metadata.pkl","wb") as f:
        pickle.dump(metadata,f)