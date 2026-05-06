def nth_digit_of_repeating_decimal_a(n: int, repeating_sequence: str) -> int:
    index = (n - 1) % len(repeating_sequence)
    return int(repeating_sequence[index])
