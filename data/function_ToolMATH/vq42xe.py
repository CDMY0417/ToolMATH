def geometric_series_sum_n(first_term: float, ratio: float, n_terms: int):
    if ratio == 1:
        return first_term * n_terms
    return first_term * (1 - ratio ** n_terms) / (1 - ratio)
