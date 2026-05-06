def multiply_polynomial(coefficients: list[float]) -> list[float]:
    if coefficients[0] < 0:
        return [-c for c in coefficients]
    return coefficients
