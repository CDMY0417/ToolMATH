def nth_digit_of_repeating_decimal(non_repeating: str, repeating: str, n: int):
    total_length = len(non_repeating) + len(repeating)
    if n <= len(non_repeating):
        return non_repeating[n-1]
    n -= len(non_repeating)
    index_in_repeating = (n - 1) % len(repeating)
    return repeating[index_in_repeating]
