def scale_polynomial_roots(coefficients: list[float], factor: float):
    degree = len(coefficients) - 1
    return [coeff * (factor ** (degree - i)) for i, coeff in enumerate(coefficients)]
