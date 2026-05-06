def sum_geometric_series_a(first_term: float, common_ratio: float, num_terms: int) -> float:
    if common_ratio == 1:
        return num_terms * first_term
    return first_term * (1 - common_ratio**num_terms) / (1 - common_ratio)
