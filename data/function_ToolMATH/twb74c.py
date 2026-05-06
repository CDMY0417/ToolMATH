def evaluate_polynomial_at_value(c: float, x: float, coefficients: tuple):
    a, b, d = coefficients
    return c * x**3 + a * x**2 + b * x + d
