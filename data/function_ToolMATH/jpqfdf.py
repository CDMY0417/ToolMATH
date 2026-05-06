def words_with_no_vowels(length: int, characters: list[str]) -> int:
    return len([c for c in characters if c not in 'AEIOU']) ** length
