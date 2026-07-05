import argparse
import sys

from src.loader import load_documents
from src.chunker import chunk_text
from src.embeddings import create_embeddings
from src.indexer import save_index

from src.retriever import Retriever
from src.answer import compose_answer

def ingest_documents(folder):

    # Step 1: Load documents
    print("\n\n Step 1: Loading documents from folder:", folder)
    docs = load_documents(folder)
    print("\n\n Step 2: Loaded documents >>> ", len(docs), " documents found.")
    # Step 2: Build metadata
    metadata = []

    for doc in docs:
        chunks = chunk_text(doc["text"])
        print("\n\n Step i: Chunked document >>> ", doc["filename"], " into ", len(chunks), " chunks.")
        for chunk in chunks:
            print("\n\n Step j: Adding chunk to metadata >>> ", chunk)
            metadata.append({
                "filename": doc["filename"],
                "chunk": chunk
            })
    print("\n\n Step 3: Metadata built >>> ", len(metadata), " chunks in total.")
    # Step 3: Generate embeddings
    vectors = create_embeddings(metadata)
    print("\n\n Step 4: Embeddings generated >>> ", vectors.shape)
    

    # Step 4: Save FAISS index and metadata
    save_index(vectors, metadata)
    print("\n\n Step 5: FAISS index and metadata saved successfully.")
    print("Documents indexed successfully!")


def ask_question(question):

    print("\nLoading index...")

    retriever = Retriever()

    results = retriever.search(question)

    response = compose_answer(results)

    print("\nAnswer:")
    print(response["answer"])

    print("\nSources:")

    if response["sources"]:

        for source in response["sources"]:
            print("-", source)

    else:

        print("None")

def main():

    parser = argparse.ArgumentParser(
        description="GenAI Backend Assessment"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ingest command
    ingest_parser = subparsers.add_parser("ingest")
    ingest_parser.add_argument(
        "folder",
        help="Path to documents folder"
    )

    # ask
    ask_parser = subparsers.add_parser("ask")
    print("ask_parser >>> ",ask_parser)
    ask_parser.add_argument("question")
    print("Pointer 1")
    args = parser.parse_args()
    print("Pointer 2")

    if args.command == "ingest":

        ingest_documents(args.folder)
    elif args.command == "ask":
        print("Pointer 3")
        ask_question(args.question)
    else:

        parser.print_help()


if __name__ == "__main__":
    main()