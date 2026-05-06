def evaluate_polynomial_v(coefficients: list[float], x: float) -> float:
    return sum(coef * x**i for i, coef in enumerate(coefficients))
