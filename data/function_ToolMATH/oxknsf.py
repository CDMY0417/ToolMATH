def compute_quadratic_remainder(k: int) -> tuple:
    linear_coefficient = 2 * k - 9
    constant_term = k**2 - 8 * k + 10
    return (linear_coefficient, constant_term)
