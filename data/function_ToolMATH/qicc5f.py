def apply_remainder_theorem(coefficients: list[float], x: float) -> float:
    result = 0
    degree = len(coefficients) - 1
    for coefficient in coefficients:
        result += coefficient * (x ** degree)
        degree -= 1
    return result
