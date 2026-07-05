GenAI Backend Engineering Exercise
Overview

This project is a command-line Retrieval-Augmented Generation (RAG) application that answers questions from a local collection of .txt and .md documents.

The application:

Reads documents from a local folder
Splits them into searchable chunks
Generates embeddings using a local embedding model
Stores embeddings in a FAISS vector index
Retrieves relevant document chunks for user questions
Returns an answer along with the source document(s)

No paid services or external APIs are required.

Project Structure
genai-assignment/
│
├── app.py
├── requirements.txt
├── README.md
├── NOTES.md
│
├── docs/
│   ├── refund-policy.md
│   └── faq.txt
│
├── index/
│   ├── faiss.index          # Generated after ingestion
│   └── metadata.pkl         # Generated after ingestion
│
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── indexer.py
│   ├── retriever.py
│   └── answer.py
│
└── tests/
    ├── test_loader.py
    ├── test_chunker.py
    ├── test_retriever.py
    ├── test_answer.py
    └── test_cli.py
Prerequisites
Python 3.10 or later
pip
Git (optional)
Installation
1. Clone the repository
git clone <repository-url>
cd genai-assignment

Or download and extract the project.

2. Create a virtual environment
Windows
python -m venv .venv
.venv\Scripts\activate
Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
Preparing Documents

Place all supported documents inside the docs directory.

Example:

docs/
    refund-policy.md
    faq.txt

Supported file types:

.txt
.md
Build the Search Index

Run:

python app.py ingest docs

Example output:

Loading documents...
Chunking documents...
Generating embeddings...
Saving FAISS index...
Documents indexed successfully.

After successful ingestion, the following files will be created automatically:

index/
    faiss.index
    metadata.pkl
Ask Questions

After the documents have been indexed, ask questions using:

python app.py ask "What is the refund policy?"

Example:

Answer:
Customers may request a refund within 30 days of purchase.

Sources:
refund-policy.md

Another example:

python app.py ask "When is customer support available?"

Output:

Answer:
Our support team is available Monday through Friday from 9 AM to 6 PM.

Sources:
faq.txt
Running Automated Tests

Run all tests:

pytest

Run a specific test:

pytest tests/test_loader.py

Run with verbose output:

pytest -v
Error Handling

The application handles common error scenarios including:

Missing documents directory
Unsupported file types
Asking questions before ingestion
Missing FAISS index
Missing metadata file
Invalid CLI commands
Technologies Used
Python
FAISS
Sentence Transformers
NumPy
argparse
pytest
Notes
The application works entirely offline.
No paid APIs or cloud services are required.
The FAISS index is persisted locally and reused for future queries.
Source document references are included in every answer.