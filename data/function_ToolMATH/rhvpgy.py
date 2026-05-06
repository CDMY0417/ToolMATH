def add_equations_b(coefficients1: list[int], constant1: int, coefficients2: list[int], constant2: int):
    new_coeffs = [c1 + c2 for c1, c2 in zip(coefficients1, coefficients2)]
    new_constant = constant1 + constant2
    return new_coeffs, new_constant
