def evaluate_polynomial_j(coefficients: list[float], x: float) -> float:
    result = 0
    degree = len(coefficients) - 1
    for coeff in coefficients:
        result += coeff * (x ** degree)
        degree -= 1
    return result
