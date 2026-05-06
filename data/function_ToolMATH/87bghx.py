def adjust_quadratic_coefficient(coeffs: list[float], target_b: float) -> list[float]:
    a, b, c = coeffs
    factor = target_b / b
    return [a * factor, b * factor, c * factor]
