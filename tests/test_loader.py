from src.loader import load_documents


def test_load_documents():

    docs = load_documents("tests/test_docs")

    assert len(docs) == 2

    filenames = [doc["filename"] for doc in docs]

    assert "sample.md" in filenames

    assert "sample.txt" in filenames