def geometric_series_sum_o(first_term: float, common_ratio: float, number_of_terms: int) -> float:
    if common_ratio == 1:
        return first_term * number_of_terms
    return first_term * (common_ratio ** number_of_terms - 1) / (common_ratio - 1)
