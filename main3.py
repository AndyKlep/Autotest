def count_vowels(text: str) -> int:
    """Возвращает количество гласных букв в строке."""

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in text if char in vowels)