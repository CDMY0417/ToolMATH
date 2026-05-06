def sum_of_terms_a(first_term: float, difference: float, positions: list[int]) -> float:
    return sum(first_term + (pos - 1) * difference for pos in positions)
