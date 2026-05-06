def arithmetic_sequence_term_count_a(last_term: int, first_term: int, common_difference: int) -> int:
    n = (last_term - first_term) // common_difference + 1
    return n
