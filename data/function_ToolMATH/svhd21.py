def sum_arithmetic_series_g(first_term: int, last_term: int, num_terms: int) -> int:
    mean = (first_term + last_term) / 2
    return int(mean * num_terms)
