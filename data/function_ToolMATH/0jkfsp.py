def find_term_in_geometric_sequence(first_term: float, common_ratio: float, term_index: int):
    return first_term * (common_ratio ** (term_index - 1))
