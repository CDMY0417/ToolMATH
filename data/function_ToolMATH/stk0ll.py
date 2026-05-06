def evaluate_polynomial_t(coefficients: list[float], x: float) -> float:
    return sum(coefficient * (x ** i) for i, coefficient in enumerate(coefficients))
