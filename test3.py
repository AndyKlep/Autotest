from main3 import count_vowels


def test_only_vowels():
    """Проверка строки, содержащей только гласные буквы."""

    text = "аеёиоуыэюя"
    assert count_vowels(text) == 10


def test_string_without_vowels():
    """Проверка строки без гласных букв."""

    text = "бвгд123!?"
    assert count_vowels(text) == 0


def test_mixed_string_lowercase():
    """Проверка смешанной строки со строчными буквами."""

    text = "Программирование"
    assert count_vowels(text) == 7


def test_mixed_string_uppercase_and_lowercase():
    """Проверка смешанной строки с прописными и строчными буквами."""

    text = "Абракадабра ЁЖик"
    assert count_vowels(text) == 7


def test_empty_string():
    """Проверка пустой строки."""

    assert count_vowels("") == 0