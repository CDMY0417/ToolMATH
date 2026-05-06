def get_nth_digit_of_repeating_sequence(sequence: str, n: int):
    index = (n - 1) % len(sequence)
    return int(sequence[index])
