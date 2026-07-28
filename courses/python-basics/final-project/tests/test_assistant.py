import json
from pathlib import Path

import pytest

from assistant import calculate_course_price, load_knowledge, local_answer


def test_price_calculation():
    assert calculate_course_price(3, 20) == {"total": 60, "currency": "EUR"}


@pytest.mark.parametrize("participants", [0, -1, 101, "3"])
def test_price_rejects_invalid_participants(participants):
    with pytest.raises(ValueError):
        calculate_course_price(participants, 20)


def test_price_rejects_negative_unit_price():
    with pytest.raises(ValueError):
        calculate_course_price(1, -0.1)


def test_local_answer_uses_knowledge(tmp_path: Path):
    path = tmp_path / "knowledge.json"
    path.write_text(json.dumps({"x": {"keywords": ["python"], "answer": "Taip", "source": "test"}}), encoding="utf-8")
    assert local_answer("  PYTHON ", load_knowledge(path)) == "Taip (Šaltinis: test)"


def test_local_answer_returns_none_for_unknown():
    assert local_answer("oras", {"x": {"keywords": ["python"], "answer": "Taip", "source": "test"}}) is None
