def geometric_sequence_common_ratio_a(second_term: float, fourth_term: float):
    r_squared = fourth_term / second_term
    r1 = r_squared ** 0.5
    r2 = -r1
    return r1, r2
