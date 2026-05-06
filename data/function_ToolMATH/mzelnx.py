def geometric_series_sum_g(first_term: float, common_ratio: float, num_terms: int):
    if common_ratio == 1:
        return first_term * num_terms
    return first_term * (1 - common_ratio ** num_terms) / (1 - common_ratio)
