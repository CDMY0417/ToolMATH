def standard_form_quadratic(lhs_coeffs: tuple, rhs_coeffs: tuple):
    a1, b1, c1 = lhs_coeffs
    a2, b2, c2 = rhs_coeffs
    return (a1 - a2, b1 - b2, c1 - c2)
