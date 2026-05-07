"""Тесты для модуля grades."""

import pytest
from grades import get_average, get_grade, is_passed

def test_get_average():
    assert get_average([80, 90, 100]) == 90
    assert get_average([50, 50]) == 50
    assert get_average([0, 0, 0]) == 0

def test_get_average_empty():
    with pytest.raises(ValueError):
        get_average([])

def test_get_grade():
    assert get_grade(95) == "Отлично"
    assert get_grade(70) == "Хорошо"
    assert get_grade(50) == "Удовлетворительно"
    assert get_grade(49) == "Неудовлетворительно"

def test_is_passed():
    assert is_passed(50) is True
    assert is_passed(49) is False
    assert is_passed(100) is True
    assert is_passed(0) is False
