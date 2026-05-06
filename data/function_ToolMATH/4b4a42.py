def arithmetic_progression_terms(first_term: float, common_difference: float, n_terms: int):
    return [first_term + i * common_difference for i in range(n_terms)]
