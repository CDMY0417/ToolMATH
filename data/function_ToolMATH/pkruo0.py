def letter_in_repeated_pattern(pattern: str, position: int) -> str:
    index = (position - 1) % len(pattern)
    return pattern[index]
