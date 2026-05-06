def geometric_progression_terms(first_term: float, common_ratio: float, n_terms: int):
    return [first_term * common_ratio ** i for i in range(n_terms)]
