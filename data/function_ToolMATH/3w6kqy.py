def polynomial_degree(coefficients: list[float]) -> int:
    for i in range(len(coefficients) - 1, -1, -1):
        if coefficients[i] != 0:
            return i
    return 0
