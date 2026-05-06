def evaluate_polynomial_o(coefficients: list[float], x: float) -> float:
    result = 0
    power = len(coefficients) - 1
    for coefficient in coefficients:
        result += coefficient * (x ** power)
        power -= 1
    return result
