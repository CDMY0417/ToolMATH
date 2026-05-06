def sum_of_arithmetic_progression(first_term: int, num_terms: int, common_difference: int) -> int:
    return num_terms * (2 * first_term + (num_terms - 1) * common_difference) // 2
