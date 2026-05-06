def nth_digit_in_repeating_sequence(sequence: str, n: int):
    cycle_length = len(sequence)
    index = (n - 1) % cycle_length
    return sequence[index]
