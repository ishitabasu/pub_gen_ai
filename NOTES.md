
# In order to Give response to any questions
We have implemented retriever.py and answer.py. These modules will:

Load faiss.index
Load metadata.pkl
Convert the question to an embedding
Search FAISS for the nearest chunks
Display the answer and source documents

Run below command to test:
pytest