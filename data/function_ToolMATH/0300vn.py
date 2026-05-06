def match_coefficients_a(coefficients1: list, coefficients2: list) -> list:
    return [x == y for x, y in zip(coefficients1, coefficients2)]
