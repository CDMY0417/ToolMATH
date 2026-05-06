def constant_term_of_composed_polynomial(g3_constant: int, g2_constant: int, g1_constant: int, coefficients_f: list):
    return coefficients_f[0] * g3_constant + coefficients_f[1] * g2_constant + coefficients_f[2] * g1_constant + coefficients_f[3]
