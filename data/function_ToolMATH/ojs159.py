def geometric_sequence_sum(first_term: int, common_ratio: int, num_terms: int) -> int:
    return first_term * (common_ratio ** num_terms - 1) // (common_ratio - 1)
