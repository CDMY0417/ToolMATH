def nth_term_in_inversely_proportional_sequence(first_term: float, second_term: float, n: int) -> float:
    return second_term if n % 2 == 0 else first_term
