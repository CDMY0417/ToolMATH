def vieta_sums_a(coefficients: list[float]):
    a_plus_b_plus_c = -coefficients[1] / coefficients[0]
    ab_plus_ac_plus_bc = coefficients[2] / coefficients[0]
    abc = -coefficients[3] / coefficients[0]
    return a_plus_b_plus_c, ab_plus_ac_plus_bc, abc
