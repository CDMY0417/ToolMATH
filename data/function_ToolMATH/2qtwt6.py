def evaluate_polynomial_b(coefficients: list[float], x: float) -> float:
    result = 0
    n = len(coefficients)
    for i in range(n):
        result += coefficients[i] * (x ** (n - i - 1))
    return result
