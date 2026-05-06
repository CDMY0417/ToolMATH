def degree_of_polynomial_a(coefficients: list[float]) -> int:
    for i in range(len(coefficients) - 1, -1, -1):
        if coefficients[i] != 0:
            return i
    return -1  # Represents the zero polynomial which technically has an undefined degree
