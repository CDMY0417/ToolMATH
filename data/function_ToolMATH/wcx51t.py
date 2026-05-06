def polynomial_substitution(coefficients: list[float], x: float) -> float:
    result = 0
    degree = len(coefficients) - 1
    for c in coefficients:
        result += c * (x ** degree)
        degree -= 1
    return result
