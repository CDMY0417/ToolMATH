def get_nth_repeating_pattern_element(pattern: str, n: int) -> str:
    index = (n - 1) % len(pattern)
    return pattern[index]
