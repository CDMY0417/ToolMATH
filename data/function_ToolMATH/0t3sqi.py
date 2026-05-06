def geometric_series_sum_u(first_term: int, common_ratio: float, num_terms: int) -> float:
    return first_term * (1 - common_ratio ** num_terms) / (1 - common_ratio)
