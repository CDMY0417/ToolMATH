def finite_geometric_series_sum(first_term: float, common_ratio: float, num_terms: int) -> float:
    return first_term * (1 - common_ratio**num_terms) / (1 - common_ratio)
