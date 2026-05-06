def nth_term_of_geometric_series(first_term: float, common_ratio: float, n: int) -> float:
    return first_term * (common_ratio ** (n - 1))
