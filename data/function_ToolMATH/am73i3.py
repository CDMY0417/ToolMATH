def calculate_geometric_nth_term(first_term: float, common_ratio: float, n: int) -> float:
    return first_term * (common_ratio ** (n - 1))
