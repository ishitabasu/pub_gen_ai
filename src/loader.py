# loader.py

from pathlib import Path

def load_documents(folder):

    documents = []

    path = Path(folder)

    if not path.exists():
        raise FileNotFoundError("Directory not found.")

    for file in path.iterdir():

        if file.suffix in [".txt", ".md"]:

            documents.append(
                {
                    "filename": file.name,
                    "text": file.read_text(encoding="utf-8")
                }
            )

    return documents

