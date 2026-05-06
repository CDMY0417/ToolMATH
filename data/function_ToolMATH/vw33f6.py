def evaluate_polynomial_z(coefficients: list[float], x: float) -> float:
    result = 0
    for power, coeff in enumerate(coefficients):
        result += coeff * (x ** power)
    return result
