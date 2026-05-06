def evaluate_polynomial_horner(coefficients: list[float], x: float) -> float:
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result
