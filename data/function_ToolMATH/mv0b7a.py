def evaluate_polynomial_expression(a: int, b: int, c: int) -> float:
    numerator = a**3 + b**2 + c
    denominator = a + b**2 + c**3
    return numerator / denominator if denominator != 0 else 'undefined'
