def evaluate_polynomial_at_roots(coefficients: list[float], roots: list[float]) -> list[float]:
    return [sum(coef * (root ** idx) for idx, coef in enumerate(coefficients[::-1])) for root in roots]
