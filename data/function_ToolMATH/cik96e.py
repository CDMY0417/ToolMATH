def arithmetic_sequence_term_count(first_term: int, common_difference: int, last_term: int) -> int:
    return ((last_term - first_term) // common_difference) + 1
