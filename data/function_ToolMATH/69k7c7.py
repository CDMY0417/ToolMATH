def calculate_common_ratio(first_term: float, last_term: float, num_terms: int) -> float:
    return (last_term / first_term) ** (1 / (num_terms - 1))
