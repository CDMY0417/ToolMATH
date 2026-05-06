def first_term_geometric_sequence(term_value: int, position: int, common_ratio: float) -> float:
    return term_value / (common_ratio ** (position - 1))
