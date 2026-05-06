def evaluate_polynomial_y(coefficients: list[int], x: int) -> int:
    result = 0
    for power, coefficient in enumerate(coefficients[::-1]):
        result += coefficient * (x ** power)
    return result
