def find_n_for_arithmetic_term(first_term: int, common_difference: int, target_value: int) -> int:
    return (target_value - first_term + common_difference) // common_difference
