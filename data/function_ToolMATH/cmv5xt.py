def geometric_term_less_than_threshold(initial_term: float, common_ratio: float, threshold: float):
    k = 0
    term = initial_term
    while term >= threshold:
        term *= common_ratio
        k += 1
    return k
