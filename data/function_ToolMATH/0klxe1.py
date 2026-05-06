def sum_partial_fraction_sequence(A: float, B: float, C: float, terms: int):
    total_sum = 0
    for n in range(1, terms + 1):
        term_sum = (A/n) + (B/(n + 1)) + (C/(n + 2))
        total_sum += term_sum
    return total_sum
