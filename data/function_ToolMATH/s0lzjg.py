def solve_inverse_variation(x0: float, y0: float, y: float) -> float:
    k = x0 ** 2 * y0
    x_squared = k / y
    return x_squared ** 0.5
