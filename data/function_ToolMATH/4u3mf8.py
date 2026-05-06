def product_of_quadratic_roots_a(a_coeff: float, b_coeff: float, c_coeff: float) -> float:
    if a_coeff != 0:
        return c_coeff / a_coeff
    return float('nan')
