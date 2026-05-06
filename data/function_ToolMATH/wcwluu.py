def sum_of_arithmetic_sequence_h(first_term: int, num_of_terms: int, common_difference: int) -> int:
    last_term = first_term + (num_of_terms - 1) * common_difference
    return num_of_terms * (first_term + last_term) // 2
