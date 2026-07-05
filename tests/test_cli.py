import subprocess
import sys


def test_ingest_command():
    result = subprocess.run(
        [
            sys.executable,   # <-- Use the current Python interpreter
            "app.py",
            "ingest",
            "docs"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Documents indexed successfully!" in result.stdout


def test_ask_command():
    result = subprocess.run(
        [
            sys.executable,   # <-- Use the current Python interpreter
            "app.py",
            "ask",
            "refund policy"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "answer" in result.stdout.lower()