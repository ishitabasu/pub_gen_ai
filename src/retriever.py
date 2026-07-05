import faiss
import pickle
import os

from src.embeddings import model


class Retriever:

    def __init__(self):

        if not os.path.exists("index/faiss.index"):
            raise FileNotFoundError(
                "FAISS index not found. Run 'python app.py ingest docs' first."
            )

        self.index = faiss.read_index("index/faiss.index")

        with open("index/metadata.pkl", "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, question, top_k=3):

        # Convert question into embedding
        query_vector = model.encode(
            [question],
            convert_to_numpy=True
        )

        # Search FAISS
        distances, indices = self.index.search(query_vector, top_k)

        results = []

        for idx in indices[0]:

            if idx != -1:
                results.append(self.metadata[idx])

        return results