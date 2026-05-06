def evaluate_polynomial_u(coefficients: list[float], x: float) -> float:
    return sum(coefficient * (x ** i) for i, coefficient in enumerate(coefficients))
