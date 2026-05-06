def nth_term_arithmetic_sequence(known_term: int, position_of_known_term: int, n: int, difference: int) -> int:
    return known_term + (n - position_of_known_term) * difference
