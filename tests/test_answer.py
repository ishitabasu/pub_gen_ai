from src.answer import compose_answer


def test_compose_answer():

    results = [
        {
            "filename": "refund.md",
            "chunk": "Refund within 30 days."
        }
    ]

    response = compose_answer(results)

    assert response["answer"] == "Refund within 30 days."

    assert "refund.md" in response["sources"]


def test_empty_answer():

    response = compose_answer([])

    assert "could not find" in response["answer"].lower()

    assert response["sources"] == []