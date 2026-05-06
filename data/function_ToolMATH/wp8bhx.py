def constant_coefficient_of_expression(coefficients: list[float], constants: list[float]) -> float:
    return sum(c * k for c, k in zip(coefficients, constants))
