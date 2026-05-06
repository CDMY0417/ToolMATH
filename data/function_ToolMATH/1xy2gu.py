def next_two_terms_geometric_sequence(recent_term: float, common_ratio: float):
    next_term_1 = recent_term * common_ratio
    next_term_2 = next_term_1 * common_ratio
    return next_term_1, next_term_2
