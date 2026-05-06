def compute_quadratic_coefficients_from_roots(r1: int, r2: int):
    b = -(r1 + r2)
    c = r1 * r2
    return (b, c)
