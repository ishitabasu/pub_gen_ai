import subprocess


def test_ingest_command():

    result = subprocess.run(
        [
            "python",
            "app.py",
            "ingest",
            "docs"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0

    assert "successfully" in result.stdout.lower()


def test_ask_command():

    result = subprocess.run(
        [
            "python",
            "app.py",
            "ask",
            "refund policy"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0

    assert "answer" in result.stdout.lower()