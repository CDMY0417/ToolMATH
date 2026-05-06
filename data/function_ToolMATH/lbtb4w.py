def arithmetic_sequence_nth_term_f(known_term: int, term_position: int, target_position: int, common_difference: int) -> int:
    n_diff = target_position - term_position
    return known_term + n_diff * common_difference
