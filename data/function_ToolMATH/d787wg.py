def polynomial_at_point(coefficients: list[int], x: int) -> int:
    result = 0
    degree = len(coefficients) - 1
    for coeff in coefficients:
        result += coeff * (x ** degree)
        degree -= 1
    return result
