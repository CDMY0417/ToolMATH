def total_lollipops_in_arithmetic_sequence(first_term: int, num_terms: int, common_difference: int) -> int:
    total = 0
    for i in range(num_terms):
        total += first_term + i * common_difference
    return total
