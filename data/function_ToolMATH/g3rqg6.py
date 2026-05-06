def find_nth_element_in_repeated_pattern(pattern: list, n: int):
    pattern_length = len(pattern)
    index = (n - 1) % pattern_length
    return pattern[index]
