def expand_quadratic_product(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    coeff_x4 = a1 * a2
    coeff_x3 = a1 * b2 + b1 * a2
    coeff_x2 = a1 * c2 + b1 * b2 + c1 * a2
    coeff_x1 = b1 * c2 + c1 * b2
    coeff_x0 = c1 * c2
    return coeff_x4, coeff_x3, coeff_x2, coeff_x1, coeff_x0
