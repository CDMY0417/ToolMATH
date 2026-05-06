def evaluate_polynomial_k(coefficients: list[float], x: int) -> float:
    result = 0
    degree = len(coefficients) - 1
    for i, coeff in enumerate(coefficients):
        result += coeff * (x ** (degree - i))
    return result
