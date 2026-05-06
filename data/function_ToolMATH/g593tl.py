def match_polynomial_coefficients_a(lhs_coeffs: list[float], rhs_coeffs: list[float]):
    equations = []
    for lc, rc in zip(lhs_coeffs, rhs_coeffs):
        equations.append((lc, rc))
    return equations
