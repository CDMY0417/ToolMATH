def calculate_geometric_term(first_term: int, ratio: int, term_index: int) -> int:
    return first_term * (ratio ** (term_index - 1))
