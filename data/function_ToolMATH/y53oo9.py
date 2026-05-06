def geometric_sequence_sum_a(first_term: float, common_ratio: float, n: int) -> float:
    if common_ratio == 1:
        return first_term * n
    return first_term * (1 - common_ratio ** n) / (1 - common_ratio)
