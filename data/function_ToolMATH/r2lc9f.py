def evaluate_polynomial_at_point_b(coefficients: list[int], point: int) -> int:
    result = 0
    x_power = len(coefficients) - 1
    for coefficient in coefficients:
        result += coefficient * (point ** x_power)
        x_power -= 1
    return result
