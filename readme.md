# GenAI Backend Engineering Exercise

## Overview

This project implements a command-line Retrieval-Augmented Generation (RAG) application that answers questions from a local collection of `.txt` and `.md` documents.

The application performs the following tasks:

* Reads documents from a local directory
* Splits documents into searchable chunks
* Generates vector embeddings using a local embedding model
* Builds and stores a FAISS vector index
* Retrieves relevant document chunks for user queries
* Returns an answer along with the source document(s)

The entire application runs locally and does not require any paid services or external APIs.

---

## Project Structure

```text
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
│   ├── faiss.index
│   └── metadata.pkl
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
```

---

## Prerequisites

* Python 3.10 or later
* pip

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ishitabasu/pub_gen_ai.git
cd genai-assignment
```

### 2. Create and activate a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Supported Documents

The application supports the following file types:

* `.txt`
* `.md`

Place all documents inside the `docs/` directory before running the ingestion command.

Example:

```text
docs/
├── refund-policy.md
└── faq.txt
```

---

## Build the Search Index

Run the following command to ingest the documents and build the local FAISS index:

```bash
python app.py ingest docs
```

This command:

* Reads all supported documents
* Splits them into chunks
* Generates embeddings
* Builds a FAISS vector index
* Stores metadata locally

After successful ingestion, the following files are generated automatically:

```text
index/
├── faiss.index
└── metadata.pkl
```

---

## Ask Questions

Once the documents have been indexed, questions can be asked using:

```bash
python app.py ask "What is the refund policy?"
```

Example output:

```text
Answer:
Customers may request a refund within 30 days of purchase.

Sources:
refund-policy.md
```

If the answer cannot be supported by the available documents:

```text
Answer:
I could not find enough support for that answer in the provided documents.

Sources:
None
```

---

## Running Tests

Run all automated tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_loader.py
```

Run tests with verbose output:

```bash
pytest -v
```

---

## Error Handling

The application handles common error scenarios, including:

* Invalid command-line usage
* Missing documents directory
* Unsupported document types
* Missing FAISS index
* Asking questions before document ingestion
* Missing metadata file

---

## Technologies Used

* Python
* FAISS
* Sentence Transformers
* NumPy
* argparse
* pytest

---

## Example Workflow

```bash
# Build the search index
python app.py ingest docs

# Ask a question
python app.py ask "What is the refund policy?"

# Run automated tests
pytest
```

---

## Future Improvements

* Overlapping document chunking
* Hybrid retrieval (BM25 + Vector Search)
* Similarity threshold for unsupported queries
* Local LLM-based answer summarization
* Additional document format support (PDF, DOCX)
