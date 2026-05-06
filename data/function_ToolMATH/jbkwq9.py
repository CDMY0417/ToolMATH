def least_positive_term_in_arithmetic_sequence(first_term: int, common_difference: int) -> int:
    n = 1
    while True:
        term = first_term + (n - 1) * common_difference
        if term > 0:
            return term
        n += 1
