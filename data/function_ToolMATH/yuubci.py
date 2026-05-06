def nth_digit_in_repeating_sequence_a(n: int, cycle_length: int):
    if cycle_length == 0:
        return None  # No repeating sequence
    return (n - 1) % cycle_length
