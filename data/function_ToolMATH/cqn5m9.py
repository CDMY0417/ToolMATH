def match_polynomial_coefficients(coefficients1: list[float], coefficients2: list[float]):
    return {i: (coeff1, coeff2) for i, (coeff1, coeff2) in enumerate(zip(coefficients1, coefficients2))}
